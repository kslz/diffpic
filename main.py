# -*- coding: utf-8 -*-
"""
    @Time : 2023/8/27 2:26
    @Author : 李子
    @Url : https://github.com/kslz
"""
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk

class ImageDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图片展示小程序")
        self.root.geometry("800x600")

        self.image_label = tk.Label(root)
        self.image_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.path_entry_1 = tk.Entry(root)
        self.path_entry_1.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.path_entry_1.drop_target_register(DND_FILES)
        self.path_entry_1.dnd_bind('<<Drop>>', self.on_drop)

        self.button_1 = tk.Button(root, text="显示图片 1", command=self.display_image_1)
        self.button_1.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.path_entry_2 = tk.Entry(root)
        self.path_entry_2.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        self.path_entry_2.drop_target_register(DND_FILES)
        self.path_entry_2.dnd_bind('<<Drop>>', self.on_drop)

        self.button_2 = tk.Button(root, text="显示图片 2", command=self.display_image_2)
        self.button_2.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

    def on_drop(self, event):
        path = event.data
        event.widget.delete(0, tk.END)
        event.widget.insert(0, path)

    def display_image_1(self):
        path = self.path_entry_1.get()
        if path:
            self.display_image(path)

    def display_image_2(self):
        path = self.path_entry_2.get()
        if path:
            self.display_image(path)

    def display_image(self, image_path):
        img = Image.open(image_path)
        img = self.resize_image(img)
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

    def resize_image(self, img):
        label_width = self.image_label.winfo_width()
        label_height = self.image_label.winfo_height()
        img.thumbnail((label_width, label_height))
        return img

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = ImageDisplayApp(root)
    root.mainloop()