prompt = """
Review the task description and the corresponding code snippet using the additive 6-point scoring system described below. Points are accumulated based on the satisfaction of each criterion:

- Basic Functionality (2 points): Add two points if the code runs without errors and demonstrates a basic attempt to solve the problem, even if it is incomplete or contains some bugs.
- Boundary Check (1 point): Add another point if the code effectively handles core cases and performs necessary boundary checks, ensuring that the code behaves correctly under different scenarios and input ranges.
- Requirement Coverage (1 point): Award a third point if the code covers most of the requirements specified in the task description, fulfilling the core functionality effectively, regardless of minor inefficiencies or lack of advanced features.
- Readability and Documentation (1 point): Grant a fourth point if the code is well-organized and readable, with comments explaining critical sections of the code, making it easy to understand by other developers, even if there are minor areas lacking documentation.
- Excellence in Coding Practices (1 point): Bestow a fifth point if the code exemplifies best practices in coding standards, including efficiency, error handling, and scalability, clearly reflecting an expert-level understanding and meticulous attention to detail in the implementation.

Task: {DESCRIPTION}

<code> {CODE} </code>

After examining the task descriptionand the corresponding code:
- Briefly justify your total score, up to 100 words.
- Conclude with the score using the format: "Score: <total points>"

The output format:
```json
{
    "score":"total points",
    "justification":"your reason up to 100 words."
}
```

"""