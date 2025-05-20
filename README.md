# ImplicitHittingSet

# 🔍 Implicit Hitting Set Solver

This repository provides an efficient and modular implementation of an **Implicit Hitting Set (IHS) solver**, a powerful technique for solving a wide class of combinatorial optimization problems, especially in AI, verification, and computational biology.

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8+-blue)

---

## 📌 What is an Implicit Hitting Set?

An **Implicit Hitting Set** framework solves problems where:

* The full list of constraints (sets to hit) is **too large to enumerate upfront**.
* A **separation oracle** provides violated constraints when given a candidate solution.

Instead of pre-generating all sets, the algorithm **iteratively constructs** a hitting set by:

1. Generating a candidate solution.
2. Querying the oracle for violated sets.
3. Adding those sets and re-solving.

This approach is efficient for problems where constraints are exponentially many but can be identified lazily.

---

## 🚀 Use Cases

* **AI planning & synthesis**
* **Formal verification (e.g., counterexample-guided abstraction refinement)**
* **MaxSAT & minimal unsatisfiable subsets (MUS)**
* **Network diagnostics / root cause analysis**
* **Computational biology (e.g., gene interaction networks)**

---

## 🛠️ Features

* Modular implementation (plug your own oracle or solver)
* Works with **Z3**, **PySAT**, or custom SAT/ILP solvers
* Supports minimal hitting sets and cost-based variants
* Easily extensible for custom applications
* Lightweight and Pythonic API

---

## 🧪 Example Usage

```python
from ihs_solver import ImplicitHittingSet
from oracles import example_oracle

solver = ImplicitHittingSet(
    universe=[1, 2, 3, 4],
    oracle=example_oracle,
    solver_backend="z3"  # or "pysat", "ilp"
)

hitting_set = solver.solve()
print("Minimal Hitting Set:", hitting_set)
```

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/implicit-hitting-set.git
cd implicit-hitting-set
pip install -r requirements.txt
```

> You can install additional solver support with:

```bash
pip install z3-solver pysat
```

---

## 📂 Project Structure

```
implicit-hitting-set/
├── ihs_solver.py        # Core algorithm
├── oracles/             # Example oracles
├── solvers/             # Pluggable backend interfaces (Z3, PySAT)
├── tests/               # Unit tests
├── examples/            # Usage examples
└── README.md
```

---

## 📈 Architecture Diagram

```
+----------------------------+
|   User Application        |
+------------+--------------+
             |
             v
+------------+--------------+
| ImplicitHittingSet API    |
+------------+--------------+
             |
     +-------+--------+
     |    Oracle       | <--- Lazy constraint generation
     +-----------------+
     |  Solver Backend | <--- Z3 / PySAT / ILP
     +-----------------+
```

---

## 🧠 Citation & Reference

If you use this code in your research, please cite:

```
@article{ihs2020,
  title={Efficient Implicit Hitting Set Algorithms},
  author={Your Name},
  year={2020},
  journal={arXiv preprint arXiv:xxxx.xxxxx}
}
```

---

## 🤝 Contributing

PRs welcome! Feel free to open issues or submit improvements.

* Add new solvers
* Improve example oracles
* Expand test coverage

---

## 📬 Contact

For questions or collaborations, reach out to \[[youremail@example.com](mailto:youremail@example.com)].

---

**Let’s make combinatorial optimization smarter and faster, one hitting set at a time.**
