#default nombre_jugador = "Protagonista"
default pregunta_colo = False
default pregunta_pibe = False
default pregunta_viejo = False

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
        $ pregunta_viejo = True
        
        "- El viejo falleció, lo encontramos sin vida en la calle, a unas cuadras."

        "- Le hicimos el velorio y no fue nadie. No sabemos que carajos le pasó."
        
        "- Apareció muerto de un día para el otro. Viviá en el talar por el lado de los Lopez."

        menu:
            "Acercarse al Pibe Farías y pedirle que pare, para tocar vos" if pregunta_pibe:
                    jump Lo_harias_mejor
            "Preguntarle al Tarta “¿Ese quién es?”" if not pregunta_pibe:
                    jump El_Pibe
            "Acercarse a la colorada Dowley" if pregunta_colo:
                    jump La_señora_Dowley
            "Preguntarle al Tarta por la señora colorada" if not pregunta_colo:
                    jump La_del_whisky_caro
            "Ir al rancho de El Viejo a investigar.":
                jump Que_paso

    label El_Pibe:
        $ pregunta_pibe = True
        "- ¿Ese? llegó hace dos días, es el Pibe Farías, ¿te acordás de él? el hijo de la Flavia."
        "- Parece que vino a llevarse a la madre a la ciudad, porque está enferma. ¿Es bueno no?"
        "“Ciertamente el Pibe Farías no toca mal, pero tiene las manías de los chicos de ciudad. Además obviamente ahora no hay nadie que se compare con vos” pensás."

        menu:
            "Acercarse a la colorada Dowley" if pregunta_colo:
                    jump La_señora_Dowley
            "Preguntarle al Tarta por la señora colorada" if not pregunta_colo:
                    jump La_del_whisky_caro
            "Ir al rancho de El Viejo a investigar." if pregunta_viejo:
                    jump Que_paso
            "Preguntarle al Tarta por El Viejo" if not pregunta_viejo:
                    jump Malas_noticias
            "Acercarse al Pibe Farías y pedirle que pare, para tocar vos":
                jump Lo_harias_mejor
    
    label La_del_whisky_caro:
        $ pregunta_colo = True

        "- Es la señora Dowley, parece que es de la capital."
        "- Llegó ayer y me preguntó por “artistas locales”, al día siguiente apareció el Farías."
        "- Parece encantada con él."
        "- Ayer y hoy me pidió el mejor whisky que tuviera."

        menu:
            "Acercarse al Pibe Farías y pedirle que pare, para tocar vos" if pregunta_pibe:
                    jump Lo_harias_mejor
            "Preguntarle al Tarta “¿Ese quién es?”" if not pregunta_pibe:
                    jump El_Pibe
            "Ir al rancho de El Viejo a investigar." if pregunta_viejo:
                    jump Que_paso
            "Preguntarle al Tarta por El Viejo" if not pregunta_viejo:
                    jump Malas_noticias
            "Acercarse a la colorada Dowley":
                jump La_señora_Dowley

    label La_señora_Dowley:
        "Te acercas a la mesa de la colorada Dowley."

        "Te parás frente a una de las sillas y la señora te invita a sentarte cuando ve que llevás una guitarra."
        
        "- ¡Buenas tardes señor!"

        "Dice ella con una voz agravada pero melodiosa y continúa:"
        
        "- Muy buena voz la de aquel joven, El Farías, ¿no?"

        menu:
            "Respondés: Yo lo haría mucho mejor":
                jump La_colorada_curiosa
            "Respondés: No lo hace mal, pero seguramente usté escuchó mejores alguna vez, en la ciudad seguro hay muchos buenos músicos.":
                jump Admitiendo_la_torpeza_del_Farias

    label Admitiendo_la_torpeza_del_Farias:
        "La señora se acomoda el peinado y se queda mirándote unos segundos."

        "- Bueno, es verdad que por el estudio, pasaron muchos músicos y algunos eran muy buenos, mucho mejores que aquel joven."

        menu:
            "¿Por el estudio? (preguntás extrañado)":
                jump Colony_Records

    label Colony_Records:
        $ presentacion_colorada = True

        "- Me presento correctamente, soy Diana Dowley."

        "- Vine a buscar talentos al interior."
        
        "- Represento a la discográfica Colony Records."

        "- Supongo que no la conocés, se instaló hace poco en el país pero afuera es muy conocida."
        
        "- Veo que llevas tu guitarra ¿creés poder hacerlo mejor que el joven Farias?"

        menu:
            "Obviamente, ya va a ver":
                jump Lo_harias_mejor
    
    label Lo_harias_mejor:
        "Te acercás al rincón en que el pibe está tocando."

        "Él te saluda con la cabeza."

        "Le mostrás tu guitarra como para que te de paso."

        "Te hace una seña de que esperes un minuto, que él va a tocar una canción más."

        menu:
            "Esperás a que termine su canción":
                jump El_Pibe_Farías
            "Ni bien él empieza a tocar vos empezás a tocar sobre su canción":
                jump El_pibe_deja_de_tocar

    label El_Pibe_Farías:
        $ reputacion_con_el_mandinga -= 15

        "Esperás a que él termine, y te saluda presentandose como Farías, el Pibe Farías."

        "Te sede su lugar y se va a sentar junto a la colorada."

        jump Hechizando_a_toda_la_pulpería

    label El_pibe_deja_de_tocar:
        $ reputacion_con_el_mandinga -= 5

        "El pibe empieza a tocar y enseguida copías sus acordes."

        "Después del cuarto acorde él deja de tocar, su cara se transforma ahora está muy triste."

        "Se va cabizbajo a la mesa de la colorada."

        jump Hechizando_a_toda_la_pulpería

    label La_colorada_curiosa:
        "- ¿Entonces creés que podés hacerlo mejor que él?"
        
        "Te dice ella casi desafiante, entonces le hace una seña al Farías."

        "El pibe corta abruptamente su interpretación y viene rápidamente a la mesa."

        "Se sienta y la colorada te habla de nuevo a vos."

        "- Es su turno don... (y hace una seña para que le digas tu nombre)."

        menu:
            "[nombre_jugador] me llamo, respondés y vas al rincón de los cantores y payadores":
                jump Hechizando_a_toda_la_pulpería