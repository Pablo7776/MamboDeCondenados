define DEV_LABELS = True

default current_label = ""

screen dev_label():
    if DEV_LABELS:
        frame:
            xalign 1.0
            yalign 0.0
            xoffset -10
            yoffset 10
            background "#0008"
            padding (6, 6)

            # Muestra lo que tenga current_label
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

    # Esta función se ejecuta automáticamente cada vez que Ren'Py entra a un label
    def on_label_jump(name, *args, **kwargs):
        store.current_label = name   # <<--- actualiza el texto

    if DEV_LABELS:
        config.label_callback = on_label_jump
