import tkinter as Tk

class App(Tk.Tk):
    def __init__(self):
        Tk.Tk.__init__(self)
        self.scrollbar = Tk.Scrollbar(master=self, highlightcolor = "red", highlightbackground="blue")
        self.scrollbar.pack(side=Tk.RIGHT, fill=Tk.Y)

        self.listbox = Tk.Listbox(master=self, yscrollcommand=self.scrollbar.set)
        for i in range(1000):
            self.listbox.insert(Tk.END, str(i))
        self.listbox.pack(side=Tk.LEFT, fill=Tk.BOTH)

        self.scrollbar.config(command=self.listbox.yview)

master = App()
master.mainloop()