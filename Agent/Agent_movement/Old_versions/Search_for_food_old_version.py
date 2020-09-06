from Simulation.Display_settings import *
import numpy
from Simulation.Array import world_array


def search_for_food_main_old_version(agent_list, num):
    """
    used to to make agent search and find food

    :param agent_list: agent list
    :param num: agent identity
    """

    # if food in agent sense view
    if 1 in world_array[
            (agent_list[num].x - agent_list[num].sense): (agent_list[num].x + agent_list[num].sense + 1),
            (agent_list[num].y - agent_list[num].sense): (agent_list[num].y + agent_list[num].sense + 1)]:

        # find index of food in agent sense view
        food_index = numpy.where(world_array[
              (agent_list[num].x - agent_list[num].sense): (agent_list[num].x + agent_list[num].sense + 1),
              (agent_list[num].y - agent_list[num].sense): (agent_list[num].y + agent_list[num].sense + 1)])


        # To find the nearest food from the agent
        closest_food_list = []
        for i in range(len(food_index[0][:])):
            # add to the closest food list the sum of each food index
            closest_food_list.append(food_index[0][i] + food_index[1][i])

        # find the closest number to 10 in the list which means it will be the nearest food
        closest_food = closest_food_list.index(min(closest_food_list, key=lambda x: abs(x - 20)))

        # if want to print info
        if print_TF == True:
            print(len(food_index[0][:]))
            print("list: " + str(closest_food_list))
            print("Closest: " + str(closest_food))
            print(food_index)
            print("end")

        # calculating the food position in world array
        # Calculating the x position of the agent
        if food_index[1][closest_food] > agent_list[num].sense - 10:
            food_index_loc_x = food_index[1][closest_food] - 11 + agent_list[num].x + 1
        else:
            food_index_loc_x = food_index[1][closest_food] - 11 + agent_list[num].x

        # Calculating the y position of the agent
        if food_index[0][closest_food] > agent_list[num].sense - 10:
            food_index_loc_y = food_index[0][closest_food] - 11 + agent_list[num].y + 1
        else:
            food_index_loc_y = food_index[0][closest_food] - 11 + agent_list[num].y

        # show agent sense view
        agent_sense = world_array[
              (agent_list[num].x - agent_list[num].sense): (agent_list[num].x + agent_list[num].sense + 1),
              (agent_list[num].y - agent_list[num].sense): (agent_list[num].y + agent_list[num].sense + 1)]

        # info agent sense view
        if print_TF is True:
            print(agent_list[num].name)
            print("food move")
            print("agent location: " + str(agent_list[num].x), str(agent_list[num].y))
            print("food array index: " + str(food_index))
            print("food location: " + str(food_index_loc_x) + ", " + str(food_index_loc_y))
            print("Agent energy " + str(agent_list[num].energy))
            print(agent_sense.shape)
            print(agent_sense)


        # if agent reached food
        if food_index_loc_x == agent_list[num].x and food_index_loc_y == agent_list[num].y:
            # print(str(agent_list[num].name) + 'reached food target')
            # print(numpy.where(world_array == 1))
            if print_TF == True:
                print(str(agent_list[num].name) + 'reached food target')
            # delete food in world array
            world_array[agent_list[num].x, agent_list[num].y] = 0

            # make agent food count increase by one
            agent_list[num].food += 1
            if print_TF == True:
                print("agent_food "+ str(agent_list[num].food))

        # if agent not reached food but in sense view
        else:
            if print_TF == True:
                print("Agent moving towards food target")

            # if food location x is on the right side of the agent
            if food_index[0][closest_food] > 10:
                # agent move towards the right
                agent_list[num].x += (1 * agent_list[num].speed)

            # if food location y is on the left side of the agent
            elif food_index[0][closest_food] < 10:
                # agent move towards the left
                agent_list[num].x += (-1 * agent_list[num].speed)

            # if food location y is below agent
            elif food_index[1][closest_food] > 10:
                # agent move downwards
                agent_list[num].y += (1 * agent_list[num].speed)

            # if food location y is above agent
            elif food_index[1][closest_food] < 10:
                # agent move upwards
                agent_list[num].y += (-1 * agent_list[num].speed)
            # agent losses energy
            energy_cost(agent_list, num)

            # remove agent last random move because did not an random move
            agent_list[num].x_or_y = None
            agent_list[num].neg_pos = None

    # food is not in agent sense view
    else:
        # agent makes a random move
        if print_TF == True:
            print("random_move")
        random_move(agent_list, num)
