# nota #
#dos tipor de faders:
#burn_transition y Dissolve()

label capitulo1:    


    play pisadas sfx_galope loop


    scene gauchoACaballo with burn_transition

    show gaucho_a_caballo:
        xoffset 0
        yoffset 700

    "Bienvenid@ al Mambo de los Condenados"
    "Vos, guitarrista y cantor venido a menos, que ahora va al galope por la pampa."
    "Subís por un cerro con un camino empinado."
    play ambiente sfx_SonidoAmbienteTerror loop fadein 1.0

    play fx sfx_viento1 loop fadein 1.0
    "El canto de Los pájaros, que hasta hace poco era alegre y armonioso, ahora suena como gritos de dolor."

    scene salamanca with Dissolve(3.0)
    

    "De repente, aparece frente tuyo la piedra roja de la que te había hablado el viejo, que siempre está en la pulpería de tu pueblo." 

    stop pisadas fadeout 1.0
    "Atás y asegurás tu guitarra a la silla de tu fiel caballo, y luego pronunciás {i}La Palabra{/i}, esa que aquel viejo te confesó."
    "Entonces, se abre una cueva en la roca; das un paso dentro, el caballo relincha y sale corriendo hacia el campo."


    jump Las_primeras_pruebas

    label Las_primeras_pruebas:

        scene placeholder with Dissolve(3.0)

        
        stop fx fadeout 1.0
        "En el primer pasillo de este laberinto te sacás los zapatos, el sombrero y el pañuelo. Así debe ser."
        "Ya sumido en la oscuridad, comenzás a escuchar el arpa tenebrosa y pronto sentís la presencia del basilisco."
        "Menos mal que no se ve; si no te petrificaría. Con su siseo, el basilisco te guía para atravesar este laberinto, seguís ese ruido senpertino y lo lográs superar."
        
        "Ya en el pasillo recto y angosto empezás a caminar sin guía. Después de unos pasos, sentís las primeras alimañas:"
        
        "serpientes, iguanas y tarántulas comienzan a trepar por tu cuerpo."

        "Tenés que quedarte completamente quieto, inmóvil, aguantando la respiración."
        "De a una van trepando por tus piernas, tu pecho, tu cabeza, tus hombros... y bajan por tu espalda, siguiendo su camino sin hacerte daño."
        "Todas esas criaturas pasan por tu cuerpo hasta dejarte atrás, y ahora sí, podés avanzar."

        
        scene placeholder6 with fade

        play fx sfx_respiracion_chivo 
        "Entonces aparece ese animal grotezco del que te había contado el viejo: un chivo de pelo negro, ojos endemoniados, cuernos tan curvados como un espiral."
        "El animal bufa en tu dirección. Lo rodeás fácilmente sin que se mosquee, pero..."
        "cuando por fin llegás al otro lado, el chivo se da vuelta, corre, te topea y te arroja a un profundo hoyo."

    jump La_caida

    label La_caida:
        scene caida with fade
        "El hueco es profundo, más que profundo, estás cayendo al abismo."
        "Ves pasar murciélagos a tu lado, seguís cayendo y repentinamente te desmayás."
        scene placeholder with fade
        "Despertás y estás en el fondo, ves sobre vos el abismo que sube en espirales de roca viva."

        "Te levantás y delante tuyo no podés ver más allá, es una profunda oscuridad."
        "¿Qué decidís?"


        menu:
            "Trepar por el abismo para salir":
                jump Trepar_por_el_abismo_para_salir
            "Dar un paso hacia la oscuridad":
                jump Dar_un_paso_hacia_la_oscuridad
            
    
    label Trepar_por_el_abismo_para_salir:
        scene placeholder3 with fade
        "Luego de mucho esfuerzo y luchar contra murciélagos que te atacaban débilmente lográs llegar hasta el borde del hoyo."
        "Estás de vuelta frente a aquel chivo endemoniado que te mira colérico."
        menu:
            "Enfrentarlo":
                jump  Te_enfrentas_al_chivo
            "Esquivarlo":
                jump Intentas_esquivar_al_chivo


        label Te_enfrentas_al_chivo:
            scene placeholder6 with fade
            "El chivo corre hacia vos, lográs evitar el primer golpe y le pegás una patada."
            "Se da vuelta y vuelve a intentar embestirte, de éste no pudiste zafar, caés al suelo, , te defendes con patadas y trompadas."
            "Pero el chivo es pesado y sus pezuñas son como hachas contra tu cuerpo, tras unos cuantos minutos de pisotones tu cuerpo yace inerte en la oscuridad de la cueva."
            "tras unos cuantos minutos de pisotones tu cuerpo yace inerte en la oscuridad de la cueva."
            scene placeholder with fade
            "Moriste, el juego ha terminado junto a tu vida."

            play sound "audio/capitulo1/GritoDeMiedo.ogg"
            return
            #menu:
            #    "Volver a empezar":
            #        jump capitulo1
            #    "Salir":
            #        return

                

        label Intentas_esquivar_al_chivo:
            scene placeholder6 with fade
            "Si antes pudiste pasar por al lado de él sin que se de cuenta ¿por qué no intentarlo nuevamente?."
            "Das un paso y el chivo corre tan rápidamente hacia vos que no lográs evitarlo, te tira nuevamente por el hueco del que acabás de salir." 
            scene caida with fade
            menu:
                "Caes y caes a lo profundo del abismo nuevamene":
                    jump La_caida




    label Dar_un_paso_hacia_la_oscuridad:
        scene placeholder2 with fade

        "Escuchas una pequeña explosión y se comienzan a prender, a cada lado, cien antorchas"
        "Lográs ver una sala con cortinas magníficas que cubren paredes de roca negra con piso y columnas de mármol que sostienen un techo de tierra y rocas."
        "En el fondo de la sala un enorme trono rodeado de lechuzas, quirquinchos, perros, chanchos, culebras y sapos, frente a él, hechiceros, brujas y diablillos."
        "Viniste para esto"
        menu:
            "Gritar ¡¿DÓNDE ESTÁ EL MANDINGA?!":
                jump DÓNDE_ESTÁ_EL_MANDINGA
            "Esperar en silencio":
                jump Esperar_en_silencio

        
        label Esperar_en_silencio:

            "Se desmorona una de las paredes que deja un gran agujero en uno de los costados de la sala."
            "Él atraviesa las cortinas, un enorme ser, mitad serpiente, mitad humano, ES EL MANDINGA."
            "Se sienta en su trono y te mira con un gesto entre curioso y vehemente."

            Mandinga "- ¿Qué desea el que me busca?"

            "Su voz retumba como un trueno en toda la habitación y una vez termina su frase queda resonando un zumbido siseante en el ambiente."

            menu:
                "Reculás ante su presencia":
                    jump Recular
                "¡Quiero hechizar a todo el mundo con mi canto!":
                    jump Quiero_hechizar

        label DÓNDE_ESTÁ_EL_MANDINGA:
            scene placeholder6 with fade
            $ reputacion_con_el_mandinga -= 10
            "De repente escuchás una explosión mucho mayor que la de antes."
            "Se abre un agujero en una de las paredes y él atraviesa las cortinas, un enorme ser, mitad serpiente, mitad humano, ES EL MANDINGA."
            "Se sienta en su trono y te mira con un gesto entre curioso y vehemente."
            
            Mandinga "- ¿Qué desea el que me busca?"
            "Su voz retumba como un trueno en toda la habitación y una vez termina su frase queda resonando un zumbido siseante en el ambiente."

            menu:
                "Reculás ante su presencia":
                    jump Recular
                "¡Quiero hechizar a todo el mundo con mi canto!":
                    jump Quiero_hechizar



            label Recular:
                scene placeholder5 with fade
                "Te arrepientes, empiezas a balbucear y… "
                "despertás, parece todo haber sido un mal sueño, estás completamente borracho con la cabeza sobre una mesa de la pulpería del Tarta."
                "Una guitarra suena, parece que eso te despertó, el payador empieza a contar una vieja leyenda de estas tierras, la leyenda de La Salamanca."
            return
            #menu:
            #    "Volver a empezar":
            #        jump capitulo1
            #    "Salir":
            #        return




