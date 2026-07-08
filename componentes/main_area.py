import customtkinter as ctk

class MainArea(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.configure(fg_color="red")

        self.pack(

            side="right",
            fill="both",
            expand=True

        )