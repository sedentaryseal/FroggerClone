# ----- Frogger Clone -----

# author: sedentaryseal

# ----- Importing any modules -----

import pygame
from pygame.locals import *
from pygame.locals import KEYDOWN
import time
from pygame.sprite import Sprite
import sys

width, height = 840, 600

water = pygame.image.load("assets/water.png")
grass = pygame.image.load("assets/grass.png")
road = pygame.image.load("assets/road.png")

startPos = [0,0] # holds position of frog, represents an 15x11 grid
frogPos = [0,0]
livesPos = 10 # Holds the y value of the players lives

# ----- Sprite Classes -----

class Frog(pygame.sprite.Sprite):  # represents the main Frog class
    """
    Class for the main sprite, the frog.
    """
    
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load("assets/frog.png")
        self.d = 50 # Distance the frog can move per keypress
        self.x = 15 # Starting position of the frog
        self.y = 15
        self.attachedTo = None
        self.rect = self.image.get_rect()
        self.next_update_time = 0
        self.hitBy = None
        self.beenHit = False

    def get_rect(self):
        r = self.get_rect()
        
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def attach(self, object):
        # If the frog meets a log, log class passed into here
        self.attachedTo = object

    def hit(self, object):
        self.hitBy = object
        self.beenHit = True

    def dead(self):
        self.image = pygame.image.load("assets/frog-dead.png")

    def alive(self):
        self.image = pygame.image.load("assets/frog.png")
        self.x = 15
        self.y = 15
        startPos = [0,0]

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def update(self, current_time, bottom):
        if self.next_update_time < current_time:
            if self.attachedTo != None:
                if self.attachedTo == boxes[0]:
                    self.y += 4
                    if self.y > 600:
                        print "Frog Died"
                        sys.exit()
                    # print self.attachedTo
                if self.attachedTo == boxes[2]:
                    self.y -= 2
                    if self.y < 0:
                        print "Frog Died"
                        sys.exit()
                if self.attachedTo == boxes[10]:
                    self.y += 4
                    if self.y > 600:
                        print "Frog Died"
                        sys.exit()
                if self.attachedTo == boxes[9]:
                    self.y -= 2
                    if self.y < 0:
                        print "Frog Died"
                        sys.exit()
                if self.attachedTo == boxes[8]:
                    self.y -= 2
                    if self.y < 0:
                        print "Frog Died"
                        sys.exit()
                if self.attachedTo == boxes[3]:
                    self.y -= 2
                    if self.y < 0:
                        print "Frog Died"
                        sys.exit()
                if self.attachedTo == boxes[1]:
                    self.y += 4
                    if self.y > 600:
                        print "Frog Died"
                        sys.exit()
            if self.beenHit == True:
                print "Frog has been run over"
                sys.exit() 
            self.next_update_time = current_time + 10

