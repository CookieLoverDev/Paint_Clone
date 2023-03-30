import tkinter as tk
from PIL import Image, ImageDraw
from tkinter.colorchooser import askcolor
from tkinter import filedialog

class Paint:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Paint from Wallmart")

        self.brush_size = 15
        self.current_color = "#000000"

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both")

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)

        self.save_btn = tk.Button(self.frame, text="Save", command=self.save)
        self.save_btn.grid(row=0, column=0, sticky=tk.W+tk.E, padx=5)

        self.clear_btn = tk.Button(self.frame, text="Clear", command=self.clear)
        self.clear_btn.grid(row=0, column=1, sticky=tk.W+tk.E, padx=5)

        self.color_btn = tk.Button(self.frame, text="Change Color", command=self.choose_color)
        self.color_btn.grid(row=0, column=2, sticky=tk.W+tk.E, padx=5)

        self.brush_btn = tk.Scale(self.frame, from_= 1, to=20, orient="horizontal")
        self.brush_btn.grid(row=0, column=3, sticky=tk.W+tk.E, pady=5, padx=5)

        self.canvas = tk.Canvas(self.frame, width=500, height=500, bg='#FFFFFF')
        self.canvas.grid(row=1, columnspan=4)
        self.canvas.bind("<B1-Motion>", self.paint)

        self.image = Image.new("RGB", (510, 510), "#FFFFFF")
        self.draw = ImageDraw.Draw(self.image)

    def paint(self, event):
        x1, y1 = event.x, event.y
        x2, y2 = event.x, event.y
        self.brush_size = self.brush_btn.get()
        self.canvas.create_line(x1, y1, x2, y2, fill=self.current_color, width=self.brush_size, capstyle="round", smooth=True)
        self.draw.line([x1, y1, x2+self.brush_size, y2+self.brush_size], fill=self.current_color, width=self.brush_size)
    
    def save(self):
        filename = filedialog.asksaveasfilename(
            initialfile="untitled.png",
            defaultextension="png",
            filetypes=[("PNG", "JPG"), (".png", ".jpg")]
        )

        if filename != "":
            self.image.save(filename)

    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, 1000, 1000], fill="#FFFFFF")

    def choose_color(self):
        color = askcolor(title="Choose color")
        self.current_color = color[1]

    def run(self):
        self.root.mainloop()

app = Paint()
app.run()