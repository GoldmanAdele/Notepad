import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import scrolledtext

import time


class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Notepad')
        self.root.geometry("1200x660")

        #set variable for open file name
        global open_file_name_status
        open_file_name_status = False

        global selected
        selected =False

        # create Menu
        self.my_menu = tk.Menu(root)
        self.root.config(menu=self.my_menu)



        #Select a font
        our_font = root.font.Font(family="Helvetica", size="32")



    # Create New File Functionsize
    def new_file():
        # Delete previous text
        my_text.delete("1.0",END)
        # Update Status bar
        self.root.title('New File')
        status_bar.config(text="New File        ")
        global open_file_name_status
        open_file_name_status = False



    # Create Open File Function
    def open_file():
        # Delete previous text
        my_text.delete("1.0",END)

        # Grab Filename
        text_file = filedialog.askopenfilename(initialdir="C:/Users/HP/Documents/",title="Open File",
                                               filetypes=[("Text Files","*.txt"),("HTML Files","*.html"), ("Python Files","*.py"),("ALL Files","*.*")])

        #check if theres a file open
        if text_file:
            #make filename globally accessible
            global open_file_name_status
            open_file_name_status = text_file

            #Update Status x Title bars
            name = text_file
            status_bar.config(text=f'{name}        ')
            name = name.rsplit('/', 1)[-1]
            self.root.title(f'{name} - Notepad!')

            #Open the file
            text_file = open(text_file, 'r')
            content = text_file.read()
            #View the file
            my_text.insert(END, content)
            #Close the opened file
            text_file.close()

    #Save as file function
    def save_as_file():
        text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Users/HP/Documents/", title="Save File", filetypes=[("Text Files","*.txt"),("HTML Files","*.html"),  ("Python Files","*.py"),("ALL Files","*.*")])
        if text_file:
            #Update Status x Title bars
            name = text_file
            status_bar.config(text=f'Saved {name}        ')
            name = name.rsplit('/', 1)[-1]
            self.root.title(f'{name} - Notepad!')

            #save the file
            text_file = open(text_file, 'w')
            text_file.write(my_text.get(1.0, END))

            #close the file
            text_file.close()

    #Save File
    def save_file():
        global open_file_name_status
        if open_file_name_status:
            text_file = open(open_file_name_status, 'w')
            text_file.write(my_text.get(1.0, END))
            #close the file
            text_file.close()
            #Put status update or pop code

            status_bar.config(text=f'Saved {open_file_name_status}        ')
        else:
            save_as_file()

    #Cut Text
    def cut_text(e):
        #define selected text as a variable
        global selected
        #check if a keyboard shortcut was used
        if e:
            selected = self.root.clipboard_get()
        else:
            if my_text.selection_get():
                #grab selected text
                selected = my_text.selection_get()
                #delete seleted text from text box
                my_text.delete("sel.first", "sel.last")
                #clear th e clipt board, include selected text
                self.root.clipboard_clear()
                self.root.clipboard_append(selected)


    #Copy Text
    def copy_text(e):
        global selected
        #check if a keyboard shortcut was used
        if e:
            selected = self.root.clipboard_get()
        if my_text.selection_get():
            #grab selected text
            selected = my_text.selection_get()
            #clear th e clipt board, include selected text
            self.root.clipboard_clear()
            self.root.clipboard_append(selected)

    #Paste Text
    def paste_text(e):
        global selected
        #check if event e - a keyboard shortcut was used
        if e:
            selected = self.root.clipboard_get()
        else:
            if selected:
                #define cursor position
                position = my_text.index(INSERT)
                my_text.insert(position, selected)


    # create Text widget
    my_text = scrolledtext.ScrolledText
        #(font=our_font,selectbackground="yellow",selectforeground="black", undo=True, yscrollcommand=text_scroll.set, xscrollcommand=side_scroll.set,wrap=NONE)
#    my_text.pack()

    # create our scrollbar for the text box    text_scroll = Scrollbar()    text_scroll.pack(side=RIGHT,fill=Y)

    #horizontal scrollbar
   # side_scroll= Scrollbar(my_text, orient='horizontal')
   # side_scroll.pack(side=BOTTOM, fill=X)


    #Add listbox
 #   my_listbox = OptionMenu(my_text, selectmode=SINGLE, width=80)
 #   my_listbox.place(x=0,y=0)


    #Add fonts
    #for f in font.families():
    #    my_listbox.insert('end', f)

    # configure our scrollbar    text_scroll.config(command=my_text.yview)    side_scroll.config(command=my_text.xview)

    # Add File Menu
    file_menu = Menu(my_menu,tearoff=False)
    self.my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Save As", command=save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=self.root.quit)

    # Add Edit Menu
    edit_menu = Menu(self.my_menu,tearoff=False)
    self.my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut       ", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
    edit_menu.add_command(label="Copy      ", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
    edit_menu.add_command(label="Paste     ", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
    edit_menu.add_separator()
    edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(Ctrl+z)")
    edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="(Ctrl+y)")

    new_window_btn = Button(my_frame, text="New Window", command=new_window)
    new_window_btn.place(x=120,y=-10)

    # Add Status Bar to bottom of APP
    status_bar = Label(self.root, text='Ready        ', anchor=E)
    status_bar.pack(fill=X, side=BOTTOM, ipady=5)




if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()