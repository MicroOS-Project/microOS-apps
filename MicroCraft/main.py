os.chdir('/apps/MicroCraft/')
import worldgen
from game import playgame

selectedoption = 0

def selectworld():
    display.fill(320)
    worlds = os.listdir('/apps/MicroCraft/worlds/')
    print(worlds)
    worlds.append('New World')
    
    worldnum = 0

    for i in worlds:
        display.text(font, i, 4, 4+10*worldnum, st7789.WHITE, 320)
        worldnum += 1
        
    selectedworld = 0
    while True:
        time.sleep(0.15)
        display.rect(2, 3+10*selectedworld, 236, 10, 320)
        if xa.read() < minval:
            break
        if ya.read() < minval:
            selectedworld-=1
        if ya.read() > maxval:
            selectedworld+=1
        if selectedworld > worldnum-1:
            selectedworld = 0
        if selectedworld < 0:
            selectedworld = worldnum-1
            
        if btn.value() == 0:
            if worlds[selectedworld] == 'New World':
                name = keyboard()
                worldgen.generateworld(name)
                playgame(name)
                selectworld()
            else:
                playgame(worlds[selectedworld])
                selectworld()

        display.rect(2, 3+10*selectedworld, 236, 10, st7789.GREEN)

def options():
    print('options')

def redrawmainmenu():
    display.fill(320)
    #todo: make this a picture of the actual game

    display.text(fontlarge, 'MICROCRAFT', 40, 30, st7789.WHITE, 320)
    #todo: make font the minecraft font

    #buttons
    display.rect(30, 109, 190, 15, st7789.WHITE)
    display.rect(30, 139, 190, 15, st7789.WHITE)
    #text for buttons
    display.text(font, 'Start Game', 80, 112, st7789.WHITE, 320)
    display.text(font, 'Options', 90, 142, st7789.WHITE, 320)

    display.rect(30, 109+30*selectedoption, 190, 15, st7789.GREEN)

redrawmainmenu()

while True:
    display.rect(30, 109+30*selectedoption, 190, 15, st7789.WHITE)
    if xa.read() < minval:
        break
    
    if ya.read() < minval:
        selectedoption -= 1
        
    if ya.read() > maxval:
        selectedoption += 1
        
    if selectedoption > 1:
        selectedoption = 0

    if selectedoption < 0:
        selectedoption = 1

    if btn.value() == 0:
        if selectedoption == 0:
            selectworld()
            redrawmainmenu()
        if selectedoption == 1:
            options()
            redrawmainmenu()

    display.rect(30, 109+30*selectedoption, 190, 15, st7789.GREEN)
    time.sleep(0.15)
    
os.chdir('/')