import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog, Text, Toplevel
import qrcode
from PIL import Image, ImageTk
import cv2
import os
import webbrowser
from utils import apply_styles
from compressor import compress_text, decompress_text, is_compressed

class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator and Scanner")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Apply styles
        apply_styles()
        
        # Setup UI elements
        self.setup_ui()

    def setup_ui(self):
        # Create notebook (tabs)
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill="both")
        
        # Create frames for each tab
        self.create_generator_tab(notebook)
        self.create_scanner_tab(notebook)
        
    def create_generator_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Generate QR Code")
        
        label = ttk.Label(frame, text="Enter text or URL:", font=("Helvetica", 12))
        label.pack(pady=10)
        
        self.entry = ttk.Entry(frame, width=50)
        self.entry.pack(pady=10)
        
        generate_button = ttk.Button(frame, text="Generate QR Code", command=self.generate_qr_code)
        generate_button.pack(pady=10)
        
        self.qr_image_label = ttk.Label(frame)
        self.qr_image_label.pack(pady=10)
        
    def create_scanner_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Scan QR Code")
        
        scan_button = ttk.Button(frame, text="Scan QR Code", command=self.scan_qr_code)
        scan_button.pack(pady=10)
        
        self.scanned_text_label = ttk.Label(frame, text="", font=("Helvetica", 12))
        self.scanned_text_label.pack(pady=10)
        
    def generate_qr_code(self):
        text = self.entry.get()
        if not text:
            messagebox.showwarning("Input Error", "Please enter text or URL.")
            return

        if len(text) > 100:  # Adjust the length threshold as needed
            text = compress_text(text)

        try:
            while True:
                # Ask user for filename
                filename = simpledialog.askstring("Filename", "Enter filename for the QR code:")
                if not filename:
                    messagebox.showwarning("Input Error", "Filename cannot be empty.")
                    return

                qr_image_path = os.path.join("assets", f"{filename}.png")

                if os.path.exists(qr_image_path):
                    messagebox.showwarning("File Exists", "A file with this name already exists. Please enter a different filename.")
                else:
                    break

            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(text)
            qr.make(fit=True)

            # Ensure the assets directory exists
            assets_dir = "assets"
            if not os.path.exists(assets_dir):
                os.makedirs(assets_dir)

            qr_image = qr.make_image(fill='black', back_color='white')
            qr_image.save(qr_image_path)

            self.display_qr_code(qr_image_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate QR Code: {e}")

            
    def display_qr_code(self, qr_image_path):
        image = Image.open(qr_image_path)
        image = image.resize((200, 200), Image.Resampling.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        photo = ImageTk.PhotoImage(image)
        
        self.qr_image_label.config(image=photo)
        self.qr_image_label.image = photo
        
    def scan_qr_code(self):
        try:
            qr_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
            if not qr_image_path:
                return
            
            image = cv2.imread(qr_image_path)
            detector = cv2.QRCodeDetector()
            data, bbox, _ = detector.detectAndDecode(image)
            
            if bbox is not None:
                # Clear the previous scanned text
                for widget in self.scanned_text_label.winfo_children():
                    widget.destroy()
                
                if is_compressed(data):
                    data = decompress_text(data)

                if self.is_url(data):
                    preview = data if len(data) <= 50 else data[:47] + "..."
                    link_label = ttk.Label(self.scanned_text_label, text=preview, font=("Helvetica", 12), foreground="blue", cursor="hand2")
                    link_label.pack()
                    link_label.bind("<Button-1>", lambda e: webbrowser.open_new(data))
                elif len(data) > 100:
                    self.open_text_pad_window(data)
                else:
                    self.scanned_text_label.config(text=f"Scanned Text: {data}")
            else:
                self.scanned_text_label.config(text="No QR code found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to scan QR Code: {e}")
            
    def open_text_pad_window(self, text):
        text_pad = Toplevel(self.root)
        text_pad.title("Scanned Text")
        text_pad.geometry("600x400")

        text_widget = Text(text_pad, wrap="word")
        text_widget.pack(expand=True, fill="both")
        text_widget.insert("1.0", text)
        text_widget.config(state="disabled")
            
    def is_url(self, text):
        import re
        url_pattern = re.compile(r'http[s]?://')
        return re.match(url_pattern, text) is not None
