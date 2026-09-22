"""System 3: AI agent.

Uses:
1. LLM
2. Private-data tools
3. Reason -> Act -> Observe loop
"""

import json

from config import client, MODEL, QUESTIONS, banner
from tools import TOOL_FUNCTIONS


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_computer_info",
            "description": "Get private information about one computer.",
            "parameters": {
                "type": "object",
                "properties": {
                    "pc_id": {
                        "type": "string",
                        "description": "Computer ID such as PC01"
                    }
                },
                "required": ["pc_id"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_available_computers",
            "description": "Get all computers that are currently available.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


SYSTEM_PROMPT = """You are an AI agent for a college computer lab.

You have access to private computer-lab information through tools.

Use the tools when the user's question requires private data.

Do not invent computer information.

When you have enough information, give a clear final answer.

You may use multiple tools when necessary.
"""


def run_agent(question):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    max_steps = 6

    for step in range(1, max_steps + 1):

        print(f"\nAgent step {step}")

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0
        )

        message = response.choices[0].message

        # -----------------------------------------
        # Agent has finished
        # -----------------------------------------

        if not message.tool_calls:

            return message.content.strip()


        # -----------------------------------------
        # Add assistant tool-call message
        # -----------------------------------------

        messages.append(message)


        # -----------------------------------------
        # Execute every requested tool
        # -----------------------------------------

        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name

            raw_arguments = tool_call.function.arguments

            print(f"Tool called: {tool_name}")
            print(f"Raw arguments: {raw_arguments}")


            # Safely convert arguments to dictionary
            try:

                arguments = json.loads(raw_arguments)

            except json.JSONDecodeError:

                arguments = {}


            # -----------------------------------------
            # FIX FOR EMPTY ARGUMENT
            # -----------------------------------------

            if not isinstance(arguments, dict):

                arguments = {}


            if "" in arguments:

                arguments = {}


            print(f"Arguments: {arguments}")


            # -----------------------------------------
            # Find the Python function
            # -----------------------------------------

            function = TOOL_FUNCTIONS.get(tool_name)


            if function is None:

                result = {
                    "error": f"Unknown tool: {tool_name}"
                }


            # get_available_computers() needs NO arguments
            elif tool_name == "get_available_computers":

                result = function()


            # calculator needs expression
            elif tool_name == "calculator":

                if "expression" not in arguments:

                    result = {
                        "error": "Calculator requires an expression."
                    }

                else:

                    result = function(
                        expression=arguments["expression"]
                    )


            # get_computer_info needs pc_id
            elif tool_name == "get_computer_info":

                if "pc_id" not in arguments:

                    result = {
                        "error": "Computer ID is required."
                    }

                else:

                    result = function(
                        pc_id=arguments["pc_id"]
                    )


            else:

                result = {
                    "error": "Unsupported tool."
                }


            print(f"Tool result: {result}")


            # -----------------------------------------
            # Send tool result back to the LLM
            # -----------------------------------------

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                }
            )


    return (
        "The agent reached the maximum number "
        "of steps without completing the task."
    )


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

banner("SYSTEM 3 — AI AGENT")


for question in QUESTIONS:

    print(f"Q: {question}")

    answer = run_agent(question)

    print(f"\nA: {answer}")

    print("\n" + "-" * 60)