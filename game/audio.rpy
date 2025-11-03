define af = renpy.audio.filter
# Crear filtro de paso bajo (no aplicarlo todavía)
define lowpass_filtro_viento = af.Lowpass(300.0)
define lowpass_filtro_estatica = af.Lowpass(300.0)

init python:
    # Canales de sonido y ambiente
    renpy.music.register_channel("viento", "sfx", True)
    renpy.music.register_channel("estatica", "sfx", True)
    renpy.music.register_channel("acufeno", "sfx", False)

    
    
    # Canales de audio
    renpy.music.register_channel("ambiente", "sfx", True)
    renpy.music.register_channel("fx", "sfx", False)
    renpy.music.register_channel("pisadas", "sfx", True)


