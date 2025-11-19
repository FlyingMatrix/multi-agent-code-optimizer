import concurrent.futures
from agents.complexity_agent import analyze_complexity
from agents.optimizer_agent import suggest_optimizations
from agents.profiler_agent import profile_estimation
from agents.quality_agent import review_quality
from agents.code_generator_agent import generate_optimized_code

def run_all_agents(script: str):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            # here in this dict, keys are Future objects (each representing an asynchronous task)
            executor.submit(analyze_complexity, script): "Complexity Analysis",
            executor.submit(suggest_optimizations, script): "Optimization Suggestions",
            executor.submit(profile_estimation, script): "Profiling Insights",
            executor.submit(review_quality, script): "Code Quality Review"
        }

        results = {}
        for future in concurrent.futures.as_completed(futures):
            role = futures[future]
            try:
                results[role] = future.result()
            except Exception as e:
                results[role] = f"Error: {e}"

        # generate optimized code using the suggestions
        if "Optimization Suggestions" in results:
            results["Optimized Code"] = generate_optimized_code(
                original_script=script,
                optimizer_suggestions=results["Optimization Suggestions"]
            )
        
        return results
