import os
import re
from utils.orchestrator import run_all_agents
from agents.coordinator_agent import summarize_results

# folder containing the Python scripts
CODE_FOLDER = "code_to_review"

def extract_python_code(ai_output: str) -> str:
    """
    Extract only the Python code from the AI agent output.
    Removes markdown, explanations, and text outside code blocks.
    """
    # match code blocks with ```python ... ``` or ``` ... ```
    code_blocks = re.findall(r"```(?:python)?\s*(.*?)```", ai_output, re.DOTALL)
    if code_blocks:
        return "\n\n".join(code_blocks).strip()
    # if no markdown code block is found, return the full output
    return ai_output.strip()

if __name__ == "__main__":

    # loop through all files in the folder
    for filename in os.listdir(CODE_FOLDER):
        if filename.endswith(".py"):
            file_path = os.path.join(CODE_FOLDER, filename)

            # read the original python file
            with open(file_path, "r", encoding="utf-8") as f:
                code_to_check = f.read()
            print(f"\nProcessing file: {filename}\n")

            results = run_all_agents(code_to_check)

            print("\n======== AI Agent Report ========\n")
            for section, output in results.items():
                print(f"\n--- {section} ---\n{output}\n")

            summary = summarize_results(results)
            print("\n======== Final Summary ========\n", summary)

            # if the "Optimized Code" is available, save it as a new file
            if "Optimized Code" in results:
                optimized_code = extract_python_code(results["Optimized Code"])
                base_name, ext = os.path.splitext(filename)
                optimized_file_path = os.path.join(CODE_FOLDER, f"{base_name}_optimized.py")

                with open(optimized_file_path, "w", encoding="utf-8") as f:
                    f.write(optimized_code)
                print(f"Optimized code saved to: {optimized_file_path}")

        else:
            print(f"Skipping non-Python file: {filename}")  
