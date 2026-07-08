import customtkinter as ctk

from config.theme import *

class Dashboard(ctk.CTkFrame):

        def __init__(self, master):

            super().__init__(master)

            self.criar_layout()

        def criar_layout(self):

            titulo = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Segoe UI", 30, "bold")
        )

            titulo.pack(pady=30)