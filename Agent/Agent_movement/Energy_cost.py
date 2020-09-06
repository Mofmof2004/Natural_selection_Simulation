

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
