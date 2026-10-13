import ollama
import subprocess
import os

local_env = os.environ.copy()

# calls a locally run gemma model to help complete simple tasks
def gemma(role, task):
    try:
        print(f"\n Currently running gemma on {task} with role {role}")
        response = ollama.generate(model='gemma4:e4b', prompt=f"Role: {role} + Task: {task}")
        print(response['response'])
    except Exception as e:
        print(f"\nOllama execution error: {e}")
    
def gemini(role, task): print(role, task)

def gpt(role, task): print(role, task)

def opus(role, task):
    model="claude-opus-5-5"
    # Allow opus to run on auto, with max turns to prevent infinite loops
    cmd = [
        "claude",
        "--model",
        model,
        "-p",
        task + '' + role,
        "--allowedTools", "All",
        "--permission-mode", "auto",
        "--max-turns", "15"
    ]
    result = subprocess.run(
    cmd, 
    capture_output=True, 
    text=True, 
    check=True, 
    env=local_env
    )
    return result.stdout.strip()