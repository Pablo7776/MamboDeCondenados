label capitulo1:    

    # ESCENA 1.1

    # (SFX: galope de caballo)
    # (SFX: viento y estática)
    # (SFX: canto de pájaros)
    
    # SFX
    play SFX_1 sfx_GalopeCaballo loop fadein 1
    # play SFX_2 sfx_VientoYEstatica loop fadein 4 volume 0.3
    
    # BGM TEST
    # play BGM bgm_VidalaInicio loop fadein 1

    # ESCENA
    show gauchoACaballo at subir_centrada with black_transition

    $ mostrar_repu()

    "¡Vos! guitarrista y cantor venido a menos,"
    "que ahora vas al galope por el campo argentino, camino a La Salamanca."
    "Arrancaste este viaje hace unos días y ya estás llegando a tu destino."

    stop SFX_1 fadeout 3
    

    "El canto de los pájaros, 
    que hasta hace poco era alegre y armonioso, 
    ahora suena como gritos de dolor."
    
    hide gauchoACaballo
    
    # stop SFX_2 fadeout 3

    # ESCENA 1.2
    # (SFX:Sonido ambiental de terror que se intensifica)
    # (SFX: sigue el sonido del viento)
    # (SFX: el canto de los pájaros se convierte en graznidos y ululaciones)

    # SFX
    # play SFX_1 sfx_SonidoAmbienteTerror loop fadein 2.0 
    # play SFX_1 sfx_AmbientalTerror loop fadein 1.5
    play SFX_1 sfx_VientoYEstatica loop fadein 1.5 volume 0.5

    show salamanca at subir_centrada with Dissolve(3.0)
    

    "Aparece frente a vos esa piedra roja, de la que te habló aquel viejo, el que siempre está en la pulpería de tu pueblo."
    "Ese que te contó como en La Salamanca se puede hacer un pacto con el Mandinga para conseguir el don que uno quiera."
    "Atás y asegurás tu guitarra a la silla de tu fiel caballo, y luego pronunciás La Palabra, la que el viejo te confesó."
    ###(SFX: crujido de piedras arrastrándose)
    "Entonces, se abre una cueva en la roca; das un paso dentro, el caballo sale corriendo despavorido hacia el campo."
 
    ###(sfx: relincho con fade out)

    # Sale reproduciendo SFX_2 en loop
    jump Las_primeras_pruebas

    label Las_primeras_pruebas:
        # ESCENA 1.3

        # Callar sonido de viento y estatica
        stop SFX_2 fadeout 5

        hide salamanca

        $ aplicar_lpf("SFX_1",1500)

        show cueva at subir_centrada, desvanecer with Dissolve(2.0)
        
        # Nota: Esto aplica filtro pero esos canales no se estan reproduciendo
        # $ renpy.music.set_audio_filter("viento", lowpass_filtro_viento, replace=True)
        # $ renpy.music.set_audio_filter("estatica", lowpass_filtro_estatica, replace=True)
        
        "En el primer pasillo de este laberinto te sacás las botas, el sombrero y el pañuelo."
        "Así debe ser."
        "Ya sumido en la oscuridad sentís la presencia del basilisco."
        "Menos mal que no se ve nada; porque, si no, tu cuerpo ya sería piedra."
        ###(SFX: siseo grave)
        "Con su siseo, el basilisco te guía para atravesar este laberinto."
        
        # ESCENA 1.4
        ###(SFX: sonido de pisadas de insectos y siseos de serpientes)

        "Dejás atrás el laberinto y en un nuevo pasillo recto sentís que algo trepa tus pies descalzos, algo no, muchos pequeños pies. Son cientos, una marea de alimañas. Sentís el roce de algún reptil, una víbora quizás."
        "Sentís el cosquilleo de unas patas y unas pinzas, son alacranes que están subiendo por tus piernas."
        "..."
        "Pero te quedás tieso, sin moverte."
        "Sin temblequear."
        "Las alimañas siguen su camino sin hacerte daño."
        "El viejo te lo había dicho:"
        "“Cuando la patota de bichos se te acerque quedate tieso, no muevas ni un pelo y van a pasar embaladas sin darte bola”."

        
        hide cueva
        show placeholder_negro at subir_centrada with Dissolve(1.0)

        play SFX_2 sfx_respiracion_chivo loop
    
        "Entonces aparece ese animal grotesco del que te había contado el viejo: un chivo de pelo negro, ojos endemoniados y cuernos tan curvados como una espiral."
        
        hide placeholder_negro
        # show chivo at subir_centrada with Dissolve(1.0)
        show chivo_animado at subir_centrada, vibrar2, flash_repeat with Dissolve(1.0) 



        "Un chivo de pelo negro, inmenso, mucho más grande que cualquier bestia del campo."
        "Tiene los cuernos retorcidos como ramas secas."
        "Sus ojos amarillos que te miran con una inteligencia burlona."
        "Apesta a azufre y a sangre vieja."
        play SFX_2 sfx_respiracion_chivo 
        "Empezás a rodearlo. Te pegás a la pared de la cueva, aguantando la respiración."
        "El animal no se mueve. Te sigue con la mirada, quieto, como quien mira a una mosca."
        "Cuando por fin llegás al otro lado, el chivo se da vuelta, corre desaforado."
        ###(SFX: Trote de cabra)
        "Corre derecho hacia vos."
        "Te topeta y te tira a un profundo hoyo."
        ###(SFX: sonido de grito cayendo)

        stop SFX_2 fadeout 2.0

    jump La_caida

    label La_caida:
        
        # ESCENA 1.6
        hide chivo_animado
        show caida1 at subir_centrada with Dissolve(4.0)
        ###(SFX: Sonido de viento al caer)        
        "El hueco es profundo, más que profundo, estás cayendo al abismo."
        "Ves pasar lechuzas negras a tu lado, seguís cayendo y de repente te desmayás."
        
        hide caida1
        show cuevaFondo at subir_centrada with Dissolve(4.0)

        play SFX_2 sfx_Goteo loop fadein 1.0 volume 0.8
        # ESCENA 1.7
        
        "Despertás y estás en el fondo, ves sobre vos el abismo que sube en espirales de roca viva."
        "Te levantás y no podés ver nada delante tuyo, es sólo una profunda oscuridad."  
        label opciones17:
            $ hover_opcion = None
            $ opciones = [
                {"texto":"Trepás por el abismo para salir", "jump":"Trepar_por_el_abismo_para_salir", "nota":opcion_mala},
                {"texto":"Dás un paso hacia la oscuridad", "jump":"Dar_un_paso_hacia_la_oscuridad", "nota":opcion_neutral},
            ]

            call screen guitarra_choice(opciones)

            return            
    
    label Trepar_por_el_abismo_para_salir:
        
        # ESCENA 1.7A.1

        hide cuevaFondo
        show chivo_animado at subir_centrada,vibrar2, flash_repeat with Dissolve(1.0)

        play SFX_2 sfx_respiracion_chivo

        "Luego de mucho esfuerzo y luchar contra lechuzas que te atacaban débilmente lográs llegar hasta el borde del hoyo."
        "Estás de vuelta frente a aquel chivo endemoniado que te mira colérico."
        
        label opciones17A1:
            $ hover_opcion = None
            $ opciones = [
                {"texto":"Lo enfrentás", "jump":"Te_enfrentas_al_chivo", "nota":opcion_mala},
                {"texto":"Lo esquivás", "jump":"Intentas_esquivar_al_chivo", "nota":opcion_neutral},
            ]

            call screen guitarra_choice(opciones)

            return


        label Te_enfrentas_al_chivo:

            #ESCENA 1.7A.1a.1

            "El chivo corre hacia vos, lográs evitar el primer golpe y le pegás una patada."
            ###(SFX: Trote de cabra)
            "Se da vuelta y vuelve a intentar embestirte, de éste no pudiste zafar, caés al suelo y te defendes a las patadas y a las trompadas."
            "Pero el chivo es pesado y sus pezuñas son como hachas contra tu cuerpo."
            
            #ESCENA 1.7A.1a.2
            stop SFX_2 fadeout 1.0
            hide chivo_animado
            show muerte at subir_centrada with Dissolve(1.0)
            ###(SFX: Fade out del sonido ambiental de terror.)
            ###(SFX: pisotones contra un cráneo)
            "Tras unos cuantos minutos de pisotones tu cuerpo yace inerte en la oscuridad de la cueva."
            "Moriste, tu mambo ha terminado junto con tu vida."

            return
                

        label Intentas_esquivar_al_chivo:
            #ESCENA 1.7A.1b.1

            "Si antes pudiste pasar por al lado de él sin que se de cuenta ¿por qué no intentarlo nuevamente?"
            ###(SFX: Trote de cabra)
            "Das un paso y el chivo corre tan rápidamente hacia vos que no lográs evitarlo, te tira nuevamente por el hueco del que saliste." 
            "Caés y caés a lo profundo del abismo nuevamente."
            stop SFX_2 fadeout 1.0
            jump La_caida


    label Dar_un_paso_hacia_la_oscuridad:
        # ESCENA 1.7B.1
        
        $ quitar_filtros("SFX_1")
        stop SFX_1 fadeout 1.0
        stop SFX_2 fadeout 1.0

        hide cuevaFondo
        show trono at subir_centrada with Dissolve(1.0)
        
        play SFX_1 sfx_inicio_fuego

        play SFX_2 sfx_CrepitarFuego fadein 1 loop
        
        "Das el primer paso hacia la oscuridad."
        "A ambos lados, cien antorchas despiertan una tras otra, y la llamarada te ciega por un instante."
        ### Se podrá agregar un VFX de brillo intenso que luego se desvanece? Debería venir de una escena en negro y recién acá aparecer el trono. O agregar unas dos o tres imágenes de antorchas en primer plano, luego brillo y luego el trono.
        
        # play SFX_2 sfx_hoguera_pequena loop fadein 1.0  # Este sonido no funciona pq esta mal el formato , no debe ser WAV
        
        # play SFX_2 ruidoRosa loop fadein 1.0
        
        "Lográs ver la enorme sala con sus cortinas magníficas, su piso y sus columnas de mármol."
        "En el fondo el enorme trono, escondidas entre las columnas y detrás de él ves lechuzas, quirquinchos, perros, chanchos, culebras y sapos, también, hechiceros, brujas y diablillos."
        "Viniste a esto."
        
        label opciones17B1:
            $ hover_opcion = None
            $ opciones = [
                {"texto":"{image=hablando} ¡¿DÓNDE ESTÁ EL MANDINGA?!", "jump":"DÓNDE_ESTÁ_EL_MANDINGA", "nota":opcion_muymala},
                {"texto":"Esperás quieto y en silencio", "jump":"Esperar_en_silencio", "nota":opcion_neutral},
            ]

            call screen guitarra_choice(opciones)

            return

        
        label Esperar_en_silencio:
            # ESCENA 1.7B.1b.1
            
            hide trono
            # show mandi at subir_centrada, with Dissolve(5.0)
            show mandingaMiradaCuriosa at subir_centrada, with Dissolve(5.0)
   
            play SFX_2 sfx_trueno volume 0.5

            "Se desmorona una de las paredes que deja un gran agujero en uno de los costados de la sala."
            "Él atraviesa las cortinas, un enorme ser, mitad serpiente, mitad humano, ES EL MANDINGA."
            "Se sienta en su trono y te mira con un gesto curioso."
            
            # hide mandi
            # show mandi2 at subir_centrada,vibrar, with Dissolve(0.5)
            hide mandingaMiradaCuriosa
            show mandingaMiradaCuriosa at subir_centrada,vibrar, with Dissolve(0.5)
            
            play SFX_2 sfx_basilisco

            ### personaje ##########################
            pause 0.01
            # show mandinga_placeholder:
            #     xoffset 0
            #     yoffset 36

            Mandinga "¿Qué es lo que deseás de mí humano?"
            ###(SFX: siseo)

            # hide mandinga_placeholder
            pause 1.5 
            # show mandi2 at subir_centrada

            label opiones17B1b1:

                $ opciones = [
                    {"texto":"Te ponés a cantar tus desgracias", "jump":"Recular", "nota":opcion_mala},
                    {"texto":"{image=hablando} ¡Quiero hechizar a todo el mundo con mi canto!", "jump":"Quiero_hechizar", "nota":opcion_neutral},
                ]

                call screen guitarra_choice(opciones)

                return

        label DÓNDE_ESTÁ_EL_MANDINGA:
            
            # ESCENA 1.7B.1a.1
            hide trono
            show mandingaMiradaEnojada at subir_centrada, with Dissolve(5.0)
   
            $ reputacion_con_el_mandinga -= 10
            $ mostrar_repu()

            play sound sfx_trueno ### Volumen 1

            "Se abre un agujero en una de las paredes y él atraviesa las cortinas."
            "Un enorme ser, con pequeños cuernos, mitad serpiente, mitad humano."
            "ES EL MANDINGA." ###Aplicar VFX shake sobre el texto
            "Se sienta en su trono y te mira con un gesto severo y vehemente."
            
            hide mandingaMiradaEnojada
            show mandingaMiradaEnojada at subir_centrada,vibrar, with Dissolve(0.5)
            
            play SFX_2 sfx_basilisco

            ### personaje ##########################
            pause 0.01
            # show mandinga_placeholder at mostrar_izquierda


            Mandinga "¿Qué es lo que deseás de mí desgraciado?"
            
            # hide mandinga_placeholder

            pause 1.5 
            
            # show mandi2 at subir_centrada

            label opiones17B1a1:
                

                $ opciones = [
                    {"texto":"Te ponés a cantar tus desgracias", "jump":"Recular", "nota":opcion_mala},
                    {"texto":"{image=hablando} ¡Quiero hechizar a todo el mundo con mi canto!", "jump":"Quiero_hechizar", "nota":opcion_neutral},
                ]

                call screen guitarra_choice(opciones)

                return



            label Recular:
                # ESCENA 1.7B.2
                ###(Música: vidala de 0:46 volumen bajo)

                "Cuando intentás empezar a cantar no sale nada de tu garganta"

                ###(SFX:Risa grave y burlona del Mandinga, con fade out)
                ###(MÚSICA: la vidla empieza a subir de volumen)
                "El Mandinga se empieza a reír de vos"
                # show mandinga_placeholder at mostrar_izquierda
                ###(VFX: fundido a negro de mandi2 (o su reemplazo))
                # hide mandi2
                ###(SFX: bullicio de gente en la pulpería con fade in)
                Mandinga "Acá no se viene a eso cantorsucho de segunda"
                ###(SFX: el siseo del Mandinga)
                # hide mandinga_placeholder
                
                stop SFX_1 fadeout 1.0
                stop SFX_2 fadeout 1.0
                # Aca estaria bueno reveer el orden ya que no da lugar al fadeout
                play SFX_1 sfx_taberna loop fadein 1.0

                play BGM bgm_Vidala fadein 2.0
               
                show pulperia at subir_centrada with Dissolve(1.0)
                "Poco a poco vas recuperando la conciencia"
                "..."
                "Te despertás completamente borracho, con la cabeza sobre una mesa de la pulpería del Tarta."
                "Una guitarra suena; parece que eso te despertó."
                "Un vidalero empieza a contar una vieja leyenda de tus tierras: la leyenda de La Salamanca."
                
                hide pulperia

            return


