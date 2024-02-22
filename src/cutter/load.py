import customtkinter as ctk
from PIL import ImageTk

class AppImage(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk | ctk.CTkFrame, image_path: str, **kwargs):
        super().__init__(master)
        self.image = ImageTk.PhotoImage(file=image_path)
        self.image_canvas = ctk.CTkCanvas(self, width=self.image.width(), height=self.image.height(),
                                        bg=master.cget("bg"), highlightthickness=0, bd=0)
        self.image_canvas.create_image(0, 0, anchor=ctk.NW, image=self.image)
        self.image_canvas.pack(kwargs)

