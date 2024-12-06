# 1. correct code

correct_prompt = """Below is an instruction that describes a programming task. Your goal is to generate a correct code to the #Given Instruction#.

#Given Instruction#: {prompt}

#Response#:
"""

# 2. incorrect code

incorrect_prompt = """Below is an instruction that describes a programming task. Your goal is to generate a code solution to the #Given Instruction#.

Your solution MUST contain at least one of the following types of errors:
1. Syntax Error: This type of error occurs when the code violates the grammar rules of the programming language. For example, forgetting to close a parenthesis or a quotation mark, or misspelling a keyword. 
2. Logical Error: These errors sneak into your code when there’s a misunderstanding of the problem you’re solving, leading to incorrect results despite the code running without crashing. For example, calculating the average of a list of numbers by summing them up but forgetting to divide by the count of the numbers.
3. Type Error: This error occurs when an operation is applied to an object of an inappropriate type. For example, attempting to concatenate a string with an integer without converting the integer to a string first.
4. Name Error: This happens when the code attempts to reference a variable or a function name that hasn’t been defined. For example, trying to print a variable that hasn’t been declared.
5. Timeout Error: This error occurs when your code gets stuck in a loop that never ends, either due to a logic flaw or acondition that never becomes false. In programming, such an error can cause your application to hang indefinitely, consuming resources and potentially leading to a crash if not handled properly. For example, writing a loop that waits for a certain condition to change, but the condition is never updated within the loop.

Do not explain the errors in the solution. Just write your thoughts and code as normal. 
Do not mention this is an incorrect solution in any form (e.g., in text/code/comments). Just pretend you are writing the correct code and still not recognizing the errors. 

#Given Instruction#: {prompt}

#Response#:
"""

# 3. score

score_prompt  = """
Please assess the quality of code to the given programming question using 6-point scoring system described below.
Here is the programming question: 
{prompt}
#End of programming question#
Here is the code: 
{ans}
#End of code#
Here is the scoring system:
Rule 1. Basic Functionality: if the code does not have obvious bugs (such as syntax error and logical errors) and demonstrates a basic attempt to solve the problem, give 2 points. Otherwise, give 0 point.
Rule 2. Boundary Check: if the code effectively handles core cases and performs necessary boundary checks, ensuring that the code behaves correctly under different scenarios and input ranges, give 1 point. Otherwise, give 0 point.
Rule 3. Requirement Coverage: if the code covers most of the requirements specified in the task description, fulfilling the core functionality effectively, give 1 point. Otherwise, give 0 point.
Rule 4. Readability and Documentation: if the code is well-organized and readable, with comments explaining critical sections of the code, making it easy to understand by other developers, give 1 point. Otherwise, give 0 point.
Rule 5. Coding Practices: if the code exemplifies best practices in coding standards, including efficiency, error handling, and scalability, clearly reflecting an expert-level understanding and meticulous attention to detail in the implementation, give 1 point. Otherwise, give 0 point.
#End of scoring system#
Firstly, provide a step-by-step analysis for programming question and code, starting with "Code Analysis:"
Next, score the code according the five rules in the scoring system rigorously, following the "Score: Rule 1. Basic Functionality, Rule 2. Boundary Check, Rule 3. Requirement Coverage, Rule 4. Readability and Documentation, Rule 5. Coding Practices."
"""

# 4. create

# 4.1 easy

create_prompt_easy = """I want you to act as an Instruction Creator.
Your goal is to draw inspiration from the #Given Instruction# to create a brand-new and high-quality instruction. Just create the new instruction, Do not provide your solution.
Make the new instruction more rare and different with the #Given Instruction#, but the new instruction should belong to the same domain as the #Given Instruction#.
The length and difficulty level of the new instruction MUST be similar to that of the #Given Instruction#.
The new instruction must be reasonable and must be understood and responded to by humans.

The new instruction should start with "#Created Instruction#:".

#Given Instruction#:
{prompt}

#Created Instruction#:
"""

# 4.2 medium and hard 

create_prompt_medium_hard = """I want you to act as an Instruction Creator.
Your goal is to draw inspiration from the #Given Instruction# to create a brand-new and high-quality instruction.

This new instruction should belong to the same domain and the same task type as the #Given Instruction#
The LENGTH and difficulty level of the #Created Instruction# should be similar to that of the #Given Instruction#.
The #Created Instruction# must be reasonable and must be understood and responded to by humans.

The #Created Instruction# should start with "#Created Instruction#:".

#Given Instruction#:
{prompt}

#Created Instruction#:

"""