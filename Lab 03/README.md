# Lab Task 03 – Image Enhancement and Intensity Transformations

**Course:** Digital Image Processing Lab, Dept. of Software Engineering, UAJK  
**Roll No:** 2024-SE-16 | **Instructor:** Engr. Fahad Nisar

## Files
| File | Purpose |
|---|---|
| `2024-SE-16-Lab03.ipynb` | Notebook with all 11 operations and 11 dry runs (already executed, outputs visible) |
| `2024-SE-16-Lab03.docx` | Word report with figures, dry-run tables and explanations |
| `Butterfly.jpg` | Input colour image (1408 x 768) |
| `Butterfly_gray.png` | 8-bit grayscale version created by the notebook |
| `figures/` | PNG figures created by the notebook and used in the report |
| `dryrun_results.json` | Dry-run values saved by the notebook |
| `requirements.txt` | Python packages needed |

## How to run
1. Install Python 3 and the packages: `pip install -r requirements.txt`
2. Put `Butterfly.jpg` in the same folder as the notebook.
3. Open `2024-SE-16-Lab03.ipynb` in Jupyter or VS Code.
4. Choose **Kernel -> Restart & Run All**. Figures are saved to `figures/`.

## Before submitting
- Replace `YOUR NAME HERE` with your name in the first notebook cell and on the title page of the report.
- Restart the kernel and run all cells once more so the outputs are fresh.
- Do not submit the virtual environment folder.

## Notes
- The colour image is converted once to grayscale (`cv2.cvtColor`) and saved as `Butterfly_gray.png`.
- All arithmetic uses wider types (`int16`/`float`), clips to 0-255, then converts to `uint8` (fractions truncated).
- Images are displayed with `vmin=0, vmax=255`.
- Results: Otsu threshold = 122; white pixels: fixed 40.13 %, Otsu 44.32 %, adaptive 84.42 %.
