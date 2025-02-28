
# easy

prompt_easy = """I want you to act as an Instruction Creator.
Your goal is to draw inspiration from the #Given Instruction# to create a brand-new and high-quality instruction. Just create the new instruction, Do not provide your solution.
Make the new instruction more rare and different with the #Given Instruction#, but the new instruction should belong to the same domain as the #Given Instruction#.
The length and difficulty level of the new instruction MUST be similar to that of the #Given Instruction#.
The new instruction must be reasonable and must be understood and responded to by humans.

The new instruction should start with "#Created Instruction#:".

#Given Instruction#:
{prompt}

#Created Instruction#:
"""

# medium and hard 

prompt_medium_hard = """I want you to act as an Instruction Creator.
Your goal is to draw inspiration from the #Given Instruction# to create a brand-new and high-quality instruction.

This new instruction should belong to the same domain and the same task type as the #Given Instruction#
The LENGTH and difficulty level of the #Created Instruction# should be similar to that of the #Given Instruction#.
The #Created Instruction# must be reasonable and must be understood and responded to by humans.

The #Created Instruction# should start with "#Created Instruction#:".

#Given Instruction#:
{prompt}

#Created Instruction#:

"""