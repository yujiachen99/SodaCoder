import re
from typing import List, Tuple, Dict
from typing import Optional, Callable, Dict
import ast
import contextlib
import faulthandler
import io
import os
import multiprocessing
import platform
import signal
import tempfile

import json
import subprocess
import os
import tempfile


def execute_cpp(completion: str, timeout: float):

    with tempfile.TemporaryDirectory() as tmpdirname:
        code_path = os.path.join(tmpdirname, "code.cpp")
        exec_path = os.path.join(tmpdirname, "exec")

        with open(code_path, "w") as file:
            file.write(completion)

        compile_result = subprocess.run(["g++", code_path, "-o", exec_path], capture_output=True)
        if compile_result.returncode != 0:
            try: 
                output = compile_result.stderr.decode('utf-8')
            except UnicodeDecodeError:
                output = compile_result.stderr.decode('latin1')

            return {"passed":False , "result": f"compile_error: {output}"}
            # return {"output": compile_result.stderr, "error": True, "type": "compile_error"}

    
        try:
            exec_result = subprocess.run([exec_path], capture_output=True, timeout=timeout)  # 使用timeout参数
            if exec_result.returncode == 0:

                try: 
                    output = exec_result.stdout.decode('utf-8')
                except UnicodeDecodeError:
                    output = exec_result.stdout.decode('latin1')

                return {"passed":True , "result":output}
                # return {"output": exec_result.stdout, "error": False, "type": "success"}
            else:

                try: 
                    output = exec_result.stderr.decode('utf-8')
                except UnicodeDecodeError:
                    output = exec_result.stderr.decode('latin1')

                return {"passed":False , "result":f"runtime_error: {output}"}
                # return {"output": exec_result.stderr, "error": True, "type": "runtime_error"}
        except subprocess.TimeoutExpired:
            return {"passed":False , "result":"Execution timed out"}
            # return {"output": "Execution timed out", "error": True, "type": "timeout"}

def execute_c(completion: str, timeout: float):

    with tempfile.TemporaryDirectory() as tmpdirname:
        code_path = os.path.join(tmpdirname, "code.c")
        exec_path = os.path.join(tmpdirname, "exec")

       
        with open(code_path, "w") as file:
            file.write(completion)

       
        compile_result = subprocess.run(["gcc", code_path, "-o", exec_path], capture_output=True)
        if compile_result.returncode != 0:
            try: 
                output = compile_result.stderr.decode('utf-8')
            except UnicodeDecodeError:
                output = compile_result.stderr.decode('latin1')
          
            return {"passed":False , "result": f"compile_error: {output}"}
            # return {"output": compile_result.stderr, "error": True, "type": "compile_error"}
    
        try:
            exec_result = subprocess.run([exec_path], capture_output=True, timeout=timeout)  # 使用timeout参数
            try: 
                output = exec_result.stdout.decode('utf-8')
            except UnicodeDecodeError:
                output = exec_result.stdout.decode('latin1')

            if exec_result.returncode == 0:
                return {"passed":True , "result":output}
                # return {"output": exec_result.stdout, "error": False, "type": "success"}
            else:
                try: 
                    output = exec_result.stderr.decode('utf-8')
                except UnicodeDecodeError:
                    output = exec_result.stderr.decode('latin1')
                return {"passed":False , "result":f"runtime_error: {output}"}
                # return {"output": exec_result.stderr, "error": True, "type": "runtime_error"}
        except subprocess.TimeoutExpired:
            return {"passed":False , "result":"Execution timed out"}
            # return {"output": "Execution timed out", "error": True, "type": "timeout"}

def execute_java(completion: str, timeout: float):
    
    def extract_class_name(completion):
    
        match = re.search(r'public\s+class\s+(\w+)', completion)
        if match:
            return match.group(1)  
        return None
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        class_name = extract_class_name(completion)
        if not class_name:
            
            return {"passed":False , "result":"compile_error: No public class name found in the provided Java code."}
        
       

        code_path = os.path.join(tmpdirname, f"{class_name}.java")
        
        with open(code_path, "w",encoding='utf-8') as file:
            file.write(completion)

        
        compile_result = subprocess.run(["javac", code_path], capture_output=True)
        if compile_result.returncode != 0:

            try: 
                output = compile_result.stderr.decode('utf-8')
            except UnicodeDecodeError:
                output = compile_result.stderr.decode('latin1')

            return {"passed":False , "result": f"compile_error: {output}"}
            # return {"output": compile_result.stderr, "error": True, "type": "compile_error"}
        
        
        try:
            exec_result = subprocess.run(["java", "-cp", tmpdirname, class_name], capture_output=True, timeout=timeout)
            if exec_result.returncode == 0:
                try: 
                    output = exec_result.stdout.decode('utf-8')
                except UnicodeDecodeError:
                    output = exec_result.stdout.decode('latin1')
                # return {"output": exec_result.stdout, "error": False, "type": "success"}
                return {"passed":True , "result":output}
            else:
                # return {"output": exec_result.stderr, "error": True, "type": "runtime_error"}

                try: 
                    output = exec_result.stderr.decode('utf-8')
                except UnicodeDecodeError:
                    output = exec_result.stderr.decode('latin1')

                return {"passed":False , "result":f"runtime_error: {output}"}
        except subprocess.TimeoutExpired:
            # return {"output": "Execution timed out", "error": True, "type": "timeout"}
            return {"passed":False , "result":"timeout"}

