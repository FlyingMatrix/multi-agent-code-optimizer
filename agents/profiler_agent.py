from ollama import chat
import utils.config as config

def profile_estimation(script: str):
    prompt = f"""
                You are a Python runtime profiler.
                Estimate how this script will behave in terms of CPU and memory usage.
                Point out potential bottlenecks and scalability concerns.
                Code:
                {script}
            """
    response = chat(model=config.MODEL, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]
