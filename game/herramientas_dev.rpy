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
