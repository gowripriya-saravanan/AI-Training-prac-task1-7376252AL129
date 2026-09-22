"""System 2: Rule-based workflow.

Uses fixed Python rules and private computer-lab data.
It does not use an LLM.
"""

from config import COMPUTERS, QUESTIONS, banner


def get_available_computers():

    result = []

    for pc_id, info in COMPUTERS.items():

        if info["status"] == "Available":
            result.append(pc_id)

    return result


def get_16gb_computers():

    result = []

    for pc_id, info in COMPUTERS.items():

        if (
            info["status"] == "Available"
            and info["ram"] >= 16
        ):
            result.append(pc_id)

    return result


def calculate_total_ram():

    total = 0

    for info in COMPUTERS.values():

        if info["status"] == "Available":
            total += info["ram"]

    return total


def find_ml_computers():

    result = []

    for pc_id, info in COMPUTERS.items():

        if (
            info["status"] == "Available"
            and info["ram"] >= 16
            and "SSD" in info["storage"]
        ):
            result.append(pc_id)

    return result


def answer_question(question):

    question = question.lower()


    # Question 1

    if "currently available" in question:

        computers = get_available_computers()

        return (
            "Available computers: "
            + ", ".join(computers)
        )


    # Question 2

    elif "at least 16 gb ram" in question:

        computers = get_16gb_computers()

        return (
            "Available computers with at least "
            "16 GB RAM: "
            + ", ".join(computers)
        )


    # Question 3

    elif "total" in question and "ram" in question:

        total = calculate_total_ram()

        return (
            f"Total RAM on available computers: "
            f"{total} GB"
        )


    # Question 4

    elif (
        "python" in question
        and "machine learning" in question
    ):

        computers = find_ml_computers()

        return (
            "Suitable available computers: "
            + ", ".join(computers)
        )


    else:

        return (
            "Sorry, I can only answer questions "
            "covered by my predefined rules."
        )


banner("SYSTEM 2 — RULE-BASED WORKFLOW")


for question in QUESTIONS:

    answer = answer_question(question)

    print(f"Q: {question}")
    print(f"A: {answer}")
    print()