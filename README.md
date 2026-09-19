# Mathematical Computing & Data Structures in Python 🐍🧮

A modular, well-structured library of algorithms, linear data structures, mathematical simulations, and linear algebra routines implemented in pure Python. Designed as a foundational sandbox for **Mathematics & Computing (MnC)** students and computer science enthusiasts.

---

## 📌 Repository Overview

This repository aggregates foundational Python implementations covering:
- **Data Structures**: Stacks, Queues, Deques with overflow/underflow checks and interactive CLI menus.
- **Searching & Sorting**: Linear Search, Binary Search, Modified Hash/Bucket Search, Bubble Sort, Selection Sort, Insertion Sort.
- **Linear Algebra & Matrices**: Matrix creation (manual, random, string conversion), matrix multiplication, and determinants.
- **Mathematical Computing**: Fibonacci memoization, Pascal's Triangle ($nCr$), Power Series expansions, Armstrong Numbers, Quadratic Equation roots, Factorials, Base Conversions, and Diophantine solvers ($x+y+z=N$).
- **Utilities**: Countdown Timer, Random Number Generators, String/Digit manipulation, and CLI visual star patterns.

---

## 📁 Repository Structure

```
.
├── 📂 Data_Structures/
│   ├── stack.py               # Interactive Stack (Push, Pop, Peek, Overflow/Underflow)
│   ├── queue.py               # Interactive Queue (Enqueue, Dequeue, Peek, IsFull)
│   ├── deque.py               # Interactive Double-Ended Queue (Front/Rear operations)
│   └── python_lists.py        # Dynamic List operations benchmark
│
├── 📂 Searching_and_Sorting/
│   ├── binary_search.py       # O(log N) Binary Search implementation
│   ├── linear_search.py       # O(N) Linear Search implementation
│   ├── modified_hash_search.py# Digit-bucket based hash searching algorithm
│   ├── bubble_sort.py         # Bubble Sort with in-place element swapping
│   ├── selection_sort.py      # Selection Sort utilizing minimum index tracking
│   ├── insertion_sort.py      # Insertion Sort implementation
│   └── letter_search.py       # String search and frequency tracking
│
├── 📂 Linear_Algebra/
│   ├── matrix_formation.py    # Manual, random, and string-to-matrix generation
│   ├── matrix_multiplication.py# Matrix multiplication with shape validation
│   └── determinants.py        # Matrix determinant computations
│
├── 📂 Mathematics_and_Algorithms/
│   ├── fibonacci.py           # Iterative Fibonacci sequence with time benchmarking
│   ├── pascals_triangle.py    # Combinatorial Pascal's Triangle via nCr factorials
│   ├── power_series.py        # Power Series Taylor expansion computations
│   ├── quadratic_roots.py     # Quadratic formula discriminant evaluator
│   ├── armstrong_number.py    # Armstrong / Narcissistic number verifier
│   ├── factorial.py           # Iterative factorial computation
│   ├── base_conversion.py     # Decimal to arbitrary Base-N number converter
│   └── equation_solver.py     # Diophantine solver for x + y + z = N
│
└── 📂 Utilities/
    ├── countdown_timer.py     # Interactive CLI countdown timer
    ├── random_generator.py    # Random number generator scripts
    ├── digits_in_string.py    # String digit filter and counter
    └── star_patterns.py       # CLI star/triangle pattern renderer
```

---

## 🚀 Detailed Module Descriptions

### 1. 🗂️ Data Structures
- **Stack (`stack.py`)**: Menu-driven stack supporting `Push`, `Pop`, `Peek`, `OverFlow`, `IsEmpty`, and `Size` validations.
- **Queue (`queue.py`)**: First-In-First-Out (FIFO) structure supporting `Enqueue`, `Dequeue`, `Peek`, `IsFull`, `IsEmpty`, and `Size`.
- **Deque (`deque.py`)**: Double-Ended Queue with front and rear insertions and deletions (`InsertionFront`, `InsertionRear`, `DeletionFront`, `DeletionRear`).

### 2. 🔍 Searching & Sorting
- **Binary Search**: Fast $O(\log N)$ search on sorted arrays using array midpoint partitioning.
- **Linear Search**: $O(N)$ linear scan returning 1-based element indices.
- **Modified Hash Search**: Digit-bucket hashing partitioning elements into 0–9 buckets across digit place values.
- **Sorting Algorithms**: Pure Python implementations of **Bubble Sort**, **Selection Sort**, and **Insertion Sort**.

### 3. 📐 Linear Algebra & Matrix Computing
- **Matrix Operations**: Flexible matrix instantiation (manual input, random matrices, string conversion) and matrix multiplication.
- **Determinants**: Computations of 2x2 and higher-order matrix determinants.

### 4. 🧮 Mathematical Logic & Numerical Methods
- **Fibonacci Series**: Optimized iterative dynamic memoization reducing recursive complexity from $O(2^N)$ down to $O(N)$ time with runtime benchmarking via `time`.
- **Pascal's Triangle**: Evaluates combinatorial rows using $nCr = \frac{n!}{r!(n-r)!}$.
- **Base Conversions**: Modular arithmetic for converting decimal numbers into arbitrary base systems.
- **Diophantine Equations**: Solver evaluating combinations for equations of the form $x + y + z = N$.

---

## 🛠️ Usage & Execution

All scripts are written in standard **Python 3** without external third-party dependencies required.

To run any script interactively:
```bash
python3 Data_Structures/stack.py
python3 Searching_and_Sorting/binary_search.py
python3 Mathematics_and_Algorithms/fibonacci.py
```

---

## 📈 Roadmap & Next Steps
- [ ] Migrate algorithm solutions to **C++** using **The Ideal Two-Step Workflow**.
- [ ] Expand LeetCode / HackerRank problem solutions into dedicated subfolders.
- [ ] Implement STL container equivalents (`std::vector`, `std::unordered_map`, `std::deque`) in C++.
