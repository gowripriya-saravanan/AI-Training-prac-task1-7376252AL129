# College Computer Lab Assistant
## Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

This project demonstrates three different approaches for building a College Computer Lab Assistant. The scenario uses a small private computer-lab dataset containing computer IDs, RAM, storage type, operating system, and current availability status.

The private dataset contains five computers: PC01, PC02, PC03, PC04, and PC05. The system is designed to answer questions about computer availability and specifications.

Example questions include which computers are currently available, which available computers have at least 16 GB RAM, the total RAM of available computers, and which available computer may be suitable for Python and machine learning.

The computer-lab information is treated as private data. The three approaches differ mainly in how they access and use this information.

## 2. Plain Chatbot

The plain chatbot uses a Large Language Model (LLM) to understand and respond to user questions. It does not receive the private computer-lab dataset and does not have access to any tools.

The chatbot can generate natural-language responses and handle questions flexibly. However, because the private computer information is not provided to it, it cannot reliably answer questions that require the actual lab data.

For example, if a user asks which computers are currently available, the chatbot does not have access to the actual lab records. It can provide a general response, but it cannot verify the current status of the computers.

The main advantage of the plain chatbot is its ability to communicate naturally. Its main limitation in this scenario is the lack of access to private data.

## 3. Rule-Based Workflow

The rule-based workflow does not use an LLM. Instead, it uses predefined Python functions and conditional statements to process the user's questions.

The workflow has direct access to the private computer-lab data. For example, it can check which computers have the status "Available" and which available computers have at least 16 GB of RAM.

Because the workflow uses fixed rules, its results are predictable for the questions that have been programmed. This makes it easier to control how the private data is processed.

However, the workflow is less flexible when a user asks a new question that is not covered by the predefined rules. In that situation, the program must be modified by adding new rules or functions.

Therefore, the rule-based workflow is useful for clearly defined and predictable tasks.

## 4. AI Agent

The AI agent combines an LLM with private-data tools and a multi-step loop.

The agent can use tools to access the private computer-lab information. The tools used in this project include `get_computer_info`, `get_available_computers`, and `calculator`.

The agent follows a reason, act, and observe process. First, the LLM interprets the user's request. It can then select an appropriate tool, receive the tool result, and continue processing until it has enough information to provide a final answer.

For example, when the user asks about available computers, the agent can call the `get_available_computers` tool. When a calculation is required, it can use the calculator tool.

This makes the agent capable of handling more flexible requests than a fixed workflow. The agent can combine information from tools and perform multiple steps before producing its final response.

## 5. Comparison

| Criterion | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | High for language | Low | High |
| Decision-making | LLM-generated response | Fixed rules | LLM-based tool selection |
| Tool usage | No | No | Yes |
| Private-data access | No | Yes | Yes, through tools |
| Multi-step task handling | Limited | Limited to programmed steps | Yes |
| Automation | Basic conversation | Fixed automated tasks | Dynamic automated tasks |
| Reliability | May lack private facts | Predictable for programmed cases | Depends on model and tools |

## 6. Flexibility

The plain chatbot can understand many types of natural-language questions because it uses an LLM. However, its flexibility is limited by the fact that it does not have access to the private computer-lab information.

The rule-based workflow has lower flexibility because the questions and processing steps are predefined in Python. If a new type of question is introduced, additional rules may be required.

The AI agent provides flexible interaction because the LLM can interpret the user's request and decide which available tool should be used. It can therefore handle different combinations of private information and calculations.

## 7. Decision-Making

The plain chatbot generates responses using the LLM but does not make decisions using the private computer-lab data.

The rule-based workflow makes decisions using predefined conditions. For example, it can check whether a computer's status is "Available" or whether its RAM is at least 16 GB.

The AI agent uses the LLM to determine which tool should be called and what information is needed. The result from the tool can then be used for the next step.

## 8. Tool Usage

The plain chatbot does not use external tools in this project.

The rule-based workflow uses Python functions to process the private data, but it does not have an LLM deciding dynamically which tool to use.

The AI agent uses tools dynamically. The available tools include a computer-information tool, an available-computers tool, and a calculator tool.

This allows the agent to perform actions instead of only generating text.

## 9. Private-Data Access

The plain chatbot does not have access to the private computer-lab dataset.

The rule-based workflow directly accesses the private computer-lab data stored in the project.

The AI agent accesses private information through controlled tools. This means the LLM does not need direct access to the complete private dataset. Instead, it can request the information required for the current task through the available tools.

## 10. Multi-Step Task Handling

The plain chatbot can explain a multi-step process in natural language, but in this project it does not have access to the tools or private data required to actually perform the steps.

The rule-based workflow can perform multiple programmed operations, but those operations must be defined in advance.

The AI agent can perform multiple steps dynamically. For example, it can retrieve available computers, examine their RAM values, and use the information to answer a more complex question.

## 11. Automation

The plain chatbot mainly provides conversational responses.

The rule-based workflow can automatically perform predefined tasks whenever the corresponding rules are triggered.

The AI agent provides dynamic automation because it can interpret a user's request, select tools, process tool results, and continue until the task is completed.

## 12. Reliability

The plain chatbot may not be reliable for private-data questions because it does not have access to the actual computer-lab records.

The rule-based workflow provides predictable results for the questions and conditions that have been explicitly programmed. Its reliability depends on the correctness of the rules and private data.

The AI agent can provide useful answers by retrieving current information through tools. However, its reliability depends on the correctness of the private data, the tools, and the LLM's tool selection and interpretation.

## 13. Suitability Analysis

For this chosen computer-lab scenario, the three approaches provide different capabilities.

The plain chatbot is useful when the task mainly requires general conversation and does not depend on private computer-lab information. Since it does not have access to the private dataset, it is not designed to provide reliable answers about the actual computers in the lab.

The rule-based workflow is useful for predefined computer-lab questions. Since its rules directly operate on the private dataset, its answers are predictable for the cases covered by the program. However, adding every possible user question would require adding more rules.

The AI agent is suitable when the assistant must handle flexible requests over private lab data and may need multiple tool calls. This conclusion follows from the comparison because the AI agent combines private-data access, tool usage, flexible decision-making, and multi-step task handling.

The rule-based workflow remains appropriate for a fixed set of highly predictable queries, while the plain chatbot is appropriate when private lab facts are not required.

## 14. Conclusion

A plain chatbot is suitable for general conversation and tasks that do not require access to private structured data.

A rule-based workflow is suitable when tasks are clearly defined and predictable results are important. It provides direct control over how the private data is processed.

An AI agent is suitable when the system needs an LLM to understand flexible user requests, access private information through tools, and perform multiple steps before producing an answer.

For the College Computer Lab Assistant scenario, the AI agent is the most suitable approach when the main requirement is to handle flexible user requests over private lab data while using tools for information retrieval and calculations.

The three approaches therefore demonstrate different levels of flexibility, control, private-data access, and automation. The appropriate approach depends on the requirements of the application.