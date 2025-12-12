# A2A BigQuery Agent

This sample demonstrates the **Agent-to-Agent (A2A)** architecture in the Agent Development Kit (ADK), showcasing how multiple agents can work together to handle complex tasks as well as connect to databases like BigQuery through agentic tool calls. The sample implements an agent that can check fruit inventory in a kitchen as well as suggest recipes based on the provided fruits.

## Overview

The A2A BigQuery Agent consists of:

- **Root Agent** (`root_agent`): The main orchestrator that delegates tasks to specialized sub-agents
- **Check Inventory Agent** (`check_inventory_agent`): A local sub-agent that is connected to BigQuery as a tool and can query a fruit inventory table based on a user's prompt
- **Recipe Agent** (`recipe_agent`): A remote A2A agent that provides a sweet and savory recipe based on a user's fruit input

## Architecture

add image of agent architecture here

## Key Features

### 1. **Local Sub-Agent Integration**
- The `check_inventory_agent` demonstrates how to create and integrate local sub-agents
- Handles checking the inventory of fruits
- Uses a BigQuery tool call (`query_fruits`) to query the user prompt against the BigQuery table

### 2. **Remote A2A Agent Integration**
- The `recipe_agent` shows how to connect to remote agent services
- Communicates with a separate service via HTTP at `http://localhost:8001/a2a/recipe_agent`
- Demonstrates cross-service agent communication

### 3. **Agent Orchestration**
- The root agent intelligently delegates tasks based on user requests
- Provides clear workflow coordination between multiple agents

