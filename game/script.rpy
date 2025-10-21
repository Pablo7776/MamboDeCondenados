define p = Character("Protagonista")
define Mandinga = Character("Mandinga", color="#FF0000")
#default reputacion_con_el_mandinga = 100
define config.default_text_cps = 20



image logo = "images/y.png"

label start:
    # Cargar la reputación persistente o usar 100 si no existe
    # Si existe el valor persistente, cargarlo, sino usar 100
    if persistent.reputacion_con_el_mandinga is not None:
        $ reputacion_con_el_mandinga = persistent.reputacion_con_el_mandinga
    else:
        $ reputacion_con_el_mandinga = 100

    if persistent.humanidad is not None:
        $ humanidad = persistent.humanidad
    else:
        $ humanidad = 100

    stop music fadeout 1.0
    scene fondo
    with fade
    "{cps=20}Texto apareciendo lentamente...{/cps}"

    
    ######pruebas
    #show logo at left
    #"El logo está a la izquierda."

    #show logo at Move((0.0, 0.5), (1.0, 0.5), 10.0)
    #"Ahora el logo se mueve de izquierda a derecha en 2 segundos."
    #############

    menu:
        "ir a cap 1":
            jump capitulo1
        "ir a cap 2":
            jump capitulo2
        "ejemplos de texto con efectos":
            jump ejemplosTexto
        "ir a ejemplo clickeable":
            jump ejemplosClickeables

