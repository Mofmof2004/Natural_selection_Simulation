import random
from Simulation.Display_settings import *
from Agent.Agent_movement.Agent_on_border import agent_on_border
from Agent.Agent_movement.Energy_cost import energy_cost


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

