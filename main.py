while True:
    print("Light Level:" + input.light_level())
    if input.light_level() < 20:
        light.set_all(light.rgb(235,255,52))
    elif input.light_level() < 100:
        light.set_all(light.rgb(0,0,255))
    else:
        light.set_all(light.rgb(0,0,0))