def render(blocks, bs=24):
    display.fill(0)
    colors=[0, 0, 290, 320, 299552, 12, 3430008]
    row=0
    collum=0
    for i in blocks:
        row=0
        for n in i:
            color=colors[n]
            display.fill_rect(collum*bs, row*bs, bs, bs, color)
            row+=1
        collum+=1