import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

scenario = """
You are helping a student plan a trip.

The student has two travel options:

Option A:
- Travel cost: ₹1500
- Travel time: 5 hours
- Hotel cost: ₹2000

Option B:
- Travel cost: ₹2200
- Travel time: 3 hours
- Hotel cost: ₹2000

Answer these questions:
1. Which option has the lower total cost?
2. Which option has the shorter travel time?
3. Explain the comparison briefly.
4. Can you provide the current weather at the destination without using an external tool?
"""

response = client.chat.completions.create(
    model=os.getenv("MODEL", "openai/gpt-oss-20b"),
    messages=[
        {
            "role": "system",
            "content": "Answer directly. Do not use external tools."
        },
        {
            "role": "user",
            "content": scenario
        }
    ]
)

print("===== DIRECT PROMPTING =====")
print(response.choices[0].message.content)