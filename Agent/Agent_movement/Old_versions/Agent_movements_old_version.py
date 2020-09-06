import random
from Simulation.Display_settings import *
from Simulation.Array import world_array



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
            search_for_food_main(agent_list, num)
        # if agent food count is 1 and still ove the energy limit
        elif 0 < agent_list[num].food < 2 and agent_list[num].energy > energy_limit:
            search_for_food_main(agent_list, num)
            # make agent search for food
            # search_for_food_main(agent_list, num)
        else:
            # make agent go home
            go_home(agent_list, num)


def energy_cost(agent_list, num):
    """
    Use to calculate and update the energy cost of the agent movement for the agent list.
    Energy cost is dependent of size, speed, sense

    :param agent_list: agent list
    :param num: agent identity

    """

    size = agent_list[num].size/10
    speed = agent_list[num].speed / 10
    sense = agent_list[num].sense / 10

    # Substracting the energy cost of the agent to its energy
    agent_list[num].energy += -(int(((size**3)*(speed**2)+ sense)))


def agent_on_border(agent_list, num, x_or_y, move_direction):
    """
    used to move an agent on the border of thw world back inside the world
    :param agent_list: The agent list
    :param num: which agent
    :param border_move: border move count
    """
    # Check if agent is not in the corner of the world
    if agent_list[num].x == 0 or agent_list[num].x == world_size and \
        agent_list[num].y == 0 or agent_list[num].y == world_size:
        print("Have to do")

    # Else that agent is just on a border
    else:
        # check if agent is on the x axes border of the world
        if agent_list[num].x == 0:
            # Check if last move was on the x axes
            if agent_list[num].x_or_y == 0:
                # Add to agent y position -1 or 1
                agent_list[num].y += move_direction * agent_list[num].speed
                # update random move save
                agent_list[num].x_or_y = 1
                agent_list[num].neg_pos = move_direction
            # Check if last move was on the y axes
            elif agent_list[num].x_or_y == 1:
                # Check if it was a positive move and that the chosen axes for this move is the y axes
                # In this case 3 in x or y will represent a
                if agent_list[num].neg_pos == 1 and x_or_y == 1 or x_or_y == 3:
                    agent_list[num].y += 1 * agent_list[num].speed
                    # update random move save
                    agent_list[num].x_or_y = 1
                    agent_list[num].neg_pos = 1
                elif agent_list[num].neg_pos == -1 and x_or_y == 1 or x_or_y == 3:
                    agent_list[num].y += -1 * agent_list[num].speed
                    # update random move save
                    agent_list[num].x_or_y = 1
                    agent_list[num].neg_pos = -1
                # In this case two in x or y will represent a x axes move
                elif x_or_y == 0 or x_or_y == 2:
                    agent_list[num].x += 1 * agent_list[num].speed
                    # update random move save
                    agent_list[num].x_or_y = 0
                    agent_list[num].neg_pos = 1

            # agent energy cost
            energy_cost(agent_list, num)

        # check if the agent is n the other x axes border
        elif agent_list[num].x == world_size:
            if agent_list[num].x_or_y == 0:
                agent_list[num].y += move_direction * agent_list[num].speed
                # update random move save
                agent_list[num].x_or_y = 1
                agent_list[num].neg_pos = move_direction

            elif agent_list[num].x_or_y == 1:
                if agent_list[num].neg_pos == 1 and x_or_y == 1 or x_or_y == 3:
                    agent_list[num].y += 1 * agent_list[num].speed
                    # update random move save
                    agent_list[num].x_or_y = 1
                    agent_list[num].neg_pos = 1
                elif agent_list[num].neg_pos == -1 and x_or_y == 1 or x_or_y == 3:
                    agent_list[num].y += -1 * agent_list[num].speed
                    # update random move save
                    agent_list[num].x_or_y = 1
                    agent_list[num].neg_pos = -1
                # In this case two in x or y will represent a x axes move
                elif x_or_y == 0 or x_or_y == 2:
                    agent_list[num].x += -1 * agent_list[num].speed
                    # update random move save
                    agent_list[num].x_or_y = 0
                    agent_list[num].neg_pos = -1

            # agent energy cost
            energy_cost(agent_list, num)

        # check if agent is on the y axes border of the world
        elif agent_list[num].y == 0:
            if agent_list[num].x_or_y == 1:
                agent_list[num].x += move_direction * agent_list[num].speed
                # update random move save
                agent_list[num].x_or_y = 0
                agent_list[num].neg_pos = move_direction

            elif agent_list[num].x_or_y == 0:
                if agent_list[num].neg_pos == 1 and x_or_y == 0 or x_or_y == 2:
                    agent_list[num].x += 1 * agent_list[num].speed
                    # update random move save
                    agent_list[num].x_or_y = 0
                    agent_list[num].neg_pos = 1
                elif agent_list[num].neg_pos == -1 and x_or_y == 0 or x_or_y == 2:
                    agent_list[num].x += -1 * agent_list[num].speed
                    # update random move save
                    agent_list[num].x_or_y = 0
                    agent_list[num].neg_pos = -1
                # In this case two in x or y will represent a y axes move
                elif x_or_y == 1 or x_or_y == 3:
                    agent_list[num].y += 1 * agent_list[num].speed
                    # update random move save
                    agent_list[num].x_or_y = 1
                    agent_list[num].neg_pos = 1

                # agent energy cost
            energy_cost(agent_list, num)


        elif agent_list[num].y == world_size:
            if agent_list[num].x_or_y == 1:
                agent_list[num].x += move_direction * agent_list[num].speed
                # update random move save
                agent_list[num].x_or_y = 0
                agent_list[num].neg_pos = move_direction

            elif agent_list[num].x_or_y == 0:
                if agent_list[num].neg_pos == 1 and x_or_y == 0 or x_or_y == 2:
                    agent_list[num].x += 1 * agent_list[num].speed
                    # update random move save
                    agent_list[num].x_or_y = 0
                    agent_list[num].neg_pos = 1
                elif agent_list[num].neg_pos == -1 and x_or_y == 0 or x_or_y == 2:
                    agent_list[num].x += -1 * agent_list[num].speed
                    # update random move save
                    agent_list[num].x_or_y = 0
                    agent_list[num].neg_pos = -1
                # In this case two in x or y will represent a y axes move
                elif x_or_y == 1 or x_or_y == 3:
                    agent_list[num].y += -1 * agent_list[num].speed
                    # update random move save
                    agent_list[num].x_or_y = 1
                    agent_list[num].neg_pos = -1

                # agent energy cost
            energy_cost(agent_list, num)




