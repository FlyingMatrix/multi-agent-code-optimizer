# Multi Agent Code Optimizer

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

### Define the Target

Design and build an advanced multi-agent framework that analyzes Python code efficiency and outputs optimized code based on suggested improvements.

### Roles of Each Agent

| Agent | Role                  | Task                                                                                                                                                 |
| ----- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| A     | Complexity Analyst    | Analyze time and space complexity and identify inefficiencies.                                                                                       |
| B     | Optimizer             | Suggest algorithmic improvements to make the script faster and more memory-efficient.                                                                |
| C     | Profiler              | Estimate the script’s runtime, CPU/GPU utilization, and memory footprint, and identify potential bottlenecks and scalability issues.                 |
| D     | Code Quality Reviewer | Review code style, readability, and maintainability, and suggest clean-code improvements.                                                            |
| E     | Coordinator           | Synthesize the findings from all agents into one comprehensive, cohesive report.                                                                     |
| F     | Coder Generator       | Generate an optimized Python script based on suggested improvements, while maintaining original functionality and adhering to Python best practices. |

### Architecture Overview

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

### Repository Structure

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

requirements.txt

```
ollama
concurrent.futures
python-dotenv
```

### Validation

For example, given a script:

```
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

...TBC
