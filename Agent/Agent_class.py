

class Agent:
    def __init__(self, name, x, y, hs, objective, food, food_objective, speed, size, sense, x_or_y, neg_pos, food_x, food_y, energy):
        """
        Agent class

        :param name: Agent identity
        :param x: Agent x position
        :param y: Agent y position
        :param hx: Home x position

        :param objective:  Agent objective
        :param food: Agent food count
        :param speed: Agent speed
        :param size: Agent size
        :param sense: Agent sense

        :param x_or_y: which axes has the random move been
        :param neg_pos: did agent move positively or negativiley
        :param energy: Agent energy
        """
        # Agent identity
        self.name = name

        # Agent positions
        self.x = x
        self.y = y

        # Closest home border
        self.hs = hs

        # Agent food info
        self.objective = objective
        self.food = food
        self.food_objective = food_objective

        # Agent mutation factors
        self.speed = speed
        self.size = size
        self.sense = sense

        # Agent random move
        self.x_or_y = x_or_y
        self.neg_pos = neg_pos

        # Food target position
        self.food_x = food_x
        self.food_y = food_y

        # Agent Energy count
        self.energy = energy

    def __str__(self):
        return "Theoph's agent, located at " + str(self.x) + "," + str(self.y)

    def __repr__(self):
        return self.__str__()