def random_move(agent_list, num):
    """
    Use to move the agent in a random direction when it can't find food

    :param agent_list: Agent list
    :param num: Agent identity
    """

    # Choose randomly if the agent will move in a positive or negative direction
    move_direction = random.choice([-1, 1])

    # Choose randomly if the agent will move on the x or y axes or agent move the same movement as last move
    # 2 is to give a higher chance for agent to move on a straight line
    x_or_y = random.choice([0, 1, 2, 3])

    # if first random move
    if agent_list[num].x_or_y is None and agent_list[num].neg_pos is None:




        # Check if a border move
        if agent_list[num].x == 0 or agent_list[num].x == world_size or \
                agent_list[num].y == 0 or agent_list[num].y == world_size:
            # Check is agent is on the world border
            agent_on_border(agent_list, num, x_or_y, move_direction)

        # Agent not on the border of the world
        else:
            # Agent random move
            if x_or_y == 0:

                # changing agent x position
                agent_list[num].x += move_direction * agent_list[num].speed

                # update agent  move
                agent_list[num].x_or_y = 0
                agent_list[num].neg_pos = move_direction

                # Updating agent energy
                energy_cost(agent_list, num)

            # if the agent will move on the y axes
            elif x_or_y == 1:

                # Changing agent y position
                agent_list[num].y += move_direction * agent_list[num].speed

                # update agent  move
                agent_list[num].x_or_y = 1
                agent_list[num].neg_pos = move_direction

                # Updating agent energy
                energy_cost(agent_list,num)

    # if not first random move
    else:
        # Check if a border move
        if agent_list[num].x == 0 or agent_list[num].x == world_size or \
                agent_list[num].y == 0 or agent_list[num].y == world_size:
            # Check is agent is on the world border
            agent_on_border(agent_list, num, x_or_y, move_direction)

        # Agent not on the border of the world
        else:
            # to add chance for agent to do a straight move and not turn
            if x_or_y == 2 or x_or_y == 3:
                # if last move was on the x axes
                if agent_list[num].x_or_y == 0:
                    # change agent x pos
                    agent_list[num].x += agent_list[num].neg_pos * agent_list[num].speed

                # if last move was on the y
                elif agent_list[num].x_or_y == 1:
                    # change agent y pos
                    agent_list[num].y += agent_list[num].neg_pos * agent_list[num].speed

                # Updating agent energy
                energy_cost(agent_list, num)

            # if number chosen is 0 or 1 = make a normal random move
            elif x_or_y == 0 or x_or_y == 1:

                # if last move was on the x axes
                if agent_list[num].x_or_y == 0:
                    # if last move on the right
                    if agent_list[num].neg_pos == 1:
                        # if move on the x axes
                        if x_or_y == 0:
                            # move towards the right
                            agent_list[num].x += 1 * agent_list[num].speed

                            # update agent  move
                            agent_list[num].x_or_y = 0
                            agent_list[num].neg_pos = 1

                        # if move on the y axes
                        elif x_or_y == 1:
                            # move up or down
                            agent_list[num].y += move_direction * agent_list[num].speed

                            # update agent  move
                            agent_list[num].x_or_y = 1
                            agent_list[num].neg_pos = move_direction

                    # if last move was on the left
                    elif agent_list[num].neg_pos == -1:
                        # if move on the x axes
                        if x_or_y == 0:

                            # move to the left
                            agent_list[num].x += -1

                            # update agent  move
                            agent_list[num].x_or_y = 0
                            agent_list[num].neg_pos = -1

                        # if move on the y axes
                        elif x_or_y == 1:
                            # move up or down
                            agent_list[num].y += move_direction * agent_list[num].speed

                            # update agent  move
                            agent_list[num].x_or_y = 1
                            agent_list[num].neg_pos = move_direction

                    # Updating agent energy
                    energy_cost(agent_list, num)

                # if last move was on the y axes
                elif agent_list[num].x_or_y == 1:

                    # if last move downwards
                    if agent_list[num].neg_pos == 1:
                        # if move on the y axes
                        if x_or_y == 1:
                            # move downwards
                            agent_list[num].y += 1 * agent_list[num].speed

                            # update agent  move
                            agent_list[num].x_or_y = 1
                            agent_list[num].neg_pos = 1

                        # if move on the x axes
                        elif x_or_y == 0:
                            # move right or left
                            agent_list[num].x += move_direction * agent_list[num].speed

                            # update agent  move
                            agent_list[num].x_or_y = 0
                            agent_list[num].neg_pos = move_direction

                    # if last move upwards
                    elif agent_list[num].neg_pos == -1:
                        # if move on the y axes
                        if x_or_y == 1:
                            # move upwards
                            agent_list[num].y += -1 * agent_list[num].speed

                            # update agent  move
                            agent_list[num].x_or_y = 1
                            agent_list[num].neg_pos = -1
                        # if move on the x axes
                        elif x_or_y == 0:
                            # move right or left
                            agent_list[num].x += move_direction * agent_list[num].speed

                            # update agent  move
                            agent_list[num].x_or_y = 0
                            agent_list[num].neg_pos = move_direction

                    # Updating agent energy
                    energy_cost(agent_list, num)



