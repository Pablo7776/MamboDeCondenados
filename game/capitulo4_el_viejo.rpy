label Que_paso:
    $ reputacion_con_el_mandinga -= 25
    
    if Vida_china == True:
        "Llevás a la china a tu casa y le prometés que vas a volver."
        
        "Ella te besa con pasión e incluso parece que se le cae una lágrima cuando al fin te despedís."

    "Camino a la casa del viejo se hace cada vez más de noche."
    
    "El camino es largo, tenés que ir a campo traviesa, pero ya ves el límite del talar en el que está su rancho."

    "Estando a tiro de boleadora ves que hay una luz naranja, como una luz mala."

    "Una luz anaranjada que "danza" en el borde del talar."

    menu:
        "Das la vuelta y volvés al pueblo":
            jump Un_camino_de_alimanas
        "Te ocultás entre los pastos y esperas":
            jump La_luz_mala
        "Empezás a tocar la guitarra, seguro El Mandinga te proteje":
            jump El_canto_de_la_luz

    label Un_camino_de_alimanas:
        "Cuando estás volviendo en la oscura noche ves como el camino que entra a tu pueblo está alfombrado de alacranes."

        menu:
            "Corrés por el costado del camino para ver qué es lo que está pasando." if reputacion_con_el_mandinga < 60:
                jump Las_huestes_llegaron
            "Corrés por el costado del camino para ver qué es lo que está pasando." if reputacion_con_el_mandinga > 59:
                jump Un walicho de La Salamanca

    