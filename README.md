# Multi Agent Code Optimizer

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

### 🚀 Define the Target

Design and build an advanced multi-agent framework that analyzes Python code efficiency and outputs optimized code based on suggested improvements.

### 🤖 Roles of Each Agent

| Agent | Role                  | Task                                                                                                                                                 |
| ----- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| A     | Complexity Analyst    | Analyze time and space complexity and identify inefficiencies.                                                                                       |
| B     | Optimizer             | Suggest algorithmic improvements to make the script faster and more memory-efficient.                                                                |
| C     | Profiler              | Estimate the script’s runtime, CPU/GPU utilization, and memory footprint, and identify potential bottlenecks and scalability issues.                 |
| D     | Code Quality Reviewer | Review code style, readability, and maintainability, and suggest clean-code improvements.                                                            |
| E     | Coordinator           | Synthesize the findings from all agents into one comprehensive, cohesive report.                                                                     |
| F     | Code Generator        | Generate an optimized Python script based on suggested improvements, while maintaining original functionality and adhering to Python best practices. |

### 🛠️ Architecture Overview

```
Input Script → Orchestrator → [Agent A, B, C, D in parallel]
                                            ↓
                        Suggested Improvements(from all agents) → [Agent E]
                                                                      ↓
                                    Input Script → [Agent F] ← Combined Report
                                                       ↓
                                                Optimized Script
```

- The **Orchestrator** coordinates agents by assigning tasks and managing inter-agent communication.

- 4 **Worker agents (A, B, C, D)** work in parallel to analyze Python code efficiency.

- **Agent E** consolidates the suggested improvements from all agents into a comprehensive, cohesive report.

- **Agent F** generates an optimized Python script by applying suggestions from the combined report.

### 🧩 Repository Structure

```
multi-agent-code-optimizer/
│
├── agents/
│   ├── __init__.py
│   ├── complexity_agent.py
│   ├── optimizer_agent.py
│   ├── profiler_agent.py
│   ├── quality_agent.py
│   ├── coordinator_agent.py
│   └── code_generator_agent.py
├── utils/
│   ├── config.py
│   └── orchestrator.py
├── code_to_review/
│   ├── example.py
│   └── example_optimized.py
├── .env
├── main.py
├── requirements.txt
└── README.md
```

> `requirements.txt`

```
ollama
concurrent.futures
python-dotenv
```

> `.env`

```
MODEL = "llama3"
```

### 💻 Installation and Usage

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/flyingmatrix/multi-agent-code-optimizer
   ```

2. **Create and activate a virtual environment (optional):**
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Pull Llama-3 model locally:**
   
   ```bash
   ollama pull llama3
   ```

5. **Run the code optimizer:**
   
   Make sure that all Python scripts intended for optimization are located in the `code_to_review` directory. Then run:
   
   ```bash
   python main.py
   ```

### 💡 Validation

- For example, consider the following code in the script  `example.py`:

```
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)   
```

- Final summary of optimization recommendations from the code optimizer:

```
======== Final Summary ========
 The results are an analysis of a recursive function calculating the factorial of a given integer `n`. The analysis includes:

1. **Complexity Analysis**: The time complexity is O(n) because each recursive call reduces the value of `n` by 1, and the number of calls grows linearly with `n`. 
The space complexity is also O(n) due to the creation of new stack frames for each recursive call.
2. **Code Quality Review**: The code is easy to understand, but there are some minor issues:
        * Readability: The intention is clear, but there's no docstring explaining what the function does or its parameters.
        * Maintainability: The code is simple and doesn't have any complex logic or dependencies, making it relatively easy to maintain.
        * PEP8 Adherence: There are some minor issues with indentation and spacing between lines.
3. **Optimization Suggestions**: To improve performance:
        * Use iteration instead of recursion for better memory efficiency and speed.
        * Follow Python best practices: use meaningful variable names, avoid unnecessary computations, and take advantage of built-in libraries (like `math.factorial`).
4. **Profiling Insights**:
        * The function has a time complexity of O(2^n), which means its running time grows exponentially with the input size `n`.
        * CPU usage will increase rapidly as `n` grows.
        * Memory usage will also grow linearly with `n`, but since each stack frame is relatively small, this should not be a major concern.
5. **Suggestions**:
        * Use an iterative approach to reduce CPU usage and improve scalability.
        * Implement memoization to avoid redundant computations.
        * Optimize the recursive function by reducing the number of recursive calls or using more efficient algorithms.

The optimized code uses an iterative approach, initializes the result to 1 instead of calculating it inside the loop, and takes advantage of the built-in `math.factorial` function from the Python standard library.
Optimized code saved to: code_to_review\example_optimized.py
```

- The optimized code in the script `example_optimized.py`:

```
import math

def factorial(value):
    if value < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif value == 0 or value == 1:
        return 1
    else:
        return math.factorial(value)  
```
