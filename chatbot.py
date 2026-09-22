"""System 1: Plain chatbot.

The LLM does not receive private computer-lab data.
"""

from config import client, MODEL, QUESTIONS, banner


SYSTEM_PROMPT = """You are a helpful college computer lab assistant.

Answer the user's questions clearly and concisely.

You do not have access to the college's private
computer-lab database.

If you do not know a specific fact, say that you do not know.
"""


banner("SYSTEM 1 — PLAIN CHATBOT")


for question in QUESTIONS:

    response = client.chat.completions.create(
        model=MODEL,

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ],

        temperature=0
    )

    answer = response.choices[0].message.content.strip()

    print(f"Q: {question}")
    print(f"A: {answer}")
    print()