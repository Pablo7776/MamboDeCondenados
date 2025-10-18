default nombre_jugador = "Protagonista"


label capitulo2:
    "hola"

    jump Comenzar 

    label Comenzar:
        "[nombre_jugador], trepás nuevamente por el abismo en espiral por el que caiste."

        "Te encontrás cara a cara con el chivo negro, pero esta vez no te ataca. Se acerca lentamente y te lame los pies; con su saliva sana tus heridas."

        "Las alimañas te miran con respeto desde sus cuevas. Cuando llegás al laberinto, otra vez aparece el basilisco: te guía para salir. En la última curva te esperan tus botas, tu sombrero y tu pañuelo, que te los volvés a poner."

        "Das un paso afuera y la piedra que se había abierto antes ahora se cierra crujiendo suavemente. Escuchás un galope y ves llegar a tu caballo, con tu guitarra aún bien atada a su silla."

        "Te ponés la guitarra en la espalda y comenzás a cabalgar. Pasan las horas y ya se te está haciendo de noche. Ves a lo lejos una tranquera y, al fondo del campo, un pequeño rancho."

        "Un poco más adelante, una frondosa higuera bajo la que podrías refugiarte del rocío."

        menu:
                "Entrar al campo y golpear la puerta":
                    jump puerta_del_rancho
                "Pasar la noche bajo la higuera":
                    jump noche_ante_las_estrellas