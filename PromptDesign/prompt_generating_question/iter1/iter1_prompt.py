
prompt = """I want you to act as an Instruction Creator. 
Your goal is to draw inspiration from the #Given Instruction# to create a brand-new and high-quality instruction.

Here is some steps you should follow: 
1. Analyze and summarize the #Given Instruction#'s design approach and purpose.
2. Use this as inspiration to create a new coding problem in a real-world scenario. It should contain a similar core concept but include some additional or more complex logic to make it more challenging and engaging.
3. Clearly describe the #Created Instruction#, including its background, requirements, and input-output format.
4. The #Created Instruction# must be reasonable and must be understood and responded to by humans.
5. Make sure the #Created Instruction# helps practice coding logic and problem-solving skills.

#Given Instruction#:
{prompt}

#Created Instruction#:

"""