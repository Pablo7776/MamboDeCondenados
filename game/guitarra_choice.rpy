# ---------------------------------
# VARIABLES DE CONTROL
# ---------------------------------

default hover_opcion = None

# ---------------------------------
# ANIMACIONES DE CUERDAS
# ---------------------------------

image cuerda1_anim:
    "gui/Elecciones_guitarra/Mastil_fijo.png"
    0.1
    "gui/Elecciones_guitarra/Cuerda1/OndaB1.png"
    0.1
    "gui/Elecciones_guitarra/Cuerda1/OndaS1.png"
    0.1
    repeat

image cuerda2_anim:
    "gui/Elecciones_guitarra/Mastil_fijo.png"
    0.1
    "gui/Elecciones_guitarra/Cuerda2/OndaB2.png"
    0.1
    "gui/Elecciones_guitarra/Cuerda2/OndaS2.png"
    0.1
    repeat

image cuerda3_anim:
    "gui/Elecciones_guitarra/Mastil_fijo.png"
    0.1
    "gui/Elecciones_guitarra/Cuerda3/OndaB3.png"
    0.1
    "gui/Elecciones_guitarra/Cuerda3/OndaS3.png"
    0.1
    repeat

image cuerda4_anim:
    "gui/Elecciones_guitarra/Mastil_fijo.png"
    0.1
    "gui/Elecciones_guitarra/Cuerda4/OndaB4.png"
    0.1
    "gui/Elecciones_guitarra/Cuerda4/OndaS4.png"
    0.1
    repeat

image cuerda5_anim:
    "gui/Elecciones_guitarra/Mastil_fijo.png"
    0.1
    "gui/Elecciones_guitarra/Cuerda5/OndaB5.png"
    0.1
    "gui/Elecciones_guitarra/Cuerda5/OndaS5.png"
    0.1
    repeat

image cuerda6_anim:
    "gui/Elecciones_guitarra/Mastil_fijo.png"
    0.1
    "gui/Elecciones_guitarra/Cuerda6/OndaB6.png"
    0.1
    "gui/Elecciones_guitarra/Cuerda6/OndaS6.png"
    0.1
    repeat

init python:

    def tocar_nota(nota):
        renpy.sound.play(nota, channel="fx")

screen guitarra_choice(opciones):

    add "gui/Elecciones_guitarra/Mastil_fijo.png"

    if hover_opcion == 0:
        add "cuerda1_anim"
    elif hover_opcion == 1:
        add "cuerda2_anim"
    elif hover_opcion == 2:
        add "cuerda3_anim"
    elif hover_opcion == 3:
        add "cuerda4_anim"

    vbox:
        xalign 0.5
        yalign 0.1
        spacing 14

        for i, opcion in enumerate(opciones):

            textbutton opcion["texto"]:

                xsize 920
                padding (14, 10)

                xalign 0.5
                text_xalign 0.5
                text_text_align 0.5

                background Solid("#000000a6")

                hovered [
                    SetVariable("hover_opcion", i),
                    Function(tocar_nota, opcion["nota"])
                ]

                unhovered SetVariable("hover_opcion", None)

                action Jump(opcion["jump"])

