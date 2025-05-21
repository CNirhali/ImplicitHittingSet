# Implicit Hitting Set Solver

This project implements and compares different algorithms for solving the Implicit Hitting Set (IHS) problem. It includes three different approaches:
1. Base algorithm
2. Advanced algorithm with frequency-based optimization
3. GF(2) algorithm using linear algebra

## Features

- Multiple IHS solving algorithms
- Benchmarking suite for performance comparison
- Interactive Streamlit visualization interface
- Support for manual conflict input
- Visual comparison of solution sizes and coverage

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ImplicitHittingSet.git
cd ImplicitHittingSet
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Benchmark

To run the benchmarking suite and compare the performance of different algorithms:

```bash
python benchmark.py
```

This will generate benchmark results for different problem sizes and save comparison plots.

### Using the Interactive Interface

To launch the Streamlit visualization interface:

```bash
streamlit run app.py
```

The interface allows you to:
- Adjust problem parameters (number of elements, conflicts, and conflict size)
- View and compare solutions from different algorithms
- Add custom conflicts manually
- Visualize solution sizes and coverage ratios

### Using the Algorithms in Your Code

```python
from ihs import BaseIHS, AdvancedIHS, GF2IHS

# Create a problem instance
ihs = BaseIHS()  # or AdvancedIHS() or GF2IHS()

# Add conflicts
ihs.add_conflict({1, 2, 3})
ihs.add_conflict({2, 3, 4})
ihs.add_conflict({1, 4, 5})

# Find the minimal hitting set
solution = ihs.find_minimal_hitting_set()
print(f"Solution: {solution}")
```

## Project Structure

```
ImplicitHittingSet/
├── ihs/
│   ├── __init__.py
│   ├── base.py
│   ├── advanced.py
│   └── gf2.py
├── app.py
├── benchmark.py
├── requirements.txt
└── README.md
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
