from Simulation.Display_settings import *
import random
from Agent.Agent_class import Agent


def dead(agents_list, num):
    """
    Use when an agent dies

    :param agents_list: agent list
    :param num: identity of the agent
    """
    print(agents_list)
    # delete agent from the population graph
    agents_list.pop(num)


# def Survive():


def reproduce(agents_list, num):
    """
    Use when agent reproduces and its offspring mutates
    :param agents_list: agent list
    :param num: agent identity
    """
    # creating the speed, size and sense of the offspring with the mother speed, size, sense and mutation rate
    new_agent_speed = agents_list[num].speed + random.randrange((-mutate_speed*10), (mutate_speed*10), 1) / 10
    new_agent_size = agents_list[num].size + random.randrange((-mutate_size*10), (mutate_size*10), 1) / 10
    new_agent_sense = agents_list[num].sense + random.randrange((-mutate_sense*10), (mutate_sense*10), 1) / 10
    # add new agent to the population list
    agents_list.append(Agent((len(agents_list)), random.randint(0, world_size), random.randint(0, world_size), None, None, search_food, 0, new_agent_speed, new_agent_size, new_agent_sense, start_energy))
    # print(agents_list[-1].speed)
    # print(agents_list[-1].size)
    # print(agents_list[-1].sense)





