class Settings:
    # Clase para guardar toda la configuración del juego.
    def __init__(self):
        # Inicializa la configuración del juego.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        
        # Configuración de la nave
        self.ship_speed = 1.5