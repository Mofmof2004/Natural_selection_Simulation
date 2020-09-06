from Visualization.Visual_general import *
from Simulation.Display_settings import *
from Visualization.Visual_accessories import *



def zoom_0(agent_list, view_zoom_count):

    # Updating the display
    gameDisplay.fill(white)
    gameDisplay.blit(world_grid, (30, 20))

    # TODO random agent mutation random
    random_order = agent_list
    for i in range(int(len(agent_list))):
        gameDisplay.blit(agent_img, (agent_list[i].x*6+30, agent_list[i].y*6+20))

    for index in food_dictionary:
        gameDisplay.blit(food_img, (food_dictionary[index][0] * 6 + 30, food_dictionary[index][1] * 6 + 20))
        # tets = numpy.where(world_array == index)
        # if len(tets[0]) == 0:
        #     print("stoooooooooooooooooooooooooooooooooooooooooopp")
        #     print(str(index) + " food in " + str(numpy.where(world_array == index)))
        #     print(food_dictionary)
    # button("Change View", 670, 570, 150, 60, grey, light_grey, view_zoom_count, add)