label Quiero_hechizar:

    # ESCENA 1.7B.3
    # show protagonista_placeholder at mostrar_derecha

    
    Protagonista "¡Quiero hechizar a todos con mi canto!"
    
    # hide protagonista_placeholder
    hide mandingaMiradaEnojada
    hide mandingaMiradaCuriosa
    show mandingaMiradaCuriosa at subir_centrada,vibrar, with Dissolve(0.5)
    
    play sound sfx_basilisco

    pause 0.01
    # show mandinga_placeholder at mostrar_izquierda
    Mandinga "Me gusta tu pasión, pero ¿estás seguro?."
    Mandinga "Eso va a costarte caro."
    ###(SFX: siseo)

    # show protagonista_placeholder at mostrar_derecha  
    Protagonista "¿Cuál es el precio?"
        
    # hide protagonista_placeholder

    Mandinga "Tu alma." ###Resaltar en rojo el texto.
    ###(SFX: siseo)
    # hide mandinga_placeholder

    pause 1.5 
    # show mandi2 at subir_centrada
    
    label opciones17B3:
        $ hover_opcion = None
        $ opciones = [
            {"texto":"{image=hablando} Preferiría que mi alma siga siendo mía", "jump":"No_se_vende_el_alma", "nota":opcion_mala},
            {"texto":"{image=hablando} ¿A dónde hay que firmar?", "jump":"A_dónde_hay_que_firmar", "nota":opcion_neutral},
        ]
        call screen guitarra_choice(opciones)

        return

    
