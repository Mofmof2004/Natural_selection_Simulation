import pygame



# Display dimensions
display_width = 850
display_height = 650

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
grey = (192, 192, 192)
light_grey = (194, 194, 194)

# Creation of the window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Natural Selection')
clock = pygame.time.Clock()


# Loading world
world_grid = pygame.image.load('Visualization/World_grid.png')

# Loading agent
# if view_zoom_count == 0:
#     print("zoom 0")
agent_img = pygame.image.load('Visualization/Agent.png')
# elif view_zoom_count == 1:
#     print("zoom 1")
#     agent_img = pygame.image.load('Visualization\Agent_zoom_1.png')

# Loading food
food_img = pygame.image.load('Visualization/Food.png')


#
# random_food_choice = random.choice([0, 1, 2])
# if random_food_choice == 0:
#     food_img = pygame.image.load('Visualization\cerise.png')
# elif random_food_choice == 1:
#     food_img = pygame.image.load('Visualization\_verdure.png')
# else:
#     food_img = pygame.image.load('Visualization\glace.png')








