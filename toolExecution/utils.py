import re
from typing import List, Tuple, Dict
from typing import Optional, Callable, Dict

def extract_code_blocks(content: str) -> Tuple[bool, str]:

    pattern_1 = re.escape("```python\n") + r"(.*?)" + re.escape("```")
    matches_1 = re.findall(pattern_1, content, re.DOTALL|re.IGNORECASE)
    if matches_1:
        return True, matches_1[0].strip()

    pattern_2 = re.escape("```cpp\n")  + r"(.*?)" + re.escape("```")
    matches_2 = re.findall(pattern_2, content, re.DOTALL|re.IGNORECASE)
    if matches_2:
        return True, matches_2[0].strip()

    pattern_3= re.escape("```java\n")  + r"(.*?)" + re.escape("```")
    matches_3 = re.findall(pattern_3, content, re.DOTALL|re.IGNORECASE)
    if matches_3:
        return True, matches_3[0].strip()

    pattern_4= re.escape("```c\n") + r"(.*?)" + re.escape("```")
    matches_4 = re.findall(pattern_4, content, re.DOTALL|re.IGNORECASE)
    if matches_4:
        return True, matches_4[0].strip()
    
    pattern_5= re.escape("```c\n") + r"(.*?)" + re.escape("```")
    matches_5 = re.findall(pattern_5, content, re.DOTALL|re.IGNORECASE)
    if matches_5:
        return True, matches_5[0].strip()

    pattern_6= re.escape("```go\n") + r"(.*?)" + re.escape("```")
    matches_6 = re.findall(pattern_6, content, re.DOTALL|re.IGNORECASE)
    
    
    if matches_6:
        return True, matches_6[0].strip()

    return False, ""

def check_complete(content: str):

    start = content.find("```")
    if start != -1:
        end = content.find("```",start+10)
        if end != -1:
            return True
        else:
            return False
    else:
        return True
    
def judge_pl(content: str):
    pattern_1 = re.escape("```python\n") + r"(.*?)"
    matches_1 = re.findall(pattern_1, content, re.DOTALL|re.IGNORECASE)
    
    pattern_2 = re.escape("```cpp\n") + r"(.*?)"
    matches_2 = re.findall(pattern_2, content, re.DOTALL|re.IGNORECASE)

    pattern_3= re.escape("```java\n") + r"(.*?)"
    matches_3 = re.findall(pattern_3, content, re.DOTALL|re.IGNORECASE)

    pattern_4= re.escape("```c\n") + r"(.*?)"
    matches_4 = re.findall(pattern_4, content, re.DOTALL|re.IGNORECASE)

    pattern_5= re.escape("```go\n") + r"(.*?)"
    matches_5 = re.findall(pattern_5, content, re.DOTALL|re.IGNORECASE)

    pattern_6= re.escape("```javascript\n") + r"(.*?)"
    matches_6 = re.findall(pattern_6, content, re.DOTALL|re.IGNORECASE)

    if matches_1:
        return "python"
    elif matches_2:
        return "cpp"
    elif matches_3:
        return "java"
    elif matches_4:
        return "c"
    elif matches_5:
        return "go"
    elif matches_6:
        return "javascript"
    else:
        return "other"
