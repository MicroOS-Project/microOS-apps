results = ''

while True:
    display.fill(0)
    display.fill_rect(10, 50, 220, 60, st7789.WHITE)
    display.rect(5, 5, 230, 40, st7789.WHITE)
    display.text(fontlarge, results, 30, 60, st7789.BLUE, st7789.WHITE)
    entered = numpad()
    try:
        results=str(eval(entered))
    except:
        results = 'ERROR'