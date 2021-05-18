from tkinter import *
from tkinter import filedialog

# COLORS
WHITE = '#FFFFFF'
BLACK = '#000000'
BLUE = '#0093FF'
GREY_0 = '#D6D6D6'
GREY_1 = '#C6C6C6'


class App:
    def __init__(self):
        self.root = None
        self.width = 500
        self.height = 500

        self.file_path_element = None
        self.file_path = "No file selected"


    def run(self):
        self.root = Tk()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False, False)
        self.root.title("Webpage Analyzer")
        self.root.configure(bg=GREY_1)

        self.file_button = Button(self.root, text="Select video", command=self.get_file)
        self.print_button = Button(self.root, text="Print", command=self.print_command)


        self.file_button.pack()
        self.print_button.pack()

        self.root.mainloop()

# ----------------------------------------------------------------------------------------------------------------------

    def get_file(self):
        self.file_path_element = filedialog.askopenfile(initialdir="/")
        self.file_path = self.file_path_element.name


    def print_command(self):
        print(self.file_path)


# ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    App().run()
