label Capítulo_4_Colony_Records:
    hide mesa
    show casaProtagonista at subir_centrada with Dissolve(1.0)

    ###AUDIO - Crepitar de fuego###
    if Vida_china:
        "Vas a tu casa junto a tu china, le contás la gran noticia de la discográfica y ella te abraza, te felicita y te llena de besos. Incluso te incentiva a aceptarlo."

    else:
        "Vas a tu casa, contento por la propuesta, con una sonrisa de oreja a oreja."

    "Al llegar a tu casa te dormís rápidamente pensando en el futuro que te depara."

    "Pero tus sueños no son tan reparadores..."

    ###AUDIO    - frenar crepitar de fuego    -  sonido ambiente terror###

    "Empezás a soñar y ves la entrada a La Salamanca, cientos de alimañas salen por montones."
    hide casaProtagonista
    show chivo at subir_centrada with Dissolve(1.0)
    "Coronando la marcha, el chivo negro endemoniado."

    "Atrás de todo cerrando la comitiva, el basilisco que te guió por el laberinto."
    hide chivo
    show naturalezaRota at subir_centrada with Dissolve(1.0)
    "Las huestes avanzan por el camino que recorriste hasta tu pueblo."

    "Ves que llegan hasta la casa de la familia de la joven china."
    hide naturalezaRota
    show chivo at subir_centrada with Dissolve(1.0)

    ###AUDIO - respiración del chivo###
    "El chivo mata a su padre y las demás alimañas destrozan la casa y se comen a sus hermanos y su madre."

    if Vida_china:
        hide chivo
        show casaProtagonista at subir_centrada with Dissolve(1.0)
        ###AUDIO        - frenar sonido ambiente terror        - llanto###
        "Te despertás por la mañana y tu joven china está llorando acurrucada con una frazada, hecha un bollito en tu cama."

    else:
        "Por último la joven china que te había abierto la puerta."

        "Ella estuvo contemplando toda la masacre, sostenida por las grandes manos de El Mandinga."
        hide chivo
        show mandingaPower at subir_centrada with Dissolve(0.5)
        "Una vez que toda su familia fue asesinada, ves como el propio Mandinga se transforma en una bestia con unas descomunales fauces."
        hide mandingaPower
        show devoraChina at subir_centrada with Dissolve(0.5)
        "Se la traga lentamente y escuchás como poco a poco se van ahogando los gritos de la joven."
        hide devoraChina
        show casaProtagonista at subir_centrada with Dissolve(1.0)
        ###AUDIO        - frenar sonido ambiente terror        - crepitar de fuego        - respiración agitada###
        "Despertás por la mañana sobresaltado, sudando frío."
    ###AUDIO    - frenar respiración agitada    - sonido auto viejo###
    "Escuchás llegar un moderno auto, con todo su ruido, y un sonido que nunca habías escuchado, parecido a una trompeta o algo así."

    menu:
        "Decidís no salir: te vas a quedar a consolar a tu china" if Vida_china is True:
            jump Consolando_a_La_China

        "Salís a por tu prometedor futuro ":
            jump Una_revelación

    label Consolando_a_La_China:
        $ reputacion_con_el_mandinga -=20
        $ mostrar_repu()
        ###AUDIO auto viejo yendose###
        "Escuchás cómo, después de un rato el auto arranca de nuevo."
        ###AUDIO        - frenar llanto        - melodia prota (alguna)###
        "Te quedás con tu china hasta la tarde, tocando la guitarra, cantando para consolarla y ofreciéndole tu hombro para llorar."

        "No entendés muy bien cómo, pero vos sabés que ese sueño que tuviste fue real y ella de alguna manera también sabe lo que pasó con su familia."

        "El contrato no lo pudiste firmar, pero por la noche tenés otra oportunidad de demostrar tu don. Vas a la pulpería nuevamente."
        
        jump Culpable

    label Culpable:
        ###AUDIO        - frenar crepitar        - frenar melodia prota        - gente en la pulpería###
        hide casaProtagonista
        show pulperia at subir_centrada with Dissolve(1.0)
        "Llegás a la pulpería y, en cuanto atravesás la puerta todas las miradas van a vos."
        hide pulperia
        show pulperiaEnojados at subir_centrada with Dissolve(1.0)
        "Ya la gente no te mira con admiración como anoche, ahora te miran con desprecio y odio."

        ###AUDIO abucheo###
        "Empiezan a abuchearte; al principio no entendés por qué, hasta que logran ponerse de acuerdo y te gritan:"

        "—¡ASESINO! ¡ASESINO!"

        "Uno de los viejos grita sobre los demás:"

        "—Encontraron muerto al Pibe Farías el que anoche estaba ocupando tu lugar. ¡Fuiste vos [nombre_jugador]!."
        
        "—Siempre fuiste un desgraciado sin talento y envidioso."

        "Te echan la culpa de eso, todos creen que fuiste vos."

        menu:
            "Te disculpás con todos, les explicás que vos no fuiste.":
                jump Otra_noche_terrible

            "Tocás la guitarra para volver a encantarlos.":
                jump Esto_se_vuelve_costumbre

    label Otra_noche_terrible:
        $ reputacion_con_el_mandinga -=15
        $ mostrar_repu()
        ###AUDIO frenar gente en la pulpería, aumentar abucheo###
        "Nadie te cree, te insultan y te echan de la pulpería."

        "Te tiran con botellas vacías y te vas corriendo."
        hide pulperiaEnojados
        ###AUDIO - frenar abucheo      - botella rompiendose        - sonido de naturaleza nocturna###
        show puebloNoche at subir_centrada with Dissolve(1.0)
        "Justo cuando cerrás la puerta escuchás cómo una estalla contra la puerta: tardabas un minuto más en irte y te daba directo en la cabeza."

        "Volvés a tu casa, en el camino se hace de noche, llegás y a pesar de todo lográs dormir."

        hide puebloNoche
        show casaProtagonista at subir_centrada with Dissolve(1.0)
        ###AUDIO        - frenar todo        - cripitar de fuego###
        "Sí, otra vez esos sueños."
        hide casaProtagonista
        show casaposeyendose at subir_centrada with Dissolve(1.0)
        "Soñás con las alimañas, pero esta vez ya están entrando al pueblo, te despertás sobresaltado por un gran estruendo."
        ###AUDIO        - frenar crepitar fuego        - sonido ambiente terror ###
        "Abrís los ojos completamente agitado..."
        #hide casaposeyendose
        #show casaPoseida at subir_centrada with Dissolve(1.0)

        
        jump Es_hora_de_rendir_cuentas #esto está en "capitulo4_el_pibe.rpy"

    label Esto_se_vuelve_costumbre:
        hide pulperiaEnojados
        show pulperiaAplaudiendo at subir_centrada with Dissolve(1.0)
        ###AUDIO    -melodía prota (alguna)     -aplausos###
        "Tu canto logró el efecto que querías: todos están alabándote nuevamente."

        "Te vas a tu casa satisfecho."
        hide pulperiaAplaudiendo
        show casaProtagonista at subir_centrada with Dissolve(1.0)
        ###AUDIO    -frenar todo    -crepitar de fuego###
        if Vida_china:
            ###AUDIO    -melodia prota (alguna)###
            "Tocás la guitarra para tu china nuevamente y hasta ella se olvida de sus pesares y se lanza sobre tus brazos."
            
            "Te dormís con una sonrisa en la cara, contento de tenerla a tu lado."
            ###AUDIO    -frenar melodia###

        "Esta noche sorprendentemente no soñaste con las alimañas, ni con El Mandinga, ni ninguna de las grandes bestias de sus huestes."
        ###AUDIO    -frenar crepitar    -naturaleza día###
        hide casaProtagonista
        show pueblo at subir_centrada with Dissolve(1.0)
        "Por la mañana salís a la calle y todos te saludan alegremente, pero a medida que va cayendo el sol sus miradas se vuelven más acusatorias."
        hide pueblo
        ###AUDIO melodia prota (alguna)###
        show pulperia at subir_centrada with Dissolve(1.0)
        "Por la noche llegás a la pulpería y el ambiente es tenso, pero volvés a tocar la guitarra y todos se apaciguan."
        hide pulperia
        show pulperiaAplaudiendo at subir_centrada with Dissolve(1.0)
        "Este ritual se repite día tras día, vas todas las noches a tocar a la pulpería para calmarlos y por la mañana te tiran flores."
        hide pulperiaAplaudiendo
        ###AUDIO    -frenar naturaleza día###
        show pueblo at subir_centrada with Dissolve(1.0)
        "Un día te quedás un rato más en tu casa, no vas a tocar a la misma hora de siempre a la pulpería, pero terminás saliendo para allá."
        ###AUDIO    -abucheo###
        "La gente se agolpa en el camino para gritarte, incluso te tiran con cosas."

        "Tenés que guitarrear ahí nomás en el medio de la calle y todos se calman."

        "Esta vez zafaste, pero ¿qué pasará la próxima?"
        hide pueblo
        ###AUDIO    -frenar todo###
        menu:
            "Seguís pasando así los días.":
                jump Mantuviste_lejos_al_Mandinga

    label Una_revelación:
        ###AUDIO    - sonido auto viejo andando###
        show ventanaAuto at subir_centrada with Dissolve(1.0)
        "Salís y te subís al auto de la Colorada Dowley, al asiento trasero, junto a ella."

        "Te saluda animosamente y empiezan a recorrer las calles charlando de trivialidades."

        "Hasta que al fin sale el tema."

        show colorada_placeholder:
            xoffset 1636
            yoffset 36

        colorada "— Bueno [nombre_jugador], vamos a hablar sobre lo que podemos ofrecerte."

        colorada "— Sabemos perfectamente que esa habilidad no te pertenece, pero podemos hacer que sí sea así."

        colorada "— Nosotros tenemos un pacto con un ser superior a ese diablo local."

        colorada "— Podemos saldar tranquilamente tu deuda con él sin que pierdas ese gran don que te concedió."

        colorada "— Obviamente, a cambio, firmarías un contrato con nosotros que deberás cumplir."

        colorada "— Podrías dedicarte a tu música, al fin y al cabo, fue por eso que quisiste tener ese don, ¿no?"

        colorada "— Vas a poder tocar frente a cientos y miles de personas, encantarlos a todos."

        hide colorada_placeholder

        "Su discográfica pagará tu deuda con él, y podrás seguir con tu don, pero vas a tener que seguir sus reglas."

        "Te vas a poder dedicar a la música pero lejos de tu pueblo y bajo la supervisión de Colony Records."

        "—¿Qué decís? —te pregunta la Colorada Dowley."

        menu:
            "Aceptás el contrato":
                jump Las_giras_interminables

            "No aceptás el contrato":
                jump Adiós_a_la_colorada_y_a_Colony_Records

    label Adiós_a_la_colorada_y_a_Colony_Records:
        "En cuanto te negás la Colorada Dowley se lamenta, te lleva a tu casa y abandona el pueblo."
        hide ventanaAuto
        ###AUDIO    -frenar ruido auto vieja    -crepitar de fuego###
        show casaProtagonista at subir_centrada with Dissolve(1.0)

        "Esa tarde pasa, no te sentís muy animado, pero por la noche, hay otra oportunidad de mostrar tu don en la pulpería de El Tarta."

        jump Culpable

    label Las_giras_interminables:
        "La colorada vuelve a dejarte en tu casa para que prepares todo para irte."
        hide ventanaAuto
        show casaProtagonista at subir_centrada with Dissolve(1.0)
        ###AUDIO    -frenar ruido auto vieja    -crepitar de fuego###
        if Vida_china:
            "Le contás todo a la china e incluso te ponés a tocar la guitarra de la alegría, ella está muy contenta por vos."
            
            "Preparás todo, esa misma noche viene a buscarte la señora Dowley para llevarlos, a vos y a tu china, a la capital."

        else:
            "Preparás todo, esa misma noche viene a buscarte la señora Dowley para llevarte a la capital."
        hide casaProtagonista
        show teatro at subir_centrada with Dissolve(1.0)
        "El contrato se firmó el mismo día que llegaste y la colorada te prometió que nunca más ibas a tener que preocuparte por El Mandinga."

        "Los primeros años fueron excelentes para vos, grabaste muchas canciones, tocaste en lugares que nunca pensaste que ibas a tocar."

        if Vida_china:
            "Pero tu china no soportó la vida de ciudad, además vos te ibas varios meses y volvías muy poco a tu casa en la ciudad."

            "Dos años después de tu primer grabación la china te dejó, muy apenada por hacerlo, pero volvió al pueblo. Vos no la seguiste, estabas viviendo tu sueño."

        "Año tras año estuviste cumpliendo con cada trabajo que te encargaban, perdiste la cuenta de cuántas personas venías hechizando desde hace rato."

        "Las giras pronto se convirtieron en algo habitual, al igual que los excesos, que cada vez eran más. Eran giras y giras sin parar; de alguna manera, había que soportarlas."

        "Hasta que un verano te dieron un descanso, ya habían pasado veinte años desde la última vez que pisaste tu pueblo, así que decidís volver."
        hide teatro
        if reputacion_con_el_mandinga > 65:
            jump Qué_cambiado_que_está_todo
        else:
            jump Ya_no_queda_nada