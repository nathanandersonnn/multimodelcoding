import ollama
import subprocess
import sys
import os

# def create_or_write_files
def call_claude_setup(prompt, model_name = "claude-opus-5-5"):

    system_instructions = (
        "You are the chief engineer delegating a project. "
        "You have 4 models available: 'gemma', 'gemini', 'gpt', 'opus'. "
        "Gemma handles small meaningful roles. Gemini is the safety officer designing tests. "
        "GPT and Opus do heavy lifting, dividing complex code work. "
        "Analyze the project and output a valid JSON array of objects representing your delegation steps. "
        "Do not output markdown code blocks, intro text, or explanations. Output ONLY valid JSON matching this format: "
        '[{"model": "gemma", "role": "helper", "task": "setup headers"}, {"model": "gemini", "role": "tester", "task": "write assertions"}]'
        f"\n\nProject Prompt: {prompt}"
    )

    cmd = ["claude", 
           "--model", 
           model_name, 
           "-p", 
           system_instructions, 
           "--allowedTools", 
           "Read"]
    
    result = subprocess.run(cmd, capture_output = True, text = True, check = True)
    return result.stdout.strip()





# calls a locally run gemma model to help complete tasks
def gemma(role, task):
    response = ollama.generate(model='gemma4:e4b', prompt=role+''+task)
    print(response['response'])

def main():
    print("Asking claude to delegate tasks...")
    raw_plan = call_claude_setup("Generate a wordle game in c++")
    print(raw_plan)
if __name__ == "__main__":
    main()