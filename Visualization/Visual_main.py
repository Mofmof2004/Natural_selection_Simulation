import time
from Visualization.Visual_general import *
from Agent.Agent_movement.Agent_movement_main import agent_mouvement_main
from Visualization.Zoom.Zoom_0 import zoom_0
from Visualization.Zoom.Zoom_1 import zoom_1
from Graph.Graph_Display import *
from Visualization.Zoom.Zoom_main import zoom_main
from Simulation.Display_settings import *
# View count

def sim_visualization(agent_list):
    pygame.init()
    # General Info
    gameexit = False

    while not gameexit:
        # Get all event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for i in range(int(len(agent_list))):
            if agent_list[i].objective == "working":
                agent_mouvement_main(agent_list, i)

        zoom_main(agent_list)
        # loop all agents
        graph_show()
        plt.show()




        time.sleep(0.1)


        pygame.display.update()
        clock.tick(60)





