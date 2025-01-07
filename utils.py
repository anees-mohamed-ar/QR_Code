from tkinter import ttk

def apply_styles():
    style = ttk.Style()
    
    # General styles
    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("TButton", font=("Helvetica", 12, "bold"))
    style.configure("TEntry", font=("Helvetica", 12))
    style.configure("TFrame", background="#f0f0f0")
    
    # Notebook styles
    style.configure("TNotebook", background="#f0f0f0")
    style.configure("TNotebook.Tab", font=("Helvetica", 12, "bold"), padding=[10, 5])
    
    # QR Code display style
    style.configure("QRCode.TLabel", font=("Helvetica", 14, "bold"), foreground="blue", background="yellow")
