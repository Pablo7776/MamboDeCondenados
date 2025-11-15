#default nombre_jugador = "Protagonista"
default pregunta_colo = False
default pregunta_pibe = False
default pregunta_viejo = False
default presentacion_colorada = False

label capitulo3:
    $ mostrar_repu()

    show naturaleza at subir_centrada with Dissolve(1.0)

    "Llegás a tu pueblo por la tarde, ya podés ver la pulpería de El Tarta."

    "De acá saliste la última vez camino a La Salamanca."

    hide naturaleza
    show pueblo at subir_centrada with Dissolve(1.0)

    "El Viejo, que siempre está tomando algo en este lugar, te dio todas las indicaciones de cómo superar esas primeras pruebas en La Salamanca."
    
    "Atás tu caballo afuera en el grueso aro de hierro incrustado en el suelo de la ochava."

    jump La_pulperia


    label La_pulperia:
        
        hide pueblo
        show pulperia at subir_centrada with Dissolve(1.0)

        "Al entrar te sorprende el sonido de una guitarra."
        
        "A un costado, en el rincón que siempre ocupás vos cuando tocás para todos, hay un chico joven tocando y cantando."

        "Además ves a una mujer mayor, colorada, que desencaja completamente en la húmeda pulpería de tu pueblo."
        
        "Ella está muy bien arreglada, tiene unos marcados rulos rojos y lleva un collar de perlas, aplaude con entusiasmo cada verso del joven guitarrista."
        
        "Del otro lado de la barra, el Tarta sirve vino a cuatro manos."
        
        "De aquel Viejo, que te explicó todo sobre el Mandinga y el pacto, ni rastros."

        menu:
                "Ir a la barra.":
                    jump El_Tarta
                "Acercarse al joven guitarrista.":
                    jump Lo_harias_mejor


    label El_Tarta:
        
        hide pulperia
        show barraPulperia at subir_centrada with Dissolve(1.0)

        "Te acercás a la barra y te hacés un hueco entre los muchachos que le piden más de un vaso cada uno al Tarta."

        "El Tarta te hace una seña con la cabeza como preguntando “¿qué querés?”."

        "Pedís un vino y, cuando se acerca para dártelo, te dice:"

        "—[nombre_jugador], tanto tiempo."
        
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
        
        "—El viejo falleció, lo encontramos sin vida en la calle, a unas cuadras."

        "—Le hicimos el velorio y no fue nadie. No sabemos qué carajos le pasó."
        
        "—Apareció muerto de un día para el otro. Viviá en el talar, en el camino donde viven los López, pero más allá."

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
        "—¿Ese? Llegó hace dos días; es el Pibe Farías, ¿te acordás de él?, el hijo de la Flavia."

        "—Parece que vino a llevarse a la madre a la ciudad, porque está enferma. ¿Es bueno no?"

        "Ciertamente el Pibe Farías no toca mal, pero tiene las manías de los chicos de ciudad. Además, pensas: 'obviamente, ahora no hay nadie que se compare conmigo'."

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

        "—Es la señora Dowley, parece que es de la capital."
        "—Llegó ayer y me preguntó por “artistas locales”, al día siguiente apareció el Farías."
        "—Parece encantada con él."
        "—Ayer y hoy me pidió el mejor whisky que tuviese."

        menu:
            "Acercarse al Pibe Farías y pedirle que pare, para tocar vos" if pregunta_pibe:
                    jump Lo_harias_mejor
            "Preguntarle al Tarta “¿Ese quién es?”" if not pregunta_pibe:
                    jump El_Pibe
            "Ir al rancho de El Viejo a investigar." if pregunta_viejo:
                    jump Que_paso
            "Preguntarle al Tarta por El Viejo" if not pregunta_viejo:
                    jump Malas_noticias
            "Acercarse a la Colorada Dowley":
                jump La_señora_Dowley

    label La_señora_Dowley:
        "Te acercás a la mesa de la Colorada Dowley."

        "Te parás frente a una de las sillas y la señora te invita a sentarte cuando ve que llevás una guitarra."
        
        "—¡Buenas tardes, señor!"

        "Dice ella con una voz grave, pero melodiosa y continúa:"
        
        "—Muy buena voz la de aquel joven, El Farías, ¿no?"

        menu:
            "Respondés: Yo lo haría mucho mejor.":
                jump La_colorada_curiosa
            "Respondés: No lo hace mal, pero seguramente usté escuchó mejores alguna vez, en la ciudad seguro hay muchos buenos músicos.":
                jump Admitiendo_la_torpeza_del_Farias

    label Admitiendo_la_torpeza_del_Farias:
        "La señora se acomoda el peinado y se queda mirándote unos segundos."

        "—Bueno, es verdad que por el estudio, pasaron muchos músicos y algunos eran muy buenos, mucho mejores que aquel joven."

        menu:
            "¿Por el estudio? (preguntás extrañado)":
                jump Colony_Records

    label Colony_Records:
        $ presentacion_colorada = True

        "—Me presento correctamente: soy Diana Dowley."

        "—Vine a buscar talentos al interior."
        
        "—Represento a la discográfica Colony Records."

        "—Supongo que no la conocés, se instaló hace poco en el país pero afuera es muy conocida."
        
        "—Veo que llevás tu guitarra. ¿Creés poder hacerlo mejor que el joven Farías?"

        menu:
            "Obviamente, ya va a ver":
                jump Lo_harias_mejor
    
    label Lo_harias_mejor:
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
        $ reputacion_con_el_mandinga -= 15

        "Esperás a que él termine, y te saluda presentándose como Farías, el Pibe Farías."

        "Te cede su lugar y se va a sentar junto a la Colorada."

        jump Hechizando_a_toda_la_pulpería

    label El_pibe_deja_de_tocar:
        $ reputacion_con_el_mandinga -= 5

        "El pibe empieza a tocar y enseguida copiás sus acordes."

        "Después del cuarto acorde, él deja de tocar; su cara se transforma: ahora está muy triste."

        "Se va cabizbajo a la mesa de la colorada."

        jump Hechizando_a_toda_la_pulpería

    label La_colorada_curiosa:
        "—¿Entonces creés que podés hacerlo mejor que él?"
        
        "Te lo dice casi desafiante; entonces le hace una seña al Farías."

        "El pibe corta abruptamente su interpretación y viene rápidamente a la mesa."

        "Se sienta y la colorada te habla de nuevo a vos."

        "—Es su turno, don... —dice, haciéndote una seña para que le digas tu nombre."

        menu:
            "[nombre_jugador] me llamo —respondés—, y vas al rincón de los cantores y payadores":
                jump Hechizando_a_toda_la_pulpería

    label Hechizando_a_toda_la_pulpería:
        $ reputacion_con_el_mandinga += 20
        "Con el primer rasgueo de tu guitarra todas las miradas se clavan en vos."
        
        "Luego de la primera estrofa, ya todos están mirándote embelesados."

        "Todos, menos la Colorada Dowley, que te mira con curiosidad."
        
        "Luego de la segunda canción, ella le dice algo al Pibe Farías."

        "Él cambia repentinamente su expresión, sale de la pulpería casi arrastrando su guitarra con una cara de pánico y terror."
        
        "Terminás de tocar y se produce una ovación inmensa."
        
        "Todos aplauden, silban y gritan por vos y tu canto."
        
        "Te vas acercando nuevamente a la mesa de la colorada y van tocándote la espalda, los hombros y felicitándote."

        if Vida_china:
            "Tu china que se había quedado tomando algo en la barra se acerca, interrumpe tu paso y te llena de besos, te pregunta si ya pueden ir a tu casa."

        menu:
            "Hacerle caso a tu china e ir a tu casa con ella." if Vida_china:
                jump La_calle_fría
            "Te vas a tu casa satisfecho" if not Vida_china:
                jump Una_noche_fría
            "Vas decidido a la mesa de la Colorada":
                jump Colony_Records_y_otro_contrato

    label Colony_Records_y_otro_contrato:
        $ reputacion_con_el_mandinga += 5
        if not presentacion_colorada:
            $ presentacion_colorada = True
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
                jump Capítulo_4_Colony_Records
    
    label Una_noche_fría:
        $ reputacion_con_el_mandinga -= 10
        "Salís de la pulpería agradecido de tu nuevo don."

        "Vas zigzagueando por culpa del alcohol por las calles de tierra hacia tu casa."

        "Cuando estás a unas cuadras de tu casa..."
        
        "... ves al pibe Farías, cuelga con una soga al cuello de una rama gruesa de un viejo caldén."

        "¿Habrá sido por lo que le dijo la Colorada?, te preguntás, recordando la situación de la pulpería."

        menu:
            "Ya alguien se hará cargo de ese pobre desgraciado, vos a lo tuyo, te vas para tu casa":
                jump Un_paso_atrás
            "Investigás qué pasó con el pibe":
                jump Capítulo_4_El_pobre_Pibe_Farías

    label Un_paso_atrás:
        "Llegás a tu casa y sentís un profundo pesar en el pecho."

        "Tocás la guitarra para tranquilizarte después de lo que viste."

        "Pero cuando lo pensás, creés que tiene que haber algo más."

        menu:
            "Volvés a la pulpería":
                jump La_joda_terminó
            "Volvés a ver que pasó con el pibe":
                jump Capítulo_4_El_pobre_Pibe_Farías

    label La_calle_fría:
        $ reputacion_con_el_mandinga -= 10

        "Salís de la pulpería con tu china, van zigzagueando por las calles, hace frío."

        "Se abrazan para no tener frío, para sentir el calor del otro y para no caerse."

        "Cuando están a unas cuadras de tu casa..."

        "... ves al pibe Farías, cuelga con una soga al cuello de una rama gruesa de un viejo caldén."

        "La china pega un grito de espanto y te das vuelta a consolarla. Van despacio, ella aún llorando por la terrible imagen, hasta que llegan a tu casa."

        "¿Habrá sido lo que le dijo la colorada? te preguntás recordando la situación de la pulpería."

        menu:
            "Ya alguien se hará cargo de ese pobre desgraciado, vos a lo tuyo, te quedás en tu casa con tu china":
                jump La_noche_en_tu_casa
            "Llevás a la china a tu casa y volvés a ver qué pasó con el pibe":
                jump Capítulo_4_El_pobre_Pibe_Farías

    label La_noche_en_tu_casa:
        "Llegan a tu casa y la china se deshace en llanto sobre tu pecho ni bien entran."
        
        "La consolás y le decís que no se preocupe, que el pibe debería tener sus motivos, no era tema suyo ni tuyo."

        "Tocás la guitarra para tranquilizarla."

        "Pero igual, cuando lo pensás, creés que tiene que haber algo más."

        menu:
            "Volvés a la pulpería":
                jump La_joda_terminó
            "Volvés a ver que pasó con el pibe":
                jump Capítulo_4_El_pobre_Pibe_Farías

    label La_joda_terminó:
        "La colorada Dowley ya no está."

        "Los borrachos aún están en la pulpería y algunos están cantando a coro una vieja vidala."

        if not pregunta_viejo:
            
            "El Tarta te ve entrar y ni bien llegás a la barra, te cuenta sobre el Viejo."

            "—El viejo falleció, lo encontramos sin vida en la calle, a unas cuadras."

            "—Le hicimos el velorio y no fue nadie. No sabemos qué carajos le pasó."

            "—Apareció muerto de un día para el otro. Viviá en el talar, en el camino donde viven los López, pero más allá."
        
        "Preguntás un poco por ahí, pero nadie vio salir a la Colorada ni nadie te comenta nada del Pibe Farías."

        "Con cada persona que hablás, y que te escuchó tocar, te alaba nuevamente, de una manera muy lisonjera."

        menu:
            "Ir a ver el cadaver del Farías":
                jump Capítulo_4_El_pobre_Pibe_Farías
            "Ir al rancho del viejo":
                jump Que_paso