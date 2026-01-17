label Capítulo_4_El_pobre_Pibe_Farías:
    $ reputacion_con_el_mandinga -= 35
    $ mostrar_repu()

    if Vida_china:
        show casaProtagonista at subir_centrada with Dissolve(1.0)
        "Llevás a la china a tu casa, se acuesta y la tapás con una gruesa frazada."
        
        "Le decís que no se preocupe, que vas a ver qué pasó."

        "Volvés sobre tus pasos y llegás al cadáver del pibe Farías."
        hide casaProtagonista
    
    show pibeColgado at subir_centrada, flash with Dissolve(1.0)
    play sound sfx_SonidoAmbienteTerror loop

    "Investigás el cadáver del joven que había estado tocando en la pulpería."

    "Parece que fue él mismo quien se quitó la vida, que se trepó al árbol, se puso la soga al cuello y saltó."

    "Encontrás debajo suyo un papelito, tiene una dirección anotada, parece de la capital."

    "Además dice “Colorada Dowley - Colony Records”, empezás a revisar por alrededor."

    hide pibeColgado
    show guitarraRota at subir_centrada with Dissolve(1.0)

    "Tirada un poco más adentro del campo está la guitarra del pibe destrozada."

    "Tiene otra nota escrita a mano enganchada entre las cuerdas:"

    "“Para Flavia, mi mamá”, dice el frente. La abrís y leés."

    "“Perdón, mamá, no voy a poder llevarte a la ciudad..."

    "... no soy tan buen cantor..."

    "... hace poco me ofrecieron grabar algo e iba a poder llevarte al hospital que necesitabas..."

    "... pero me echaron por no ser suficiente..."

    "... no fui ni buen cantor ni buen hijo..."

    "... lo siento mucho mamá.”"
    
    "Sabés perfectamente quién es Flavia: una vecina del pueblo, una señora grande y enferma."
    
    "Decidís llevar la nota vos mismo y la pasás por debajo de la puerta de La Flavia, y volvés a tu casa arrastrando los pies."

    jump La_peor_noche

    label La_peor_noche:
        hide guitarraRota
        show casaProtagonista at subir_centrada with Dissolve(1.0)

        "Llegás a tu casa desanimado."

        if Vida_china:
            "Cuando entrás a tu habitación la china ya se durmió."
            
            "Te acostás a su lado y te quedás dormido exhausto y preocupado."

        else:
            "Te metés, solo, en tu cama y te quedás dormido."

        "Empezás a soñar y ves la entrada a La Salamanca: cientos de alimañas salen por montones."

        hide casaProtagonista
        show demonios at subir_centrada with Dissolve(4.0)

        "Coronando la marcha, el chivo negro endemoniado."
        show chivo at subir_centrada with Dissolve(1.0)
        play fx sfx_respiracion_chivo 

        "Atrás de todo cerrando la comitiva, el basilisco que te guió por el laberinto."

        hide chivo

        "Las huestes avanzan por el camino que anduviste hasta tu pueblo."

        show casa at subir_centrada with Dissolve(1.0)

        "Ves que llegan hasta la casa de la familia de la joven china."

        "El chivo mata a su padre y las demás alimañas destrozan la casa y se comen a sus hermanos y su madre."

        if not Vida_china:
            "Por último la joven china que te había abierto la puerta."

            "Ella estuvo contemplando toda la masacre, sostenida por las grandes manos de El Mandinga."
            hide casa
            show mandingaPower at subir_centrada with Dissolve(1.0)
            "Una vez que toda su familia fue asesinada, ves al propio Mandinga se transforma en una bestia con unas descomunales fauces."
            
            "Se la traga lentamente y escuchás como poco a poco se van ahogando los gritos de la joven."
            hide mandingaPower

        hide demonios
        show naturalezaRota at subir_centrada with Dissolve(1.0)

        "Están cerca de tu pueblo..."
    
        "{size=70}{cps=10}\"—BIENVENIDO A MIS HUESTES, CONDENADO!\"{/cps}{/size}"

        "Resuena la voz de El Mandinga en tu sueño..."

        hide naturalezaRota
        show casaposeyendose at subir_centrada with Dissolve(0.2)
        "..."
        show casaPoseida at subir_centrada with Dissolve(0.3)
        hide casaposeyendose

        "Te despertás exaltado y lo ves, no era en tus sueños, es en persona..."
        
        jump Es_hora_de_rendir_cuentas

    label Es_hora_de_rendir_cuentas:
        hide casaposeyendose        
        show mandi at subir_centrada with Dissolve(5.0)
        play sound sfx_trueno

        "... el Mandinga está de pie junto a tu cama."
        
        if Vida_china:
            "Tiene una mano sobre la china."
        
        pause 0.01
        show mandinga_placeholder:
            xoffset 0
            yoffset 36

        Mandinga "No has hecho mucho por complacerme condenado."

        Mandinga "No te comportaste como alguien digno del don que te concedí."

        Mandinga "Vas a tener que elegir."

        Mandinga "Te dice, clara y fríamente, tus posibilidades:"

        hide mandinga_placeholder

        menu:
            "Entregás la vida de tu joven y atractiva china" if Vida_china and reputacion_con_el_mandinga > 50:
                jump La_muerte_de_la_china

            "Estás dispuesto a entregar la vida de los demás":
                jump La_Masacre_de_El_Mandinga
            
            "Entregás tu alma":
                jump Se_cobró_tu_deuda

    label La_muerte_de_la_china:
        "Ve en tu alma cuál es tu elección."

        hide mandi
        show mandingaPower at subir_centrada with Dissolve(1.0)

        "Con la mano que tenía sobre la cabeza de tu china, la levanta de un solo movimiento."

        play sound llantoChina

        "Sus gritos son ahogados por la gran palma de ese ser demoníaco, que cada vez es más grotesco, su cara se transforma y deja de ser la de un humano."

        "Su cabeza pasa a ser la de una bestia con un gran hocico y una mandíbula que se desencaja como la de una serpiente."

        hide mandingaPower
        show devoraChina at subir_centrada with Dissolve(1.0)

        "Mete en sus fauces a la muchacha que estuvo a tu lado hasta anoche."

        "Cuando dejás de escuchar sus gritos lo entendés."

        hide devoraChina
        show mandingaPower at subir_centrada with Dissolve(1.0)

        "No podés volver a pisar este pueblo."

        "Todos te vieron con ella anoche en la pulpería todos sabían que te molestaba que el Farías estuviera tocando ahí en TU lugar y ahora también está muerto."

        "El Mandinga se va sonriendo y te dice:"

        show mandinga_placeholder:
            xoffset 0
            yoffset 36

        play sound sfx_basilisco
        Mandinga "El don que te di te puede llevar lejos, pero recordá que cada hechizo cuenta."

        Mandinga "Mientras más personas hechices con tu canto más lejos me mantendré."

        hide mandinga_placeholder

        "Entonces se esfuma en una bola de humo y azufre."

        "Agarrás lo mínimo para sobrevivir en el camino, y empezás tu viaje..."

        hide mandingaPower

        jump El_viaje_eterno

    label La_Masacre_de_El_Mandinga:
        
        hide mandi
        show mandingaPower at subir_centrada with Dissolve(1.0)

        "El Mandinga, se transforma en una figura mucho más monstruosa, te toma por el cuello y de un salto atraviesa, con vos en sus manos, el techo de tu casa."

        "Desde ahí podés ver cómo sus alimañas invadieron tu pueblo, ves al basilisco, al chivo negro, a cientos de serpientes, arañas y murciélagos."
        hide mandinga_placeholder
        show huestesEnPueblo at subir_centrada with Dissolve(1.0)
        ###Acá poner una imagen de la matanza que está ocurriendo###
        "Todas esas bestias entran y salen de casas y locales matando a todos a su paso."

        "No se salva nadie: ves el cadáver del Tarta, ves a niños ser estrangulados por víboras, ves a ancianos ser pisoteados hasta la muerte por el chivo."

        if Vida_china:
            
            ### Acá estaría muy piola poner una imagen de algún tipo de arpía basada en la imagen de la china###
            "Empezás a llorar y ves como él baja nuevamente y sube con tu china. Le araña la espalda con una de sus filosas garras."
            hide huestesEnPueblo
            show arpiaChina at subir_centrada with Dissolve(1.0)
            "De la espalda de ella empiezan a salir unas plumas negras y marrones, y poco a poco ves cómo tu compañera se convierte en una especie de lechuza grotesca."

            "Sale volando y empieza a picotear los ojos de los cadáveres de la calle frente a tu casa."
            hide arpiaChina
        hide huestesEnPueblo
        jump Sucumbis_a_la_locura