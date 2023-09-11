import atexit
import tkinter as tk
from doctest import master
from tkinter import filedialog,font
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Label
from tkinter import *


class NotepadApp:
    def __init__(self,root,variable=None):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("800x600")

        self.our_font = font.Font(family="Helvetica", size="10")
        self.text_widget = scrolledtext.ScrolledText(root,font=self.our_font, wrap=tk.WORD)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        # Add Status Bar to bottom of APP
        self.status_bar = Label(self.root, text='Ready        ', anchor=E)
        self.status_bar.pack(fill=X,side=BOTTOM,ipady=5)


        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        #Add options menu list box for  for font selection
        self.my_listbox = Listbox(root, selectmode=SINGLE, width=80)
        self.my_listbox.pack(side=LEFT)

        #add font families to listbox
        for f in font.families():
            self.my_listbox.insert('end', f)


        # self.my_listbox.option_get(label="Font")
        #Add fonts


        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu, )
        self.edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="(Ctrl+x)")
        self.edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="(Ctrl+c)")
        self.edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="(Ctrl+v)")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Undo", command=self.text_widget.edit_undo, accelerator="(Ctrl+u)")
        self.edit_menu.add_command(label="Redo", command=self.text_widget.edit_redo, accelerator="(Ctrl+z)")

        # Create an instance of the undo stack
        #self.undo_stack = []
    global open_file_name_status
    open_file_name_status = False



    def new_file(self):
        self.text_widget.delete("1.0",END)
        # Update Status bar
        self.root.title('New File')
        self.status_bar.config(text="New File        ")
        open_file_name_status = False

        #Get screen content        current_content= self.text_widget.get(1.0, END)
       #Check for currently open file: check status label or check title        text_file = self.open_file_name_status        text_file = open(text_file, 'r')        content = text_file.read()
       # if current_content == content:            self.text_widget.delete(1.0, tk.END)            #update the status bar            self.text_widget.insert("New File")       else:            self.save_as_file()        open_file_name_status = text_file
    def open_file(self):
        # Delete previous text
        self.text_widget.delete("1.0",END)
        # Grab Filename
        text_file = filedialog.askopenfilename(initialdir="C:/Users/HP/Documents/",title="Open File",
                                               filetypes=[("Text Files","*.txt"),("HTML Files","*.html"),
                                                          ("Python Files","*.py"),("ALL Files","*.*")])

        #check if theres a file open
        if text_file:
            #make filename globally accessible
            open_file_name_status = text_file

            #Update Status x Title bars
            name = text_file
            self.status_bar.config(text=f'{name}        ')
            name = name.rsplit('/', 1)[-1]
            self.root.title(f'{name} - Notepad!')

            #Open the file
            text_file = open(text_file, 'r')
            content = text_file.read()
            #View the file
            self.text_widget.insert(END, content)

    def save_file(self, ):
        global open_file_name_status
        if open_file_name_status:
            text_file = open(open_file_name_status, 'w')
            text_file.write(self.text_widget.get(1.0, END))

            #Put status update or pass code
            self.status_bar.config(text=f'Saved {open_file_name_status}        ')
        else:
            self.save_as_file()

    def save_as_file(self):
        text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Users/HP/Documents/", title="Save File", filetypes=[("Text Files","*.txt"),("HTML Files","*.html"),  ("Python Files","*.py"),("ALL Files","*.*")])
        if text_file:
            #Update Status x Title bars
            name = text_file
            self.status_bar.config(text=f'Saved {name}        ')
            name = name.rsplit('/', 1)[-1]
            self.root.title(f'{name} - Notepad!')

            #save the file
            text_file = open(text_file, 'w')
            text_file.write(self.text_widget.get(1.0, END))

    def cut_text(self):
        selected_text = self.text_widget.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.text_widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.root.clipboard_clear()
        self.root.clipboard_append(selected_text)

    def copy_text(self):
        selected_text = self.text_widget.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.root.clipboard_clear()
        self.root.clipboard_append(selected_text)

    def paste_text(self):
        clipboard_text = self.root.clipboard_get()
        self.text_widget.insert(tk.INSERT, clipboard_text)






if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
