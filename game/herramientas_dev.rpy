# ---------------------------------------------------
# Variables globales
# ---------------------------------------------------
define DEV_LABELS = False
default current_label = ""
default _nombre_temp = ""  # SOLO UNA VEZ en todo el proyecto


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
            text "[current_label if current_label else '…'] \nreputación con el mandinga: [reputacion_con_el_mandinga]":
                style "dev_label_text"

style dev_label_text:
    color "#ffffff"
    size 60
    bold False
    outlines [(1, "#af0e0e", 1, 1)]

init python:
    if DEV_LABELS and "dev_label" not in config.overlay_screens:
        config.overlay_screens.append("dev_label")

    def on_label_jump(name, *args, **kwargs):
        store.current_label = name

    if DEV_LABELS:
        config.label_callback = on_label_jump


# ---------------------------------------------------
# Reputación
# ---------------------------------------------------

init python:
    def mostrar_repu():
        renpy.hide("reputacion1")
        renpy.hide("reputacion2")
        renpy.hide("reputacion3")
        renpy.hide("reputacion4")
        renpy.hide("reputacion5")

        if reputacion_con_el_mandinga > 99:
            renpy.show("reputacion5", at_list=[Position(xalign=0.9, yalign=0.9)])
        elif reputacion_con_el_mandinga > 74:
            renpy.show("reputacion4", at_list=[Position(xalign=0.9, yalign=0.9)])
        elif reputacion_con_el_mandinga > 49:
            renpy.show("reputacion3", at_list=[Position(xalign=0.9, yalign=0.9)])
        elif reputacion_con_el_mandinga > 24:
            renpy.show("reputacion2", at_list=[Position(xalign=0.9, yalign=0.9)])
        else:
            renpy.show("reputacion1", at_list=[Position(xalign=0.9, yalign=0.9)])
#**********************************
image bg base = Solid("#000")


init python:

    config.keymap['debug_menu'] = ['u']

    def clean_jump(label_name):

        renpy.scene()
        renpy.show("bg base")  # ← repone fondo negro

        renpy.music.stop()
        renpy.sound.stop()

        renpy.hide_screen("debug_jump_menu")
        renpy.jump(label_name)


screen key_listener():
    key "debug_menu" action Show("debug_jump_menu")


screen debug_jump_menu():

    tag menu   # bloquea interacción con el juego mientras está abierto

    frame:
        style "menu_frame"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 10

            text "Menú de Debug — Saltar a escena"

            textbutton "Ir a cap 1" action Function(clean_jump, "capitulo1")
            textbutton "Dar un paso hacia la oscuridad" action Function(clean_jump, "Dar_un_paso_hacia_la_oscuridad")
            textbutton "Escupir el crucifijo" action Function(clean_jump, "Escupir_el_crucifijo")
            textbutton "Ir a cap 2" action Function(clean_jump, "capitulo2")
            #textbutton "Ir a cap 3" action Function(clean_jump, "capitulo3")
            #textbutton "Capítulo 4 — El pobre Pibe Farías" action Function(clean_jump, "Capítulo_4_El_pobre_Pibe_Farías")
            #textbutton "Capítulo 4 — El viejo" action Function(clean_jump, "capitulo4_el_viejo")
            #textbutton "Capítulo 4 — Colony Records" action Function(clean_jump, "Capítulo_4_Colony_Records")

            null height 15

            textbutton "Cerrar" action Hide("debug_jump_menu")
