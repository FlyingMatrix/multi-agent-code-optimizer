from ollama import chat
import utils.config as config

def review_quality(script: str):
    prompt = f"""
                You are a Python code style reviewer.
                Evaluate code readability, maintainability, and adherence to PEP8.
                Suggest improvements for clean code.
                Code:
                {script}
            """
    response = chat(model=config.MODEL, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]
