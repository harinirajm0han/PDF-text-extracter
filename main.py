import tkinter
import PyPDF2
from tkinter import filedialog

def openFile():
    filename = filedialog.askopenfilename(
        title="Open PDF file",
        initialdir=r'C:\Users\Harini Rajmohan\OneDrive\Desktop\Personal',
        filetypes=[('PDF files', '*.pdf')]
    )
    
    if filename:  # Ensure that a file was selected
        print(filename)
        filename_label.configure(text=filename)
        outputfile_text.delete("1.0", tkinter.END)
        
        try:
            reader = PyPDF2.PdfReader(filename)
            for i in range(len(reader.pages)):  # Use len(reader.pages)
                current_text = reader.pages[i].extract_text()  # Use extract_text() method
                outputfile_text.insert(tkinter.END, current_text)
        except Exception as e:
            outputfile_text.insert(tkinter.END, f"Error reading PDF file: {e}")
    else:
        filename_label.configure(text="No File Selected")
        outputfile_text.delete("1.0", tkinter.END)

root = tkinter.Tk()
root.title("PDF Text Extractor")

filename_label = tkinter.Label(root, text="No File Selected")
outputfile_text = tkinter.Text(root)
openfile_button = tkinter.Button(root, text="Open PDF File", command=openFile)

filename_label.pack()
outputfile_text.pack()
openfile_button.pack()

root.mainloop()
