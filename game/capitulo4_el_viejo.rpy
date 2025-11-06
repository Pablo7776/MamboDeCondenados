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
        "Ahora tu pueblo está engualichado, ves un poco a tu alrededor y no tiene sentido ni siquiera ir a ver si los que conocés están bien. La gente empieza a salir como perdida a caminar sin sentido por los caminos."

        "Agarrás fuerte tu guitarra, te subís al caballo y empezás a cabalgar hacia otro destino en la pampa, a otra pulpería en la que encantar a todos con tu canto."

        "Y así seguís tu vida, preso de esa deuda que te perseguirá por siempre"
        
        jump El_viaje_eterno

    label En_lo_oscuro_del_bosque:
        $ reputacion_con_el_mandinga -=15

        "Empezás a caminar y en un momento se escucha un zumbido muy fuerte, como si miles de mangangás hubieran entrado al talar de repente."

        "Termina el zumbido que te hizo taparte los oidos y estalla una luz roja desde el centro del bosque que ilumina todo el cielo."

        "La luz se apaga rápidamente, ves como delante algo brilla naranja de manera intermitente."

        menu:
            "Das la vuelta y volvés al pueblo":
                jump Un_camino_de_alimanas
            "Salís corriendo hacia el centro del bosque para ver que está pasando":
                jump Un_claro_despejado

    label Escapa_al_bosque:
        "En cuanto dejás de tocar la luz deja de emitir sonido y se frena en seco."

        "Vuelve flotando rápidamente hasta el borde del bosque, vuelve a ''cantar'' lo que tocaste mientras su color se va tornando en un rojo oscuro."
        
        "De repente entra en el bosque muy rápidamente y desapareciendo entre las ramas."

        menu:
            "Das la vuelta y volvés al pueblo":
                jump Un_camino_de_alimanas
            "Decidís entrar al talar a ver que pasa ahí adentro":
                jump En_lo_oscuro_del_bosque
    
    label Un_claro_despejado:
        $ Reputacion_mandinga -=15

        "Llegás a un claro en el medio del talar y no hay nada excepto unas luciernagas que brillan con una fuerte luz naranja, nada más."

        "Si hubo algo en algún momento ya no está y no dejó ningún rastro."

        "No entendés bien que pasó pero das la vuelta y volvés al pueblo."
        
        jump Un_camino_de_alimanas

    label Su_propia_melodia:
        $ Reputacion_mandinga -= 15

        "Seguís tocando, sobre tu música la luz empieza a chillar unas notas muy agudas que suenan por encima de lo que vos estás tocando."

        "Escuchás esas notas con total claridad, se vuelve roja y su melodía resuena en el campo."

        ##play melo1 loop fadein 0.5

        "Entonces cuando está a un metro tuyo se desvanece suavemente, metiendose en la tierra en forma de hilos de luz roja."

        menu:
            "Todo esto te parece muy extraño y decidís dar la vuelta y volver a tu pueblo.":
                jump Un_camino_de_alimanas
            "Sin poder sacarte esa última melodía de la cabeza te metés en el talar a buscar el rancho del viejo y averiguar qué le pasó.":
                jump El_rancho_del_viejo

    label El_rancho_del_viejo:
        "Caminás por el talar hasta encontrarte con el destartalado rancho del viejo."

        "Entrás facilmente porque la puerta está destrozada."

        "El rancho queda justo en un claro del bosque, a pesar de ser de noche la luz de la luna entra por la puerta y las pocas ventanas y te deja ver en su interior."

        "Lo primero que te llama la atención es un cuaderno muy extraño, forrado con cueros y pieles de distintos animales."

        "Lo abrís y a pesar de que está en un idioma que no conocés, de alguna manera, podés entenderlo."
        
        "Son canciones, o más bien una sola canción, instrucciones de cómo hay que tocarla, los acordes que se tienen que hacer y la letra del cántico."
        
        "Cuando te das cuenta ya la estás interpretando"
        
        jump La_cancion_del_viejo

    label La_cancion_del_viejo:
        "Vas pasando las hojas y seguís tocando, tu cántico al igual que lo que estás leyendo están en un idioma totalmente desconocido para vos, pero podés reproducirlo a la perfección."

        "Acorde tras acorde y página tras página la canción va resonando en todo el oscuro rancho."

        "Hasta que las anotaciones terminan abruptamente."

        "¿cómo sigue esta canción te preguntas e intentas buscar la respuesta en tu mente?"

        ##Acá en cada opción se debería reproducir una melodía al pasar el mouse por arriba

        menu:
            "Tocás esta melodía": ##Una melodía que sonó cuando hechizó a la familia de La China.
                jump Un_profundo_silencio
            "Tocás esta melodía": ##La melodía que "toco" la luz
                jump Los_animales_del_bosque
            "Tocás esta melodía": ##Parte de la canción del menú
                jump Un_profundo_silencio
    
    