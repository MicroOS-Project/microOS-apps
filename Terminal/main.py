display.fill(0)
while True:
    typed=unubstructingkeyboard()
    if xa.read() >= maxval:
        break
    try:
        results=eval(typed)
        display.fill(0)
        display.text(font, results, 2, 20)
    except:
        display.fill(0)
        display.text(font, 'ERROR!', 2, 20)