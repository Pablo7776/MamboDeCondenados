#default nombre_jugador = "Protagonista"
default pregunta_colo = False
default pregunta_pibe = False
default pregunta_viejo = False
default presentacion_colorada = False

label capitulo3:
    $ mostrar_repu()
    #hide higuera with Dissolve(6.0)
    play fx sfx_pajaritos fadein 1.0
    show naturaleza at subir_centrada with Dissolve(6.0)
    stop music fadeout 2.0
    play sound sfx_galope fadein 1.5
    #play fx sfx_pajaritos fadein 1.0
    
    ##Caballo check y pájaros## AUDIO

    "Llegás a tu pueblo por la tarde, ya podés ver la pulpería de El Tarta."

    "De acá saliste la última vez camino a La Salamanca."

    hide naturaleza
    show pueblo at subir_centrada with Dissolve(1.0)

    "El Viejo, que siempre está tomando algo en este lugar, te dio todas las indicaciones de cómo superar esas primeras pruebas en La Salamanca."
    
    "Atás tu caballo afuera en el grueso aro de hierro incrustado en el suelo de la ochava."
    stop fx
    stop sound

    jump La_pulperia


    label La_pulperia:
        
        hide pueblo
        ##Frenar caballo y pájaros## AUDIO

        show pulperia at subir_centrada with Dissolve(1.0)
        play sound sfx_taberna loop fadein 1.0

        ##Ruido ambiente de gente check## AUDIO
        ##Melodia guitarra pibe## AUDIO
        play music melo_pibe loop fadein 1.0


        "Al entrar te sorprende el sonido de la guitarra."
        
        "A un costado, en el rincón que siempre ocupás vos cuando tocás para todos, hay un chico joven tocando y cantando."

        "Además ves a una mujer mayor, colorada, que desencaja completamente en la húmeda pulpería de tu pueblo."
        
        "Ella está muy bien arreglada, tiene unos marcados rulos rojos y lleva un collar de perlas, aplaude con entusiasmo cada verso del joven guitarrista."
        
        "El Tarta sirve vino a cuatro manos."
        
        "De aquel Viejo, que te explicó todo sobre el Mandinga y el pacto, ni rastros."

        menu:
                "Ir a la barra, a hablar con El Tarta.":
                    hide pulperia
                    jump El_Tarta
                "Acercarse al joven guitarrista.":
                    hide pulperia
                    jump Lo_harias_mejor


    label El_Tarta:
        show barraPulperia at subir_centrada with Dissolve(1.0)
        

        "Te acercás a la barra y te hacés un hueco entre los muchachos que le piden más de un vaso cada uno al Tarta."

        "El Tarta te hace una seña con la cabeza como preguntando “¿qué querés?”."

        "Pedís un vino y se acerca para dártelo."
        show tarta_placeholder:
            xoffset 0
            yoffset 36

        Tarta "—[nombre_jugador], tanto tiempo."
        
        hide tarta_placeholder

        "Le respondés el saludo y se queda ahí un rato, esperando que continúes la conversación."

        menu:
            "Preguntarle al Tarta “¿Ese quién es?”":
                jump El_Pibe
            "Preguntarle al Tarta por la señora colorada":
                jump La_del_whisky_caro
            "Preguntarle al Tarta por El Viejo":
                jump Malas_noticias

    label Malas_noticias:
        $ pregunta_viejo = True

        show tarta_placeholder:
            xoffset 0
            yoffset 36
        
        Tarta "El viejo falleció, lo encontramos sin vida en la calle, a unas cuadras."

        Tarta "Le hicimos el velorio y no fue nadie. No sabemos qué carajos le pasó."
        
        Tarta "Apareció muerto de un día para el otro. Vivía en el talar, en el camino donde viven los López, pero más allá."

        hide tarta_placeholder

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
                    jump capitulo4_el_viejo

    label El_Pibe:
        $ pregunta_pibe = True
        show tarta_placeholder:
            xoffset 0
            yoffset 36
        Tarta "¿Ese? Llegó hace dos días; es el Pibe Farías, ¿te acordás de él?, el hijo de la Flavia."

        Tarta "Parece que vino a llevarse a la madre a la ciudad, porque está enferma. ¿Es bueno no?"

        hide tarta_placeholder

        show protagonista_placeholder:
            xoffset 1636
            yoffset 36
        # 
        # redefinir el personaje p con el nombre elegido
        $ p = Character(nombre_jugador)
        #

        p "Ciertamente el Pibe Farías no toca mal, pero tiene las manías de los chicos de ciudad."
        
        p "Pensás: obviamente, ahora no hay nadie que se compare conmigo."
        
        hide protagonista_placeholder

        menu:
            "Acercarse a la colorada Dowley" if pregunta_colo:
                    jump La_señora_Dowley
            "Preguntarle al Tarta por la señora colorada" if not pregunta_colo:
                    jump La_del_whisky_caro
            "Ir al rancho de El Viejo a investigar." if pregunta_viejo:
                    jump continuara
                    #jump capitulo4_el_viejo
            "Preguntarle al Tarta por El Viejo" if not pregunta_viejo:
                    jump Malas_noticias
            "Acercarse al Pibe Farías y pedirle que pare, para tocar vos":
                jump Lo_harias_mejor
    
    label La_del_whisky_caro:
        $ pregunta_colo = True

        show tarta_placeholder:
            xoffset 0
            yoffset 36

        Tarta "Es la señora Dowley, parece que es de la capital."
        Tarta "Llegó ayer y me preguntó por “artistas locales”, al día siguiente apareció el Farías."
        Tarta "Parece encantada con él."
        Tarta "Ayer y hoy me pidió el mejor whisky que tuviese."

        hide tarta_placeholder

        menu:
            "Acercarse al Pibe Farías y pedirle que pare, para tocar vos" if pregunta_pibe:
                    jump Lo_harias_mejor
            "Preguntarle al Tarta “¿Ese quién es?”" if not pregunta_pibe:
                    jump El_Pibe
            "Ir al rancho de El Viejo a investigar." if pregunta_viejo:
                    jump continuara
                    #jump capitulo4_el_viejo
            "Preguntarle al Tarta por El Viejo" if not pregunta_viejo:
                    jump Malas_noticias
            "Acercarse a la Colorada Dowley":
                jump La_señora_Dowley

    label La_señora_Dowley:
        hide barraPulperia
        show pibeYColorada at subir_centrada with Dissolve(1.0)

        "Te acercás a la mesa de la Colorada Dowley."

        "Te parás frente a una de las sillas y la señora te invita a sentarte cuando ve que llevás una guitarra."

        hide pibeYColorada
        show mesa at subir_centrada with Dissolve(1.0)
        
        show colorada_placeholder:
            xoffset 0
            yoffset 36

        colorada "¡Buenas tardes, señor!"

        hide colorada_placeholder

        "Dice ella con una voz grave, pero melodiosa y continúa:"
        
        show colorada_placeholder:
            xoffset 0
            yoffset 36

        colorada "Muy buena voz la de aquel joven, El Farías, ¿no?"

        hide colorada_placeholder

        menu:
            "Respondés: Yo lo haría mucho mejor.":
                jump La_colorada_curiosa
            "Respondés: No lo hace mal, pero seguro usté escuchó mejores músicos alguna vez. En la ciudad seguro que hay muchos buenos guitarristas y cantores.":
                jump Admitiendo_la_torpeza_del_Farias

    label Admitiendo_la_torpeza_del_Farias:
        "La señora se acomoda el peinado y se queda mirándote unos segundos."

        show colorada_placeholder:
            xoffset 0
            yoffset 36

        colorada "Bueno, es verdad que por el estudio de grabación, pasaron muchos músicos y algunos eran muy buenos, mucho mejores que aquel joven."

        hide colorada_placeholder

        menu:
            "¿Por el estudio de grabación? (preguntás extrañado)":
                jump Colony_Records

    label Colony_Records:
        $ presentacion_colorada = True

        show colorada_placeholder:
            xoffset 0
            yoffset 36

        colorada "Me presento correctamente: soy Diana Dowley."

        colorada "Vine a buscar talentos al interior."
        
        colorada "Represento a la discográfica Colony Records."

        colorada "Supongo que no la conocés, se instaló hace poco en el país pero afuera es muy conocida."
        
        colorada "Veo que llevás tu guitarra. ¿Creés poder hacerlo mejor que el joven Farías?"
        
        hide colorada_placeholder

        hide mesa

        menu:
            "Obviamente, ya va a ver": ### ### el fondo negro acá es intecional????
                jump Lo_harias_mejor
    
    label Lo_harias_mejor:
        hide barraPulperia
        show pibeYColorada at subir_centrada with Dissolve(1.0)

        "Te acercás al rincón en que el pibe está tocando."

        "Él te saluda con la cabeza."

        "Le mostrás tu guitarra, como para que te dé paso."

        "Te hace una seña de que esperes un minuto, que él va a tocar una canción más."

        menu:
            "Esperás a que termine su canción":
                jump El_Pibe_Farías
            "Ni bien él empieza a tocar vos empezás a tocar sobre su canción":
                jump El_pibe_deja_de_tocar

    label El_Pibe_Farías:
        $ reputacion_con_el_mandinga -= 20
        $ mostrar_repu()

        "Esperás a que él termine, y te saluda presentándose como Farías, el Pibe Farías."
        
        ##Frenar Melodia guitarra pibe## AUDIO
        stop music fadeout 1.0

        "Te cede su lugar y se va a sentar junto a la Colorada."

        jump Hechizando_a_toda_la_pulpería

    label El_pibe_deja_de_tocar:
        stop music fadeout 2.0
        ##Frenar Melodia guitarra pibe## AUDIO

        $ reputacion_con_el_mandinga += 5
        $ mostrar_repu()

        ##Melodía pibe 2## AUDIO  #### SE PEUDE USAR LA CHACARERA
        "El pibe empieza a tocar y enseguida copiás sus acordes."
        
        ##Melodía pibe 2 duplicada## AUDIO QUE ACÄ EMPIECE OTRA VEZ LA CHACARERA EN OTRO CANAL

        "Después del cuarto acorde, él deja de tocar; su cara se transforma: ahora está muy triste."
        ##Frenar Melodía pibe 2## AUDIO FRENA LA PRIMER CHACARERA
        "Se va cabizbajo a la mesa de la colorada."
        ##Frenar Melodía pibe 2 duplicada## AUDIO FRENA LA SEGUNDA CHACARERA
        jump Hechizando_a_toda_la_pulpería

    label La_colorada_curiosa:
        ### Hay que meter todo lo que se usa pa que sea un diálogo de la colorada
        
        show colorada_placeholder:
            xoffset 0
            yoffset 36

        colorada "¿Entonces creés que podés hacerlo mejor que él?"
        
        hide colorada_placeholder

        "Te lo dice casi desafiante; entonces le hace una seña al Farías."

        stop music 
        ##Frenar Melodia guitarra pibe## AUDIO

        "El pibe viene rápidamente a la mesa."

        "Se sienta y la colorada te habla de nuevo a vos."

        ### Hay que meter todo lo que se usa pa que sea un diálogo de la colorada
        "—Es su turno, don... ¿Cuál es su nombre?"

        menu:
            "[nombre_jugador] me llamo —respondés—, y vas al rincón de los cantores y payadores":
                jump Hechizando_a_toda_la_pulpería

    label Hechizando_a_toda_la_pulpería:
        $ reputacion_con_el_mandinga += 20
        $ mostrar_repu()
        hide pibeYColorada
        hide mesa
        show pulperia at subir_centrada with Dissolve(1.0)
        ##Melodia prota1## AUDIO
        "Con el primer rasgueo de tu guitarra todas las miradas se clavan en vos."

        stop sfx_taberna fadeout 2.0
        ##Frenar (fade out) Ruido ambiente de gente## AUDIO
        "Luego de la primera estrofa, ya todos están mirándote embelesados."

        "Todos, menos la Colorada Dowley, que te mira con curiosidad."
        
        "Luego de la segunda vuelta, ella le dice algo al Pibe Farías."
        ##Frenar (fade out) Melodia prota1## AUDIO
        ##Melodia prota2## AUDIO

        "Él cambia repentinamente su expresión, sale de la pulpería casi arrastrando su guitarra con una cara de pánico y terror."
        
        "Terminás de tocar y se produce una ovación inmensa."
        ##Frenar (fade out) Melodia prota2## 
        play sound sfx_aplausos fadein 0.5
        
        ##Ovación## AUDIO
        hide pulperia
        show pulperiaAplaudiendo at subir_centrada with Dissolve(1.0)
        
        "Te levantás y te acercás nuevamente a la mesa de la colorada y van tocándote la espalda, los hombros y felicitándote."
        
        ##Ruido ambiente de gente## AUDIO
        play sound sfx_taberna  fadein 1.0


        if Vida_china:
            "Tu china que se había quedado tomando algo en la barra se acerca, interrumpe tu paso y te llena de besos."
            ### Hay que meter todo lo que se usa pa que sea un diálogo de la china ###
            China "¿Ya podemos ir a tu casa?"

        menu:
            "Hacerle caso a tu china e ir a tu casa con ella." if Vida_china:
                jump La_calle_fría
            "Te vas a tu casa satisfecho" if not Vida_china:
                jump Una_noche_fría
            "Vas decidido a la mesa de la Colorada":
                jump Colony_Records_y_otro_contrato

    label Colony_Records_y_otro_contrato:
        $ reputacion_con_el_mandinga += 5
        $ mostrar_repu()
        if not presentacion_colorada:
            $ presentacion_colorada = True
        
        hide pulperiaAplaudiendo
        show mesa at subir_centrada with Dissolve(1.0)
        
        ### Hay que meter todo lo que se usa pa que sea un diálogo de la colorada ###
        "—Me presento correctamente, soy Diana Dowley."

        "—Vine a buscar talentos al interior."

        "—Represento a la discográfica Colony Records."

        "—Supongo que no la conocés; se instaló hace poco en el país, pero afuera es muy conocida."

        "—Me parece que tenés mucho potencial para ser parte de nuestros artistas."

        "—Podrías conseguir mucho dinero, mucha fama y mucho más. Te llevaríamos por todo el país. Incluso puede que hasta al extranjero."

        "—Te propongo algo: nos podemos encontrar mañana por la mañana, me estoy quedando en una estancia a unos kilómetros."

        "—Paso por vos a la mañana; si no salís, supondré que no querés ser parte de esta gran aventura que te propongo."
        
        "—Obviamente, tendrías que mudarte, al menos un tiempo, a la capital. Yo puedo organizar sin problemas esa mudanza."

        menu:
            "Ya estás seguro de que no querés aceptar este trato" if Vida_china:
                jump La_calle_fría
            "Ya estás seguro de que no querés aceptar este trato" if not Vida_china:
                jump Una_noche_fría
            "Lo vas a pensar, pero estás casi seguro de que sí, que te vas a sumar a la discográfica":
                jump continuara
                #jump Capítulo_4_Colony_Records
    
    label Una_noche_fría:
        
        $ reputacion_con_el_mandinga -= 10
        $ mostrar_repu()

        stop sfx_taberna fadeout 1.0
        ##Frenar Ruido ambiente de gente## AUDIO
        play sound sfx_noche fadein 0.5
        ##Pájaros, naturaleza## AUDIO

        "Salís de la pulpería agradecido de tu nuevo don."

        hide pulperiaAplaudiendo
        hide mesa
        show pueblo at subir_centrada with Dissolve(1.0)

        "Vas zigzagueando por culpa del alcohol por las calles de tierra hacia tu casa."

        "Cuando estás a unas cuadras de tu casa..."

        hide pueblo
        play sound sfx_SonidoAmbienteTerror loop fadein 1.0

        ##Frenar Pájaros, naturaleza## AUDIO
        show pibeColgado at subir_centrada with Dissolve(1.0)
        ##Sonido tenso, violines## AUDIO
        stop sfx_noche
        ##Ruidos tétricos naturaleza## AUDIO
        
        "... ves al pibe Farías, cuelga con una soga al cuello de una rama gruesa de un viejo caldén."

        "¿Habrá sido por lo que le dijo la Colorada?, te preguntás, recordando la situación de la pulpería."

        menu:
            "Ya alguien se hará cargo de ese pobre desgraciado, vos a lo tuyo, te vas para tu casa":
                jump Un_paso_atrás
            "Investigás qué pasó con el pibe":
                hide pibeColgado
                jump continuara
                #jump Capítulo_4_El_pobre_Pibe_Farías

    label Un_paso_atrás:
        hide pibeColgado
        show casaProtagonista at subir_centrada with Dissolve(1.0)
        stop sfx_SonidoAmbienteTerror
        ##Frenar Sonido tenso, violines## AUDIO
        ##Frenar Ruidos tétricos naturaleza## AUDIO


        "Llegás a tu casa y sentís un profundo pesar en el pecho."

        ##Melodia prota1 (bajita)## AUDIO
        "Tocás la guitarra para tranquilizarte después de lo que viste."

        "Pero cuando lo pensás, creés que tiene que haber algo más."
        ##Frenar Melodia prota1 (bajita)## AUDIO
        menu:
            "Volvés a la pulpería":
                jump La_joda_terminó
            "Volvés a ver qué pasó con el pibe":
                hide casaProtagonista
                jump continuara
                #jump Capítulo_4_El_pobre_Pibe_Farías

    label La_calle_fría:
        $ reputacion_con_el_mandinga -= 10
        $ mostrar_repu()
        
        "Salís de la pulpería con tu china, van zigzagueando por las calles, hace frío."

        hide mesa
        hide pulperiaAplaudiendo
        
        stop sfx_taberna fadeout 1.0
        ##Frenar Ruido ambiente de gente## AUDIO
        play sound sfx_noche fadein 0.5
        ##Pájaros, naturaleza## AUDIO
        
        show pueblo at subir_centrada with Dissolve(1.0)

        "Se abrazan para no tener frío, para sentir el calor del otro y para no caerse."

        "Cuando están a unas cuadras de tu casa..."

        hide pueblo
        play music sfx_SonidoAmbienteTerror loop fadein 1.0
        ##Frenar Pájaros, naturaleza## AUDIO
        show pibeColgado at subir_centrada with Dissolve(1.0)
        ##Sonido tenso, violines## AUDIO
        stop sfx_noche
        ##Ruidos tétricos naturaleza## AUDIO

        "... ves al pibe Farías, cuelga con una soga al cuello de una rama gruesa de un viejo caldén."

        ##Grito ahogado (sin loop)##AUDIO
        "La china pega un grito de espanto y te das vuelta a consolarla. Van despacio, ella aún llorando por la terrible imagen, hasta que llegan a tu casa."

        "¿Habrá sido lo que le dijo la colorada? te preguntás recordando la situación de la pulpería."

        menu:
            "Ya alguien se hará cargo de ese pobre desgraciado, vos a lo tuyo, te quedás en tu casa con tu china":
                jump La_noche_en_tu_casa
            "Llevás a la china a tu casa y volvés a ver qué pasó con el pibe":
                jump continuara
                #jump Capítulo_4_El_pobre_Pibe_Farías

    label La_noche_en_tu_casa:
        hide pibeColgado
        show casaProtagonista at subir_centrada with Dissolve(1.0)
        stop music
        ##Frenar Sonido tenso, violines## AUDIO
        ##Frenar Ruidos tétricos naturaleza## AUDIO

        "Llegan a tu casa y la china se deshace en llanto sobre tu pecho ni bien entran."
        
        "La consolás y le decís que no se preocupe, que el pibe debería tener sus motivos, no era tema suyo ni tuyo."
        ##Melodia prota1 (bajita)## AUDIO
        "Tocás la guitarra para tranquilizarla."

        "Pero igual, cuando lo pensás, creés que tiene que haber algo más."
        ##Frenar Melodia prota1 (bajita)## AUDIO
        menu:
            "Volvés a la pulpería":
                jump La_joda_terminó
            "Volvés a ver qué pasó con el pibe":
                hide casaProtagonista
                jump continuara
                #jump Capítulo_4_El_pobre_Pibe_Farías

    label La_joda_terminó:
        hide casaProtagonista
        show pulperia at subir_centrada with Dissolve(1.0)

        play sound sfx_taberna loop fadein 1.0
        
        ##Ruido ambiente de gente## AUDIO
        
        "La colorada Dowley ya no está."

        "Los borrachos aún están en la pulpería y algunos están cantando a coro una vieja vidala."

        if not pregunta_viejo:
            
            "El Tarta te ve entrar y ni bien llegás a la barra, te cuenta sobre el Viejo."
            show tarta_placeholder:
                xoffset 0
                yoffset 36

            "—El viejo falleció, lo encontramos sin vida en la calle, a unas cuadras."

            "—Le hicimos el velorio y no fue nadie. No sabemos qué carajos le pasó."

            "—Apareció muerto de un día para el otro. Vivía en el talar, en el camino donde viven los López, pero más allá."

            hide tarta_placeholder
        
        "Preguntás un poco por ahí, pero nadie vio salir a la Colorada ni nadie te comenta nada del Pibe Farías."

        "Con cada persona que hablás, y que te escuchó tocar, te alaba nuevamente, de una manera muy lisonjera."

        ##Frenar ruido ambiente de gente## AUDIO
        stop sfx_taberna fadeout 1.0

        menu:
            "Ir a ver el cadaver del Farías":
                hide pulperia
                jump continuara
                #jump Capítulo_4_El_pobre_Pibe_Farías
            "Ir al rancho del viejo":
                jump continuara
                #jump capitulo4_el_viejo