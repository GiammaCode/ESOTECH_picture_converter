import tkinter as tk
from tkinter import filedialog, messagebox

class MainView:
    def __init__(self, root):
        self.root = root
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def create_widgets(self):
        # Label e Entry per cartella input
        self.input_label = tk.Label(self.root, text="Cartella origine (HEIC):")
        self.input_label.pack(pady=5)
        self.input_entry = tk.Entry(self.root, width=50)
        self.input_entry.pack(pady=5)
        self.input_button = tk.Button(self.root, text="Sfoglia", command=self.browse_input)
        self.input_button.pack(pady=5)

        # Label e Entry per cartella output
        self.output_label = tk.Label(self.root, text="Cartella destinazione (JPG):")
        self.output_label.pack(pady=5)
        self.output_entry = tk.Entry(self.root, width=50)
        self.output_entry.pack(pady=5)
        self.output_button = tk.Button(self.root, text="Sfoglia", command=self.browse_output)
        self.output_button.pack(pady=5)

        # Bottone di avvio conversione
        self.convert_button = tk.Button(self.root, text="Avvia Conversione", command=self.controller.start_conversion)
        self.convert_button.pack(pady=20)

    def browse_input(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, folder_selected)

    def browse_output(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, folder_selected)

    def get_input_folder(self):
        return self.input_entry.get()

    def get_output_folder(self):
        return self.output_entry.get()

    def show_message(self, message, title="Info"):
        messagebox.showinfo(title, message)

    def show_error(self, message, title="Errore"):
        messagebox.showerror(title, message)
