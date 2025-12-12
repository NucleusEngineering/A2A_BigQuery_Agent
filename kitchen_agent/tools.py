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

import json
from google.cloud import bigquery


def query_fruits(query: str) -> dict:
    """Executes a Google Standard SQL query against the fruits table.

    Args:
        query (str): The Google Standard SQL query to execute.

    Returns:
        dict: A dictionary containing the query results.
    """
    print(f"Executing query: {query}")
    try:
        client = bigquery.Client()
        query_job = client.query(query)
        results = query_job.result()  # Waits for the job to complete.

        records = [dict(row) for row in results]

        return {
            "status": "success",
            "results": records,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }

schema_fruits = json.dumps(
  [
    {
      "name": "name",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "quantity",
      "type": "INTEGER",
      "mode": "NULLABLE"
    }
  ]
)