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
                jump Un_walicho_de_La_Salamanca

    label La_luz_mala:
        "La luz está un rato más danzando en el borde del talar."

        "Hasta que da un salto, como expandiendose, se vuelve roja y entra rápidamente en el bosque como una flecha."

        menu:
            "Decidís entrar al talar a ver que pasa ahí adentro":
                jump En_lo_oscuro_del_bosque
            "Das la vuelta y dejás atrás a esa extraña luz":
                jump Un_camino_de_alimanas

    label El_canto_de_la_luz:
        "En cuanto empezás a tocar la guitarra la luz reacciona y escuchás como empieza a hacer un ruido como a un bombo flojo."

        "Entonces la luz encara hacia donde vos estás y a medida que se acerca vas notando que su ''canto'' se va mimetizando con el tuyo"
        
        "Podés distinguir como inmita las notas y el ritmo de tu guitarra."

        "Se acerca un poco más y su canto que había empezado a ser armonioso se va convirtiendo poco a poco en un sonido más áspero y chillón, y su luz se vuelve más oscura."

        menu:
            "Seguís tocando":
                jump Su_propia_melodia
            "Dejás de tocar":
                jump Escapa_al_bosque

    label Las_huestes_llegaron:
        "Cuando al fin llegás ves como las alimañas, El Mandinga, incluso el chivo negro están destrozando el pueblo y matándolos a todos."

        if Vida_china:
            "Incluso a El Tarta, a La China, a todos. De la manera más sangrienta, de maneras que nunca imaginaste que podía matarse a una persona."
        else:
            "Incluso a El Tarta, su cuerpo yace inherte frente a la pulpería, masacraron a todos. De la manera más sangrienta, de maneras que nunca imaginaste que podía matarse a una persona."
        
        "Pero, lejos de sentirte triste, te empezás a reir desaforadamente viendo toda la escena."
        
        "Agarrás tu guitarra y empezás a cantar avanzando entre los cadaveres, las calles con charcos de sangre y las casas incencidadas."

        "Hacés bailar a las huestes del mandinga con tu canto"
        
        jump Sucumbis_a_la_locura

    label Un_walicho_de_La_Salamanca:
        "Una caravana de alacranes, vívoras y murciélagos recorren las calles de tu pueblo, vos pasas a su lado como si nada, sos una más de las alimañas."

        "Llegás al centro, a la plaza principal y hay un grupo de brujas de La Salamanca haciendo un gualicho."

        "Te acercás, te reciben cordialmente y te explican cómo funciona tu pacto con El Mandinga."

        "Te dicen que cada vez que hechizás a una persona con tu canto, estás pagando parte de la deuda que tenés con El Mandinga."

        "Si no hechizás personas con tu canto a donde vayas, El Mandinga mandará a alguien más a que lo haga."

        "Si dejás de encantar personas vas a estar cada vez más cerca de que él venga a cobrarte el alma, esa deuda firmada con sangre que contrajiste."

        jump El_camino_del_condenado


    label El_camino_del_condenado:
        "Ahora tu pueblo está engualichado, ves un poco a tu alrededor y no tiene sentido ni siquiera ir a ver si los que conocés están bien."

        "Agarrás fuerte tu guitarra, te subís al caballo y empezás a cabalgar hacia otro destino en la pampa, a otra pulpería en la que encantar a todos con tu canto."

        "Y así seguís tu vida, preso de esa deuda que te perseguirá por siempre"
        
        jump El_viaje_eterno