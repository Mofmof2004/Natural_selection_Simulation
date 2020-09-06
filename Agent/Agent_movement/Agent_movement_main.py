from Simulation.Display_settings import *
from Agent.Agent_movement.Search_for_food import search_for_food
from Agent.Agent_movement.Go_home import go_home

def agent_mouvement_main(agent_list, num):
    """
    The main function to control the agent movement

    :param agent_list: List of agent objects
    :param num: Agent reference
    """
    # check if agent dead
    if agent_list[num].energy <= 0:
        # if dead remove from the working list
        working.pop(working.index(agent_list[num].name))
        # change objective of the agent
        agent_list[num].objective = "finished"
        # Remove agent from the population list
        agent_list.pop()
        if print_TF == True:
            print("dead")

    # if agent still alive
    else:

        # if agent have eaten 0 food
        if agent_list[num].food == 0:
            # if yes make agent search for food
            # search_for_food_main(agent_list, num)
            search_for_food(agent_list, num)
        # if agent food count is 1 and still ove the energy limit
        elif 0 < agent_list[num].food < 2 and agent_list[num].energy > energy_limit:
            search_for_food(agent_list, num)
            # make agent search for food
            # search_for_food_main(agent_list, num)
        else:
            # make agent go home
            go_home(agent_list, num)
