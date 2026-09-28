# Day 2 Assignment

## Reasoning and Acting: Comparing Direct Prompting, Chain-of-Thought, and ReAct

---

## 1. Scenario

The scenario used in this assignment is student trip planning.

The student has two travel options:

### Option A
- Travel cost: ₹1500
- Travel time: 5 hours
- Hotel cost: ₹2000

### Option B
- Travel cost: ₹2200
- Travel time: 3 hours
- Hotel cost: ₹2000

The scenario contains questions that require reasoning and calculation.

It also contains a question about current weather, which requires access to an external information source or tool.

---

## 2. Direct Prompting

Direct prompting sends the user's question directly to the language model and asks it to provide an answer.

In this experiment, the model was given the travel information and asked to compare the two options.

The model calculated the total cost of each option and compared their travel times.

Direct prompting did not use an external tool in this implementation. Therefore, it could not obtain current weather information using an external source.

### Advantages

- Simple to implement.
- Fast to execute.
- Suitable for simple questions.
- Requires fewer processing steps.

### Limitations

- Does not use external tools in this implementation.
- Cannot obtain current information such as live weather.
- May be less suitable for tasks requiring multiple external actions.

---

## 3. Chain-of-Thought Style Reasoning

The second approach uses structured, step-by-step reasoning to solve the problem.

The model was asked to calculate the total cost of both travel options and compare their travel times.

### Calculations

Option A:

₹1500 + ₹2000 = ₹3500

Option B:

₹2200 + ₹2000 = ₹4200

Therefore, Option A has the lower total cost.

Option B has the shorter travel time because it requires 3 hours compared with 5 hours for Option A.

The Chain-of-Thought style approach provides a structured explanation of the calculations.

However, in this implementation it did not use an external tool, so it could not obtain current weather information.

### Advantages

- Useful for multi-step calculations.
- Provides a structured solution.
- Makes the calculation easier to follow.

### Limitations

- Does not use external tools in this implementation.
- Cannot independently obtain current weather information.
- May require more processing than direct prompting.

---

## 4. ReAct Agent

The ReAct agent combines reasoning with actions and observations.

In this implementation, the ReAct agent can use a weather tool to obtain current weather information.

The process used by the agent is:

1. The user provides the question.
2. The agent determines that current weather information is required.
3. The agent calls the `get_weather` tool.
4. The weather tool obtains the current weather information.
5. The agent observes the returned information.
6. The agent uses the observation to produce the final answer.

The ReAct approach therefore combines reasoning with interaction with an external tool.

The terminal output demonstrated the action and observation performed by the agent.

### Advantages

- Can use external tools.
- Can obtain current information.
- Combines reasoning with actions.
- Suitable for tasks that require multiple steps and external information.

### Limitations

- More complex to implement.
- Tool calls can increase processing time.
- The result depends partly on the reliability of the external tool.

---

## 5. Comparison Table

| Basis | Direct Prompting | Chain-of-Thought | ReAct Agent |
|---|---|---|---|
| Reasoning depth | Basic/direct reasoning | Structured multi-step reasoning | Reasoning combined with actions |
| Tool usage | No external tool | No external tool in this implementation | Uses external weather tool |
| Reliability on multi-step questions | Suitable for simpler tasks | Useful for multi-step calculations | Useful for multi-step tasks involving tools |
| Transparency | Mainly provides the final answer | Provides a concise step-by-step explanation | Shows tool action and observation |
| Speed / cost | Generally simple and fast | May require more processing | Tool calls add processing overhead |
| Consistency | Can vary depending on temperature | Can vary at non-zero temperature | Can vary depending on reasoning and tool results |

---

## 6. Self-Consistency Observation

The same reasoning question was run five times using a non-zero temperature.

The five outputs were recorded and compared.

The expected correct answer is ₹2000 because:

₹5000 − ₹1200 − ₹800 − ₹1000 = ₹2000.

The results were:

| Run | Answer |
|---|---:|
| Run 1 | ₹2000 |
| Run 2 | ₹2000 |
| Run 3 | ₹2000 |
| Run 4 | ₹2000 |
| Run 5 | ₹2000 |

The majority answer was ₹2000.

The majority answer is correct.

All five runs produced the same answer, showing consistency for this particular question.

At temperature 0, the model is expected to produce more deterministic responses because there is less sampling variation.

---

## 7. Suitability Analysis

### Direct Prompting

Direct prompting is suitable when the problem is simple and all the required information is already available in the prompt.

In this experiment, it was sufficient for calculating and comparing the travel options.

However, it could not obtain current weather information because no external tool was provided.

### Chain-of-Thought

Chain-of-Thought style reasoning is useful when a problem contains several calculation or reasoning steps.

In this experiment, it helped organize the travel-cost calculations and comparison.

However, it did not have access to the weather tool.

### ReAct

ReAct is suitable when the task requires both reasoning and interaction with external tools.

In this experiment, the ReAct agent used the weather tool to obtain current weather information and incorporated the observation into its final answer.

Therefore, ReAct demonstrates an additional capability compared with the other two approaches when external information is required.

---

## 8. Conclusion

The experiment compared Direct Prompting, Chain-of-Thought style reasoning, and ReAct.

Direct Prompting is simple and suitable for straightforward questions where the required information is already available.

Chain-of-Thought style reasoning is useful for problems involving multiple calculation or reasoning steps.

ReAct combines reasoning with actions and external tools. It is useful when a task requires information that is not available directly in the prompt.

The self-consistency experiment also demonstrated how running the same question multiple times with a non-zero temperature can produce multiple responses, which can then be compared to identify a majority answer.

In this experiment, all five runs produced the correct answer of ₹2000, showing consistent results for the selected question.

Overall, the appropriate approach depends on the requirements of the task.