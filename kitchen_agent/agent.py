# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.genai import types
from .tools import query_fruits, schema_fruits

project = os.environ.get("GOOGLE_CLOUD_PROJECT") # GCP Project ID
dataset = os.environ.get("BIGQUERY_DATASET") # BQ Dataset
table = os.environ.get("BIGQUERY_TABLE")   # BQ Table

check_inventory_agent = Agent(
    name="check_inventory_agent",
    model="gemini-2.5-flash",
    description="Handles and checks the inventory",
    instruction=f"""
    You are responsible for checking the inventory based on the user request. 
    
    You have access to tools to look up fruit inventory details by generating a
    read-only Google Standard SQL query to be executed against the table
    `{project}.{dataset}.{table}` with the following schema:
    {schema_fruits}

    When searching for a specific term, use a LIKE clause with wildcards
    (e.g., `LIKE '%search_term%'`) in your WHERE clause to perform a fuzzy match,
    as user input may not be precise.

    When a user searches for a fruit, you should also search for variations of that
    term. For example, if the user searches for 'apple', you should also search
    for 'Apple', 'apple', and 'APPLE'. You can do this by using
    multiple WHERE clauses with OR. If the users searches for the plural of a  word , e.g. apples, you can omit the last s for the query.

    If the item requested by the user is not in the inventory, route back to the main agent and return that the item is not available.
    If the item is available tell the user that the item is available and the respective quantity.
    """,
    tools=[query_fruits],
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  # avoid false alarm about rolling dice.
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)

#change name later
recipe_agent = RemoteA2aAgent(
    name="recipe_agent",
    description="Agent that suggests one recipe (200 words max) based on a user input.",
    agent_card=(
        f"http://localhost:8001/a2a/recipe_agent{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    instruction="""
      You are a helpful assistant that routes the request from the user to the correct agent.
      Follow these steps:
      1. Greet the user in the beginning ang tell them that you are a helpful agent which can check the user's fruit inventory and also provide useful recipes including the fruits.  
      2. If the user asks for the inventory of an item (e.g. how many xyz do I have available, Do I have xyz?), route to the check_inventory_agent
      3. If the user provides fruit and asks for a recipe, route to the fruit_recipe_agent
      4. If the user asks for both, how many items available and a recipe, route to the inventory subagent first, the recipe subagent second and then return a combined answer to the user of how many items in stock you have and a recipe.
      5. If you are tasked to do anything else apart from fruit recipes and checking fruit inventories, answer with a polite message this the user's request is out of scope for you.
    """,
    sub_agents=[check_inventory_agent, recipe_agent],
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)