def execute_python(completion: str, timeout: float) -> Dict:
    """
    Evaluates the functional correctness of a completion by running the test
    suite provided in the problem. 

    :param completion_id: an optional completion ID so we can match
        the results later even if execution finishes asynchronously.
    """

    def unsafe_execute():

        with create_tempdir():

            # These system calls are needed when cleaning up tempdir.
            import os
            import shutil
            rmtree = shutil.rmtree
            rmdir = os.rmdir
            chdir = os.chdir

            # Disable functionalities that can make destructive changes to the test.
            reliability_guard()

            # Construct the check program and run it.
            check_program = (
                completion
            )

            try:
                exec_globals = {}
                with swallow_io():
                    with time_limit(timeout):
# WARNING
# This program exists to execute untrusted model-generated code. Although
# it is highly unlikely that model-generated code will do something overtly
# malicious in response to this test suite, model-generated code may act
# destructively due to a lack of model capability or alignment.
# Users are strongly encouraged to sandbox this evaluation suite so that it 
# does not perform destructive actions on their host or network. For more 
# information on how OpenAI sandboxes its code, see the accompanying paper.
# Once you have read this disclaimer and taken appropriate precautions, 
# uncomment the following line and proceed at your own risk:
                        exec(check_program, exec_globals)
                result.append("passed")
            except TimeoutException:
                result.append("timed out")
            except BaseException as e:
                result.append(f"failed: {e}")

            # Needed for cleaning up.
            shutil.rmtree = rmtree
            os.rmdir = rmdir
            os.chdir = chdir

    manager = multiprocessing.Manager()
    result = manager.list()

    p = multiprocessing.Process(target=unsafe_execute)
    p.start()
    p.join(timeout=timeout + 1)
    if p.is_alive():
        p.kill()

    if not result:
        result.append("timed out")

    return dict(
        passed=result[0] == "passed",
        result=result[0]
    )

def execute_go(completion: str, timeout: float):

    with create_tempdir():
        open(f"main_test.go", 'w').write(completion)
        
        try:
            exec_result = subprocess.run(["go", "test", f"-timeout={timeout}s", "main_test.go"], timeout=timeout, capture_output=True)  # 使用timeout参数
            if exec_result.returncode == 0:

                try: 
                    output = exec_result.stdout.decode('utf-8')
                except UnicodeDecodeError:
                    output = exec_result.stdout.decode('latin1')

                return {"passed":True , "result":output}
                # return {"output": exec_result.stdout, "error": False, "type": "success"}
            else:

                try: 
                    output = exec_result.stderr.decode('utf-8')
                except UnicodeDecodeError:
                    output = exec_result.stderr.decode('latin1')

                return {"passed":False , "result":f"runtime_error: {output}"}
                # return {"output": exec_result.stderr, "error": True, "type": "runtime_error"}
        except subprocess.TimeoutExpired:
            return {"passed":False , "result":"Execution timed out"}
            # return {"output": "Execution timed out", "error": True, "type": "timeout"}

def execute_js(completion: str, timeout: float):

    with create_tempdir():
        open(f"test.js", 'w').write(completion)

        # Run program.
        try:
            exec_result =  subprocess.run(["node", "test.js"], timeout=timeout, capture_output=True)
        
            if exec_result.returncode == 0:

                try: 
                    output = exec_result.stdout.decode('utf-8')
                except UnicodeDecodeError:
                    output = exec_result.stdout.decode('latin1')

                return {"passed":True , "result":output}
                # return {"output": exec_result.stdout, "error": False, "type": "success"}
            else:

                try: 
                    output = exec_result.stderr.decode('utf-8')
                except UnicodeDecodeError:
                    output = exec_result.stderr.decode('latin1')

                return {"passed":False , "result":f"runtime_error: {output}"}
                # return {"output": exec_result.stderr, "error": True, "type": "runtime_error"}
        except subprocess.TimeoutExpired:
            return {"passed":False , "result":"Execution timed out"}
            # return {"output": "Execution timed out", "error": True, "type": "timeout"}


@contextlib.contextmanager
def time_limit(seconds: float):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    signal.setitimer(signal.ITIMER_REAL, seconds)
    signal.signal(signal.SIGALRM, signal_handler)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)


@contextlib.contextmanager
def swallow_io():
    stream = WriteOnlyStringIO()
    with contextlib.redirect_stdout(stream):
        with contextlib.redirect_stderr(stream):
            with redirect_stdin(stream):
                yield


@contextlib.contextmanager
def create_tempdir():
    with tempfile.TemporaryDirectory() as dirname:
        with chdir(dirname):
            yield dirname


class TimeoutException(Exception):
    pass


class WriteOnlyStringIO(io.StringIO):
    """ StringIO that throws an exception when it's read from """

    def read(self, *args, **kwargs):
        raise IOError

    def readline(self, *args, **kwargs):
        raise 
