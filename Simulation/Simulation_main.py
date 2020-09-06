# Modules

# Files
from Graph.Graph_Display import *
from Simulation.Reset import Reset_day
from Agent.Dead_Survive_Reproduce import *
from Visualization.Visual_main import sim_visualization
from Simulation.Display_settings import *


def simulation_start():

    # day count
    day_count = 0

    # Creating all the agents using list comprehension
    # x, y, hx, hy, objective, food, speed, size, sense,food_x, food_y,  energy
    agents = [Agent((index+2), random.randint(0, world_size), random.randint(0, world_size),
                    None, search_food, 0, None,
                    start_speed, start_size, start_sense,
                    None, None, None, None, start_energy) for index in range(num_agents)]

    # Clearing graph files
    file = open('Graph/Population.txt', "w")
    file.write("%s %s %s\n" % (int(day_count), ",", int(num_agents)))
    file.close()

    gameexit = False

    while not gameexit:
        # days start
        if days_run > day_count:
            # add 1 to the day count
            day_count += 1

            # Reset day
            Reset_day(agents, search_food)

            # day continue running until all agent finished their day
            while len(working) != 0:
                # Call simulation visualization function
                sim_visualization(agents)
                # Show graph
                graph_show()
                plt.show()

