# SVG to Decal PDF Generator

A Python script that converts SVG images into professional PDF sheets with multiple decal sizes. Perfect for hobbyists, modelers, or anyone needing to print custom-sized decals from a single SVG design.

**✨ Key Features:**
- Converts SVG images into multi-size decal sheets
- Customizable decal sizes and layouts
- Works with any SVG file with proper transparency support
- Simple one-click operation on Windows

**Note:** This script is designed specifically for SVG (vector) images. SVGs scale cleanly and support transparency natively, making them ideal for decal production.

---

## 🚀 Quick Start

### Windows (Recommended)
1. **Download** or clone this repository
2. **Install dependencies** - Double-click `install_deps.bat` 
3. **Add your SVG** - Place your SVG file in the project folder
4. **Generate decals** - Double-click `run_decal_generator.bat` and follow the prompts
5. **Done!** - Your PDF will be created in the same folder

### Mac/Linux
1. **Download** or clone this repository
2. **Install dependencies:**
   ```bash
   pip install reportlab svglib
   ```
3. **Generate decals:**
   ```bash
   python make_decals_sheet.py your_file.svg
   ```
4. **Done!** - Your PDF will be created in the same folder

---

## 📋 Requirements

- **Python 3.7+** - [Download from python.org](https://www.python.org/downloads/)
- **Python packages:** `reportlab`, `svglib` (auto-installed with setup scripts)

## 📖 Detailed Usage

### Basic Usage
```bash
python make_decals_sheet.py your_decal.svg
```
This creates `your_decal_decals.pdf` with multiple decal sizes.

### Custom Output Name
```bash
python make_decals_sheet.py your_decal.svg --output custom_name.pdf
```

### Windows Batch File
Double-click `run_decal_generator.bat` for an interactive experience with prompts.

---

## 📁 Sample Files

Check the `samples/` folder for:
- `mymeara.svg` - Example SVG input file
- `mymeara_decals.pdf` - Example generated output

---
## 🛠️ Creating SVG Files

You can create or edit SVG files using these free tools:
- **[Inkscape](https://inkscape.org/)** - Full-featured desktop editor
- **[Vectr](https://vectr.com/)** - Simple online/desktop editor  
- **[Boxy SVG](https://boxy-svg.com/)** - Browser-based editor

## ⚙️ Customization
## ⚙️ Customization

Want different decal sizes? Easy! 

**To customize decal sizes and layout:**

1. **Open `make_decals_sheet.py`** in any text editor
2. **Find the customization section** (look for `# === CUSTOMIZATION: SIZES & LAYOUT ===`)
3. **Edit the sizes list:**
   ```python
   sizes = [
       (4, 4),   # 4 mm tall, 4 rows
       (6, 5),   # 6 mm tall, 5 rows  
       (8, 4),   # 8 mm tall, 4 rows
       (12, 3),  # 12 mm tall, 3 rows
       (20, 2)   # 20 mm tall, 2 rows
   ]
   ```
4. **Adjust spacing** by changing the `gap_mm` variable

**Examples:**
- Add tiny decals: `(2, 6)` = 2mm tall, 6 rows
- Add huge decals: `(30, 1)` = 30mm tall, 1 row  
- Remove a size: Just delete that line

---

## 🔧 Troubleshooting

**"Module not found" error?**
- Run `pip install reportlab svglib` or double-click `install_deps.bat` (Windows)

**SVG not rendering correctly?**  
- Try opening and re-saving your SVG in [Inkscape](https://inkscape.org/)
- Make sure your SVG uses standard formatting

**Python not found?**
- Install Python from [python.org](https://www.python.org/downloads/) 
- Make sure to check "Add Python to PATH" during installation

**Need help?**
- Check the `samples/` folder for working examples
- Make sure your SVG file is in the same folder as the script

---

## 📄 License

MIT License - Feel free to use this for personal and commercial projects!
