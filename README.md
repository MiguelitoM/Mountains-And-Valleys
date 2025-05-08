# 🏔️ Mountains and Valleys

This project was developed as part of the course *Fundamentals of Programming* at Técnico Lisboa.

## 🧠 Objective

The goal is to build a set of Python functions that allow analysis of a rectangular grid-like territory. The territory is composed of intersections between vertical and horizontal paths. Each intersection may or may not contain a mountain.

The program identifies:
- Mountain chains (connected intersections occupied by mountains)
- Valleys (free intersections adjacent to a mountain or its chain)
- Connections between intersections
- Overall structure of the territory

## 🧱 Territory Structure

- The **territory** is represented as a tuple of tuples of integers:
  - `1` → Mountain
  - `0` → Free intersection

- Each **intersection** is a tuple like `('A', 1)`, where:
  - `'A'` is the vertical path (from `'A'` to `'Z'`)
  - `1` is the horizontal path (from `1` to `99`)

### Example of a 5x4 territory:

```python
territory = (
    (0,1,0,0),
    (0,0,0,0),
    (0,0,1,0),
    (1,0,0,0),
    (0,0,0,0)
)
```

This corresponds to:

```
  A B C D E
4 . . . . .
3 . . X . .
2 X . . . .
1 . . . X .
  A B C D E
```

## ⚙️ Key Functions

The program includes functions to:

- Validate the territory and its intersections
- Get adjacent intersections
- Determine if two intersections are connected
- Find the last intersection in the territory
- Convert the territory into a string representation
- Identify mountain chains and valleys

## ▶️ How to Run

Run the Python file containing the implemented functions:

```bash
python3 projeto.py
```

No external libraries are required. Only built-in Python 3 features are used.

---

> A small but complete program to explore spatial connectivity and logical structures on a grid using pure Python.
