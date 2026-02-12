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

#### Para poner dípticos horizontales con una imagen arriba y otra abajo###
transform hdiptico_superior: 
    xalign 0.5
    yalign 0.14

transform hdiptico_inferior: 
    xalign 0.5
    yalign 0.44

#### Para poner dípticos verticales, una imagen a la izquierda y otra a la derecha###
transform vdiptico_izquierda: 
    xalign 0.34
    yalign 0.1

transform vdiptico_derecha: 
    xalign 0.66
    yalign 0.1

### Para poner tripticos verticales###
transform vtriptico_izquierda: 
    xalign 0.28
    yalign 0.1

transform vtriptico_centro: 
    xalign 0.5
    yalign 0.1

transform vtriptico_derecha: 
    xalign 0.72
    yalign 0.1
