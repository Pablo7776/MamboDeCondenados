define p = Character("Protagonista")
define Mandinga = Character("Mandinga", color="#FF0000")
image logo = "images/y.png"

label start:
    stop music fadeout 1.0
    scene fondo
    with fade


    
    ######pruebas
    #show logo at left
    #"El logo está a la izquierda."

    #show logo at Move((0.0, 0.5), (1.0, 0.5), 10.0)
    #"Ahora el logo se mueve de izquierda a derecha en 2 segundos."
    #############

    menu:
        "ir a cap 1":
            jump capitulo1
        "ejemplos de texto con efectos":
            jump ejemplosTexto
        "ir a ejemplo clickeable":
            jump ejemplosClickeables

