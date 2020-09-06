from Simulation.Display_settings import *
from Agent.Agent_movement.Energy_cost import energy_cost

def agent_on_border_move(agent_list, num, agent_x_or_y_axes, agent_move_direction):
    if agent_x_or_y_axes == 0:
        # Add to agent y position -1 or 1
        agent_list[num].x += agent_move_direction * agent_list[num].speed
    elif agent_x_or_y_axes == 1:
        agent_list[num].y += agent_move_direction * agent_list[num].speed
    # update random move save
    agent_list[num].x_or_y = agent_x_or_y_axes
    agent_list[num].neg_pos = agent_move_direction


def agent_on_border(agent_list, num, x_or_y, move_direction):
    """
    used to move an agent on the border of thw world back inside the world
    :param agent_list: The agent list
    :param num: which agent
    :param border_move: border move count
    """
    # Check if agent is not in the corner of the world
    if agent_list[num].x == 0 and agent_list[num].y == 0 or \
       agent_list[num].x == 0 and agent_list[num].y == world_size or \
       agent_list[num].x == world_size and agent_list[num].y == 0 or \
       agent_list[num].x == world_size and agent_list[num].y == world_size:

        # Check if the agent is on the left side
        if agent_list[num].x == 0:
            # Check if agent last move was on the x axes and if the agent is on the bottom left of the world
            if agent_list[num].x_or_y == 0 and agent_list[num].y == 0:
                # call function for agent movement on the y axes += 1
                agent_on_border_move(agent_list, num, 1, 1)
            # Check if agent last move was on the x axes and if the agent is on the upper left of the world
            elif agent_list[num].x_or_y == 0 and agent_list[num].y == world_size:
                # call function for agent movement on the y axes += -1
                agent_on_border_move(agent_list, num, 1, -1)


            # Check if agent last move was on the y axes and on the lower left of the world
            if agent_list[num].x_or_y == 1 and agent_list[num].y == 0:
                # call function for agent movement on the x axes += 1
                agent_on_border_move(agent_list, num, 0, 1)
            # Check if the agent last move was on the y axes an is on the upper left
            elif agent_list[num].x_or_y == 1 and agent_list[num].y == world_size:
                # call function for agent movement on the x axes += 1
                agent_on_border_move(agent_list, num, 0, 1)

            #   Check that agent has spawn in a corner
            elif agent_list[num].x_or_y == None and agent_list[num].y == world_size or agent_list[num].y == 0:
                # call function for agent movement on the x axes += 1
                agent_on_border_move(agent_list, num, 0, 1)

                # Check if agent is on the right side of the world
        elif agent_list[num].x == world_size:
            # Check if agent last move was on the x axes and agent on the upper right
            if agent_list[num].x_or_y == 0 and agent_list[num].y == 0:
                # call function for agent movement on the y axes += 1
                agent_on_border_move(agent_list, num, 1, 1)

            # Check if agent last move was on the x axes and is located on the lower
            elif agent_list[num].x_or_y == 0 and agent_list[num].y == world_size:
                # call function for agent movement on the y axes += -1
                agent_on_border_move(agent_list, num, 1, -1)

            # Check id agent last move on the y axes and is located upper right
            if agent_list[num].x_or_y == 1 and agent_list[num].y == 0:
                # call function for agent movement on the x axes += -1
                agent_on_border_move(agent_list, num, 0, -1)
            # Check if agent last move was on the y axes and is located on lower right
            elif agent_list[num].x_or_y == 1 and agent_list[num].y == world_size:
                # call function for agent movement on the x axes
                agent_on_border_move(agent_list, num, 0, -1)

            #   Check that agent has spawn in a corner
            elif agent_list[num].x_or_y == None and agent_list[num].y == world_size or agent_list[num].y == 0:
                # call function for agent movement on the x axes += 1
                agent_on_border_move(agent_list, num, 0, -1)


    # Else that agent is just on a border
    else:

        # check if agent is on the x axes border of the world
        if agent_list[num].x == 0:
            # Check if last move was on the x axes
            if agent_list[num].x_or_y == 0:
                # call function for agent movement
                agent_on_border_move(agent_list, num, 1, move_direction)

            # Check if last move was on the y axes
            elif agent_list[num].x_or_y == 1:
                # Check if it was a positive move and that the chosen axes for this move is the y axes
                # In this case 3 in x or y will represent a
                if agent_list[num].neg_pos == 1 and x_or_y == 1 or x_or_y == 3:
                    # call function for agent movement
                    agent_on_border_move(agent_list, num, 1, 1)

                elif agent_list[num].neg_pos == -1 and x_or_y == 1 or x_or_y == 3:
                    # call function for agent movement
                    agent_on_border_move(agent_list, num, 1, -1)

                # In this case two in x or y will represent a x axes move
                elif x_or_y == 0 or x_or_y == 2:
                    # call function for agent movement
                    agent_on_border_move(agent_list, num, 0, 1)
            # If agent spawn on a border
            else:
                agent_on_border_move(agent_list, num, 0, 1)

            # agent energy cost
            energy_cost(agent_list, num)

        # check if the agent is n the other x axes border
        elif agent_list[num].x == world_size:
            if agent_list[num].x_or_y == 0:
                # call function for agent movement
                agent_on_border_move(agent_list, num, 1, move_direction)

            elif agent_list[num].x_or_y == 1:
                if agent_list[num].neg_pos == 1 and x_or_y == 1 or x_or_y == 3:
                    # call function for agent movement
                    agent_on_border_move(agent_list, num, 1, 1)

                elif agent_list[num].neg_pos == -1 and x_or_y == 1 or x_or_y == 3:
                    # call function for agent movement
                    agent_on_border_move(agent_list, num, 1, -1)

                # In this case two in x or y will represent a x axes move
                elif x_or_y == 0 or x_or_y == 2:
                    # call function for agent movement
                    agent_on_border_move(agent_list, num, 0, -1)
            # If agent spawn on a border
            else:
                agent_on_border_move(agent_list, num, 0, -1)

            # agent energy cost
            energy_cost(agent_list, num)

        # check if agent is on the y axes border of the world
        elif agent_list[num].y == 0:
            if agent_list[num].x_or_y == 1:
                # call function for agent movement
                agent_on_border_move(agent_list, num, 0, move_direction)

            elif agent_list[num].x_or_y == 0:
                if agent_list[num].neg_pos == 1 and x_or_y == 0 or x_or_y == 2:
                    # call function for agent movement
                    agent_on_border_move(agent_list, num, 0, 1)

                elif agent_list[num].neg_pos == -1 and x_or_y == 0 or x_or_y == 2:
                    # call function for agent movement
                    agent_on_border_move(agent_list, num, 0, -1)
                # In this case two in x or y will represent a y axes move
                elif x_or_y == 1 or x_or_y == 3:
                    # call function for agent movement
                    agent_on_border_move(agent_list, num, 1, 1)
            # If agent spawn on a border
            else:
                agent_on_border_move(agent_list, num, 1, 1)

                # agent energy cost
            energy_cost(agent_list, num)

        elif agent_list[num].y == world_size:
            if agent_list[num].x_or_y == 1:
                # call function for agent movement
                agent_on_border_move(agent_list, num, 0, move_direction)


            elif agent_list[num].x_or_y == 0:
                if agent_list[num].neg_pos == 1 and x_or_y == 0 or x_or_y == 2:
                    # call function for agent movement
                    agent_on_border_move(agent_list, num, 0, 1)

                elif agent_list[num].neg_pos == -1 and x_or_y == 0 or x_or_y == 2:
                    # call function for agent movement
                    agent_on_border_move(agent_list, num, 0, -1)

                # In this case two in x or y will represent a y axes move
                elif x_or_y == 1 or x_or_y == 3:
                    # call function for agent movement
                    agent_on_border_move(agent_list, num, 1, -1)
            # If agent spawn on a border
            else:
                agent_on_border_move(agent_list, num, 1, -1)

                # agent energy cost
            energy_cost(agent_list, num)


