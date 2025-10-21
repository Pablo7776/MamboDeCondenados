default nombre_jugador = "Vos!"


label capitulo2:
    "[nombre_jugador], trepás nuevamente por el abismo en espiral por el que caiste."

    "Te encontrás cara a cara con el chivo negro, pero esta vez no te ataca. Se acerca lentamente y te lame los pies; con su saliva sana tus heridas."

    "Las alimañas te miran con respeto desde sus cuevas. Cuando llegás al laberinto, otra vez aparece el basilisco: te guía para salir." 
    
    "En la última curva te esperan tus botas, tu sombrero y tu pañuelo, que te los volvés a poner."

    "Das un paso afuera y la piedra que se había abierto antes ahora se cierra crujiendo suavemente."
    
    "Escuchás un galope y ves llegar a tu caballo, con tu guitarra aún bien atada a su silla."

    "Te ponés la guitarra en la espalda y comenzás a cabalgar. Pasan las horas y ya se te está haciendo de noche." 
    
    "A lo lejos ves una tranquera y al fondo del campo un pequeño rancho."

    "Un poco más adelante una frondosa higuera bajo la que podrías refugiarte del rocío."

    menu:
        "Entrar al campo y golpeás la puerta":
            jump puerta_del_rancho
        "Pasás la noche bajo la higuera":
            jump noche_ante_las_estrellas

label noche_ante_las_estrellas:
    $ reputacion_con_el_mandinga -= 10
    "Encontrás una gran higuera a un costado del camino, atás tu caballo y te recostás debajo de aquél custodio de la pampa."

    "Por la noche en tus sueños se repite la frase que dijo El Mandinga: ¡Bienvenido a mis huestes CONDENADO!]" # efecto de texto

    "Ves como las alimañas de La Salamanca salen de la cueva y se dirigen al camino que andaste para llegar hasta acá."

    "Queda retumbando la última palabra, "CONDENADO" te levantás agitado."

    "Tenés una deuda importante que saldar con ese poderoso ser de las profundidades."

    menu:
        "Cabalgás pensativo rumbo a la pulpería del Tarta, en tu pueblo.":
            jump capitulo3

label puerta_del_rancho:
    "Una china joven te abre la puerta, un poco asustada, te pregunta con voz temblorosa"

    "- ¿Quién es? ¿Qué necesita?"

    menu:
        "- Soy [nombre_jugador] vengo viajando hace medio día, se me hizo de noche en el camino, quería saber si me podían dar techo esta noche, a cambio puedo ofrecer mi música. - Y mostrás tu guitarra.":
            jump Fuiste_cordíal_y_se_te_agradece_por_ello

        "- ¿Y qué voy a necesitar? ¡Necesito entrar! ¡Hace frío!":
            jump No_fuiste_muy_cordial
        
        "- Soy [nombre_jugador]. - Sacás tu guitarra y tocás un primer acorde":
            jump Tus_primeros_hechizados

label Tus_primeros_hechizados:
    $ reputacion_con_el_mandinga += 10
    "Empezás a rasguear la guitarra y cuando te das cuenta ya estás improvisando versos junto a toda la familia."

    "Los padres de la joven lloran y sus hermanos miran sin poder quitar la vista de tus cuerdas."

    "Pero La China, ella está absolutamente entregada a tu canto, a tu hechizo."

    "Cenan y te rodean de halagos y agradecimientos."

    "Te muestran una habitación en la que podés dormir, es la habitación de los padres de la familia, ellos van a dormir en el comedor para dejarte la mejor cama de la casa."

    "Te dormís y empezás a soñar"

    "Es la voz de El Mandinga ... CONDENA.. !" # efecto texto

    "Te despierta una voz dulce y alguien que te sacude suavemente, es la china que te abrió la puerta"

    "- Disculpe, ¿puedo.... estar con usted esta noche?" #efecto

    menu:
        "Aceptar":
            jump La_noche_de_pasión
        "Rechazar":
            jump Una_mañana_incómoda

