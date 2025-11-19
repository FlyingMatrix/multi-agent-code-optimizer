from ollama import chat
import utils.config as config

def generate_optimized_code(original_script: str, optimizer_suggestions: str):
    prompt = f"""
                You are a Python code generator.
                You are given a Python script and a list of optimization suggestions.
                Your task is to produce a new, fully optimized Python script that implements the suggestions.
                Ensure the functionality remains the same and follow Python best practices.

                Original script:
                {original_script}

                Optimization suggestions:
                {optimizer_suggestions}
            """
    response = chat(model=config.MODEL, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]
