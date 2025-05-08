# 🏔️ Mountains and Valleys

This project was developed as part of the course *Fundamentals of Programming* at Técnico Lisboa.

## 🧠 Objective

The goal is to build a set of Python functions that allow analysis of a rectangular grid-like territory. The territory is composed of intersections between vertical and horizontal paths. Each intersection may or may not contain a mountain.

The program identifies:
- Mountain chains (connected intersections occupied by mountains)
- Valleys (connected free intersections adjacent to mountains)
- Connections between intersections
- Overall structure of the territory

---

## 🗺️ Key Concepts

### 📌 Territory

A **territory** is a rectangular grid formed by the intersections of:
- Vertical paths (labeled `'A'` to `'Z'`)
- Horizontal paths (numbered from `1` to `99`)

Each intersection is either **occupied by a mountain (1)** or **free (0)**.

📦 Internal representation:
```python
territory = (
    (0,1,0,0),
    (0,0,0,0),
    (0,0,1,0),
    (1,0,0,0),
    (0,0,0,0)
)
```

### 📌 Intersection

An **intersection** is a tuple with:
- A vertical identifier (e.g., `'A'`)
- A horizontal number (e.g., `2`)

Example: `('C', 3)` refers to column `'C'` and row `3`.

🧭 The reading order of the grid is from **left to right**, then **bottom to top**.

### 📌 Mountain Chains and Valleys

- A **mountain chain** is a group of connected intersections occupied by mountains.
- A **valley** is a set of connected free intersections adjacent to a mountain or to any mountain in a chain.

---

## 🔍 Visual Example

Territory with mountains at intersections A2, C3, and D1:

```
  A B C D E
4 . . . . .
3 . . X . .
2 X . . . .
1 . . . X .
  A B C D E
```

- There are **two mountain chains**:
  - One with a single mountain at `('C', 3)`
  - One connecting `('A', 2)` and `('D', 1)` via other mountain intersections
- The **valleys** are the free intersections directly adjacent to these mountains

---

## ▶️ How to Run

To execute your code:

```bash
python3 projeto.py
```

## ✅ Running Tests

If you have unit tests (using `pytest`), you can run them as follows:

### 1. Install pytest

```bash
pip3 install pytest
```

### 2. Run tests

```bash
pytest
```

Make sure your test file is named like `test_projeto.py` and is in the same directory.

---

> A compact Python program to explore connectivity and structure in grid systems — with mountains, valleys, and logical exploration.