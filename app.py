import ollama
import os

# def create_or_write_files

def gemma(role, task):
    response = ollama.generate(model='gemma4:e4b', prompt=role+''+task)
    print(response['response'])
def main():
    gemma("engineer", "say hi")
if __name__ == "__main__":
    main()