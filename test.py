from tkinter import *
import os
from tkinter import filedialog

 
root = Tk()
root.geometry("500x350")
frame = Frame(root)
frame.grid()
 


source_type = StringVar()

def get_type():
	return source_type.get()
def select_source_folder():
	global source_folder
	folder_name = filedialog.askdirectory()
	return source_folder.set(folder_name)

label = Label(frame, text = "Please select Preferred Options ")
label.grid(row = 0, column = 0, columnspan = 4)

label = Label(frame, text = "Please select Source Type to mutate ")
label.grid(row = 1, column = 0, columnspan = 2)
Rbttn_file = Radiobutton(frame, text = "File", variable = source_type, value = 1, command=get_type)
Rbttn_file.grid(row = 1, column = 2, padx = 3, pady = 3)
Rbttn_directory = Radiobutton(frame, text = "Folder", variable = source_type, value = 2, command=get_type)
Rbttn_directory.grid(row = 1, column = 3, padx = 3, pady = 3)
label = Label(frame, text = get_type)
label.grid(row = 2, column = 0)


label = Label(frame, text = "Please select Source ")
label.grid(row = 2, column = 0)

source_folder = StringVar()


file_folder_select_button = Button(frame, text = "Select Source", command = select_source_folder)
file_folder_select_button.grid(row = 2, column = 1)
lbl1 = Label(master=frame, textvariable=source_folder)
lbl1.grid(row = 2, column = 2, columnspan = 2)

print(source_folder)

operator_list = [
'AOD',
"AOR",
"ASR",
"BCR",
"COD",
"COI",
"CRP",
"DDL"
    ]
operator_listbox = Listbox(frame)

for i in range(len(operator_list)):
    operator_listbox.insert(i,operator_list[i])  
operator_listbox.grid()
 
root.title("Wrapper for Mut.py")
root.mainloop()
