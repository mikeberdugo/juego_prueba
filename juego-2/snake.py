import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
width = 640
height = 480

# Puntuación inicial
score = 0
# Fuente de texto
font = pygame.font.Font(None, 36)

snake_length = 1
# Lista para almacenar el cuerpo de la serpiente
snake_body = []

mode = 0

# Definir el tamaño del bloque
block_size = 20

# Calcular la cantidad de bloques en el ancho y alto de la ventana
block_width = width // block_size
block_height = height // block_size

# Definir los colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


# Crear la ventana
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Definir la posición inicial de la serpiente
snake_x = random.randint(0, block_width - 1) * block_size
snake_y = random.randint(0, block_height - 1) * block_size

# Inicializar la dirección de la serpiente
snake_direction = "RIGHT"

# Definir la velocidad de la serpiente
snake_dx = 0
snake_dy = 0
snake_speed = 6.0

# Definir la posición inicial de la comida
food_x = random.randint(0, block_width - 1) * block_size
food_y = random.randint(0, block_height - 1) * block_size


# poison 
poison_x1 = random.randint(10, block_width - 1) * block_size
poison_y1 = random.randint(10, block_height - 1) * block_size
            
poison_x2 = random.randint(10, block_width - 1) * block_size
poison_y2 = random.randint(10, block_height - 1) * block_size

escalab = 0.3

# Bucle principal del juego
    
    
def run():
    screen.fill(white)
    # Bucle principal del juego
    while True:
        if mode == 0 : 
            menu_init()
        elif mode == 1 :
            game()
        elif mode == 2 :
            game_over()
            
        # Actualizar la pantalla
        clock.tick(12)


def game_over():
    global score
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    screen.fill(black)
    text = font.render("Puntuación: " + str(score), True,white)
    screen.blit(text, (width // 2,height // 2))
    pygame.display.flip()
    



def menu_init():
    global mode
    screen.fill(black)
    screen.fill(white)
    start_button = pygame.transform.scale(pygame.image.load("menu/boton-de-inicio.png"), ((int(height* escalab ), int(height * escalab))))
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (width // 2,height // 2)
    screen.blit(start_button, start_button_rect)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_pos):
                mode = 1

        if mode == 1 :
            break
        
    

def game():
    global snake_direction,snake_x,snake_y,food_x ,food_y,poison_x1,poison_y1,poison_x2,poison_y2,score,mode,snake_length,snake_speed
    numero_aleatorio = 0 
    while True:
        cont = 0 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != "DOWN":
                    snake_direction = "UP"
                elif event.key == pygame.K_DOWN and snake_direction != "UP":
                    snake_direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                    snake_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                    snake_direction = "RIGHT"

        # Mover la serpiente
        if snake_direction == "UP":
            snake_y -= block_size
        elif snake_direction == "DOWN":
            snake_y += block_size
        elif snake_direction == "LEFT":
            snake_x -= block_size
        elif snake_direction == "RIGHT":
            snake_x += block_size


        snake_x += snake_dx
        snake_y += snake_dy
        
        # Verificar si la serpiente ha alcanzado los límites de la ventana
        if snake_x < 10 or snake_x >= width-10 or snake_y < 10 or snake_y >= height-10:
            mode = 2 
            break
        
        
        

        # Verificar si la serpiente ha comido la comida
        if snake_x == food_x and snake_y == food_y:
            # Generar nueva posición para la comida
            score += 1
            snake_length += 1
            snake_speed += 0.1
            food_x = random.randint(10, block_width - 1) * block_size
            food_y = random.randint(10, block_height - 1) * block_size
            
            poison_x1 = random.randint(10, block_width - 1) * block_size
            poison_y1 = random.randint(10, block_height - 1) * block_size
            
            poison_x2 = random.randint(10, block_width - 1) * block_size
            poison_y2 = random.randint(10, block_height - 1) * block_size
            # Aumentar la longitud de la serpiente
            
            
        if 10 == food_x and 10 == food_y : 
            food_x = random.randint(10, block_width - 1) * block_size
            food_y = random.randint(10, block_height - 1) * block_size
            
        if 10 == snake_x and 10 == snake_y : 
            mode = 2 
            break
            

            
        if snake_x == poison_x2 and snake_y == poison_y2:
            score -= 1
            snake_length -= 1
            snake_body.pop()
            food_x = random.randint(10, block_width - 1) * block_size
            food_y = random.randint(10, block_height - 1) * block_size
            
            poison_x1 = random.randint(10, block_width - 1) * block_size
            poison_y1 = random.randint(10, block_height - 1) * block_size
            
            poison_x2 = random.randint(10, block_width - 1) * block_size
            poison_y2 = random.randint(10, block_height - 1) * block_size
        
        
        if snake_x == poison_x1 and snake_y == poison_y1:
            score -= 1
            snake_length -= 1
            snake_body.pop()
            food_x = random.randint(10, block_width - 1) * block_size
            food_y = random.randint(10, block_height - 1) * block_size
            
            poison_x1 = random.randint(10, block_width - 1) * block_size
            poison_y1 = random.randint(10, block_height - 1) * block_size
            
            poison_x2 = random.randint(10, block_width - 1) * block_size
            poison_y2 = random.randint(10, block_height - 1) * block_size
            
            


            
        # Limpiar la pantalla
        screen.fill(black)
        screen.fill(white)
        
        
        
        # Dibujar la serpiente
            # Actualizar el cuerpo de la serpiente
        snake_body.insert(0, (snake_x, snake_y))
        if len(snake_body) > snake_length:
            snake_body.pop()
        
        if snake_length == 1 :
            pygame.draw.rect(screen, green, (snake_x,snake_y, block_size, block_size))
        else : 
            for x, y in snake_body:
                cont+= 1
                pygame.draw.rect(screen, green, (x,y, block_size, block_size))
                if cont == 1:
                    aux_x,aux_y = x,y
                else:    
                    if aux_x == x and aux_y == y:
                        mode = 2 
                        break
        
        if mode == 2:
            break

        # Dibujar la comida
        pygame.draw.rect(screen, red, (food_x, food_y, block_size, block_size))
        
        #dibuja los venenos 
        pygame.draw.rect(screen, black, (poison_x1, poison_y1, block_size, block_size))
        
        pygame.draw.rect(screen, black, (poison_x2, poison_y2, block_size, block_size))
        
        # dibuja el puntaje 
        text = font.render("Puntuación: " + str(score), True,black)
        screen.blit(text, (10, 10))

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad del juego
        clock.tick(snake_speed)


if __name__ == "__main__":
    run()
    pygame.quit()