import tkinter as tk
from tkinter import filedialog, messagebox
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

root = tk.Tk()
root.title('PDF merger')
root.geometry('400x600')

listbox = tk.Listbox(root, selectmode=tk.EXTENDED)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

select_button = tk.Button(root, text='Select PDF Files', command=select_pdfs)
select_button.pack(fill=tk.X)
remove_button = tk.Button(root, text='Remove Selected PDFs', command=remove_selected_pdfs)
remove_button.pack(fill=tk.X)
merge_button = tk.Button(root, text='Merge PDFs', command=merge_pdfs)
merge_button.pack(fill=tk.X)

root.mainloop()
# How to make executable file
# pip install pyinstaller
# pyinstaller --onefile --windowed main.py