import tkinter as tk
from tkinter import messagebox
from docx import Document

# List of words to display as options
words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Function to create the Word document
def create_document():
    selected_words = []
    for word, var in checkboxes.items():
        if var.get():
            selected_words.append(word)

    if not selected_words:
        messagebox.showwarning("Warning", "No words selected!")
        return

    document = Document()
    for word in selected_words:
        document.add_heading(word, level=1)

    document.save("SelectedWords.docx")
    messagebox.showinfo("Success", "Word document created successfully!")

# Create the main tkinter window
root = tk.Tk()
root.title("Word Selection")

# Dictionary to hold checkbox variables
checkboxes = {}

# Add checkboxes for each word
for word in words:
    var = tk.BooleanVar()
    checkboxes[word] = var
    checkbox = tk.Checkbutton(root, text=word, variable=var)
    checkbox.pack(anchor="w")

# Add a button to generate the document
generate_button = tk.Button(root, text="Generate Document", command=create_document)
generate_button.pack(pady=10)

# Run the application
root.mainloop()
