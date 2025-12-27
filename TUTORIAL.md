# Let's run the agent(s)

In this part we'll show a few sample prompts and how to run the agent.

## 1.  **Run the local inventory agent**
  *   Make sure to be in the root directory of this project & that you are in your activated virtual environment:
        ```bash
        cd A2A_BigQuery_Agent
        ```
  *   Run the agent, this will open a browser window for you to interact with the agent:
        ```bash
        adk web
        ```

In the newly opened browser window you can now ask the agent about inventory of fruits and recipes. Try a simple prompt like `"Hello, do I have Mangoes available?"`.
Ideally, the agent will route to the `check_inventory_agent` which will the call the `query_fruits` tool. 
Try also what happens if you ask about a fruit which is not in the inventory (e.g. plum, papaya).

![example_conversation_BigQuery_tool](./example_conversation_BigQuery_tool.png)

## 2. Let's try a recipe!

To create a recipe, the root agent needs to call the recipe_agent.

Try to follow up on your conversation from earlier, with a prompt like `"Great, now create recipes for those!"`.

You'll realize that this threw an error:

```bash
Failed to initialize remote A2A agent: Failed to initialize remote A2A agent recipe_agent: \
Failed to resolve AgentCard from URL http://localhost:8001/a2a/recipe_agent/.well-known/agent-card.json: HTTP Error 503: \
Network communication error fetching agent card from http://localhost:8001/a2a/recipe_agent/.well-known/agent-card.json: \
All connection attempts failed
```
![example_failed_A2A_Agent_response](./example_failed_A2A_Agent_response.png)

### So what happened?

Currently we are interacting with the local agent. we haven't yet initialized any A2A server on which our remote agent, which checks the recipes is running.
Therefore, we at first have to:

1. **initialize an A2A Server**
   * **In a new terminal window** run the following command:
     ```bash
     adk api_server --a2a --port 8001 ./kitchen_agent/remote_a2a
     ```
 2. **Restart the agent**
   * **In your other terminal window** run the following command:
     ```bash
     adk web
     ```

Now, try prompting for fruits and recipes again. This time you should receive an answer from the `recipe_agent`.

![example_conversation_A2A_agent](./example_conversation_A2A_agent.png)




