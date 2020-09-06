from Simulation.Display_settings import *
from Agent.Agent_movement.Energy_cost import energy_cost


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

