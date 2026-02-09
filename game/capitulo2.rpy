default nombre_jugador = "Ramón"
default Vida_china = False

label capitulo2:
    # ESCENA 2.1
    stop music fadeout 12.0
    play ambiente sfx_SonidoAmbienteTerror loop fadein 1.0
    
    $ mostrar_repu()

    show caida1 at subir_centrada with Dissolve(5.0)

    "[nombre_jugador], trepás nuevamente por el abismo en espiral por el que caíste."

    "Te encontrás cara a cara con el chivo negro, pero esta vez no te ataca. Se acerca lentamente y te lame los pies; con su saliva sana tus heridas."

    "Las alimañas te miran con respeto desde sus cuevas. Cuando llegás al laberinto, otra vez aparece el basilisco: te guía para salir." 
    
    "En la última curva te esperan tus botas, tu sombrero y tu pañuelo, que te los volvés a poner."

    "Das un paso afuera y la piedra que se había abierto antes ahora se cierra suavemente."

    stop ambiente
    play sound sfx_viento1 loop volume 0.7

    hide caida1

    #ESCENA 2.2
    show ranchoHiguera at subir_centrada with Dissolve(1.0)
    
    play fx sfx_galope 

    "Ves llegar a tu caballo, con tu guitarra aún bien atada a la silla."

    "Te ponés la guitarra en la espalda y comenzás a cabalgar. Pasan las horas y ya se te está haciendo de noche." 
    
    "A lo lejos ves una tranquera y al fondo del campo un pequeño rancho."

    "Un poco más adelante una frondosa higuera bajo la que podrías refugiarte del rocío."
    
    stop sfx_galope
    stop audio
    stop viento
    stop fx
    stop estatica

    ###"HASTA ACA LA DEMO DE LA PRIMERA ETAPA"###
    ###Ni siquiera debería entrar al menú de opciones, directamente un continuará###

    label opciones22:

        $ opciones = [
            {"texto":"Entrás al campo y golpeás la puerta", "jump":"puerta_del_rancho", "nota":opcion_neutral},
            {"texto":"Pasás la noche bajo la higuera", "jump":"noche_ante_las_estrellas", "nota":opcion_muymala},
        ]
        call screen guitarra_choice(opciones)


label noche_ante_las_estrellas:
    # ESCENA 2.2A.1
    $ reputacion_con_el_mandinga -= 30
    $ mostrar_repu()

    play sound sfx_noche loop fadein 2.0
    
    hide ranchoHiguera
    show higuera at subir_centrada with Dissolve(3.0)
    
    "Encontrás una gran higuera a un costado del camino, atás tu caballo y te recostás debajo de aquel custodio de la pampa."

    play fx ruidoRosa volume 0.5

    "Por la noche en tus sueños se repite la frase que dijo El Mandinga:"
    
    "{size=70}{cps=10}—BIENVENIDO A MIS HUESTES, CONDENADO!{/cps}{/size}" # efecto de texto

    "Ves, en sueños, cómo las alimañas de La Salamanca salen de la cueva y se dirigen al camino que andaste para llegar hasta acá."

    "Queda retumbando, en tu mente, la palabra \"CONDENADO\""

    stop fx fadeout 3.0

    "Te levantás agitado." 

    "Tenés una deuda importante que saldar con ese poderoso ser de las profundidades."
   
    stop sound fadeout 2.0

    "Cabalgás pensativo rumbo a la pulpería del Tarta, en tu pueblo."
    
    hide higuera with Dissolve(4.0)

    jump continuara
    #menu:
    #jump continuara
        #"Al tercer capítulo":
        #    jump capitulo3

