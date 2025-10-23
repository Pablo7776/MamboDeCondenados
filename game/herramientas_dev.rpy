# ---------------------------------------------------
# Variables globales
# ---------------------------------------------------
define DEV_LABELS = True
default current_label = ""
default _nombre_temp = ""  # SOLO UNA VEZ en todo el proyecto

#default nombre_jugador = "Protagonista"  # nombre final del jugador

# ---------------------------------------------------
# Dev label
# ---------------------------------------------------
screen dev_label():
    if DEV_LABELS:
        frame:
            xalign 1.0
            yalign 0.0
            xoffset -10
            yoffset 10
            background "#0008"
            padding (6, 6)
            text "[current_label if current_label else '…'] \nreputación con el mandinga: [reputacion_con_el_mandinga] \nhumanidad: [humanidad]":
                style "dev_label_text"

style dev_label_text:
    color "#ffffff"
    size 40
    bold True
    outlines [(2, "#000000", 0, 0)]

init python:
    if DEV_LABELS and "dev_label" not in config.overlay_screens:
        config.overlay_screens.append("dev_label")

    def on_label_jump(name, *args, **kwargs):
        store.current_label = name

    if DEV_LABELS:
        config.label_callback = on_label_jump

    # Canales de audio
    renpy.music.register_channel("ambiente", "sfx", True)
    renpy.music.register_channel("fx", "sfx", False)
    renpy.music.register_channel("pisadas", "sfx", True)

# ---------------------------------------------------
# Estilo botón pergamino
# ---------------------------------------------------
style pergamino_boton is default:
    background "#d9b77a"
    hover_background "#f5d58a"
    padding (20, 10)
    xalign 0.5
    yalign 0.5
    size 35
    color "#000000"

# ---------------------------------------------------
# Screen input
# ---------------------------------------------------
# Screen input
screen pergamino_input_simple(prompt):
    default input_text = ""  # variable local al screen

    frame:
        xalign 0.5
        yalign 0.5
        background "#f5f1e0"
        padding (20, 20)

        vbox:
            spacing 20
            text prompt size 40 color "#4b2e05" xalign 0.5

            input:
                value input_text
                length 20
                pixel_width 400
                color "#2b1a00"
                size 40

            textbutton "Firmar" style "pergamino_boton" action Return(input_text)