label Quiero_hechizar:
    "- ¡Quiero hechizar a todos con mi canto!"

    "Le decís a aquel ser del inframundo"

    Mandinga "- Me gusta tu pasión, pero no tan rápido, eso va a costarte el alma."

    "Su voz vuelve a hacer temblar las paredes y termina en siseo."

    menu:
        "Reculás, ¿quién le entregaría su alma a un ser así?":
            jump Recular
        "¿A dónde hay que firmar?":
            jump A_dónde_hay_que_firmar


label A_dónde_hay_que_firmar:
    scene placeholder with fade
    "Aceptás vender tu alma y el Mandinga te dice que aún hay unas pruebas más que debés superar."
    "Hace un gesto con su mano y ante vos se abre el suelo"
    "Una gran grieta separa la sala al medio, de un lado estás vos, del otro el Mandinga, su trono y sus seguidores."
    "Él saca un enorme facón de su costado y lo revolea, queda sobre la raja que se abrió en la tierra, formando un puente con el filo hacia arriba."

    Mandinga "- Vení conmigo"

    "Dice el Mandinga abriendo los brazos como invitándote a su regazo serpentino y luego señala el filo del cuchillo que acaba de lanzar."

    menu:
        "Pasás decididamente":
            jump Pasar_decididamente

        "Pasás cautelosamente":
            jump Pasar_cautelosamente

    label Pasar_decididamente:
        "Comenzás decididamente a caminar sobre el filo del facón."
        "Paso tras paso tus pies sangran pero no sentís dolor."
        "Cuando llegás a la mitad ves una luz dorada bajo tus pies, mirás hacia abajo y hay un crucifijo del que emana la luz."
        
        Mandinga "-¡ESCUPILO!"

        "La voz del Mandinga suena más fuerte que nunca, hace temblar todo y casi estás a punto de caerte, pero recuperás el equilibrio."
        menu:
            "Escupís el crucifijo":
                jump Escupir_el_crucifijo
            "Decís “eso es una blasfemia“":
                jump Pasar_cautelosamente

        label Pasar_cautelosamente:
            scene placeholder3 with fade
            "Das un paso sobre el cuchillo y dudás, el filo del facón se hunde en tu pie y no podés frenar la fuerza de la gravedad."
            "Empezás a caer sobre ese último paso, tu cuerpo se desbalancea y cae."
            "Yacés en dos mitades en lo profundo de la grieta del infierno."
            "Moriste, el juego ha terminado junto a tu vida."
            return
            #menu:
            #    "Volver a empezar":
            #        jump capitulo1
            #    "Salir":
            #        return

    label Escupir_el_crucifijo:
        scene placeholder6 with fade
        stop ambiente fadeout 1.0
        play fx crucifijo
         
        "Escupís el crucifijo y seguís por el filo del facón, lográs llegar al otro lado."
        "Una bruja te recibe con un pergamino abierto, un diablillo moja una pluma en la sangre de tus pies y te la da."
    

        $ nombre_jugador = renpy.input("¿Con qué nombre vas a firmar el contrato?") 
        $ nombre_jugador = nombre_jugador.strip()

        if nombre_jugador == "":
            $ nombre_jugador = "Protagonista"

        # redefinir el personaje p con el nombre elegido
        $ p = Character(nombre_jugador)
        play sound "audio/capitulo1/risaDiabolica.wav"
        $ humanidad -= 10
        p "- Mi nombre es [nombre_jugador] y te vendo mi alma Mandinga."


        menu:
            "¡Lo lograste!":
                jump Lo_lograste
            
    label Lo_lograste:

        Mandinga "-¡BIENVENIDO A MIS HUESTES, CONDENADO!"

        "Resuena una vez más la voz del Mandinga, mucho más fuerte, mucho más demoníaca."
        "Las brujas, los brujos y los diablillos arrancan la fiesta a tu alrededor, sentís como tu garganta arde y luego se calma y empezás a cantar junto a los demás."
        "Las alimañas te levantan sobre sus lomos y te pasean por toda la sala, tu voz y tu canto ahora suena como nunca antes sonó."
        scene placeholder3 with fade
        menu:
            "En un rancho cercano...":
                jump En_un_rancho_cercano

    label En_un_rancho_cercano:
        stop music fadeout 1.0


        "A pocos kilómetros una señora se despierta asustada por el alboroto, empieza a rezar..."
        "- ¡Dios nos salve, que hoy hay baile en La Salamanca!"

        menu:
            "Al segundo capítulo":
                jump capitulo2

    label Al_segundo_capítulo:
        "aun en desarrollo..."