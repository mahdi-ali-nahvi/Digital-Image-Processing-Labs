# Lab Task 02 – Digital Images, Pixels, Color, and Basic Transformations

**Course:** Digital Image Processing Lab  
**Department:** Software Engineering, The University of Azad Jammu and Kashmir  
**Instructor:** Engr. Fahad Nisar | **Semester:** Fifth | **Session:** 2024-28 (SE)  
**Student:** YOUR NAME – 2024-SET-YOUR_ROLL_NO

## Overview
This project uses **NumPy**, **OpenCV** and **Matplotlib** to load, inspect, display, analyse,
transform and save a digital image. It covers coordinates and indexing, BGR vs RGB, channel
separation, grayscale conversion, cropping, resizing, histograms, resolution and bit depth.

## Project structure
| File | Description |
| --- | --- |
| `lab02.py` | Main script that performs Steps 2–7 and prints labelled results |
| `Butterfly.jpg` | Input colour image (1408 × 768 px, my own image – not the instructor's) |
| `resized_crop.png` | Output: 100 × 100 crop resized to 200 × 200 px |
| `grayscale_histogram.png` | Output: 256-bin grayscale histogram |
| `channels_figure.png`, `crop_resize_figure.png`, `bit_depth_figure.png` | Extra figures saved automatically by the script |
| `.gitignore` | Excludes `.venv/` and Python cache files |
| `2024-SET-YOUR_ROLL_NO-LAB02.docx` | Lab report |

## Setup (Windows)
```bat
mkdir dip-lab-02
cd dip-lab-02
python -m venv .venv
.venv\Scripts\activate.bat          :: PowerShell: .venv\Scripts\Activate.ps1
pip install numpy opencv-python matplotlib
python -c "import sys, numpy, cv2, matplotlib; print(sys.executable)"
```

## Run
```bat
python lab02.py
```
Matplotlib windows open one after another (close each to continue). Console output is printed in
labelled sections for every step. When finished, leave the environment with:
```bat
deactivate
```

## What the script does
1. **Load** – `cv.imread()` with a `FileNotFoundError` check; prints shape and dtype.
2. **Inspect** – height, width, channels, top-left and centre pixels, global and per-channel min/max.
3. **Colour** – BGR→RGB, grayscale, R/G/B channels, a 2 × 3 figure, centre pixel as HEX.
4. **Crop/Resize/Save** – exact 100 × 100 crop, resize to 200 × 200, save `resized_crop.png`.
5. **Histogram** – 256-bin grayscale histogram saved as `grayscale_histogram.png`.
6. **Bit depth** – 8-bit gradient quantized to 4, 2 and 1 bit, with unique-value counts (256, 16, 4, 2).

## Using a different image
Change `IMAGE_PATH` at the top of `lab02.py`. The image must be a colour JPG/PNG of at least
300 × 300 px. If your image is smaller than 610 × 350 px, adjust the crop coordinates in Step 5.

## Requirements
Python 3, numpy, opencv-python, matplotlib.

## Key results (Butterfly.jpg)
- Shape `(768, 1408, 3)`, dtype `uint8`; global and per-channel range 0–255
- Top-left pixel (B, G, R) = [174 203 218]; centre pixel [384, 704] = [25 20 21]
- Centre pixel RGB (21, 20, 25) → HEX `#151419`
- Crop `(100, 100, 3)` → resized `(200, 200, 3)`, saved successfully
- Mean gray level ≈ 118, median 116 → image is **balanced** (22.8 % dark, 60.7 % mid, 16.5 % bright)
- Unique values: 256 / 16 / 4 / 2 for 8 / 4 / 2 / 1-bit
