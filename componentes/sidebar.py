import customtkinter as ctk

from config.theme import *

class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        
        super().__init__(master)

        self.configure(

            width=220,

            fg_color=SIDEBAR

        )

        self.pack(

            side="left",

            fill="y"


        )

        self.criar_botao("🏠 Dashboard")

        self.criar_botao("👥 Clientes")

        self.criar_botao("📄 Relatórios")

        self.criar_botao("⚙ Configurações")

    def criar_botao(self, texto):

            botao = ctk.CTkButton(

            self,

            text=texto

    )

            botao.pack(

            fill="x",

            padx=15,

            pady=8

    )