import tkinter as tk
from wcag_contrast_ratio import rgb

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Contrast Suggestor')
        self.configure(background="black")
        self.geometry("500x700")
        self.length = 500
        self.height = 700
        self.text_var = tk.StringVar()
        self.bg_var = tk.StringVar()
        self.entry_frame = tk.Frame(self, bg ="white", width=self.length, height = (self.height/10)*1.5)
        self.display1 = tk.Frame(self, bg = "white", width=self.length - 10, height=(self.height/10)*4.25)
        self.display1.grid(row=0, column=0, pady = 5)
        self.display2 = tk.Frame(self, bg="white", width=self.length - 10, height=(self.height / 10) * 4.25)
        self.display2.grid(row=1, column=0, pady=(0, 5))
        self.entry_frame.grid(row = 2, column = 0, sticky = tk.S)
        self.entry_frame.pack_propagate(False)
        self.create_widgets()

    def create_widgets(self):
        text_frame = tk.Frame(self.entry_frame)
        text_frame.pack(side=tk.TOP, pady=(5,0))
        text_label = tk.Label(text_frame, text = "Enter the text color as a hexcode")
        text_entry = tk.Entry(text_frame, textvariable=self.text_var, font=('calibre', 10, 'normal'))
        text_label.grid(row=0, column=0)
        text_entry.grid(row=0, column=1)
        bg_frame = tk.Frame(self.entry_frame)
        bg_frame.pack(side=tk.TOP, pady=2)
        bg_label = tk.Label(bg_frame, text="Enter the text color as a hexcode")
        bg_entry = tk.Entry(bg_frame, textvariable=self.bg_var, font=('calibre', 10, 'normal'))
        bg_label.grid(row=0, column=0)
        bg_entry.grid(row=0, column=1)
        submit_frame = tk.Frame(self.entry_frame)
        submit_frame.pack(side=tk.TOP, pady=2)
        submit_button = tk.Button(self.entry_frame, text="Submit", command = lambda: self.submit())
        submit_button.pack()

    def submit(self):
        print(f"Text: {self.text_var.get()}, BG: {self.bg_var.get()}")

