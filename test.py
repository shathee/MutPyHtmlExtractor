from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style, Radiobutton
from tkinter import filedialog


class MainGuiClass(Frame):

    def __init__(self):
        super().__init__()
        self.grid(column = 4,row = 4,padx = 50,pady = 50)
        self.select_source_type_var = IntVar()
        self.source = StringVar()
        self.initUI()

    def type_sel(self):
        selection = self.select_source_type_var
        return selection.get()

    def source_select(self):
        type = self.type_sel()
        if(type == 1):
            filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        elif(type == 2):
            filename = filedialog.askdirectory(initialdir = "/")
        else:
            filename = 'no type selected'
        
        self.source.set(filename)
        

    def initUI(self):

        self.master.title("MutPy Gui")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, pad=5, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)



        lbl = Label(self, text="Please select preferred options", font=("Arial", 25))
        lbl.grid(row=0, column=0, columnspan=4, pady=10)

        
        source_select_radio_type_lbl = Label(self, text="Please select Source type")
        source_select_radio_type_lbl.grid(pady=5, padx=5, columnspan=2)
        source_select_radio_type_btn1 = Radiobutton(self,text="File", variable=self.select_source_type_var, value=1, command=self.type_sel)
        source_select_radio_type_btn1.grid(row=1, column=2, pady=5, padx=5)
        source_select_radio_type_btn2 = Radiobutton(self,text="Folder/Directory", variable=self.select_source_type_var, value=2, command=self.type_sel)
        source_select_radio_type_btn2.grid(row=1, column=3, pady=5, padx=5)
        
        source_selector_btn = Button(self, text="Select Source to Mutate", command=self.source_select)
        source_selector_btn.grid(row=2, column=2)

        source_lbl = Label(self, textvariable=self.source, font=("Arial", 12))
        source_lbl.grid(row=3, column=0, columnspan=4, pady=5)

        mutation_operator_dict = {
            "AOD":"arithmetic operator deletion",
            "AOR":"arithmetic operator replacement",
            "ASR":"assignment operator replacement",
            "BCR":"break continue replacement",
            "COD":"conditional operator deletion",
            "COI":"conditional operator insertion",
            "CRP":"constant replacement",
            "DDL":"decorator deletion",
            "EHD":"exception handler deletion",
            "EXS":"exception swallowing",
            "IHD":"hiding variable deletion",
            "IOD":"overriding method deletion",
            "IOP":"overridden method calling position change",
            "LCR":"logical connector replacement",
            "LOD":"logical operator deletion",
            "LOR":"logical operator replacement",
            "ROR":"relational operator replacement",
            "SCD":"super calling deletion",
            "SCI":"super calling insert",
            "SIR":"slice index remove",
        }

        operator_listbox = Listbox (self)
        operator_listbox.grid(row=4, column=0, columnspan=4, pady=5)
        for key in mutation_operator_dict:
            operator_listbox.insert(END, key) 
            

            # lstbox.insert(END, '{}: {}'.format(key, d[key]))

        # abtn = Button(self, text="Select Source to Mutate")
        # abtn.grid(row=2, column=2)

        # cbtn = Button(self, text="Close")
        # cbtn.grid(row=2, column=3, pady=4)

        # hbtn = Button(self, text="Help")
        # hbtn.grid(row=5, column=0, padx=5)

        # obtn = Button(self, text="OK")
        # obtn.grid(row=5, column=3)


def main():

    root = Tk()
    root.geometry("500x400")
    app = MainGuiClass()
    root.mainloop()


if __name__ == '__main__':
    main()