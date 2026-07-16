import customtkinter as ctk
from componentes.card import Card
from config.theme import *

class Dashboard(ctk.CTkFrame):

        def __init__(self, master):

            super().__init__(master)
            

            self.criar_layout()        

        def criar_layout(self):
            

    # =========================
    # TÍTULO DO DASHBOARD
    # =========================
            titulo = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Segoe UI", 30, "bold")
    )

            titulo.pack(pady=30)


    # =========================
    # ÁREA DOS CARDS
    # =========================
            self.cards_frame = ctk.CTkFrame(
            self
    )

            self.cards_frame.pack(
            padx=10,
            pady=10
            
    )


    # =========================
    # CARD CLIENTES
    # =========================
                      
            self.criar_card(
            "👥",
            "Clientes",
            "25"
)
                       
            self.criar_card(
           "📺",
           "Anúcios",
           "18"
)    
           
            self.criar_card(
            "💰",
            "Receitas",
            "100"
        )    
            
            self.criar_card(
           "💰",
           "Exibições",
           "1000"
        )    

                     
        def criar_card(self, icone, titulo, valor):

                card = Card(
                self.cards_frame,
                icone=icone,
                titulo=titulo,
                valor=valor
)

                card.pack(
                side="left",
                padx=20,
                pady=20
)