import customtkinter as ctk
from config.theme import *

class Card(ctk.CTkFrame):

       def __init__(self, master, icone, titulo, valor):

              super().__init__(master)

              self.configure(
                width=CARD_WIDTH,
                height=CARD_HEIGHT,
                corner_radius=CARD_RADIUS,
                fg_color=CARD
        )

              self.pack_propagate(False)

              self.icone = icone
              self.titulo = titulo
              self.valor = valor
              self.label_titulo = ctk.CTkLabel(

                     self,

                     text=f"{self.icone} {self.titulo}",

                     font=SUBTITLE,

                     text_color=TEXT

       )

              self.label_titulo.pack(
                     pady=(15,5)
)
     

              self.label_valor = ctk.CTkLabel(

              self,

              text=self.valor,

              font=("Segoe UI",30,"bold"),

              text_color=TEXT

)      

              self.label_valor.pack(
                     pady=(0,15,)
                     
                     
       )