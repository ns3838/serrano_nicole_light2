while (true) {
    console.log("Light Level:" + input.lightLevel())
    if (input.lightLevel() < 20) {
        light.setAll(light.rgb(235, 255, 52))
    } else if (input.lightLevel() < 100) {
        light.setAll(light.rgb(0, 0, 255))
    } else {
        light.setAll(light.rgb(0, 0, 0))
    }
    
}
