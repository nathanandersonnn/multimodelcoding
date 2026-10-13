import subprocess

# def create_or_write_files
def call_claude_setup(prompt, model_name = "claude-sonnet-5-5"):
    system_instructions = (
        # prompt for delegating 
        "You are the chief engineer delegating a project. "
        "You have 4 models available: 'gemma', 'gemini', 'gpt', 'opus'. "
        "Gemma handles small meaningful roles. Gemini is the safety officer designing tests. "
        "GPT and Opus do heavy lifting, dividing complex code work. "
        "Analyze the project and output a valid JSON array of objects representing your delegation steps. "
        "Do not output markdown code blocks, intro text, or explanations. Output ONLY valid JSON matching this format: "
        '[{"model": "gemma", "role": "helper", "task": "setup headers"}, {"model": "gemini", "role": "tester", "task": "write assertions"}]'
        f"\nProject Prompt: {prompt}"
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
