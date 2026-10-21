# Lab 01 – Python Setup, Fundamentals, and Imports

**Course:** Digital Image Processing Lab
**Instructor:** Engr. Fahad Nisar
**Department:** Software Engineering, The University of Azad Jammu and Kashmir
**Semester / Session:** Fifth / 2024-28 (SE)
**Student:** [Your full name] | **Roll No.:** 2024-SET-[Your roll number]
**Assigned:** October 16, 2026 | **Due:** October 23, 2026, 11:59 PM

## Overview

This lab sets up a Python development environment on Windows and practises the basic Python concepts used in later Digital Image Processing labs. It covers installing Python and VS Code, running a first program, six exercises on core Python features, installing NumPy, Pillow and Matplotlib, and verifying the imports.

## Environment

| Item | Version / Detail |
|---|---|
| Operating system | Windows |
| Python | 3.12.10 |
| pip | 25.0.1 |
| Editor | Visual Studio Code with the Python extension by Microsoft |
| Interpreter | Python 3.12 (64-bit), global installation |
| NumPy | 2.5.4 |
| Pillow | 13.0.0 |
| Matplotlib | 3.11.2 |

## Files

| File | Description |
|---|---|
| `hello.py` | First Python program; prints `Hello, Digital Image Processing!` |
| `basics.py` | Solutions to Exercises 1–6 |
| `Lab01_Imports.py` | Import statements for NumPy, Pillow and Matplotlib |
| `README.md` | This file |
| Lab report (`.docx`) | Report with labelled screenshots and explanations |

## Setup Steps

1. Install Python 3 from <https://www.python.org/downloads/>.
2. Verify the installation in Command Prompt:
   ```
   python --version
   python -m pip --version
   ```
3. Install VS Code from <https://code.visualstudio.com/>, install the **Python** extension (Ctrl + Shift + X), then choose **Python: Select Interpreter** (Ctrl + Shift + P) and select Python 3.12.
4. Install the required packages:
   ```
   python -m pip install numpy pillow matplotlib
   ```
5. Confirm the packages are installed:
   ```
   python -m pip show numpy pillow matplotlib
   ```

## How to Run

Open a terminal in the Lab 01 project folder and run:

```
python hello.py
python basics.py
python Lab01_Imports.py
```

## What Each File Does

### hello.py
Prints `Hello, Digital Image Processing!`.

### basics.py

| Exercise | Topic | Expected result |
|---|---|---|
| 1 | Variables and data types | Types `int`, `int`, `str`, `bool`; total pixels `307200` |
| 2 | `if` / `elif` / `else` | `-1` Invalid, `0` Dark, `127` Dark, `128` Bright, `255` Bright, `256` Invalid |
| 3 | `for` and `while` loops | `20` Dark, `130` Bright, `255` Bright; then `0 1 2` |
| 4 | Functions | `is_bright(127)` → `False`, `is_bright(128)` → `True`, `is_bright(200, 210)` → `False` |
| 5 | Lists and tuples | `0`, `[0, 150, 255, 64]`, length `4`, then `640` and `480` |
| 6 | Dictionaries and sets | `640`, `RGB`, and `3` unique labels |

### Lab01_Imports.py
Contains only the three import statements below. It prints nothing; a clean run with no error confirms the packages are installed.

```python
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
```

## Key Concepts

- **Python vs pip:** Python is the language and interpreter that runs `.py` files. pip is the package manager that installs extra libraries such as NumPy, Pillow and Matplotlib.
- **Mutable vs immutable:** A list can be changed after creation, so items can be replaced or appended. A tuple cannot be changed once created.
- **Packages:** NumPy provides numerical arrays, Pillow provides image tools, and Matplotlib provides plotting.

## Submission Checklist

- [ ] Name and complete roll number at the top of the report
- [ ] Report named `2024-SET-<roll no>.docx` (or `.pdf`)
- [ ] Labelled screenshots for every step
- [ ] `hello.py`, `basics.py` and the imports file submitted with the report
- [ ] Short explanation of Python vs pip and the purpose of the imports
- [ ] Submitted before October 23, 2026, 11:59 PM
