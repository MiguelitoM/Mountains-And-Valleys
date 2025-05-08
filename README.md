
## Mountains and Valleys – Overview

### Territory  
A territory is defined as a rectangular grid with **N vertical paths** (labelled with letters from A to Z) and **M horizontal paths** (labelled with numbers from 1 to 99).  

### Intersections  
An **intersection** is a point where a vertical and a horizontal path meet. It is uniquely identified by combining the labels of the corresponding paths (e.g., 'B3'). Two intersections are considered **adjacent** if they are directly connected by a vertical or horizontal segment without any other intersection in between. Each intersection can either be **free** or **occupied by a mountain**.

### Mountain Chains and Valleys  
Occupied or free intersections are said to be **connected** if there is a path between them that only passes through other occupied or free intersections, respectively.  
- A **mountain chain** is a group of connected, occupied intersections that are not linked to any other mountain.  
- A **valley** consists of all free intersections adjacent to at least one mountain in a given chain.

### Examples  
📷 *Diagram description:*  
- In **Example a)**, the territory consists of 7 vertical and 4 horizontal paths, with mountains placed at intersections A2, C3, and D1.  
- **Example b)** shows two distinct mountain chains:  
  1. (A1, A2, B2, A3)  
  2. (C3)  
- **Example c)** illustrates the valleys: green dots represent the valley associated with the first chain, and yellow dots with the second.

---

### Testing

This repository includes the following components:

- ✅ A detailed project description in Portuguese  
- ✅ A Python implementation of the solution  
- ✅ Two sets of automated tests (not authored by me)

To run the available tests, use the following commands:

```bash
pip install pytest
pytest tests.py
pytest extra_tests.py
```
