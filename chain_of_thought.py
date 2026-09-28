import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

scenario = """
You are helping a student plan a trip.

Option A:
- Travel cost: ₹1500
- Travel time: 5 hours
- Hotel cost: ₹2000

Option B:
- Travel cost: ₹2200
- Travel time: 3 hours
- Hotel cost: ₹2000

Solve these questions:

1. Calculate the total cost of Option A.
2. Calculate the total cost of Option B.
3. Identify which option is cheaper.
4. Identify which option has the shorter travel time.
5. Explain your answer using clear numbered steps.
6. Explain why you cannot provide CURRENT weather information
   without access to an external information source.
"""

response = client.chat.completions.create(
    model=os.getenv("MODEL", "openai/gpt-oss-20b"),
    messages=[
        {
            "role": "system",
            "content": """
            Solve the problem carefully in multiple steps.
            Give only a concise step-by-step explanation of the
            solution, not hidden internal reasoning.
            Do not use external tools.
            """
        },
        {
            "role": "user",
            "content": scenario
        }
    ]
)

print("===== CHAIN-OF-THOUGHT STYLE =====")
print(response.choices[0].message.content)