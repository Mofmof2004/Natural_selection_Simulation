from Simulation.Display_settings import *
from Simulation.Array import world_array
from Agent.Agent_movement.Energy_cost import energy_cost
from Agent.Agent_movement.Random_movement import random_move


def search_for_food(agent_list, num):
    """
    used to to make agent search and find food

    :param agent_list: Agent List
    :param num: Agent number

    """
    # list that will contain all the names of the food in the agent sense
    food_in_view = []
    # List that will contain the distance from the agent by adding th y and x axes distance from the agent
    food_total_position = []

    # The sense view of the agent
    sense = world_array[
        (agent_list[num].x - agent_list[num].sense): (agent_list[num].x + agent_list[num].sense + 1),
        (agent_list[num].y - agent_list[num].sense): (agent_list[num].y + agent_list[num].sense + 1)]

    try:
        # Find the food in the agent sense view
        # If no food objective
        if agent_list[num].food_objective is None:
            # Try all keys in dictionary
            for index in food_dictionary:
                # Check if food in agent sense view
                if index in sense:
                    # If in sense view add to food in view list
                    food_in_view.append(index)

            # Add the x and y pos of food and add to food_total_position list
            for index in range(len(food_in_view)):
                # add total distance from agent in list
                food_total_position.append((food_dictionary[food_in_view[index]][0]) +
                                           (food_dictionary[food_in_view[index]][1]))

            # Find closest food index from agent in the food_in_view list
            closest_food_index = food_total_position.index(min(food_total_position, key=lambda x: abs(x - (agent_list[num].x + agent_list[num].y))))
            # Add food name to agent food objective
            agent_list[num].food_objective = food_in_view[closest_food_index]

        # if agent have food objective
        else:
            # add food name to food in view list
            food_in_view.append(agent_list[num].food_objective)
            # make closest food index in list 0 == the food objective
            closest_food_index = 0




        # if agent reached food
        if food_dictionary[food_in_view[closest_food_index]][0] == agent_list[num].x and food_dictionary[food_in_view[closest_food_index]][1] == agent_list[num].y:

            # delete food in world array
            world_array[agent_list[num].x, agent_list[num].y] = 0
            food_dictionary.pop(food_in_view[closest_food_index])
            agent_list[num].food_objective = None
            # make agent food count increase by one
            agent_list[num].food += 1
            if print_TF == True:
                print("agent_food " + str(agent_list[num].food_objective))

        # if agent not reached food but in sense view
        else:

            # print("Agent moving towards food target")

            # if food location x is on the right side of the agent
            if food_dictionary[food_in_view[closest_food_index]][0] > agent_list[num].x:
                # agent move towards the right
                agent_list[num].x += (1 * agent_list[num].speed)

                # update agent movement save
                agent_list[num].x_or_y = 0
                agent_list[num].neg_pos = 1


            # if food location x is on the left side of the agent
            elif food_dictionary[food_in_view[closest_food_index]][0] < agent_list[num].x:
                # agent move towards the left
                agent_list[num].x += (-1 * agent_list[num].speed)
                # update agent movement save
                agent_list[num].x_or_y = 0
                agent_list[num].neg_pos = -1


            # if food location y is below agent
            elif food_dictionary[food_in_view[closest_food_index]][1] > agent_list[num].y:
                # agent move downwards
                agent_list[num].y += (1 * agent_list[num].speed)
                # update agent movement save
                agent_list[num].x_or_y = 1
                agent_list[num].neg_pos = 1

            # if food location y is above agent
            elif food_dictionary[food_in_view[closest_food_index]][1] < agent_list[num].y:
                # agent move upwards
                agent_list[num].y += (-1 * agent_list[num].speed)
                # update agent movement save
                agent_list[num].x_or_y = 1
                agent_list[num].neg_pos = -1

            # agent losses energy
            energy_cost(agent_list, num)

    except:
        # print(str(agent_list[num].name) + " random move")
        agent_list[num].food_objective = None
        random_move(agent_list, num)