def go_home(agent_list, num):
    """
    Used to move agent to the nearest home

    :param agent_list: agent list
    :param num: agent identity
    """

    # if nearest home position is not recorded in agent
    if agent_list[num].hs is None:
        # 0 = right x border, 1 = left x border, 2 = upper y border, 3 = lower y border
        # border list
        borders = []

        # x border
        borders.append(world_size - agent_list[num].x)

        # other x border
        borders.append(agent_list[num].x)

        # y border
        borders.append(world_size - agent_list[num].y)

        # other y border
        borders.append(agent_list[num].y)

        # closest border
        closest_border = (borders.index(min(borders)))
        agent_list[num].hs = closest_border


        # Agent movement to home
    else:

        # if movement on the x axes
        # print("agent x: " + str(agent_list[num].x))
        # print("agent y: " + str(agent_list[num].y))

        # if agent mouvment will be on the x axes
        if agent_list[num].hs == 0 or agent_list[num].hs == 1:
            # check if agent not arrived at destination
            if 0 < agent_list[num].x < world_size:
                if print_TF == True:
                    print("Agent " + str(agent_list[num].name) + " moving")

                # move towards right border
                if agent_list[num].hs == 0:
                    agent_list[num].x += 1 * agent_list[num].speed
                # move towards left border
                elif agent_list[num].hs == 1:
                    agent_list[num].x += -1 * agent_list[num].speed

                # agent energy cost
                energy_cost(agent_list, num)

                # remove agent random move save
                agent_list[num].x_or_y = None
                agent_list[num].neg_pos = None

            # arrived at border
            else:
                working.pop(working.index(agent_list[num].name))
                agent_list[num].objective = "finished"

                if print_TF == True:
                    print("agent name: " + str(agent_list[num].name))
                    print(working)
                    print("Agent " + str(agent_list[num].name) + " arrived")



        # if agent will move on the y axes
        elif agent_list[num].hs == 2 or agent_list[num].hs == 3:
            # check if agent to arrived at border
            if 0 < agent_list[num].y < world_size:
                if print_TF == True:
                    print("Agent " + str(agent_list[num].name) + " moving")
                # move towards lower border
                if agent_list[num].hs == 2:
                    agent_list[num].y += 1 * agent_list[num].speed
                #     move towards upper border
                elif agent_list[num].hs == 3:
                    agent_list[num].y += -1 * agent_list[num].speed

                # agent energy cost
                energy_cost(agent_list, num)

                # agent remove agent random move
                agent_list[num].x_or_y = None
                agent_list[num].neg_pos = None
            # arrived at border
            else:
                # remove agent from the working list
                working.pop(working.index(agent_list[num].name))
                # Change agent objective
                agent_list[num].objective = "finished"

                if print_TF == True:
                    print("Agent " + str(agent_list[num].name) + " arrived")


def search_for_food_main(agent_list, num):
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

            # print(str(agent_list[num].name) + 'reached food target')
            # print(numpy.where(world_array == 1))

            # print(str(agent_list[num].name) + ' reached food target')
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

            # if food location x is on the left side of the agent
            elif food_dictionary[food_in_view[closest_food_index]][0] < agent_list[num].x:
                # agent move towards the left
                agent_list[num].x += (-1 * agent_list[num].speed)

            # if food location y is below agent
            elif food_dictionary[food_in_view[closest_food_index]][1] > agent_list[num].y:
                # agent move downwards
                agent_list[num].y += (1 * agent_list[num].speed)

            # if food location y is above agent
            elif food_dictionary[food_in_view[closest_food_index]][1] < agent_list[num].y:
                # agent move upwards
                agent_list[num].y += (-1 * agent_list[num].speed)
            # agent losses energy
            energy_cost(agent_list, num)

            # remove agent last random move because did not an random move
            agent_list[num].x_or_y = None
            agent_list[num].neg_pos = None

    except:
        # print(str(agent_list[num].name) + " random move")
        agent_list[num].food_objective = None
        random_move(agent_list, num)

