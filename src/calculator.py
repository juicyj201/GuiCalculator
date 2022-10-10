import re
import tkinter
from tkinter import ttk
from tkinter import StringVar

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        if self.x > self.y:
            return self.x - self.y
        else:
            return self.y - self.x

    def mult(self):
        if self.x == 0 or self.y == 0:
            return 0
        else:
            return self.x * self.y

    def div(self):
        if self.x == 0:
            return 0
        elif self.y == 0:
            return "Cannot divide by 0"
        elif self.x == 0 and self.y == 0:
            return "Cannot divide by 0"
        else:
            return self.x / self.y


class RunWindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)

        string = StringVar()
        self.string_exp = string

        self.expression = tkinter.Label(self, textvariable=self.string_exp, height=5, font=15)
        self.zero_btn = ttk.Button(self, text="0", command=lambda e="0": self.input(e))
        self.one_btn = ttk.Button(self, text="1", command=lambda e="1": self.input(e))
        self.two_btn = ttk.Button(self, text="2", command=lambda e="2": self.input(e))
        self.three_btn = ttk.Button(self, text="3", command=lambda e="3": self.input(e))
        self.four_btn = ttk.Button(self, text="4", command=lambda e="4": self.input(e))
        self.five_btn = ttk.Button(self, text="5", command=lambda e="5": self.input(e))
        self.six_btn = ttk.Button(self, text="6", command=lambda e="6": self.input(e))
        self.seven_btn = ttk.Button(self, text="7", command=lambda e="7": self.input(e))
        self.eight_btn = ttk.Button(self, text="8", command=lambda e="8": self.input(e))
        self.nine_btn = ttk.Button(self, text="9", command=lambda e="9": self.input(e))
        self.add_btn = ttk.Button(self, text="+", command=lambda e="+": self.input(e))
        self.sub_btn = ttk.Button(self, text="-", command=lambda e="-": self.input(e))
        self.mult_btn = ttk.Button(self, text="x", command=lambda e="x": self.input(e))
        self.div_btn = ttk.Button(self, text="/", command=lambda e="/": self.input(e))
        #self.confirm_btn = ttk.Button(self, text="Confirm", command=lambda s=self.string_exp.get(): self.click(s))
        self.confirm_btn = ttk.Button(self, text="Confirm", command=self.click)
        self.reset_btn = ttk.Button(self, text="Reset", command=self.reset)

        self.expression.grid(row=0, column=0, sticky="nsew", columnspan=5)
        self.zero_btn.grid(row=1, column=0, sticky="nsew")
        self.one_btn.grid(row=1, column=1, sticky="nsew")
        self.two_btn.grid(row=1, column=2, sticky="nsew")
        self.three_btn.grid(row=2, column=0, sticky="nsew")
        self.four_btn.grid(row=2, column=1, sticky="nsew")
        self.five_btn.grid(row=2, column=2, sticky="nsew")
        self.six_btn.grid(row=3, column=0, sticky="nsew")
        self.seven_btn.grid(row=3, column=1, sticky="nsew")
        self.eight_btn.grid(row=3, column=2, sticky="nsew")
        self.nine_btn.grid(row=4, column=0, sticky="nsew", columnspan=3)
        self.confirm_btn.grid(row=1, column=4, sticky="nsew", rowspan=2)
        self.reset_btn.grid(row=3, column=4, sticky="nsew", rowspan=2)
        self.add_btn.grid(row=1, column=3, sticky="nsew")
        self.sub_btn.grid(row=2, column=3, sticky="nsew")
        self.mult_btn.grid(row=3, column=3, sticky="nsew")
        self.div_btn.grid(row=4, column=3, sticky="nsew")

    def input(self, inp):
        self.string_exp.set(self.string_exp.get() + str(inp))
        print(self.string_exp.get())

    def click(self):
        print(self.string_exp.get())
        if match := re.search(r"^(\d+)([+-x/]+)(\d+)$", self.string_exp.get()):
            x = int(match.group(1))
            y = int(match.group(3))
            operator = str(match.group(2))

            calc = Calculator(x, y)

            if operator == "+":
                self.string_exp.set(str(calc.add()))
                print(calc.add())
            elif operator == "-":
                self.string_exp.set(str(calc.sub()))
                print(calc.sub())
            elif operator == "x":
                self.string_exp.set(str(calc.mult()))
                print(calc.mult())
            elif operator == "/":
                self.string_exp.set(str(calc.div()))
                print(calc.div())
            else:
                self.string_exp.set("Wrong input, please try again")

    def reset(self):
        self.string_exp.set("")


def main():
    gui()


def gui():
    window = RunWindow()
    window.rowconfigure(0, minsize=50)
    window.columnconfigure([2, 2], minsize=50)

    # Run window
    window.eval("tk::PlaceWindow . center")
    window.mainloop()


if __name__ == "__main__":
    main()