label No_se_vende_el_alma:
                # ESCENA 1.7B.4A.1
                ###(Música: vidala de 0:46 volumen bajo)
                ###(SFX:Risa grave y burlona del Mandinga, con fade out)
                ###(MÚSICA: la vidla empieza a subir de volumen)
                "El Mandinga se empieza a reír de vos"
                # show mandinga_placeholder at mostrar_izquierda
                ###(SFX: bullicio de gente en la pulpería con fade in)
                Mandinga "Que corajudo presentarme tu deseo y no estar dispuesto a darlo todo por este don sobrenatural ..."
                ###(SFX: el siseo del Mandinga)
                ###(VFX: fundido a negro de mandi2 (o su reemplazo))
                # hide mandi2
                # hide mandinga_placeholder
                "Las últimas palabras de El Mandinga suenan lejanas mientras tus  ojos se cierran lentamente"
                stop SFX_1 fadeout 1.0
                stop SFX_2 fadeout 1.0
                # Aca estaria bueno reveer el orden ya que no da lugar al fadeout
                play SFX_1 sfx_taberna loop fadein 1.0
               
                play BGM bgm_Vidala fadein 2
                show pulperia at subir_centrada with Dissolve(1.0)
                
                "Poco a poco vas recuperando la conciencia"
                "..."
                "Te despertás completamente borracho, con la cabeza sobre una mesa de la pulpería del Tarta."
                "Una guitarra suena; parece que eso te despertó."
                "Un vidalero empieza a contar una vieja leyenda de tus tierras: la leyenda de La Salamanca."
                
                hide pulperia
                return

