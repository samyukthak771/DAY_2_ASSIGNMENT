import os
import json
from groq import Groq
from tools import get_weather

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather information for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

messages = [
    {
        "role": "system",
        "content": """
You are a ReAct-style travel assistant.

When current external information is required:
1. Decide which tool is needed.
2. Call the appropriate tool.
3. Observe the tool result.
4. Use the result to produce the final answer.

Do not reveal private internal reasoning.
Briefly describe the action and observation instead.
"""
    },
    {
        "role": "user",
        "content": """
I am planning a trip to Chennai.

My travel options are:

Option A:
- Travel cost: ₹1500
- Travel time: 5 hours
- Hotel cost: ₹2000

Option B:
- Travel cost: ₹2200
- Travel time: 3 hours
- Hotel cost: ₹2000

Tell me:
1. Which option is cheaper?
2. Which option is faster?
3. What is the current weather in Chennai?
"""
    }
]

print("===== ReACT AGENT =====")

while True:

    response = client.chat.completions.create(
        model=os.getenv("MODEL", "openai/gpt-oss-20b"),
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if not message.tool_calls:
        print("\nFINAL ANSWER:")
        print(message.content)
        break

    messages.append(message)

    for tool_call in message.tool_calls:

        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print("\nACTION:")
        print(function_name, arguments)

        if function_name == "get_weather":
            result = get_weather(arguments["city"])

            print("OBSERVATION:")
            print(result)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                }
            )