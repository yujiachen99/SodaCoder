import json
from utils import *
from checks import *

file_path= "./data/example_data.jsonl"
file_path_output = "./data/example_data_exe.jsonl"

with open(file_path,'r',encoding='utf-8') as f, open(file_path_output,'w',encoding='utf-8') as f1:
    for idx,item in enumerate(f):
        print(idx)      
        data = json.loads(item)
        task_id = data["task_id"]
        prompt = data["prompt"]
        generation = data["generation"]
        language = judge_pl(generation)
        if check_complete(generation):
            status, code = extract_code_blocks(generation)
            if status and language == "python":
                execute_res = execute_python(code,timeout=100)
            elif status and language == "cpp":
                execute_res = execute_cpp(code,timeout=100)
            elif status and language == "c":
                execute_res = execute_c(code,timeout=100)
            elif status and language == "java":
                execute_res = execute_java(code,timeout=100)
            elif status and language == "go":
                execute_res = execute_go(code,timeout=100)
            elif status and language == "javascript":
                execute_res = execute_js(code,timeout=100)
            else:
                execute_res = {"passed":"UNKNOWN", "result":"UNKNOWN"}
            res = {"task_id":task_id,"prompt":prompt,"language":language,"generation":generation,"is_complete":True,"execute_res":execute_res}
            f1.write(json.dumps(res, ensure_ascii=False) + "\n")
        else:
            res = {"task_id":task_id,"prompt":prompt,"language":language,"generation":generation,"is_complete":False}
            f1.write(json.dumps(res, ensure_ascii=False) + "\n")