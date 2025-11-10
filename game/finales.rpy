label finales:
    label Sucumbis_a_la_locura:
        "Lo perdiste todo, incluso perdiste completamente tu humanidad."
        
        "Luego de presenciar toda la matanza te unís a las huestes de La Salamanca."

        "Volvés junto a todas las alimañas a la cueva."

        "Ahí vivís por la eternidad."

        "Participando de cada baile que se hace en honor a todos los incautos que, como vos, hacen un pacto teñido de sangre con El Mandinga."

        menu:
            "Volver al menú principal":
                return

    label El_viaje_eterno:
        "Muchos años estuviste recorriendo toda la provincia tocando en cada pulpería que podías."

        "Te ibas dando cuenta de cómo cada vez que tocabas para un público nuevo tu mente y tu corazón iban volviéndose más y más fríos."

        "Hasta que una noche llegaste a un punto de no retorno, a no sentir nada."

        "Ni siquiera la satisfacción de las ovaciones que recibías. Nada de nada."

        "Y así siguieron tus días sin sobresaltos, por años y años."

        "Algunos ancianos dicen que, hace 40 años, cuando eran jóvenes, te vieron tocar."

        "Pero enseguida dicen que es imposible, si así fuera, tendrías que estar tan viejo como ellos. Pero si aquel fueras vos, no envejeciste ni una pizca."

        "Vos hace rato que dejaste de contar los años."

        "Bien hecho CONDENADO, superaste algunos de los mambos que se te presentaron."
        
        menu:
            "Volver al menú principal":
                return

    label Condenado_desgraciado:
        "El Mandinga dice con la voz más tenebrosa que jamás escuchaste:"

        "— ¡Me traicionaste basura humana, despreciable mortal!"

        "— Ya no sos digno del don que te di; es hora de cobrar tu deuda"

        "Se transforma en un ser monstruoso con una boca gigante con miles de dientes."

        "Sin que puedas defenderte ni articular palabra alguna te atrapa por el cuello, te levanta por sobre sus tremendas fauces y te traga de un solo bocado."

        menu:
            "Volver al menú principal":
                return
    
    label Sos_libre:
        "Los animales te rodean y escuchás de nuevo esa melodía, entonces te sentís muy mareado y te desmayás."

        "Soñás, pero en tus sueños ya no te persigue El Mandinga, aparece por un momento en tu sueño el viejo que sonríe satisfecho."

        if Vida_china:
            "Cuando despertás estás en una carreta junto al Tarta y a tu china."

            "Cuando, por la mañana no estabas, en tu casa ella fue a buscarte a la pulpería."
            
            "El Tarta le dijo que lo último que te había contado era sobre el viejo y fueron juntos a buscarte."
        else:
            "Cuando despertás estás en una carreta junto al Tarta."
            
            "Cuando no apareciste por la pulpería al día siguiente, El Tarta supuso que habías ido a ver qué había pasado con el viejo y te encontró tirado en el medio del talar inconsciente."

        "Volvés a tu casa y tu vida sigue prácticamente como si nada hubiera pasado."
        
        if Vida_china:
            "La china se quedó junto a vos, y lograron vivir una vida plena juntos"

        "Tu don ya no existe, pero tu deuda de alguna manera tampoco, ahora sos libre de las ataduras de El Mandinga."

        "Bien hecho, ya no eres un condenado."

        menu:
            "Volver al menú principal":
                return

    label Se_cobró_tu_deuda:
        "El Mandinga golpea el suelo con su pesado píe."

        if Vida_china:
            "Suelta la cabeza de la china, ella cae como desmayada en la cama."

        "Se abre una grieta en el suelo de tu casa, y él te hace un gesto como para que le des la mano."

        "En cuanto lo tocás ambos arden en llamas que no queman, sentís cómo algo se va de vos."

        "Es tu alma que es arrastrada por El Mandinga por las profundidades de los túneles que llevan a La Salamanca."

        "Has saldado tu deuda, El Mandinga te cobró al fin el alma."

        menu:
            "Volver al menú principal":
                return

    label Mantuviste_lejos_al_Mandinga:
        "No tenés más sueños con El Mandinga, pero la gente a tu alrededor cada vez se pone más agresiva cuando no tocás por un tiempo."

        "Hasta que un día te quedás dormido, un resfrío te dejó en cama y no tenés energías para ir a tocar, esa noche no vas a la pulpería."

        "Te despertás en medio de un incendio y escuchás a la muchedumbre abucheándote afuera."

        if Vida_china:
            "Ves a tu china acostada a tu lado. No se mueve. Debió morir recién, sin siquiera poder despertar; su cuerpo aún está caliente."

        "Lo último que llegás a escuchar antes de morir, por la asfixia del humo, son las cuerdas de tu guitarra saltar por el calor de las llamas y resonar una última vez."

        menu:
            "Volver al menú principal":
                return

    label Qué_cambiado_que_está_todo:
        "Volvés a tu pueblo, y la pulpería de El Tarta ya no existe, en su lugar hay un galpón de una firma extranjera."

        "Preguntás por ahí, y te dicen que ni bien te fuiste unos hombres de traje aparecieron y le pagaron mucha plata al Tarta para comprarle la pulpería."

        "Pero una semana después aparecieron los cuerpos sin vida de El Tarta, del Pibe que había estado tocando esa noche y su madre, La Flavia."

        "Algunas personas más también aparecieron muertas por esa época, toda gente que conocías."

        "Luego de eso volvés a la capital desanimado, pero no demasiado."

        "Tu vida sigue viviste unas décadas más sin sobresaltos hasta que tu cuerpo mortal no soportó más..."

        "... pero tu voz, esa voz por la que tanto hiciste, siguió siendo usada por la discográfica por muchos años más."

        menu:
            "Volver al menú principal":
                return

    label Ya_no_queda_nada:
        "Volvés a tu pueblo, pero ya no existe, en las calles hay algunos huesos humanos."

        "Solo queda la pulpería de El Tarta, medio destartalada. Entrás y te encontrás con El Mandinga en persona."

        "Te cuenta que cuando te fuiste, llegaron hasta las profundidades de La Salamanca unos señores de traje, a hacer un trato con él para liberarte a vos de su control."

        "A cambio de tu libertad acribillaron a todos en el pueblo."

        "A todos, al Tarta, a la madre del Farías, a los borrachos de la pulpería, a todos y cada uno de tus vecinos, todo para saldar para siempre la deuda que vos habías asumido."

        if Vida_china:
            "Por último te cuenta que cuando la china volvió al pueblo cayó en la desesperación en cuanto vio la matanza en el pueblo."

            "En ese momento aún los cadáveres estaban casi completos en las calles del pueblo."

            "Ella desesperada corrió hasta el rancho de su familia y encontró también sus restos pudriéndose, terminó quitandose la vida en la casa que la vio crecer."

        "La noticia te vuelve loco, perdiste completamente la humanidad, el propio Mandinga te extiende una soga y te señala una viga de la pulpería."

        menu:
            "Volver al menú principal":
                return