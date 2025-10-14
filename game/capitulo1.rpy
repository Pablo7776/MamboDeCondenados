label capitulo1:    

    stop music fadeout 1.0
    play sound sfx_galope

    # Mostramos una imagen de fondo
    scene gauchoACaballo with fade

    show gaucho_a_caballo:
        xoffset 0
        yoffset 700

    "Bienvenid@ al Mambo de los Condenados"
    "Nuestro protagonista va al galope por la pampa, sube un cerro por un camino empinado,"
    "los pájaros que hasta hace poco cantaban alegremente ahora suenan como gritos de dolor"

    scene salamanca with fade
    play music sfx_SonidoAmbienteTerror loop

    "y de repente aparece frente a él, la piedra roja que el viejo de la pulpería le había dicho."
    "Ese viejo le dió todos los detalles sobre cómo llegar, como pasar las primeras pruebas que tendrá que enfrentar"
    "Ata y asegura su guitarra a la silla de su fiel caballo y luego pronuncia ESA palabra"
    "se abre una cueva en la roca, da un paso dentro y su caballo relincha y sale corriendo hacia el lado contrario."

    

    jump Las_primeras_pruebas

    label Las_primeras_pruebas:


        "En el primer pasillo de este laberinto se quita los zapatos, el sombrero y el pañuelo, debe ser así"
        "ya sumido en la oscuridad comienza a escuchar el arpa y pronto siente la presencia del basilisco"
        "menos mal que no se ve, sino lo petrificaría, comienza a caminar siguiendo su siseo"
        "el basilisco lo guía para atravesar este laberinto."
        "Ya en el pasillo recto y angosto comienza a caminar, de repente siente las primeras alimañas"
        "serpientes, iguanas y tarántulas comienzan a trepar por su cuerpo y se queda completamente quieto"
        "de a una van pasando por sus piernas, su pecho, su cabeza, sus hombros y bajan por su espalda"
        "siguen su camino sin hacerle daño. Todas terminan de pasar y ahora sí, puede avanzar."
        "Entonces aparece ese animal grotezco, un chivo de pelo negro, ojos endemoniados, cuernos tan curvados como un espiral"
        "bufea en dirección hacía nuestro protagonista, que lo rodea sin que se mosquee, pero cuando por fin llega al otro lado"
        "el animal se da vuelta y corre, lo topea y lo arroja a un hoyo."


    jump La_caida

    label La_caida:

        "El hueco es profundo, más que profundo, está cayendo al abismo, ve pasar murciélagos a su lado y sigue cayendo"
        "de repente choca contra el suelo y se desmaya."
        "Despiertas y estás en el fondo, ves sobre ti el abismo que sube en espirales de roca viva"
        "te levantas y no puedes ver más allá delante tuyo, hay una profunda oscuridad."
        "¿Qué decidís?"


        menu:
            "Trepar por el abismo para salir":
                jump Trepar_por_el_abismo_para_salir
            "Dar un paso hacia la oscuridad":
                jump Dar_un_paso_hacia_la_oscuridad
            
    
    label Trepar_por_el_abismo_para_salir:
        "Luego de mucho esfuerzo y luchar contra murciélagos que te atacaban débilmente"
        "llegás hasta el borde del hoyo, estás de vuelta frente a aquel chivo endemoniado que te mira colérico."
        menu:
            "Lo enfrentás":
                jump  Te_enfrentas_al_chivo
            "Lo intentás esquivar":
                jump Intentas_esquivar_al_chivo


        label Te_enfrentas_al_chivo:
            "El chivo corre hacia vos, lográs evitar el primer golpe y le pegás una patada."
            "Se da vuelta y vuelve a intentar embestirte, de este no pudiste zafar, caes al suelo"
            "te defendes a patadas y trompadas, pero el chivo es pesado y sus pezuñas son como hachas contra tu cuerpo"
            "tras unos cuantos minutos de pisotones tu cuerpo yace inerte en la oscuridad de la cueva."
            
            "Moriste, el juego ha terminado junto a tu vida."

            play sound "audio/capitulo1/GritoDeMiedo.ogg"
            menu:
                "Volver a empezar":
                    jump capitulo1
                "Salir":
                    return

                

        label Intentas_esquivar_al_chivo:
            "Si antes pudiste pasar por al lado de él sin que se de cuenta ¿por qué no intentarlo nuevamente?."
            "Das un paso y el chivo corre tan rápidamente hacia tí que no logras evitarlo" 
            "te tira nuevamente por el hueco del que acabas de salir."
            menu:
                "Caes y caes a lo profundo del abismo nuevamene ":
                    jump La_caida




    label Dar_un_paso_hacia_la_oscuridad:
        "Escuchas una pequeña explosión y se comienzan a prender, a cada lado, cien antorchas"
        "lográs ver una sala con cortinas magníficas que cubren paredes de roca negra"
        "piso y columnas de mármol que sostienen un techo de tierra y rocas."
        "En el fondo de la sala un enorme trono rodeado de lechuzas, quirquinchos, perros, chanchos, culebras y sapos"
        "frente al trono, hechiceros, brujas y diablillos."
        "Viniste para esto"
        menu:
            "Gritar ¡¿DÓNDE ESTÁ EL MANDINGA?!":
                jump DÓNDE_ESTÁ_EL_MANDINGA
            "Esperar en silencio":
                jump Esperar_en_silencio

        
        label Esperar_en_silencio:
            "Se abre un agujero, luego de que se desmoronara una de las paredes y él atraviesa las cortinas"
            "un enorme ser, mitad serpiente, mitad humano, ES EL MANDINGA."
            "Se sienta en su trono y te mira con un gesto entre curioso y vehemente."

            Mandinga "- ¿Qué desea el que me busca?"

            "Su voz retumba como un trueno en toda la habitación y una vez termina su frase queda resonando un zumbido seseante en el ambiente."

            menu:
                "Recular":
                    jump Recular
                "¡Quiero hechizar a todo el mundo con mi canto!":
                    jump Quiero_hechizar

        label DÓNDE_ESTÁ_EL_MANDINGA:
            "De repente escuchas una explosión mucho mayor que la de antes"
            "se abre un agujero en una de las paredes y él atraviesa las cortinas"
            "un enorme ser, mitad serpiente, mitad humano, ES EL MANDINGA."
            "Se sienta en su trono y te mira con un gesto entre curioso y vehemente."
            Mandinga "- ¿Qué desea el que me busca?"
            "Su voz retumba como un trueno en toda la habitación y una vez termina su frase queda resonando un zumbido seseante en el ambiente."

            menu:
                "Recular":
                    jump Recular
                "¡Quiero hechizar a todo el mundo con mi canto!":
                    jump Quiero_hechizar



            label Recular:
                "Te arrepientes, empiezas a balbucear y… "
                "despiertas..."
                "parece todo haber sido un mal sueño, estás completamente borracho con la cabeza sobre una mesa de la pulpería del Tarta."
                "Una guitarra suena, parece que eso te despertó, el payador empieza a contar una vieja leyenda de estas tierras, la leyenda de La Salamanca."
            menu:
                "Volver a empezar":
                    jump capitulo1
                "Salir":
                    return




