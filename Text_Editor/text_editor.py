import tkinter as tk
from tkinter import filedialog, messagebox

window = tk.Tk()
window.title("Simple_Text_Editor")
window.geometry("800x600")

text_box = tk.Text(window, wrap="word", undo=True)
text_box.pack(expand=1, fill="both")


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, file.read())
        window.title(f"Simple_Text_Editor - {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_box.get(1.0, tk.END))
        window.title(f"Simple_Text_Editor - {file_path}")
            
def new_file():
    if messagebox.askyesno("New File", "Do you want to save changes?"):
        save_file()
    text_box.delete(1.0, tk.END)
    window.title("Simple_Text_Editor - New File")


def undo():
    text_box.event_generate("<<Undo>>")

def redo():
    text_box.event_generate("<<Redo>>")


def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        window.quit()


menu_bar = tk.Menu(window)
window.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)


edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)


window.mainloop()
