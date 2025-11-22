define p = Character(" ", color="#880000")
define Mandinga = Character("Mandinga", color="#880000")
define china = Character("China", color="#880000")
#default reputacion_con_el_mandinga = 100
define config.default_text_cps = 80
define burn_transition = Fade(0.6, 0.4, 0.8, color="#000000")  # naranja tipo fuego




#image logo = "images/y.png"

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

    play viento "audio/viento.mp3" loop
    play estatica "audio/ruidoRosa.mp3" loop
    #$ renpy.music.set_audio_filter("viento", lowpass_filtro_viento, replace=True)



    #play acufeno "audio/acufeno.mp3"
    
    ######pruebas
    #show logo at left
    #"El logo está a la izquierda."

    #show logo at Move((0.0, 0.5), (1.0, 0.5), 10.0)
    #"Ahora el logo se mueve de izquierda a derecha en 2 segundos."
    #############
    #jump capitulo1
    menu:
        "ir a cap 1":
            jump capitulo1
        "Dar_un_paso_hacia_la_oscuridad":
            jump Dar_un_paso_hacia_la_oscuridad
        "ir a cap 2":
            jump capitulo2
        "ir a cap 3":
            jump capitulo3
        #"ejemplos de texto con efectos":
        #    jump ejemplosTexto
        #"ir a ejemplo clickeable":
        #    jump ejemplosClickeables
        #"ir a firmar":
        #    jump Escupir_el_crucifijo
        #"continuará...":
        #    jump continuará
        #"munú sonoro":
        #    jump menuSonoro




