import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import PyPDF2

def select_pdfs():
    file_types = [("PDF Files", "*.pdf")]
    file_paths = filedialog.askopenfilenames(title="Select PDF files", filetypes=file_types)
    for path in file_paths:
        listbox.insert(tk.END, path)

def remove_selected_pdfs():
    selected_pdfs = listbox.curselection()
    for i in reversed(selected_pdfs):
        listbox.delete(i)

def merge_pdfs():
    paths = listbox.get(0, tk.END)
    if not paths:
        messagebox.showwarning("No PDFs selected", "Please select at least one PDF file")
        return

    try:
        merger = PyPDF2.PdfMerger()
        for path in paths:
            merger.append(path)

        output_pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not output_pdf_path:
            return

        merger.write(output_pdf_path)
        merger.close()
        messagebox.showinfo("Successful", "Merged PDFs successfully")
    except Exception as e:
        messagebox.showwarning("Error", f"An error occurred while merging PDFs: {e}")

# Main window
root = tk.Tk()
root.title('PDF merger')
root.geometry('450x500')
root.config(bg="#f5f5f5")

# Style customization using ttk
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 10), padding=5)
style.configure('TLabel', font=('Helvetica', 12))

# Title label
title_label = ttk.Label(root, text="PDF Merger", font=("Helvetica", 16, "bold"), background="#f5f5f5")
title_label.pack(pady=10)

# Listbox with Scrollbar
frame = ttk.Frame(root)
frame.pack(padx=20, pady=(0, 10), fill=tk.BOTH, expand=True)

listbox = tk.Listbox(frame, selectmode=tk.EXTENDED, height=15, font=("Arial", 10), bg="#ffffff", relief="solid", borderwidth=1)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=(10, 0))

select_button = ttk.Button(button_frame, text='Select PDF Files', command=select_pdfs)
select_button.grid(row=0, column=0, padx=10, pady=5)

remove_button = ttk.Button(button_frame, text='Remove Selected PDFs', command=remove_selected_pdfs)
remove_button.grid(row=0, column=1, padx=10, pady=5)

merge_button = ttk.Button(root, text='Merge PDFs', command=merge_pdfs)
merge_button.pack(pady=(10, 15))

# Final layout adjustments
for child in button_frame.winfo_children():
    child.grid_configure(padx=10, pady=5)

root.mainloop()
# How to make executable file
# pip install pyinstaller
# pyinstaller --onefile --windowed main.py