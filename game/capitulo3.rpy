#default nombre_jugador = "Protagonista"


label capitulo3:
    
    "Llegás a tu pueblo por la tarde, ya podés ver la pulpería de El Tarta."

    "De acá saliste la última vez camino a La Salamanca."

    "El Viejo, que siempre está tomando algo en este lugar, te dió todas las indicaciones de cómo superar esas primeras pruebas en La Salamnca."
    
    "Atás tu caballo afuera en el grueso aro de hierro incrustado en el suelo de la ochava."

    jump La_pulperia

    $

    label La_pulperia:
        "Al entrar te sorprende el sonido de una guitarra."
        
        "A un costado, en el rincón que siempre ocupás vos cuando tocás para todos, hay un chico joven tocando y cantando."

        "Además ves a una mujer mayor, colorada, que desencaja completamente en la humeda pulpería de tu pueblo."
        
        "Ella está muy bien arreglada, tiene unos marcados rulos rojos y lleva un collar de perlas, aplaude con entusiasmo cada verso del joven guitarrista."
        
        "Del otro lado de la barra el Tarta sirviendo vino a cuatro manos."
        
        "De aquel Viejo ni rastros."

        menu:
                "Ir a la barra":
                    jump El_Tarta
                "Acercarse al joven guitarrista":
                    jump Lo_harias_mejor
    $ pregunta_colo = false
    $ pregunta_pibe = false
    $ pregunta_viejo = false

    label El_Tarta:
        "Te acercás a la barra y te hacés un hueco entre los muchachos que le piben más de un vaso cada uno al Tarta."

        "El Tarta te hace una seña con la cabeza como preguntando “¿qué querés?”."

        "Pedís un vino y cuando se acerca para dartelo te dice"

        "- [nombre_jugador], tanto tiempo."
        
        "Le respondés el saludo y se queda ahí un rato."

        menu:
            "Preguntarle al Tarta “¿Ese quién es?”":
                jump El_Pibe
            "Preguntarle al Tarta por la señora colorada":
                jump La_del_whisky_caro
            "Preguntarle al Tarta por El Viejo":
                jump Malas_noticias

    label Malas_noticias:
        $ pregunta_viejo = true
        
        "- El viejo falleció, lo encontramos sin vida en la calle, a unas cuadras."

        "- Le hicimos el velorio y no fue nadie. No sabemos que carajos le pasó."
        
        "- Apareció muerto de un día para el otro. Viviá en el talar por el lado de los Lopez."

        menu:
            (if:$pregunta_pibe is false)[[[Preguntarle al Tarta “¿Ese quién es?” | El Pibe]]](else:)[[[Acercarse al Pibe Farías y pedirle que pare, para tocar vos -> Vos lo harías mejor]]]
            (if:$pregunta_colo is false)[[[Preguntarle al Tarta por la señora colorada -> La señora del whisky caro]]] (else:)[[[Acercarse a la colorada Dowley -> La señora Dowley]]] 
            [[Ir al rancho de El Viejo a investigar.| ¿Qué pasó?]]