#################  personajes ##############################
############################################################

define p = Character(" ", color="#D4AF37")
define Mandinga = Character("Mandinga", color="#D4AF37")
define china = Character("China", color="#D4AF37")
define colorada = Character("Colorada", color="#D4AF37")
define Tarta = Character("Tarta", color="#D4AF37")

############################################################


default reputacion_con_el_mandinga = 100



label start:
    # Cargar la reputación persistente o usar 100 si no existe
    # Si existe el valor persistente, cargarlo, sino usar 100
    if persistent.reputacion_con_el_mandinga is not None:
        $ reputacion_con_el_mandinga = persistent.reputacion_con_el_mandinga
    else:
        $ reputacion_con_el_mandinga = 100

    
    stop music fadeout 1.0

    play viento "audio/viento.mp3" loop
    play estatica "audio/ruidoRosa.mp3" loop



    ##########################################################
    
    #jump capitulo1
    
    #menu:
        
        #"ir a cap 1":
        #    jump capitulo1
        #"Dar_un_paso_hacia_la_oscuridad":
        #    jump Dar_un_paso_hacia_la_oscuridad
        #"ir a cap 2":
        #    jump capitulo2
        #"ir a cap 3":
        #    jump capitulo3
        #"ir a Capítulo_4_El_pobre_Pibe_Farías":
        #    jump Capítulo_4_El_pobre_Pibe_Farías
        #"ir a capitulo4_el_viejo":
        #    jump capitulo4_el_viejo
        #"ir a Capítulo_4_Colony_Records":
        #    jump Capítulo_4_Colony_Records
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

    jump capitulo1




