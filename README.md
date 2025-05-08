
## ⛰ Mountains and Valleys 

### Territory 
A territory is defined as a rectangular grid with **N vertical paths** (labelled with letters from A to Z) and **M horizontal paths** (labelled with numbers from 1 to 99).  

### Intersections  
An **intersection** is a point where a vertical and a horizontal path meet. It is uniquely identified by combining the labels of the corresponding paths (e.g., 'B3'). Two intersections are considered **adjacent** if they are directly connected by a vertical or horizontal segment without any other intersection in between. Each intersection can either be **free** or **occupied by a mountain**.

### Mountain Chains and Valleys  
Occupied or free intersections are said to be **connected** if there is a path between them that only passes through other occupied or free intersections, respectively.  
- A **mountain chain** is a group of connected, occupied intersections that are not linked to any other mountain.  
- A **valley** consists of all free intersections adjacent to at least one mountain in a given chain.

## 🧪 Tests

Automated tests are provided using the `pytest` framework.

1. Install the testing module:
```bash
pip install pytest
```

2. Run the available tests:
```bash
pytest tests.py
pytest extra_tests.py
```
