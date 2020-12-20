while True:
    print("Light Level:" + input.light_level())
    if input.light_level() < 6:
        light.set_all(light.rgb(0,0,255))
    elif input.light_level() < 9:
        light.set_all(light.rgb(235,255,52))
    else:
        light.set_all(light.rgb(0,0,0))