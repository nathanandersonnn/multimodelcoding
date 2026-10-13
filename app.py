import json
from delegate import call_claude_setup
from models import opus, gemini, gemma, gpt



def main():
    # begin creating plans for various models
    print("Asking claude to delegate tasks...")
    raw_plan = call_claude_setup("Generate a wordle game in c++")
    print(raw_plan)
    if raw_plan == "[]":
        print("Failed to fetch a valid plan")
        return 
    try:
        # load, map the model routes from json to their respective models
        plan = json.loads(raw_plan)
        model_mapping = {
            "gemma": gemma,
            "gemini": gemini,
            "gpt": gpt,
            "opus": opus
        }
        # begin parsing the json recieved, and assigning it to 
        for step in plan:
            target_model = step.get("model", "").lower()
            role = step.get("role", "")
            task = step.get("task", "")
            if target_model in model_mapping:
                model_mapping[target_model](role, task)
            else:
                print(f"Unknown model assignment skipped: {target_model}")
    except json.JSONDecodeError:
        print("Error: response not clean JSON")
        print(raw_plan)
if __name__ == "__main__":
    main()