define af = renpy.audio.filter

define lowpass_filtro_viento = af.Lowpass(400.0)
define lowpass_filtro_estatica = af.Lowpass(400.0)

init python:
    # Canales de sonido y ambiente
    renpy.music.register_channel("viento", "sfx", False)
    renpy.music.register_channel("estatica", "sfx", False)
    renpy.music.register_channel("acufeno", "sfx", False)

    
    
    # Canales de audio
    renpy.music.register_channel("ambiente", "sfx", False)
    renpy.music.register_channel("fx", "sfx", False)
    renpy.music.register_channel("pisadas", "sfx", False)


