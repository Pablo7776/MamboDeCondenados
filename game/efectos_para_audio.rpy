

# Efectos de sonido:

define af = renpy.audio.filter
define lowpass_filtro_viento = af.Lowpass(400.0)
define lowpass_filtro_estatica = af.Lowpass(400.0)



init python:
    

    # Funcion para aplicar LPF
    def aplicar_lpf(channel,value=400.0,duration=1,replace=True):
        # Valor del LowPassFilter
        lpf = renpy.audio.filter.Lowpass(400.0)
        renpy.music.set_audio_filter(channel, lpf, replace=replace, duration=duration)

    def aplicar_hpf(channel,value=400.0,duration=1,replace=True):
        # Valor del LowPassFilter
        lpf = renpy.audio.filter.Highpass(100.0)
        renpy.music.set_audio_filter(channel, lpf, replace=replace, duration=duration)




    # Funcion para limpiar filtros
    def quitar_filtros(channel,duration=1):
        renpy.music.set_audio_filter(channel, None, replace=True, duration=duration)


init python:
    def panear(pan,channel,delay=1):
    # valores de paneo 1 left, 0 center, -1 right
        renpy.music.set_pan(pan, delay, channel)

    def panear_izquierda(channel,delay=1):
        renpy.music.set_pan(1, delay, channel)

    def panear_derecha(channel,delay=1):
        renpy.music.set_pan(-1, delay, channel)

    def paneo_circular(channel):
        """Panea el canal hacia un lado y luego al otro varias veces.
        Args:
            channel: nombre del canal (str) o objeto canal.
            vueltas (int, optional): número de idas y vueltas. Default 2.
            side_duration (float, optional): segundos para cada paneo lateral.
            center_duration (float, optional): segundos para volver al centro al final.
        """
        # Valores por defecto.
        vueltas = 2
        side_duration = 4.0
        center_duration = 2.0

        for _ in range(vueltas):
            renpy.music.set_pan(-1, side_duration, channel)
            renpy.pause(side_duration)
            renpy.music.set_pan(1, side_duration, channel)
            renpy.pause(side_duration)

        # Volver al centro al terminar
        renpy.music.set_pan(0, center_duration, channel)
        

init python:
    # Pausar y despausar canales
    def pause_on(canal=""):
        renpy.music.set_pause(True, canal)

    def pause_off(channel=""):
        renpy.music.set_pause(False, canal)

init python:
    # Ducking de canales
    def volumen_bajar(canal="",volume=0.5,delay=0.5):
        renpy.music.set_volume(volume, delay, canal)

    def volumen_normalizar(canal="",volume=1.0,delay=0.5):
        renpy.music.set_volume(volume, delay, canal)


default preferences.volume.voice = 0.5


# Registro de canales:
init python:
    # Canales de sonido y ambiente
    renpy.music.register_channel("viento", "sfx", False)
    renpy.music.register_channel("estatica", "sfx", False)
    renpy.music.register_channel("acufeno", "sfx", False)
    
    # Canales de audio
    renpy.music.register_channel("ambiente", "sfx", False)
    renpy.music.register_channel("fx", "sfx", False)
    renpy.music.register_channel("pisadas", "sfx", False)

    

    renpy.music.register_channel(
        name="MMM", #(MainMenuMusic)
        mixer="music",
        loop=True,
        tight=True,
        file_prefix="",
        file_suffix="",
        stop_on_mute=False,
        buffer_queue=True,
        movie=False,
        framedrop=False
    )
    renpy.music.register_channel(
        name="BGM", #(BackGroundMusic)
        mixer="music",
        loop=True,
        tight=True,
        file_prefix="",
        file_suffix="",
        stop_on_mute=False,
        buffer_queue=True,
        movie=False,
        framedrop=False
    )
    renpy.music.register_channel(
        name="SFX_1", #(SFX 1)
        mixer="sfx",
        loop=False,
        tight=False,
        file_prefix="",
        file_suffix="",
        stop_on_mute=True,
        buffer_queue=True,
        movie=False,
        framedrop=False
    )
    renpy.music.register_channel(
        name="SFX_2", #(SFX 2)
        mixer="sfx",
        loop=False,
        tight=False,
        file_prefix="",
        file_suffix="",
        stop_on_mute=True,
        buffer_queue=True,
        movie=False,
        framedrop=False
    )
    renpy.music.register_channel(
        name="UI_1", #(Sonidos de UI)
        mixer="voice",
        loop=False,
        tight=False,
        file_prefix="",
        file_suffix="",
        stop_on_mute=True,
        buffer_queue=True,
        movie=False,
        framedrop=False
    )