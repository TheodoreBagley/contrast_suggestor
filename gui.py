import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Contrast Suggestor')
        self.configure(background="black")
        self.geometry("700x900")
        self.length = 700
        self.height = 900
        self.entry_frame = tk.Frame(self, bg ="white", width=self.length, height = self.height/10)
        self.display1 = tk.Frame(self, bg = "white", width=self.length - 10, height=(self.height/10)*4)
        self.display1.grid(row=0, column=0, pady = 5)
        self.entry_frame.grid(row = 3, column = 0, sticky = tk.S)
        check = 'yee'