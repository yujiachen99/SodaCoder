
prompt = """
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
