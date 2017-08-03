import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
VIOLET = (148, 0, 211)
ORANGE = (255, 140, 0)
GOLD = (255, 215, 0) 
color = [BLACK, VIOLET, ORANGE, GREEN, BLUE, RED]

def bg_color():
    return BLACK
def color_1():
    return VIOLET
def color_2():
    return ORANGE
def color_3():
    return GOLD


# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



class Building():
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(->).
            A negative integer draws the building left to right (<-).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up 
            A negative integer draws the building down 
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """
    def __init__(self, x_point, y_point, width, height, color):
    
        self.x_point = x_point 
        self.y_point = y_point
        self.width = width 
        self.height = height 
        self.color = color 

    def draw(self):
        """
        uses pygame and the global screen variable to draw the building on the screen
        """        
        pygame.draw.rect(screen, self.color, (self.x_point, self.y_point ,self.width ,self.height))
        

    def move(self, speed):
        """
        Takes in an integer that represents the speed at which the building is moving
            A positive integer moves the building to the right ->
            A negative integer moves the building to the left  <-
        Moves the building horizontally across the screen by changing the position of the
        x_point by the speed
        """
        self.x_point = self.x_point - speed



class Scroller(object):
    """
    Scroller object will create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building obecjts.
        The building objects should have "draw" and "move" methods.

    Other info:
        It has an instance variable "buildings" which is a list of buildings for the scroller
    """

    def __init__(self, width, height, base, color, speed):
        self.width = width
        self.height = height
        self.base = base
        self.base = color
        self.speed = speed
        
    def add_buildings(self):
        w2 = 100
        while w2 <= 800:
            pygame.draw.rect(screen, self.color, (self.x_point, self.y_point ,self.width ,self.height))
            


    def add_building(self, x_location):
        
        #takes in an x_location, an integer, that represents where along the x-axis toput a buildng.Adds a building to list of buildings.
        

    def draw_buildings(self):
        
        #This calls the draw method on each building.
        

    def move_buildings(self):
        
        #This calls the move method on each building passing in the speed variable As the buildings move off the screen a new one is added.
        



FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)




front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREE  N_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)

 #-------- Main Program Loop -----------


h1 = random.randint(350,550)
w1 = 100
building1 = Building(600, 800-h, w1, h1, VIOLET)

h2 = random.randint(250,450)
w1 = 100
building2 = Scroller(600, 800-h, w2, h2, ORANGE)

h3 = random.randint(150,350)
w3 = 100
building3 = Building(600, 800-h, w3, h3, GOLD)


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here]
    building1.draw()
    building1.move(5)
    building2.add_buildings()
    building2.
    
##    back_scroller.draw_buildings()
##    back_scroller.move_buildings()
##    middle_scroller.draw_buildings()
##    middle_scroller.move_buildings()
##    front_scroller.draw_buildings()
##    front_scroller.move_buildings()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


