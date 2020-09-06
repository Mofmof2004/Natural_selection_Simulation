from Simulation.Array import world_array
from Simulation.Display_settings import *
import random
import numpy


def Reset_day(agents, search_food):
    """
    Use to reset the day by adding the food, reseting all agent objective and factors
    :param agents: agent list
    :param Search_food: search for food list
    :return:
    """

    count = 0
    indices = numpy.where(world_array == 1)
    while 1 in world_array:
        world_array[(indices[0][count]), (indices[1][count])] = 0
        count += 1

    for index in range(food):
        # pick a random number from 0 to world_size -1
        food_x = (random.randrange(1, len(world_array), 1))
        food_y = (random.randrange(1, len(world_array), 1))

        # add food in array
        # food is represented as a 1
        world_array[food_x, food_y] = - index
        food_dictionary[- index] = food_x , food_y

    # Used to check that if any food have the same position
    # food wrong position counter
    wrong_pos = 1
    # Loop until all food has unique position
    while wrong_pos != 0:
        # Make food count at 0
        wrong_pos = 0
        for index in food_dictionary:
            # Find where food is located in the 2d array
            food_pos_in_array = numpy.where(world_array == index)
            # If unable the position of the food means that food has the same position than another food
            if len(food_pos_in_array[0]) == 0:
                # Create a new position
                new_food_x = (random.randrange(0, len(world_array), 1))
                new_food_y = (random.randrange(0, len(world_array), 1))

                # Update new food position
                food_dictionary[index] = new_food_x, new_food_y
                # Add new food position in the 2d array
                world_array[new_food_x, new_food_y] = index
                # add 1 to the counter
                wrong_pos += 1

                if print_TF is True:
                    print(str(index) + " food in " + str(numpy.where(world_array == index)))
                    print(food_dictionary)

    # Reset agent info
    for obj in agents:
        go_home.clear()
        # Add to agent search for food list
        search_food.append(obj.name)
        # Add to agent work list
        working.append(obj.name)
        # Reset agent objective
        obj.objective = "working"
        # Agent food count 0
        obj.food = 0
        # Reset agent energy level
        obj.energy = start_energy
        # Clear home x and y pos
        obj.home_x = None
        obj.home_y = None





