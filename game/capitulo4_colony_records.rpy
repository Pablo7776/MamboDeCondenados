label Capítulo_4_Colony_Records:
    if Vida_china:
        "Vas a tu casa junto a tu china, le contás la gran noticia de la discográfica y ella te abraza, te felicita y te llena de besos. Incluso te incentiva a aceptarlo."

    else:
        "Vas a tu casa, contento por la propuesta, con una sonrisa de oreja a oreja."

    "Al llegar a tu casas te dormís rápidamente pensando en el futuro que te depara."

    "Pero tus sueños no son tan reparadores..."

    "Empezás a soñar y ves la entrada a La Salamanca, cientos de alimañas salen por montones."

    "Coronando la marcha, el chivo negro endemoniado."

    "Atrás de todo cerrando la comitiva, el basilisco que te guió por el laberinto."

    "Las huestes avanzan por el camino que andaste hasta tu pueblo."

    "Ves como llegan hasta la casa de la familia de la joven china."

    "El chivo mata a su padre y las demás alimañas destrozan la casa y se comen a sus hermanos y su madre."

    if Vida_china:
        "Te despertás por la mañana y tu joven china está llorando acurrucada con una frazada, hecha un bollito en tu cama."

    else:
        "Por último la joven china que te había abierto la puerta."

        "Ella estuvo contemplando toda la masacre, sostenida por las grandes manos de El Mandinga."

        "Una vez que toda su familia fue asesinada, ves como el propio Mandinga se transforma en una bestia con unas descomunales fauces."

        "Se la traga lentamente y escuchás como poco a poco se van ahogando los gritos de la joven."

        "Despertás por la mañana sobresaltado, sudando frío."

    "Escuchás como llega un moderno auto, con todo su ruido y un sonido que nunca habías escuchado, parecido a una trompeta o algo así."

    menu:
        "Decidís no salir, te vas a quedar a consolar a tu china" if Vida_china is true:
            jump Consolando_a_La_China

        "Salís a por tu prometedor futuro ":
            jump Una_revelación

    label Consolando_a_La_China:
        $ Reputacion_mandinga -=20

        "Escuchás como después de un rato el auto arranca denuevo."

        "Te quedás con tu china hasta la tarde, tocando la guitarra y cantando para consolarla y dándole tu hombro para llorar."

        "No entendés muy bien cómo, pero vos sabés que ese sueño que tuviste fue real y ella de alguna manera también sabe lo que pasó con su familia."

        "El contrato no lo pudiste firmar pero por la noche tenés otra oportunidad de demostrar tu don. Vas a la pulpería nuevamente."
        
        jump Culpable

    label Culpable:
        "Llegás a la pulpería y en cuanto atravezás la puerta todas las miradas van a vos."

        "Ya la gente no te mira con admiración como anoche, ahora te miran con desprecio y odio."

        "Empiezan a abuchearte, al principio no entendés porque hasta que logran ponerse de acuerdo y te gritan:"

        "- ¡ASESINO! ¡ASESINO!"

        "Uno de los viejos grita sobre los demás:"

        "- Encontraron muerto al Pibe Farías el que anoche estaba ocupando tu lugar. ¡Fuiste vos [nombre_jugador]!."
        
        "- Siempre fuiste un desgraciado sin talento y envidioso."

        "Te hechan la culpa de eso, todos creen que fuiste vos."

        menu:
            "Te disculpás con todos, les explicás que vos no fuiste.":
                jump Otra_noche_terrible

            "Tocás la guitarra para volver a encantarlos.":
                jump Esto_se_vuelve_costumbre

    label Otra_noche_terrible:
        #reputacion_con_el_mandinga -=15

        "Nadie te cree, te insultan y te echan de la pulpería."

        "Te tiran con botellas vacias y te vas corriendo."
        
        "Justo cuando cerrás la puerta escuchás como una estalla contra la puerta, tardabas en irte un minuto más e iba derecho a tu cabeza."

        "Volvés a tu casa, en el camino se hace de noche, llegás y a pesar de todo lográs dormir."

        "Sí, otra vez esos sueños."

        "Soñas con las alimañas pero esta vez ya están entrando el pueblo, te despertás sobresaltado por un gran estruendo."

        "Abrís los ojos completamente agitado..."

        jump Es_hora_de_rendir_cuentas #esto está en "capitulo4_el_pibe.rpy"

    label Esto_se_vuelve_costumbre:
        "Tu canto logró el efecto que querías, todos están aludandote nuevamente."

        "Te vas a tu casa satisfecho."
        
        if Vida_china:
            "Tocás la guitarra para tu china nuevamente y hasta ella se olvida de sus pesares y se lanza sobre tus brazos."
            
            "Te dormís con una sonrisa en la cara, contento de tenerla a tu lado."

        "Esta noche sorprendentemente no soñaste con las alimañas, ni con El Mandinga, ni ninguna de las grandes bestias de sus huestes."

        "Por la mañana salís a la calle y todos te saludan alegremente, pero a medida que va cayendo el sol sus miradas se vuelven más acusatorias."

        "Por la noche llegás a la pulpería y el ambiente es tenso, pero volvés a tocar la guitarra y todos se apaciguan."

        "Este ritual se repite día tras día, vas todas las noches a tocar a la pulpería para calmarlos y por la mañana te tiran flores."

        "Un día te quedás un rato más en tu casas, no vas a tocar a la misma hora de siempre a la pulpería, pero terminás saliendo para allá."

        "La gente se agolpa en el camino para gritarte, incluso te tiran con cosas."

        "Tenés que guitarrear ahí nomás en el medio de la calle y todos se calman."

        "Esta vez zafaste, pero ¿qué pasará la próxima?"

        menu:
            "Seguís pasando asi los días.":
                jump Mantuviste_lejos_al_Mandinga

    label Una_revelación:
        "Salís y te subís al auto de la Colorada Dowley, al asiento de atrás junto a ella."

        "Te saluda animosamente y empiezan a recorrer las calles charlando de trivialidades."

        "Hasta que al fín sale el tema."

        "- Bueno [nombre_jugador], vamos a hablar sobre lo que podemos ofrecerte."

        "- Sabemos perfectamente que esa habilidad no te pertenece, pero podemos hacer que sí sea así."

        "- Nosotros tenemos un pacto con un ser superior a ese diablo local."

        "- Podemos saldar tranquilamente tu deuda con él sin que pierdas eses gran don que te consedió."

        "- Obviamente a cambio fimarías un contrato con nosotros deberás seguir."

        "- Podrías dedicarte a tu música, al fin y al cabo, fue por eso que quiciste tener ese don ¿no?"

        "- Vas a poder tocar frente a cientos y miles de personas, encantarlos a todos."

        "Su discográfica pagará tu deuda con él, y podrás seguir con tu don, pero vas a tener que seguir sus reglas."

        "Te vas a poder dedicar a la música pero lejos de tu pueblo y bajo la supervisión de Colony Records."

        "- ¿Qué decís?, te pregunta la colorada Dowley"

        menu:
            "Aceptás el contrato":
                jump Las_giras_interminables

            "No aceptás el contrato":
                jump Adiós_a_la_colorada_y_a_Colony_Records

    label Adiós_a_la_colorada_y_a_Colony_Records:
        "En cuanto te negás la Colorada Dowley se lamente, te lleva a tu casa y abandona el pueblo."

        "Esa tarde pasa, no te sentís muy animado, pero por la noche, hay otra oportunidad de mostrar tu don en la pulpería de El Tarta."

        jump Culpable

    label Las_giras_interminables:
        "La colorada vuelve a dejarte en tu casa para que prepares todo para irte."

        if Vida_china:
            "Le contás todo a la china e incluso te ponés a tocar la guitarre de la alegría, ella está muy contenta por vos."
            
            "Preparás todo, esa misma noche viene a buscarte la señora Dowley para llevarlos, a vos ya tu china, a la capital."

        else:
            "Preparás todo, esa misma noche viene a buscarte la señora Dowley para llevarte a la capital."

        "El contrato se firmó el mismo día que llegaste y la colorada te prometió que nunca más ibas a tener que preocuparte por El Mandinga."

        "Los primeros años fueron excelentes para vos, grabaste muchas canciones, tocaste en lugares que nunca pensaste que ibas a tocar."

        if Vida_china:
            "Pero tu china no soportó la vida de ciudad, además vos te ibas varios meses y volvías muy poco a tu casa en la ciudad."

            "Dos años después de tu primer grabación la china te dejó, muy apenada por hacerlo, pero volvió al pueblo. Vos no la seguiste, estabas viviendo tu sueño."

        "Año tras año estuviste cumpliendo con cada trabajo que te encargaban, perdiste la cuenta de cuántas personas ibas hechizando hace rato."

        "Las giras pronto se convirtieron en algo habitual, al igual que los excesos, que cada vez eran más. eran giras y giras sin parar, de alguna manera había que soportalas."

        "Hasta que un verano te dieron un descanso, ya habían pasado veinte años desde la última vez que pisaste tu pueblo, asique decidís volver."

        if reputacion_con_el_mandinga > 65:
            jump Qué_cambiado_que_está_todo
        else:
            jump Ya_no_queda_nada