class LogBig(pygame.sprite.Sprite):
    """
    Class for the biggest log
    """
    image = None;
    def __init__(self, initialPosition):
        Sprite.__init__(self)
        self.image = pygame.image.load("assets/log-3.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = initialPosition
        self.going_down = False
        self.next_update_time = 0
        self.attached = False
        self.x = 0
        self.y = 0

    def update(self, current_time, bottom):
        if self.next_update_time < current_time:
            if not self.going_down:
                self.rect.top -= 2
            if self.rect.top < -200:
                self.rect.bottom = 750
            self.next_update_time = current_time + 10

    def attach(self):
        self.attached = True

    def getx(self):
        return self.x

    def gety(self):
        return self.y

class LogMed(pygame.sprite.Sprite):
    """
    Class for the medium sized log
    """
    image = None;
    def __init__(self, initialPosition):
        Sprite.__init__(self)
        self.image = pygame.image.load("assets/log-2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = initialPosition
        self.going_down = True
        self.next_update_time = 0
        self.attached = False
        self.x = 1
        self.y = 1 
    
    def update(self, current_time, bottom):
        if self.next_update_time < current_time:
            if self.going_down:
                self.rect.top += 4
            if self.rect.bottom > 750:
                self.rect.top = -125
            self.next_update_time = current_time + 10

    def attach(self):
        self.attached = True

    def getx(self):
        return self.x

    def gety(self):
        return self.y

class Car(pygame.sprite.Sprite):
    """
    Class for the car which goes up the right side of the road
    Four instances of the Car class are created
    """
    image = None;
    def __init__(self, initialPosition):
        Sprite.__init__(self)
        self.image = pygame.image.load("assets/car-4.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = initialPosition
        self.going_down = False
        self.next_update_time = 0
        self.x = 0
        self.y = 0
        
    def update(self, current_time, bottom):
        if self.next_update_time < current_time:
            if not self.going_down:
                self.rect.top -= 2
            if self.rect.top < -50:
                self.rect.bottom = 650
            self.next_update_time = current_time + 10

    def getx(self):
        return self.x

    def gety(self):
        return self.y

class Lorry(pygame.sprite.Sprite):
    """
    Class for the lorry which goes down the left side of the road
    Two instances of the lorry class are created
    """
    image = None;
    def __init__(self, initialPosition):
        Sprite.__init__(self)
        self.image = pygame.image.load("assets/car-5.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = initialPosition
        self.going_down = True
        self.next_update_time = 0
        self.x = 0
        self.y = 0

    def update(self, current_time, bottom):
        if self.next_update_time < current_time:
            if self.going_down:
                self.rect.top += 4
            if self.rect.bottom > 650:
                self.rect.top = -50
            self.next_update_time = current_time + 10

    def getx(self):
        return self.x

    def gety(self):
        return self.y

class Lives(pygame.sprite.Sprite):
    """
    Class for how many lives the player has
    (displayed on the upper right of the screen)
    """
    image = None;
    def __init__(self, initialPosition):
        Sprite.__init__(self)
        self.image = pygame.image.load("assets/frog.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = initialPosition
        self.next_update_time = 0
        self.livesPos = 10
        self.lives = 3
        self.x = 0
        self.y = 0

    def update(self, current_time, bottom):
        if self.next_update_time < current_time:
            self.next_update_time = current_time + 10

    def kill(self):
        self.lives -= 1

def startP(y): # NEEDS REFINING: so that frog jumps to closest square, not just highest y value
    # All the y positions the frog can be within, steps of +50
    yPos = [[0,15],[1,65],[2,115],[3,165],[4,215],[5,265],[6,315],[7,365],[8,415],[9,465],[10,515],[11,565]]
    # Loop to find the closest index value so the frog isn't moved off the grid
    for i in yPos:
        if i[1] > y:
            sp = i
            break
    addOn = sp[1] - y
    return addOn

def takeLife(frog):
    # Takes a life off the frog and sets up environment again
    del livesN[-1] # Life is deleted
    frog.dead()
    Frog.remove(frog)
    startPos[0] = 0 # Resetting startPos[][]
    startPos[1] = 0
    frog.alive() # Creating a bird at the start position

def collisions(direction, sprite):
    # yPositions holds possibls y coordinates of the frog, it can only move in increments of +-50
    frog = sprite
    noLives = len(livesN)
    if noLives == 0:
        print "Game Over"
        sys.exit()
    yPositions = [[0,15],[1,65],[2,115],[3,165],[4,215],[5,265],[6,315],[7,365],[8,415],[9,465],[10,515],[11,565]]
    if direction == 3: # RIGHT
        if startPos[0] == 1:
            y = frog.gety()
            collided = boxes[0].rect.collidepoint(65,y) # boxes[0] is the first log
            if collided == 1:
                # Collision with first log detected, need to attach
                boxes[0].attach()
                frog.attach(boxes[0])
            if collided != 1:
                # No collision, frog is in the water
                takeLife(frog)
        elif startPos[0] == 2:
            frog.attach(None)
            y = frog.gety()
            for i in yPositions: # Updating startPos y value after log ride (removes boundary bugs)
                if i[1] > y:
                    newStartPos = i
                    break
            startPos[1] = newStartPos[0]
            yFrogPos = startPos[1]
            frogPosition = yPositions[yFrogPos][1]
            collided = boxes[2].rect.collidepoint(115,frogPosition)
            if collided == 1:
                # Collision with 2nd log detected, need to attach
                boxes[2].attach()
                frog.attach(boxes[2])
            if collided != 1:
                # No collision detected, frog is in the water
                takeLife(frog)
        elif startPos[0] == 3:
            frog.attach(None)
            y = frog.gety()
            for i in yPositions: # Updating startPos y value after log ride (removes boundary bugs)
                if i[1] > y:
                    newStartPos = i # BUG: y could be over 565 to 600
                    break
            startPos[1] = newStartPos[0]
            addOn = startP(frog.y)
            frog.y += addOn
        elif startPos[0] == 4:
            frog.attach(None)
            y = frog.gety()
            collided = boxes[6].rect.collidepoint(215,y)
            if collided == 1:
                # Collision with car
                takeLife(frog)
            collided1 = boxes[7].rect.collidepoint(215,y)
            if collided1 == 1:
                # Collision with car
                takeLife(frog)
        elif startPos[0] == 5:
            frog.attach(None)
            y = frog.gety()
            collided = boxes[4].rect.collidepoint(265,y)
            if collided == 1:
                # Collision with a car
                # frog.hit(boxes[4])
                takeLife(frog)
            collided1 = boxes[5].rect.collidepoint(265,y)
            if collided1 == 1:
                takeLife(frog)
                # Collision with car
                # frog.hit(boxes[5])
        elif startPos[0] == 10:
            frog.attach(None)
            y = frog.gety()
            collided = boxes[10].rect.collidepoint(515,y)
            if collided == 1:
                boxes[10].attach()
                frog.attach(boxes[10])
            if collided != 1:
                # No collision detected, frog is in the water
                takeLife(frog)
        elif startPos[0] == 11:
            frog.attach(None)
            y = frog.gety()
            collided = boxes[9].rect.collidepoint(565,y)
            if collided == 1:
                boxes[9].attach()
                frog.attach(boxes[9])
            if collided != 1:
                # No collision detected, frog is in the water
                takeLife(frog)
        elif startPos[0] == 12:
            frog.attach(None)
            y = frog.gety()
            collided = boxes[8].rect.collidepoint(615,y)
            if collided == 1:
                boxes[8].attach()
                frog.attach(boxes[8])
            if collided != 1:
                takeLife(frog)
        elif startPos[0] == 13:
            frog.attach(None)
            y = frog.gety()
            collided = boxes[1].rect.collidepoint(665,y)
            if collided == 1:
                boxes[1].attach()
                frog.attach(boxes[1])
            if collided != 1:
                takeLife(frog)
        elif startPos[0] == 14:
            frog.attach(None)
            y = frog.gety()
            collided = boxes[3].rect.collidepoint(715,y)
            if collided == 1:
                boxes[3].attach()
                frog.attach(boxes[3])
            if collided != 1:
                takeLife(frog)
        elif startPos[0] == 15:
            frog.attach(None)
            y = frog.gety()
            for i in yPositions: # Updating startPos y value after log ride (removes boundary bugs)
                if i[1] > y:
                    newStartPos = i # BUG: y could be over 565 to 600.
                    break
            startPos[1] = newStartPos[0]
            addOn = startP(frog.y)
            frog.y += addOn
    if direction == 4: # LEFT
        if startPos[0] == 0:
            frog.attach(None)
            y = frog.gety()
            for i in yPositions: # Updating startPos y value after log ride (removes boundary bugs)
                if i[1] > y:
                    newStartPos = i # BUG: y could be over 565 to 600
                    break
            startPos[1] = newStartPos[0]
            addOn = startP(frog.y)
            frog.y += addOn
        elif startPos[0] == 1:
            frog.attach(None)
            y = frog.gety()
            collided = boxes[0].rect.collidepoint(65,y) # boxes[0] is the first log
            if collided == 1:
                # Collision with first log detected, need to attach
                frog.attach(boxes[0])
            if collided != 1:
                # No collision detected, frog is in water
                takeLife(frog)
        elif startPos[0] == 2:
            frog.attach(None)
            y = frog.gety()
            collided = boxes[3].rect.collidepoint(115,y)
            if collided == 1:
                frog.attach(boxes[3])
            if collided != 1:
                # No collision detected, frog is in the water
                takeLife(frog)
        
# ----- The Main Function -----

def main():
    pygame.init()
    global boxes # List to store sprites
    boxes = []
    # Medium Logs
    for location in [[65, -120],[665, -100]]:
        boxes.append(LogMed(location))
    # Big Logs
    for location in [[115, -100],[715, 0]]:
        boxes.append(LogBig(location))  
    # Cars
    boxes.append(Car([263, 150]))
    boxes.append(Car([263, 300]))
    # Lorries
    boxes.append(Lorry([214, 0]))
    boxes.append(Lorry([214, 400]))
    # Big Logs 2
    for location in [[615, -100],[565, -50]]:
        boxes.append(LogBig(location))
    # Medium Logs 2
    for location in [[515, -120]]:
        boxes.append(LogMed(location))
    # Player Lives
    global livesN # List to hold Lives sprites
    livesN = []
    livesPos = 10 # y position of sprite
    for i in range(3):
      livesN.append(Lives([808, livesPos]))
      livesPos += 30 # Increasing the y value for adequate spacing
      
    # Set the screen size and window caption
    screen = pygame.display.set_mode([840, 600])
    pygame.display.set_caption("Frogger")

    frog = Frog() # Initialising the frog
    clock = pygame.time.Clock()
    
    # Main while loop
    while True:
        screen.fill(0) # Fill background with black
        # Draw rivers/grass/road
        for x in range(width/grass.get_width()):
            for y in range(height/grass.get_height()):
                if x in [0,3,6,7,8,9,15]:
                    screen.blit(grass,(x*50,y*50))
                elif x in [4,5]:
                    screen.blit(road,(x*50,y*50))
                elif x in [10,11,12]:
                    screen.blit(water, (x*50,y*50))
                else:
                    screen.blit(water,(x*50,y*50))
  
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    if startPos[1] - 1 < 0:
                        print "Error: Off Map"
                    else:
                        startPos[1] -= 1
                        frog.y -= frog.d
                        collisions(1, frog)
                if event.key == K_DOWN:
                    if startPos[1] + 1 > 11:
                        print "Error: Off Map"
                    else:
                        startPos[1] += 1
                        frog.y += frog.d
                        collisions(2, frog)
                if event.key == K_RIGHT:
                    if startPos[0] + 1 > 15:
                        print "Error: Off Map"
                    else:
                        startPos[0] += 1
                        frog.x += frog.d
                        collisions(3, frog)
                if event.key == K_LEFT:
                    if startPos[0] - 1 < 0:
                        print "Error: Off Map"
                    else:
                        startPos[0] -= 1
                        frog.x -= frog.d
                        collisions(4, frog)
            
        time = pygame.time.get_ticks()
        frog.update(time, 150)
        for b in boxes: # Iterating through sprites, updating and blitting them to screen
            b.update(time, 150)
            screen.blit(b.image, b.rect)
        for i in livesN: # Iterating through sprites, updating and blitting them to screen
            i.update(time, 150)
            screen.blit(i.image, i.rect) 
        frog.draw(screen) # Drawing the frog last so it is on top layer
        # Draw the game over/win message
        font = pygame.font.Font(None,100)
        won = False
        if startPos[0] == 15:
            text = font.render("YOU WIN!", 1, (255,0,0))
            textrect = text.get_rect()
            textrect.centerx, textrect.centery = 840/2,600/2
            screen.blit(text, textrect)
            won = True
        if len(livesN) == 0:
            text = font.render("GAME OVER", 1, (255,0,0))
            textrect = text.get_rect()
            textrect.centerx, textrect.centery = 840/2,600/2
            screen.blit(text, textrect)
        pygame.display.update()
        if won == True:
            sys.exit()
if __name__ == "__main__":
	main()
