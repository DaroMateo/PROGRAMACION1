import pygame

pygame.init()

ANCHO = 1200
ALTO = 900

pantalla = pygame.display.set_mode([ANCHO, ALTO])

# Imagen personaje
imagen_personaje = pygame.image.load("Programacion_I_2C/Clase_17/personaje.jpg")
imagen_personaje = pygame.transform.scale(imagen_personaje, (225, 225))
rect_personaje = imagen_personaje.get_rect() # Rect -> Ubicacion (X, Y) y Tamaño (ancho y alto) -> Colisiones
rect_personaje.x = 200
rect_personaje.y = 675

# Iamgen Roca
imagen_roca = pygame.image.load("Programacion_I_2C/Clase_17/roca.jpg")
imagen_roca = pygame.transform.scale(imagen_roca, (225, 225))
rect_roca = imagen_roca.get_rect()
rect_roca.x = (ANCHO - rect_roca.width) / 2
rect_roca.y = (ALTO - rect_roca.height) / 2

# Eventos propios

mi_evento = pygame.USEREVENT + 1 
un_segundo = 1000 # 1000 milisegundos = 1 segundo
pygame.time.set_timer(mi_evento, un_segundo)
contador_segundos = 0

# Evento para mover el personaje 

mi_evento_tick = pygame.USEREVENT + 2
pygame.time.set_timer(mi_evento_tick, 5)

# Textos en la pantalla 

nombre_ingresado = ""
fuente = pygame.font.SysFont("Arial", 72, bold=True)
mi_texto = fuente.render(f"Time: {contador_segundos}", True, "goldenrod")
nombre_usuario = fuente.render(nombre_ingresado, True, "mediumaquamarine")


corriendo = True

while corriendo == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            corriendo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            #evento.pos # -> hace lo mismo que la linea de abajo
            pos_click = pygame.mouse.get_pos() # X, Y
            
            # if pos_click[0] >= mi_boton_verde.x and pos_click[0] <= mi_boton_verde.x + mi_boton_verde.width and pos_click[1] >= mi_boton_verde.y and pos_click[1] <= mi_boton_verde.y + mi_boton_verde.height:
            if mi_boton_verde.collidepoint(pos_click) == True:
                print("Clickeo el boton")
            #print("Hizo click")
            # if evento.button == 1:
            #     print("Click IZQ")
            # if evento.button == 2:
            #     print("Click RUEDITA")
            # if evento.button == 3:
            #     print("Click DER")
            # if evento.button == 4:
            #     print("Ruedita Arriba")
            # if evento.button == 5:
            #     print("Ruedita Abajo") 
        if evento.type == mi_evento:
            contador_segundos += 1
            mi_texto = fuente.render(f"Time: {contador_segundos}", True, "goldenrod")
            #print(f"Pasaron {contador_segundos} segundos...")
        if evento.type == mi_evento_tick:
            teclas_apretadas = pygame.key.get_pressed() # Lista de Booleanos, donde True es una tecla apretada
            if teclas_apretadas[pygame.K_LEFT]:
                rect_personaje.x -= 1
                if rect_personaje.colliderect(rect_roca) == True:
                    rect_personaje.x += 1
            if teclas_apretadas[pygame.K_RIGHT]:
                rect_personaje.x += 1
                if rect_personaje.colliderect(rect_roca) == True:
                    rect_personaje.x -= 1
            if teclas_apretadas[pygame.K_UP]:
                rect_personaje.y -= 1
                if rect_personaje.colliderect(rect_roca) == True:
                    rect_personaje.y += 1
            if teclas_apretadas[pygame.K_DOWN]:
                rect_personaje.y += 1
                if rect_personaje.colliderect(rect_roca) == True:
                    rect_personaje.y -= 1
        # if evento.type == pygame.KEYDOWN:
        #     if evento.key == pygame.K_LEFT:
        #         rect_personaje.x -= 10
        #     if evento.key == pygame.K_RIGHT:
        #         rect_personaje.x += 10
        #     if evento.key == pygame.K_UP:
        #         rect_personaje.y -= 10
        #     if evento.key == pygame.K_DOWN:
        #         rect_personaje.y += 10
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                print(f"Ingreso completo {nombre_ingresado}")
            elif evento.key == pygame.K_BACKSPACE:
                nombre_ingresado = nombre_ingresado[0:-1]
            else:
                nombre_ingresado += evento.unicode
            nombre_usuario = fuente.render(nombre_ingresado, True, "mediumaquamarine")

    pantalla.fill((0, 0, 0))
    mi_boton_verde = pygame.draw.rect(pantalla, (0, 255, 0), (50, 50, 150, 75))
    pantalla.blit(imagen_personaje, rect_personaje)
    pantalla.blit(imagen_roca, rect_roca)
    pantalla.blit(mi_texto, (700, 50))
    pantalla.blit(nombre_usuario, (700, 140))
    pygame.display.flip()

pygame.quit()