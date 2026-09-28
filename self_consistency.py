import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

question = """
A student has ₹5000.

They spend:
- ₹1200 on books
- ₹800 on food
- ₹1000 on travel

How much money is left?
Show the calculation clearly.
"""

print("===== SELF-CONSISTENCY EXPERIMENT =====")

answers = []

for i in range(5):
    response = client.chat.completions.create(
        model=os.getenv("MODEL", "openai/gpt-oss-20b"),
        messages=[
            {
                "role": "system",
                "content": "Solve the problem carefully and give a concise step-by-step explanation."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.7
    )

    answer = response.choices[0].message.content

    print(f"\nRUN {i + 1}:")
    print(answer)

    answers.append(answer)

print("\n===== OBSERVATION =====")
print("The five runs are recorded above.")
print("The expected correct numerical answer is ₹2000.")
print("Compare the five responses and identify the majority answer.")
print("At temperature 0, the model is expected to be more deterministic.")