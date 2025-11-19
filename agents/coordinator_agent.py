from ollama import chat
import utils.config as config

def summarize_results(results):
    summary_prompt = f"Summarize the following results:\n{results}"
    response = chat(model=config.MODEL, messages=[{"role": "user", "content": summary_prompt}])
    return response["message"]["content"]
