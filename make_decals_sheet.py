
# make_decals_sheet.py
#
# Command-line tool to generate a PDF sheet of decals from an SVG file.
#
# Usage:
#   python make_decals_sheet.py input.svg [--output output.pdf]
#
# By default, uses a set of common decal sizes and layout. To customize, see the 'CUSTOMIZATION' section below.

import argparse
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.graphics import renderPDF
import svglib.svglib as svglib

# === CUSTOMIZATION: SIZES & LAYOUT ===
# To change the decal sizes or number of rows, edit the 'sizes' list below.
# Each tuple is (height_mm, num_rows). Add, remove, or modify as needed.
sizes = [
    (4, 4),
    (6, 5),
    (8, 4),
    (12, 3),
    (20, 2)
]

# Horizontal gap between decals in mm
gap_mm = 1  # Change this for more/less space between decals

def main():
    parser = argparse.ArgumentParser(
        description="Generate a PDF sheet of decals from an SVG image."
    )
    parser.add_argument(
        "input_svg",
        help="Path to the SVG file to use for the decals."
    )
    parser.add_argument(
        "-o", "--output",
    help="Path for the output PDF (default: <svgname>_decals.pdf)",
        default=None
    )
    args = parser.parse_args()

    svg_path = args.input_svg
    if not os.path.isfile(svg_path):
        print(f"❌ SVG file not found: {svg_path}")
        return

    # Set output PDF path
    if args.output:
        pdf_path = args.output
    else:
        base = os.path.splitext(os.path.basename(svg_path))[0]
        pdf_path = f"{base}_decals.pdf"

    # Load SVG
    try:
        drawing = svglib.svg2rlg(svg_path)
    except Exception as e:
        print(f"❌ Error loading SVG: {e}")
        return

    # Page setup
    page_w, page_h = letter
    margin = 10 * mm
    x_start = margin
    y = page_h - margin
    c = canvas.Canvas(pdf_path, pagesize=letter)

    for size_mm, rows in sizes:
        # Draw size label
        c.setFont("Helvetica-Bold", 10)
        c.drawString(x_start, y, f"{size_mm} mm")
        y -= 5 * mm

        # Scale factor to match height
        scale_factor = (size_mm * mm) / drawing.height

        # Decals per row that fit within margins
        decals_per_row = int((page_w - 2 * margin) // ((size_mm + gap_mm) * mm))

        # Draw the requested rows
        for row in range(rows):
            x = x_start
            for i in range(decals_per_row):
                c.saveState()
                c.translate(x, y - size_mm * mm)
                c.scale(scale_factor, scale_factor)
                renderPDF.draw(drawing, c, 0, 0)
                c.restoreState()
                x += (size_mm + gap_mm) * mm
            y -= (size_mm + 4) * mm  # 4 mm vertical gap between rows

    # Save the PDF
    c.save()
    print(f"✅ One-page decal sheet saved to: {os.path.abspath(pdf_path)}")

if __name__ == "__main__":
    main()
