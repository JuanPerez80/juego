import pygame
import sys
import os

# Inicializar Pygame
pygame.init()

# Obstaculos y/o tiles de la habitacion
obstaculos_habitacion = [544, 545, 546, 547, 516, 548, 517, 485, 453, 452, 451, 450, 449, 448, 486, 487, 488, 489, 490, 491, 492, 493, 461, 429, 397, 365, 366, 367, 368, 369, 370, 371, 403, 435, 467, 398, 399, 400, 432, 431, 433, 463, 464, 497, 495, 462, 468, 436, 404, 469, 437, 405, 373, 341, 340, 308, 307, 306, 573, 574, 575, 540, 541, 542, 543, 511, 510, 509, 508, 476, 477, 478, 479, 445, 414, 539, 506, 474, 475, 473, 472, 440, 441, 442, 443, 408, 409, 410, 411, 376, 377, 378, 379, 380, 344, 312, 280, 248, 216, 184, 152]


# Dimensiones de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego con Personaje Animado")

# Cargar fondo
fondo = pygame.image.load("habitacion_del_personaje.png")
fondo = pygame.transform.scale(fondo, (800, 600))  # Ajustar al tamaño de la ventana

# Cargar animaciones del personaje
ruta_personaje = "personaje"
frames_caminata = []

# Verificar que los archivos existen
for i in range(1, 5):  # Ajusta el rango según el número de frames que tengas
    archivo = os.path.join(ruta_personaje, f"Walk ({i}).png")
    if os.path.exists(archivo):
        img = pygame.image.load(archivo)
        img = pygame.transform.scale(img, (320, 320))  # Tamaño del personaje ajustado
        frames_caminata.append(img)
    else:
        print(f"⚠️ No se encontró: {archivo}")

if not frames_caminata:
    print("❌ No se cargaron imágenes de caminata. Verifica la carpeta y nombres de archivos.")
    sys.exit()

# Variables del personaje
personaje_x, personaje_y = 100, 400
personaje_ancho, personaje_alto = 80, 80  # Dimensiones del personaje
velocidad = 6
indice_frame = 0  # Para animar el personaje
reloj = pygame.time.Clock()


# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Movimiento del personaje con límites
    teclas = pygame.key.get_pressed()
    moviendo = False  # Variable para controlar si el personaje se mueve

    if teclas[pygame.K_LEFT] and personaje_x > 0:
        personaje_x -= velocidad
        moviendo = True
    if teclas[pygame.K_RIGHT] and personaje_x < ANCHO - personaje_ancho:
        personaje_x += velocidad
        moviendo = True
    if teclas[pygame.K_UP] and personaje_y > 0:
        personaje_y -= velocidad
        moviendo = True
    if teclas[pygame.K_DOWN] and personaje_y < ALTO - personaje_alto:
        personaje_y += velocidad
        moviendo = True

    # Actualizar frame de animación si el personaje se mueve
    if moviendo:
        indice_frame = (indice_frame + 1) % len(frames_caminata)

    # Dibujar fondo y personaje
    ventana.blit(fondo, (0, 0))  # Fondo
    ventana.blit(frames_caminata[indice_frame], (personaje_x, personaje_y))  # Personaje animado

    pygame.display.flip()
    reloj.tick(10)  # Controlar velocidad de animación

pygame.quit()
sys.exit()
