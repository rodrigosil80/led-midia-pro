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
            self.card_clientes = Card(
            self.cards_frame,
            icone="👥",
            titulo="Clientes",
            valor="25"
        )    

            self.card_clientes.pack(
            side="left",
            pady=20,
            padx=20
    )
            
            self.card_anuncios = Card(
            self.cards_frame,
            icone="📺",
            titulo="Anúcios",
            valor="18"
        )    

            self.card_anuncios.pack(
            side="left",
            pady=20,
            padx=20
    )
            
            self.card_receitas = Card(
            self.cards_frame,
            icone="💰",
            titulo="Receitas",
            valor="100"
        )    

            self.card_receitas.pack(
            side="left",
            pady=20,
            padx=20
    )
            
            self.card_exibicoes = Card(
            self.cards_frame,
            icone="💰",
            titulo="Exibições",
            valor="1000"
        )    

            self.card_exibicoes.pack(
            side="left",
            pady=20,
            padx=20
    )
            
            def criar_card(self, icone, titulo, valor):

                card = Card(
                    
                self.cards_frame,
                icone = icone,
                titulo = titulo,
                valor = valor

                )