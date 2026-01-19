transform vibrar:
    linear 0.05 xoffset 4 yoffset -4
    linear 0.05 xoffset -4 yoffset 4
    linear 0.05 xoffset 2 yoffset -4
    linear 0.05 xoffset -2 yoffset 2
    repeat

transform aparecer_flash:
    alpha 0.5
    linear 0.5 alpha 1.0
    linear 0.5 alpha 1.0
    repeat

transform flash:
    alpha 0.0
    linear 0.15 alpha 1.0
    linear 0.15 alpha 0.8
    alpha 0.0
    linear 0.15 alpha 1.0
    linear 0.15 alpha 0.8
    alpha 0.0
    linear 0.15 alpha 1.0
    linear 0.15 alpha 0.8
    alpha 0.0
    linear 0.15 alpha 1.0
    linear 0.15 alpha 0.8


transform desvanecer:
    linear 25.0 alpha 0.0   



transform subir_centrada:
    xalign 0.5      # centra horizontalmente
    yalign 0.1      # mueve hacia arriba (0.0 es arriba, 1.0 es abajo)
    linear 1.0 alpha 1.0  # opcional, para un fade-in suave

transform mostrar_izquierda:
    xoffset 0    
    yoffset 36      

transform mostrar_derecha:
    xoffset 1636
    yoffset 36


define black_transition = Fade(0.6, 0.4, 0.8, color="#000000")  # 