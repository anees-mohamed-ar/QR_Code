# QR Code Project

This project lets you generate and scan QR codes. It also supports compressing and decompressing text to fit larger content into QR codes.

## Features

- Generate QR codes for text or URLs.
- Scan QR codes to get the original text or URL.
- Compress and decompress text for large content.
- Save QR codes with custom filenames.
- Display scanned text in a separate text pad window for long content.
- Recognize URLs in scanned QR codes and make them clickable.
- Avoid overwriting existing QR codes with the same name.

## Requirements

- Python 3.x
- `tkinter`
- `qrcode`
- `Pillow`
- `opencv-python`

Install the required libraries:

```bash
pip install tk qrcode pillow opencv-python
```

## Files

- `main.py`: Entry point to run the QR code generator and scanner application.
- `qr_code_app.py`: Main file to run the QR code generator and scanner application.
- `compressor.py`: Contains functions to compress and decompress text.
- `utils.py`: Utility functions (styles, etc.).

## How to Run

Run the main application:

```bash
python main.py
```

## How to Use

1. **Generate QR Code**:
   - Enter text or URL.
   - Click "Generate QR Code".
   - Save the QR code with a custom filename.
2. **Scan QR Code**:
   - Click "Scan QR Code".
   - Select the QR code image file.
   - If the scanned content is a URL, it will be clickable.
   - If the scanned content is long, it will be shown in a text pad window.

## Contact Information

- **Email:** aneesmohamed113@gmail.com
- **LinkedIn:** linkedin.com/in/anees-mohamed-ar
- **GitHub:** github.com/anees-mohamed-ar
