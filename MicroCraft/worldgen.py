#random library so everything can be randomised
import random

#change these to change the size of the world
worldsizex = 10
worldsizez = 10
worldsizey = 5

#grass thickness
grassheight = 1

#define the main function
def generateworld(worldname):
    name = worldname
#make a new directory for the world data
    os.mkdir('worlds/'+name)
#make the world dir.
    world = open('worlds/'+name+'/world.mcw', 'a')

#create a basic stone and grass world
#grass
    for y in range(grassheight):
        for x in range(worldsizex):
            for z in range(worldsizez):
                if not y > 0:
                    world.write('3')
                else:
                    world.write(1)
                if z < worldsizez-1:
                    world.write(',')
            if x < worldsizex-1:
                world.write(';')
#stone
    for y in range(worldsizey):
        for x in range(worldsizex):
            for z in range(worldsizez):
                world.write('2')
                if z < worldsizez-1:
                    world.write(',')
            if x < worldsizex-1:
                world.write(';')
        if y < worldsizey-1:
            world.write('\n')


#close world
    world.close()