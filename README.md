
## Mountains and Valleys

This project focuses on developing a set of Python functions to obtain and manipulate information about a **rectangular territory** composed of **intersections between vertical and horizontal paths**. Some of these intersections may be occupied by **mountains**, while others remain free, forming patterns of **mountain chains** and **valleys**.

---

### Territory

A territory is represented as a **rectangular structure**, made up of a number of vertical paths (identified by uppercase letters from A to Z) and horizontal paths (identified by integers from 1 to 99). Each point where a vertical path crosses a horizontal one is called an **intersection**, which may be **occupied (1)** or **free (0)**.

---

### Intersections

Intersections are denoted by pairs such as `('B', 3)` and can be validated, ordered, or tested for occupation. Two intersections are **adjacent** if they share a direct horizontal or vertical path. The reading order of intersections is always from **left to right and bottom to top**.

---

### Mountain Chains and Valleys

Two occupied intersections are connected if there is a continuous path between them through other adjacent occupied intersections. The set of all such connected intersections forms a **mountain chain**.

Similarly, a group of connected free intersections forms a **chain of free intersections**. The **valley** of a mountain is the set of free intersections that are adjacent to it or to other mountains in the same chain.

---

### Examples

Several visual and textual examples are provided in the project statement (see PDF) to illustrate how to construct and represent territories, detect chains, and identify valleys.

---

### Tests

To ensure the correctness of the functions, automated tests are provided using the `pytest` framework.

1. Install the testing module:
```bash
pip install pytest
```

2. Run the available tests:
```bash
pytest tests.py
pytest extra_tests.py
```
