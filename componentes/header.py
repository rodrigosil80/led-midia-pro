import customtkinter as ctk
from config.theme import *

class Header(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.configure(height=70,
            fg_color=HEADER)
        
        self.pack( side="top", fill="x")


        self.esquerda = ctk.CTkFrame(
        self,
            fg_color="transparent"
)

        self.esquerda.pack(
            side="left",
            padx=20

)
        
        self.direita = ctk.CTkFrame(
            self,
            fg_color="transparent"
)

        self.direita.pack(
            side="right",
            padx=20
)

        #Lado esquerdo
        
        self.logo = ctk.CTkLabel(
            self.esquerda,
            text="LED Mídia Pro",
            font=TITLE,
            text_color=TEXT
)

        self.logo.pack(
            side="left", padx=20, pady=15
        )


        # Lado direito

        self.usuario = ctk.CTkLabel(
            self.direita,
            text="👤 Rodrigo Garcia",
            font=TEXT_FONT,
            text_color=TEXT

        )

        self.usuario.pack(side="right", padx=20)