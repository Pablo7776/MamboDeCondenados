#default nombre_jugador = "Protagonista"


label capitulo3:
    
    "Llegás a tu pueblo por la tarde, ya podés ver la pulpería de El Tarta."

    "De acá saliste la última vez camino a La Salamanca."

    "El Viejo, que siempre está tomando algo en este lugar, te dió todas las indicaciones de cómo superar esas primeras pruebas en La Salamnca."
    
    "Atás tu caballo afuera en el grueso aro de hierro incrustado en el suelo de la ochava."

    jump La_pulperia   

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
