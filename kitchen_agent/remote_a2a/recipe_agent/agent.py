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

from google.adk import Agent
from google.genai import types


root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="Agent that suggests 2 short recipes (200 words max) based on a user input. One recipe is sweet and one is savory.",
    instruction="""Provide 2 possible recipes (200 words max each) including the fruits the user provided.
    The recipe can also include other ingredients than fruit. E.g if user input is apple, you 
    can provide the recipe of an apple pie which also includes flower, eggs, etc. or a duck roast with glazed apples.
    One recipe has to be sweet and one has to be savory to give the user a choice. """,    
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  # avoid false alarm about rolling dice.
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)