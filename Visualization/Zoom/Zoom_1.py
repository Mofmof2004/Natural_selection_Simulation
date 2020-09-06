from Simulation.Display_settings import *
from Visualization.Visual_general import *

def zoom_1(agent_list, view_zoom_count):
    view_zoom_count += 1

    agent_num_zoom = 0
    # Updating the display
    gameDisplay.fill(white)
    gameDisplay.blit(agent_img, (290, 290))
    pygame.draw.circle(gameDisplay, (0, 0, 0), (300, 300), agent_list[agent_num_zoom].sense * 22, 3)
    pygame.draw.rect(gameDisplay, grey,(600, 0, 250, 650))
    pygame.draw.rect(gameDisplay, grey, (0, 600, 600, 50))

