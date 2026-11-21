# 2024-SE-16 – Lab Task 04: Geometric Transformations with Custom Inputs

**Course:** Digital Image Processing Lab – Department of Software Engineering, The University of Azad Jammu and Kashmir
**Instructor:** Engr. Fahad Nisar  **Session:** 2024-28 (SE), Fifth Semester
**Student:** Mahdi Ali Nahvi  **Roll No.:** 2024-SE-16

## What this project does
One reusable function, `transform(image, operation, **params)`, performs five geometric operations with
**custom, validated input** and returns the transformed image:

| Operation | Parameters | Notes |
|---|---|---|
| `scale` | `sx`, `sy`, `interpolation` | factors > 0; nearest / bilinear / bicubic / lanczos |
| `crop` | `left`, `top`, `right`, `bottom` | integers; right/bottom exclusive |
| `flip` | `direction` | horizontal / vertical / both |
| `translate` | `tx`, `ty` | positive, negative and zero allowed; canvas size kept, exposed area black |
| `rotate` | `angle`, `expand` | positive = counter-clockwise, about the image centre |

Validation (inside `transform` and in the text-input layer): unknown operations, missing/extra parameters,
non-numeric text, NaN/infinity, invalid crop boxes, unsupported choices and empty or oversized outputs are rejected with clear messages.
Declared limits: output side ≤ 8000 px, output area ≤ 40,000,000 px, |offset| ≤ 100,000 px.

## Repository contents
| File / folder | Description |
|---|---|
| `2024-SE-16-Lab04.ipynb` | The completed notebook (run from a restarted kernel; all outputs are saved in it) |
| `2024-SE-16-Lab04.docx` | Lab report with output figures and explanations of every task |
| `Butterfly.jpg` | Input image (1408 × 768) |
| `output/` | Saved transformed images (PNG) |
| `requirements.txt` | Python packages needed |
| `README.md` | This file |

## How to run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate      macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook 2024-SE-16-Lab04.ipynb
```
Then choose **Kernel → Restart & Run All**. Keep `Butterfly.jpg` in the same folder as the notebook.

### Typing your own values
In Section 4 set `RUN_INTERACTIVE = True` and run that cell. You will be prompted for an operation and its parameters;
mistakes print an error message and let you correct the input. Type `q` to quit.
It is `False` by default so *Run All* does not wait for keyboard input; the saved notebook demonstrates the prompt loop
with scripted answers (including deliberate mistakes) fed into the same `interactive_session` function.

## Notebook outline
1. Setup and declared limits
2. Load and validate the image (exists, decodes, non-zero size; BGR → RGB once; original kept read-only)
3. The `transform` function
4. User input: prompts, parsing, error handling
5. Demonstrations of all operations (enlarge/reduce, non-proportional scaling, crop, three flips, opposite translations, positive/negative rotation)
6. Interpolation comparison on an enlarged patch
7. Rejected inputs (at least one per operation) and accepted boundary inputs
8. Identity checks (scale 1, translation 0, rotation 0) – Pass/Fail table
9. Explanations: coordinates vs. array indexing, aspect-ratio distortion, rotation canvas expansion, translation clipping
10. Final checks (original unchanged, list of saved files)

## Notes
* Colour handling: images are RGB everywhere; conversion to BGR happens only when saving with OpenCV.
* Translation and rotation use `cv2.warpAffine` (bilinear, black border); scaling uses `cv2.resize` with the chosen interpolation.
* Output images are saved as lossless PNG files in `output/`.