label puerta_del_rancho:
    # ESCENA 2.2B.1
    hide ranchoHiguera
    show puertaChina at subir_centrada with Dissolve(1.0)
    
    "Una china joven te abre la puerta. Un poco asustada, te pregunta con voz temblorosa:"
    
    ### personaje ##########################
    pause 0.01
    show china_placeholder at mostrar_izquierda

    China "—¿Quién es? ¿Qué necesitás?"
   
    hide china_placeholder
    label opciones22B1:

        $ opciones = [
            {"texto":"{image=hablando} Disculpe señorita, soy [nombre_jugador]. Se me hizo de noche en el camino, me podrían dar techo esta noche, a cambio puedo ofrecer mi música", "jump":"Fuiste_cordial_y_se_te_agradece_por_ello", "nota":opcion_muymala},
            {"texto":"{image=hablando} ¡¿Qué voy a necesitar?! ¡Necesito entrar!", "jump":"No_fuiste_muy_cordial", "nota":opcion_mala},
            {"texto":"(Sacás tu guitarra y tocas un primer acorde) {image=hablando} Soy [nombre_jugador]", "jump":"Tus_primeros_hechizados", "nota":opcion_buena},
        ]
        call screen guitarra_choice(opciones)


label Tus_primeros_hechizados:
    $ reputacion_con_el_mandinga += 10
    $ mostrar_repu()

    hide puertaChina

    $ renpy.music.set_volume(1.0, channel= "fx")
    play fx sfx_hoguera_pequena
    play music musica_piedra_y_camino volume 0.7

    show casaInterior at subir_centrada with Dissolve(1.0)
    
    "Empezás a rasguear la guitarra y cuando te das cuenta ya estás improvisando versos junto a toda la familia."

    "Los padres de la joven lloran y sus hermanos miran sin poder quitar la vista de tus cuerdas."

    "Pero la joven china, ella está absolutamente entregada a tu canto, a tu hechizo."

    "Cenan y te rodean de halagos y agradecimientos."

    "Te muestran una habitación en la que podés dormir, es la habitación de los padres de la familia, ellos van a dormir en el comedor para dejarte la mejor cama de la casa."
    
    hide casaInterior
    show muerte at subir_centrada with Dissolve(5.0)
    
    $ renpy.music.set_volume(0.5, delay=2.0, channel="music")
    
    "Te dormís y empezás a soñar"

    "Es la voz de El Mandinga ... \"CONDENA...\" !" # efecto texto

    hide muerte with Dissolve(5.0)
    show casaInterior at subir_centrada with Dissolve(1.0)

    "Te despierta una voz dulce y alguien que te sacude suavemente, es la china que te abrió la puerta."

    show china_placeholder at mostrar_izquierda

    China "Disculpe, ¿puedo... estar con usted esta noche?" #efecto
    
    hide china_placeholder

    menu:
        "Aceptás la propuesta":
            jump La_noche_de_pasión
        "Rechazás la invitación, ella es muy joven para vos.":
            jump Una_mañana_incómoda

label La_noche_de_pasión:
    $ reputacion_con_el_mandinga += 10
    $ mostrar_repu()
    $ Vida_china = True
    $ renpy.music.set_volume(1.0, delay=2.0, channel="music")
    
    "Pasan juntos una noche de extrema pasión."

    "A la mañana siguiente tanto ella como su familia te ruegan que la aceptes como compañera, que la dejes acompañarte a donde vayas."

    "No te podés negar, ella es como una bendición para vos."
        
    "Te vas con la china, camino a la pulpería del Tarta y a tu pueblo"
    
    stop sound

    hide casaInterior with Dissolve(4.0)

    jump continuara
    #menu:
    #    "Al tercer capítulo":
    #        jump capitulo3

label Una_mañana_incómoda:
    $ reputacion_con_el_mandinga -= 20
    $ mostrar_repu()
    
    stop music
    
    hide casaInterior
    show muerte at subir_centrada with Dissolve(5.0)
    
    "Esa noche la rechazás, ella sale llorando de la habitación a viva voz."

    "Te volvés a dormir y volvés a soñar:"

    play fx ruidoRosa volume 0.5

    "Ves en tus sueños como las alimañas brotan de aquel cerro en el que encontraste la Salamanca."

    "Las huestes de El Mandinga, parecen recorrer el camino que vos hiciste."

    "Te despertás abruptamente exaltado cuando algo te está tocando los pies, te sacás rápidamente la colcha de encima."
    
    "Son unas cinco serpientes que estaban dentro de la cama."

    stop fx fadeout 2.0

    hide muerte with Dissolve(5.0)
    show casa at subir_centrada with Dissolve(1.0)
    
    "Salís corriendo al salón pero esa mañana todos te miran mal y prácticamente te echan de su rancho casi sin hablarte."

    stop sound

    "Te subís a tu caballo y galopás hacia tu pueblo y hacia la Pulpería del Tarta"
    hide casa with Dissolve(4.0)

    #jump capitulo3
    jump continuara
    #menu:
    #    "Al tercer capítulo":
    #        jump capitulo3

