"""Tools available to the AI agent."""

from config import COMPUTERS


def get_computer_info(pc_id):

    pc_id = pc_id.upper()

    if pc_id not in COMPUTERS:

        return {
            "error": f"Computer {pc_id} was not found."
        }

    return {
        "computer_id": pc_id,
        **COMPUTERS[pc_id]
    }


def get_available_computers():

    result = []

    for pc_id, info in COMPUTERS.items():

        if info["status"] == "Available":

            result.append({
                "computer_id": pc_id,
                **info
            })

    return result


def calculator(expression):

    allowed_characters = "0123456789+-*/(). "

    if not all(
        character in allowed_characters
        for character in expression
    ):

        return {
            "error": "Invalid characters in expression."
        }

    try:

        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return {
            "expression": expression,
            "result": result
        }

    except Exception as error:

        return {
            "error": str(error)
        }


TOOL_FUNCTIONS = {
    "get_computer_info": get_computer_info,
    "get_available_computers": get_available_computers,
    "calculator": calculator
}