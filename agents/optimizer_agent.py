from ollama import chat
import utils.config as config

def suggest_optimizations(script: str):
    prompt = f"""
                You are a Python performance engineer.
                Suggest optimizations to make this script faster or more memory-efficient.
                Focus on algorithmic improvements and Python best practices.
                Code:
                {script}
            """
    response = chat(model=config.MODEL, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]
