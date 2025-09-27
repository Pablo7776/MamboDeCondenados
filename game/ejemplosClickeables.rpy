screen clickeable():
    imagebutton:
        idle "images/cuadrado.png"
        hover "images/cuadrado2.png"
        action [Hide("clickeable"), Jump("start")]  # oculta la pantalla al hacer click
        xalign 0.5
        yalign 0.28
        xsize 200  # ancho exacto de la imagen
        ysize 200  # alto exacto de la imagen


label ejemplosClickeables:
    show screen clickeable
    "Hacé click en la imagen para volver."
    $ renpy.pause(hard=True)

