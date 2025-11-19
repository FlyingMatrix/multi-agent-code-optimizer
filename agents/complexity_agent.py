from ollama import chat
import utils.config as config

def analyze_complexity(script: str):
    prompt = f"""
                You are an algorithm complexity analyst.
                Analyze the following Python code and explain:
                1. Its time complexity.
                2. Its space complexity.
                3. Any inefficient patterns.
                Code:
                {script}
            """
    response = chat(model=config.MODEL, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]