label Quiero_hechizar:
    p "- ¡Quiero hechizar a todos con mi canto!"

    "Le dices a aquel ser del inframundo"

    Mandinga "- Me gusta tu pasión, pero no tan rápido, eso va a costarte el alma ¿estás de acuerdo?"

    "Su voz vuelve a hacer temblar las paredes y termina en siseo."

    menu:
        "Recular":
            jump Recular
        "¿A dónde hay que firmar?":
            jump A_dónde_hay_que_firmar


label A_dónde_hay_que_firmar:
    "Aceptás vender tu alma y el Mandinga te dice que aún hay unas pruebas más que debés superar"
    "hace un gesto con la mano y ante ti se abre el suelo, una gran grieta separa la sala por la mitad"
    "de un lado estás vos, del otro el Mandinga, su trono y sus seguidores."
    "Él saca un enorme facón que estaba clavado en un demonio medio moribundo y lo tira"
    "El facón, aun con sangre verde, queda formando un puente sobre la grieta con el filo hacia arriba."


    Mandinga "- Ven conmigo"

    "Dice el Mandinga abriendo los brazos como invitándote a su regazo serpentino y luego señala el filo del cuchillo que acaba de lanzar."

    menu:
        "Pasar decididamente":
            jump Pasar_decididamente

        "Pasar cautelosamente":
            jump Pasar_cautelosamente

    label Pasar_decididamente:
        "Comienzas decididamente a caminar paso tras paso sobre el filo del cuchillo, tus pies sangran pero no sentís dolor."
        "Cuando llegas a la mitad ves una luz dorada bajo tus pies, cuando mirás hacia abajo hay un crucifijo del que emana la luz."
        Mandinga "- ¡ESCÚPELO!"
        "La voz del Mandinga suena más fuerte que nunca, hace temblar todo y casi estás a punto de caerte, pero recuperás el equilibrio."
        menu:
            "Escupir el crucifijo":
                jump Escupir_el_crucifijo
            "Decir “eso es una blasfemia”":
                jump Pasar_cautelosamente

        label Pasar_cautelosamente:
            "Das un paso sobre el cuchillo y dudas, el filo del cuchillo se hunde en tu pie y no podés frenar la fuerza de la gravedad"
            "empezás a caer sobre ese último paso, tu cuerpo se desbalancea y cae."
            "Yacés en dos mitades en lo profundo de la grieta del infierno."
            "Moriste, el juego ha terminado junto a tu vida."
            menu:
                "Volver a empezar":
                    jump capitulo1
                "Salir":
                    return

    label Escupir_el_crucifijo:
        "Escupís el crucifijo y seguís por el filo del cuchillo, lográs llegar al otro lado."
        "Una bruja te recibe con un pergamino abierto, un diablillo moja una pluma en la sangre de tus pies y te la da."
    

        $ nombre_jugador = renpy.input("¿Con qué nombre vas a firmar el contrato?") 
        $ nombre_jugador = nombre_jugador.strip()

        if nombre_jugador == "":
            $ nombre_jugador = "Protagonista"

        # redefinir el personaje p con el nombre elegido
        $ p = Character(nombre_jugador)
        play sound "audio/capitulo1/risaDiabolica.wav"
        p "- Mi nombre es [nombre_jugador] y te vendo mi alma Mandinga."


        menu:
            "¡Lo lograste!":
                jump Lo_lograste
            
    label Lo_lograste:

        Mandinga "-¡BIENVENIDO A MIS HUESTE CONDENADO"

        "Resuena una vez más la voz del Mandinga, mucho más fuerte, mucho más demoniaca."
        "Las brujas, los brujos y los diablillos comienzan una fiesta a tu alrededor, sentís como tu garganta arde y luego se calma y comenzás a cantar junto a los demás, las alimañas te levantan sobre sus lomos y te pasean por toda la sala, tu voz, tu canto ahora suena como nunca antes sonó."

        menu:
            "En un rancho cercano...":
                jump En_un_rancho_cercano

    label En_un_rancho_cercano:
        "a pocos kilómetros una señora se despierta asustada por el alboroto, comienza a rezar..."
        "- ¡Dios nos salve, que hoy hay baile en La Salamanca!"

        menu:
            "Al segundo capítulo":
                jump Al_segundo_capítulo

    label Al_segundo_capítulo:
        "aun en desarrollo..."