# svg-to-decal-pdf

A Python script to convert an SVG image into a full PDF sheet of decals. Useful for hobbyists, modelers, or anyone needing to print custom-sized decals from a single SVG design.

**Note:** This script is designed specifically for SVG (vector) images. Adapting it for other image formats (like PNG, JPEG, BMP) may require significant changes due to differences in scaling and transparency handling. SVGs scale cleanly and support transparency natively, while raster images may lose quality when resized and handle transparency differently.

## Features
- Converts an SVG image into a one-page PDF with multiple rows of decals in various sizes.
- Customizable decal sizes, number of rows, and layout.
- Simple command-line interface.

## Requirements
- Python 3.7+
- Dependencies:
  - `reportlab`
  - `svglib`

## Installation
1. **Install Python:**
   - Download and install Python from [python.org](https://www.python.org/downloads/).
   - Ensure Python is added to your system PATH.
2. **Install dependencies:**
   Open a command prompt in this folder and run:
   ```sh
   pip install reportlab svglib
   ```

## Usage
1. Place your SVG file (e.g., `your_decal.svg`) in this folder.
2. Run the script from the command line:
   ```sh
   python make_decals_sheet.py your_decal.svg
   ```
   - This will create a PDF named `your_decal_decals.pdf` in the same folder.
3. **Optional arguments:**
   - To specify a custom output filename:
     ```sh
     python make_decals_sheet.py your_decal.svg --output custom_decals.pdf
     ```

## Customization
You can easily change the decal sizes, number of rows, and layout:

- **Edit `make_decals_sheet.py`:**
  - Find the section labeled `# === CUSTOMIZATION: SIZES & LAYOUT ===` near the top of the script.
  - The `sizes` list controls the decal heights (in mm) and number of rows for each size:
    ```python
    sizes = [
        (4, 4),   # 4 mm tall, 4 rows
        (6, 5),   # 6 mm tall, 5 rows
        (8, 4),   # 8 mm tall, 4 rows
        (12, 3),  # 12 mm tall, 3 rows
        (20, 2)   # 20 mm tall, 2 rows
    ]
    ```
  - To add, remove, or change sizes, simply edit this list.
  - To adjust the horizontal gap between decals, change the `gap_mm` variable.

## Troubleshooting
- If you see an error about missing modules, ensure you have installed all dependencies with `pip install reportlab svglib`.
- If your SVG does not render correctly, try editing it in a vector graphics editor (like Inkscape) and re-saving.

## License
MIT License. This script is provided as-is for personal and non-commercial use.
