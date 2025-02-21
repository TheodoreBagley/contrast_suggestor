import tkinter as tk
from logic import check_colors, suggestion_handler

# Initialize GUI
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
        # Initialize frames
        self.entry_frame = tk.Frame(self, bg ="white", width=self.length, height = (self.height/10)*1.5)
        self.display1 = tk.Frame(self, bg = "white", width=self.length - 10, height=(self.height/10)*4.25)
        self.display1.grid(row=0, column=0, pady = 5)
        self.display2 = tk.Frame(self, bg="white", width=self.length - 10, height=(self.height / 10) * 4.25)
        self.display2.grid(row=1, column=0, pady=(0, 5))
        self.entry_frame.grid(row = 2, column = 0, sticky = tk.S)
        self.entry_frame.pack_propagate(False)
        self.create_widgets()

    # Create frame and button widgets to use
    def create_widgets(self):
        text_frame = tk.Frame(self.entry_frame)
        text_frame.pack(side=tk.TOP, pady=(5,0))
        text_label = tk.Label(text_frame, text = "Enter the text color as a hexcode")
        text_entry = tk.Entry(text_frame, textvariable=self.text_var, font=('calibre', 10, 'normal'))
        text_label.grid(row=0, column=0)
        text_entry.grid(row=0, column=1)
        bg_frame = tk.Frame(self.entry_frame)
        bg_frame.pack(side=tk.TOP, pady=2)
        bg_label = tk.Label(bg_frame, text="Enter the background color as a hexcode")
        bg_entry = tk.Entry(bg_frame, textvariable=self.bg_var, font=('calibre', 10, 'normal'))
        bg_label.grid(row=0, column=0)
        bg_entry.grid(row=0, column=1)
        submit_frame = tk.Frame(self.entry_frame)
        submit_frame.pack(side=tk.TOP, pady=2)
        submit_button = tk.Button(self.entry_frame, text="Submit", command = lambda: self.submit())
        submit_button.pack()
    # function the submit button uses. basically reloads the root
    def submit(self):
        checked = check_colors(self.text_var.get(), self.bg_var.get())
        self.display1.destroy()
        self.display2.destroy()
        self.display1 = tk.Frame(self, bg = self.bg_var.get(), width=self.length - 10, height=(self.height/10)*4.25)
        self.display2 = tk.Frame(self, bg=self.text_var.get(), width=self.length - 10, height=(self.height / 10) * 4.25)
        self.display1.grid(row=0, column=0, pady = 5)
        self.display2.grid(row=1, column=0, pady=(0, 5))
        self.display1.pack_propagate(False)
        self.display2.pack_propagate(False)
        # if the check fails
        if checked[0] is False:
            d1_label = tk.Label(self.display1, text="This fails WCAG compliance", bg=self.bg_var.get(), fg=self.text_var.get(),
                                font=('calibre', 16, 'normal'))
            d1_label.pack(fill=tk.BOTH, expand=True)
            d2_label = tk.Label(self.display2, text="It is hard to read either way you use it", bg=self.text_var.get(),fg=self.bg_var.get(),
                                font=('calibre', 16, 'normal'))
            d2_label.pack(fill=tk.BOTH, expand=True)
            self.entry_frame.destroy()
            self.entry_frame = tk.Frame(self, bg="white", width=self.length, height=(self.height / 10) * 1.5)
            self.entry_frame.grid(row=2, column=0, sticky=tk.S)
            self.entry_frame.pack_propagate(False)
            center_frame = tk.Frame(self.entry_frame)
            center_frame.pack(side=tk.TOP)
            center_frame.pack_propagate(False)
            entry_label = tk.Label(center_frame, text="Would you like a suggestion?", font=('calibre', 10, 'normal'))
            entry_label.grid(row=0, column=0, pady=(4,0), sticky="EW")
            suggest_bg = tk.Button(center_frame, text="Suggest background color", font=('calibre', 10, 'normal'), command= lambda: self.suggest_color(self.text_var.get(), "text"))
            suggest_text = tk.Button(center_frame, text="Suggest text color", font=('calibre', 10, 'normal'), command= lambda: self.suggest_color(self.bg_var.get(), "bg"))
            suggest_text.grid(row=1, column=0, sticky="EW")
            suggest_bg.grid(row=2, column=0, sticky="EW")
        # if check passes
        elif checked[0] is True:
            d1_label = tk.Label(self.display1, text="This passes WCAG compliance", bg=self.bg_var.get(),
                                fg=self.text_var.get(),
                                font=('calibre', 16, 'normal'))
            d1_label.pack(fill=tk.BOTH, expand=True)
            d2_label = tk.Label(self.display2, text="It is readable either way you combine it", bg=self.text_var.get(),
                                fg=self.bg_var.get(),
                                font=('calibre', 16, 'normal'))
            d2_label.pack(fill=tk.BOTH, expand=True)
            self.entry_frame.destroy()
            self.entry_frame = tk.Frame(self, bg="white", width=self.length, height=(self.height / 10) * 1.5)
            self.entry_frame.grid(row=2, column=0, sticky=tk.S)
            self.entry_frame.pack_propagate(False)
            center_frame = tk.Frame(self.entry_frame)
            center_frame.pack(side=tk.TOP)
            center_frame.pack_propagate(False)
            entry_label = tk.Label(center_frame, text="Would you like a suggestion?",
                                   font=('calibre', 10, 'normal'))
            entry_label.grid(row=0, column=0, pady=(4, 0), sticky="EW")
            suggest_text = tk.Button(center_frame, text="Suggest background color", font=('calibre', 10, 'normal'),
                                     command=lambda: self.suggest_color(self.text_var.get(), "text"))
            suggest_bg = tk.Button(center_frame, text="Suggest text color", font=('calibre', 10, 'normal'),
                                   command=lambda: self.suggest_color(self.bg_var.get(), "bg"))
            suggest_text.grid(row=1, column=0, sticky="EW")
            suggest_bg.grid(row=2, column=0, sticky="EW")

    # suggest color and reload frame again
    def suggest_color(self, color, text_type):
        suggested_color = suggestion_handler(color)
        if text_type == "text":
            self.display1.destroy()
            self.display2.destroy()
            self.display1 = tk.Frame(self, bg=suggested_color, width=self.length - 10,
                                     height=(self.height / 10) * 4.25)
            self.display2 = tk.Frame(self, bg=color, width=self.length - 10,
                                     height=(self.height / 10) * 4.25)
            self.display1.grid(row=0, column=0, pady=5)
            self.display2.grid(row=1, column=0, pady=(0, 5))
            self.display1.pack_propagate(False)
            self.display2.pack_propagate(False)
            d1_label = tk.Label(self.display1, text="This color is a good fit", bg=suggested_color,
                                fg=color,
                                font=('calibre', 16, 'normal'))
            d1_label.pack(fill=tk.BOTH, expand=True)
            d2_label = tk.Label(self.display2, text=f"The hexcode is {suggested_color}", bg=color,
                                fg=suggested_color,
                                font=('calibre', 16, 'normal'))
            d2_label.pack(fill=tk.BOTH, expand=True)
            self.entry_frame.destroy()
            self.entry_frame = tk.Frame(self, bg="white", width=self.length, height=(self.height / 10) * 1.5)
            self.entry_frame.grid(row=2, column=0, sticky=tk.S)
            self.entry_frame.pack_propagate(False)
            center_frame = tk.Frame(self.entry_frame)
            center_frame.pack(side=tk.TOP)
            center_frame.pack_propagate(False)
            entry_label = tk.Label(center_frame, text="Would you like another suggestion?", font=('calibre', 10, 'normal'))
            entry_label.grid(row=0, column=0, pady=(4, 0), sticky="EW")
            suggest_text = tk.Button(center_frame, text="Suggest background color", font=('calibre', 10, 'normal'),
                                     command=lambda: self.suggest_color(self.text_var.get(), "text"))
            suggest_text.grid(row=1, column=0, sticky="EW")
        else:
            self.display1.destroy()
            self.display2.destroy()
            self.display1 = tk.Frame(self, bg=color, width=self.length - 10,
                                     height=(self.height / 10) * 4.25)
            self.display2 = tk.Frame(self, bg=suggested_color, width=self.length - 10,
                                     height=(self.height / 10) * 4.25)
            self.display1.grid(row=0, column=0, pady=5)
            self.display2.grid(row=1, column=0, pady=(0, 5))
            self.display1.pack_propagate(False)
            self.display2.pack_propagate(False)
            d1_label = tk.Label(self.display1, text="This color is a good fit", bg=color,
                                fg=suggested_color,
                                font=('calibre', 16, 'normal'))
            d1_label.pack(fill=tk.BOTH, expand=True)
            d2_label = tk.Label(self.display2, text=f"The hexcode is {suggested_color}", bg=suggested_color,
                                fg=color,
                                font=('calibre', 16, 'normal'))
            d2_label.pack(fill=tk.BOTH, expand=True)
            self.entry_frame.destroy()
            self.entry_frame = tk.Frame(self, bg="white", width=self.length, height=(self.height / 10) * 1.5)
            self.entry_frame.grid(row=2, column=0, sticky=tk.S)
            self.entry_frame.pack_propagate(False)
            center_frame = tk.Frame(self.entry_frame)
            center_frame.pack(side=tk.TOP)
            center_frame.pack_propagate(False)
            entry_label = tk.Label(center_frame, text="Would you like another suggestion?",
                                   font=('calibre', 10, 'normal'))
            entry_label.grid(row=0, column=0, pady=(4, 0), sticky="EW")
            suggest_bg = tk.Button(center_frame, text="Suggest text color", font=('calibre', 10, 'normal'),
                                     command=lambda: self.suggest_color(self.bg_var.get(), "bg"))
            suggest_bg.grid(row=1, column=0, sticky="EW")