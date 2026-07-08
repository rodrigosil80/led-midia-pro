import customtkinter as ctk

from componentes.header import Header
from componentes.sidebar import Sidebar
from componentes.main_area import MainArea
from telas.dashboard import Dashboard

class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("LED Mídia Pro")
        self.geometry("1400x800")
        self.header = Header(self)
        self.sidebar = Sidebar(self)
        self.main_area = MainArea(self)
        self.dashboard = Dashboard(self.main_area)

        self.dashboard.pack(
            fill="both",
        expand=True
)

if __name__ == "__main__":
    app = App()
    app.mainloop()