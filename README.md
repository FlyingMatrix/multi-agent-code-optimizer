# Multi Agent Code Optimizer

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

### Define the Goal

An advanced multi-agent system that evaluates Python code efficiency and automatically generates optimized versions based on improvement suggestions.

For example, given a script:

```
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Agents will analyze and respond like this:

- **Agent A (Complexity Analyst):** Recursion gives O(n) time and O(n) space.

- **Agent B (Optimizer):** Suggests using iteration to reduce recursion overhead.

- **Agent C (Profiler):** Estimates runtime or memory footprint.

- **Agent D (Code Quality Reviewer):** Checks style, readability, and best practices.

### Roles of Each Agent

| Agent                     | Role                           | Task                                                      |
| ------------------------- | ------------------------------ | --------------------------------------------------------- |
| **Complexity Analyst**    | Algorithm expert               | Estimate Big-O time and space complexity                  |
| **Optimizer**             | Code performance expert        | Suggest faster or more memory-efficient approaches        |
| **Profiler**              | System efficiency analyst      | Predict where bottlenecks could appear                    |
| **Code Quality Reviewer** | Style & maintainability expert | Ensure Pythonic practices, readability, and documentation |

### Architecture Overview

You can implement this with:

- A **Coordinator (Manager)** agent that assigns tasks.

- 4 **Worker** agents (the ones above).

They communicate through an **orchestrator** (your Python code).

```
Input Script → Coordinator → [Agent A, B, C, D in parallel]
                               ↓
                    Combined Report (from all agents)
```

### Environment Setup

```
multi_agent_code_review/
│
├── main.py
├── agents/
│   ├── __init__.py
│   ├── complexity_agent.py
│   ├── optimizer_agent.py
│   ├── profiler_agent.py
│   └── quality_agent.py
├── utils/
│   └── orchestrator.py
└── requirements.txt
```

requirements.txt

```
ollama
concurrent.futures
python-dotenv
```