label La_noche_de_pasión:
    $ reputacion_con_el_mandinga += 10
    $ Vida_china = True

    "Pasan juntos una noche de extrema pasión."

    "A la mañana siguiente tanto ella como su familia te ruegan que la aceptes como compañera, que la dejes acompañarte a donde vayas."

    "No te podés negar, ella es como una bendición para vos."

    menu:
        "Te vas con la china, camino a la pulpería del Tarta y a tu pueblo":
            jump capitulo3

label Una_mañana_incómoda:
    $ reputacion_con_el_mandinga -= 15

    "Esa noche la rechazás, ella sale llorando de la habitación a viva voz."

    "Te volvés a dormir y volvés a soñar:"

    "Ves en tus sueños como las alimañas brotan de aquel cerro en el que encontraste la Salamanca."

    "Las huestes de El Mandinga, parecen recorrer el camino que vos hiciste."

    "Te despertás abruptamente exsaltado cuando algo te está tocando los piés, te sacás rapidamente la colcha de encima"

    "Son unas cinco serpientes que estaban dentro de la cama."

    "Salís corriendo al salón pero esa mañana todos te miran mal y practicamente te hechan de su rancho casi sin hablarte."

    menu:
        "Te subís a tu caballo y galopás hacia tu pueblo y hacia la Pulpería del Tarta":
            jump capitulo3

label Fuiste_cordíal_y_se_te_agradece_por_ello:
    $ reputacion_con_el_mandinga -= 5

    "Te abre la puerta, aún un poco temerosa, pero viene su padre del fondo del salón y te recibe con un apretón de manos."

    "Comen en familia: vos, la china que te recibió, su padre, su madre y sus dos hermanos menores."

    "La cena fue amena, y la china no te sacaba los ojos de encima."

    "Pedís si por favor podrías tocar para ellos pero los padres se niegan."

    "Te dicen que no quieren nada a cambio de la hospitalidad, ellos hospedarían a todo buen hombre que esté exhausto en el camino."

    "Te tiran una manta gruesa sobre el suelo del comedor y te dan otra para taparte."

    "Dormís calidamente y por la noche soñás:"

    "Ves en tus sueños como las alimañas brotan de aquel cerro en el que encontraste la Salamanca."

    "Las huestes de El Mandinga, parecen recorrer el camino que vos hiciste."

    "Te despertás abruptamente en medio de la noche exsaltado cuando algo te está tocando los piés."

    "Te sacás rápidamente la colcha de encima y son unas cinco cucarachas que estaban debajo de la frazada."

    "Viene corriendo la china a preguntarte si estás bien, le señalás a donde estaban esos bichos y cuando volvés a mirar ya no están."

    "Ella te acaricia tiernamente la espalda y empieza a cantarte una nana."

    "Su voz es hermosa, y al poco tiempo estás cantando con ella, las cuerdas de tu guitarra empiezan a resonar con sus voces y cuando ya termina la canción, se besan con la joven."

    menu:
        "Te dejás llevar":
            jump La_noche_de_pasión 


label No_fuiste_muy_cordial:
    $ reputacion_con_el_mandinga -= 5
    "Asustás a la joven y cierra la puerta, te quedás ahí frente a la puerta."

    "De repente se vuelve a abrir, parece ser el padre de la joven."

    "Te hechan a rebencazos de su campo, montás de nuevo tu caballo y seguís cabalgando toda la noche."

    "Te dormís sobre la silla de montar y empezás a soñar."

    "En tus sueños se repite la frase que dijo El Mandinga:"

    "- ¡Bienvenido a mis huestes CONDENADO!]" # efecto texto

    "Ves como las alimañas de La Salamanca salen de la cueva y se dirigen al camino que andaste para llegar hasta acá."

    "Queda retumbando la última palabra, CONDENADO te levantás agitado."

    "Tenés una deuda importante que saldar con ese poderoso ser de las profundidades."

    menu:
        "Tomás las riendas y seguís cabalgando pensativo rumbo a la pulpería del Tarta, en tu pueblo.":
            jump capitulo1