label Fuiste_cordial_y_se_te_agradece_por_ello:
    $ reputacion_con_el_mandinga -= 15
    $ mostrar_repu()

    hide puertaChina

    stop sound

    $ renpy.music.set_volume(1.0, channel="sound")
    play sound sfx_hoguera_pequena loop fadein 1.0

    show casaInterior at subir_centrada with Dissolve(1.0)

    "Te abre la puerta, aún un poco temerosa, pero viene su padre del fondo del salón y te recibe con un apretón de manos."

    "Comen en familia: vos, la china que te recibió, su padre, su madre y sus dos hermanos menores."

    "La cena fue amena, y la china no te sacaba los ojos de encima."

    "Pedís si por favor podrías tocar para ellos pero los padres se niegan."

    "Te dicen que no quieren nada a cambio de la hospitalidad, ellos hospedarían a todo buen hombre que esté exhausto en el camino."

    "Te tiran una manta gruesa sobre el suelo del comedor y te dan otra para taparte."

    "Dormís cálidamente y por la noche soñás:"

    hide casaInterior
    show muerte at subir_centrada with Dissolve(5.0)

    play fx ruidoRosa volume 0.5

    "Ves en tus sueños como las alimañas brotan de aquel cerro en el que encontraste la Salamanca."

    "Las huestes de El Mandinga, parecen recorrer el camino que vos hiciste."

    "Te despertás abruptamente en medio de la noche exaltado cuando algo te está tocando los pies."

    "Te sacás rápidamente la colcha de encima y son unas cinco cucarachas que estaban debajo de la frazada."

    "Viene corriendo la china a preguntarte si estás bien, le señalás a donde estaban esos bichos y cuando volvés a mirar ya no están."

    stop fx fadeout 2.0

    hide muerte with Dissolve(5.0)
    show casaInterior at subir_centrada with Dissolve(1.0)

    "Ella te acaricia tiernamente la espalda y empieza a cantarte una nana."

    play music musica_piedra_y_camino volume 0.7

    "Su voz es hermosa, y al poco tiempo estás cantando con ella, las cuerdas de tu guitarra empiezan a resonar con sus voces y cuando ya termina la canción, se besan con la joven."

    "Te dejás llevar"
    
    jump La_noche_de_pasión 


label No_fuiste_muy_cordial:
    $ reputacion_con_el_mandinga -= 20
    $ mostrar_repu()
    
    hide puertaChina
    show casa at subir_centrada with Dissolve(1.0)

    "Asustás a la joven y cierra rápidamente, te quedás ahí frente a la puerta."

    "De repente se vuelve a abrir, parece ser el padre de la joven."

    "Te echan a rebencazos de su campo, montás de nuevo tu caballo y seguís cabalgando toda la noche."

    hide casa
    show muerte at subir_centrada with Dissolve(5.0)

    "Te dormís sobre la silla de montar y empezás a soñar."

    play fx ruidoRosa volume 0.5

    "En tus sueños se repite la frase que dijo El Mandinga:"
    
    play sound sfx_basilisco 

    "{size=70}{cps=10}\"—BIENVENIDO A MIS HUESTES, CONDENADO!\"{/cps}{/size}" # efecto texto
    ### agregar los efectos del mandinga hablando ### esto es lo que hay
    "Ves cómo las alimañas de La Salamanca salen de la cueva y se dirigen al camino que andaste para llegar hasta acá."

    "Queda retumbando la última palabra, \"CONDENADO\". Te levantás agitado."

    stop fx fadeout 2.0

    "Tenés una deuda importante que saldar con ese poderoso ser de las profundidades."

    "Tomás las riendas y seguís cabalgando pensativo rumbo a la pulpería del Tarta."
    
    hide muerte with Dissolve(4.0)
    #show naturaleza at subir_centrada with Dissolve(1.0)
    jump continuara
    #jump capitulo3
    #menu:
    #    "Al tercer capítulo":
    #        jump capitulo3