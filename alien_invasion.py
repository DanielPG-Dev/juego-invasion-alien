import sys
import pygame

class AlienInvasion:
    # Clase general para gestionar los recursos y el comportamiento del juego.
    
    def __init__(self):
    # Inicializa el juego y crea recursos.
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        # Configurar el color de fondo
        self.bg_color = (230,230,230)

# pygame.init()
# pygame.display.set_mode((1000,800))
# pygame.display.set_caption("Alien Invasion")

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

    def run_game(self):
        # Inicia el bucle para el juego.
        while True:
            # Busca eventos de teclado y ratón.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            # Redibuja la pantalla en cada paso por el bucle.
            self.screen.fill(self.bg_color)
             
            # Hace visible la última pantalla dibujada.
            pygame.display.flip()

if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()