label A_dónde_hay_que_firmar:
    # ESCENA 1.7B.4b.1
    "Aceptás vender tu alma."
    ###show mandinga_placeholder at mostrar_izquierda
    Mandinga "Perfecto, pero no terminamos todavía, hay unas pruebas que vas a tener que pasar."
    ###(SFX: siseo)
    ###hide mandinga_placeholder
    
    "El Mandinga hace un gesto con la mano y, ante vos, se abre el suelo."
    "Una gran grieta separa la sala al medio:"
    "De un lado estás vos; del otro, el Mandinga, su trono y sus seguidores."
    
    hide mandingaMiradaCuriosa
    hide mandingaMiradaEnojada

    # ESCENA 1.7B.5
    show cuchillo at subir_centrada,vibrar with Dissolve(1.0)
    
    "Él saca un enorme facón de su costado y lo revolea, queda sobre la fosa que se abrió en la tierra, formando un puente con el filo hacia arriba."

    pause 0.01
    
    play sound sfx_basilisco
    
    # show mandinga_placeholder at mostrar_izquierda


    Mandinga "Vení conmigo."
    
    # hide mandinga_placeholder

    "Abre los brazos como invitándote a su lado y luego señala el filo del cuchillo que acaba de calzar frente tuyo."

    label opciones17B5:
        $ hover_opcion = None
        $ opciones = [
            {"texto":"Pasás decididamente", "jump":"Pasar_decididamente", "nota":opcion_neutral},
            {"texto":"Pasás cautelosamente", "jump":"Pasar_cautelosamente", "nota":opcion_mala},
        ]
        call screen guitarra_choice(opciones)

        return

    label Pasar_decididamente:
        # ESCENA 1.7B.5A.1
        
        "Arrancás a caminar decidido sobre el filo del facón."
        "Paso tras paso, tus pies sangran, pero no sentís dolor."
        "Cuando llegás a la mitad ves una luz dorada bajo tus pies."
        
        # ESCENA 1.7B.5A.2

        "Mirás hacia abajo y hay un crucifijo sobre una luz que no sabés de dónde viene."
        pause 0.01
        #play SFX_2 sfx_basilisco
        # show mandinga_placeholder:
        #     xoffset 0
        #     yoffset 36
        Mandinga "—¡ESCUPILO!"
        # hide mandinga_placeholder
        
        label opciones17B5A2:
            $ hover_opcion = None
            $ opciones = [
                {"texto":"Escupís el crucifijo", "jump":"Escupir_el_crucifijo", "nota":opcion_neutral},
                {"texto":"{image=hablando} ¡Eso es una blasfemia!", "jump":"Pasar_cautelosamente", "nota":opcion_mala},
            ]
            call screen guitarra_choice(opciones)

        return
        

        label Pasar_cautelosamente:
            # ESCENA 1.7B.5B.1
            hide cuchillo
            show muerte at subir_centrada with Dissolve(1.0)
            
            "Das un paso sobre el cuchillo y dudás, el filo del facón se hunde en tu pie y no podés frenar el peso de tu cuerpo."
            "Empezás a caer sobre ese último paso, tu cuerpo se desbalancea y cae."
            play SFX_2 sfx_gritito_muerte
            "Yacés en dos mitades en lo profundo de la grieta del infierno."
            "Moriste, tu mambo ha terminado junto con tu vida."
            
            return

    label Escupir_el_crucifijo:
        # ESCENA 1.7B.5A.3
        hide cuchillo
        show demonios at subir_centrada, aparecer_flash with Dissolve(1.0)

        stop SFX_1 fadeout 1.0
        stop SFX_2 fadeout 1.0
        # El resto de los canales no se utiliza
        # stop sound fadeout 1.0
        # stop fx fadeout 1.0
        # stop audio fadeout 1.0
        # stop viento fadeout 1.0

        play SFX_1 sfx_viento1 volume 0.3
        play SFX_2 crucifijo
         
        "Escupís el crucifijo y seguís por el filo del facón, conseguís llegar al otro lado."
        "Una bruja te recibe con un pergamino abierto, un diablillo moja una pluma en la sangre de tus pies y te la da."
    
        ### Nombre del protagonista ###################################################
        $ nombre_jugador = renpy.input("¿Con qué nombre vas a firmar el contrato?") 
        $ nombre_jugador = nombre_jugador.strip()
        if nombre_jugador == "":
            $ nombre_jugador = "Protagonista"
        $ Protagonista = Character(nombre_jugador + ":", color="#D4AF37")
        
        play SFX_2 "audio/capitulo1/risaDiabolica.wav" #esto no va a funcionar pq es WAV

        pause 0.01
        # show protagonista_placeholder at mostrar_derecha
        
        Protagonista "Mi nombre es [nombre_jugador] y te vendo mi alma, Mandinga."
        
        # hide protagonista_placeholder
        stop SFX_2 fadeout 1.0
        jump Lo_lograste
            
    label Lo_lograste:
        # ESCENA 1.7B.5A.4
        pause 0.01
        play SFX_2 sfx_basilisco
        
        # show mandinga_placeholder at mostrar_izquierda

        Mandinga "{size=70}{cps=10}—BIENVENIDO A MIS HUESTES, CONDENADO!{/cps}{/size}"

        # hide mandinga_placeholder
        # play BGM musica_piedra_y_camino
        play BGM bgm_Zamba

        "Las brujas, los brujos y los diablillos arrancan la fiesta a tu alrededor, sentís como tu garganta arde y después se calma, entonces empezás a cantar junto a los demás."
        "Las alimañas te levantan sobre sus lomos y te pasean por toda la sala, tu voz y tu canto ahora suenan como nunca antes sonaron."
        
        hide demonios ###(VFX: fundido a negro lento que no se pueda pasar)
        show rancho at subir_centrada with Dissolve(3.0)
        jump En_un_rancho_cercano

    label En_un_rancho_cercano:
        # ESCENA 1.7B.5A.5
        stop SFX_1 fadeout 1.0
        stop SFX_2 fadeout 1.0

        "A pocos kilómetros una señora se despierta asustada por el alboroto y empieza a rezar..."
        
        Señora "¡Dios nos salve, que hoy hay baile en La Salamanca!"
        
        hide rancho with Dissolve(5.0)

        label opciones17B5A5:
            $ hover_opcion = None
            $ opciones = [
                {"texto":"Al segundo capítulo", "jump":"capitulo2", "nota":opcion_transicion_capitulo},
            ]
            call screen guitarra_choice(opciones)

