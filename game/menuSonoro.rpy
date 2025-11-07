label menuSonoro:  
    show screen ejemplo_hover  
    "hola"
    

screen ejemplo_hover():
    imagebutton:
        idle "placeholders/personajes/ppp.jpg"
        hover "placeholders/personajes/prota.jpg"
        #hover_sound "audio/capitulo1/sfx_galope.ogg"
        hovered Play("music", "audio/capitulo1/sfx_galope.ogg")
        unhovered Stop("music")
        action NullAction()  # no hace nada al click, solo ejemplo
