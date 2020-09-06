# Variables of simulation
world_size = 100
days_run = 100
num_agents = 200

# At what speed, size, sense will the agent have at the start of the simulation
start_speed = 1
start_size = 10
start_sense = 1

# At what energy will the agent have at the start of the day
start_energy = 2000

# how much will the agents mutate when reproducing
mutate_speed = 0.5
mutate_size = 0.5
mutate_sense = 0.5

# how many food will the world contain at the start of the day
food = 100

# the boundary when the agents will go back home
energy_limit = 100

# lists
# TODO: fix cap letter
survival_list = []
reproduce_list = []
dead_list = []

# food dictionary
food_dictionary = {}


# What agent doing
working = []



# Objectives
search_food = []
go_home = []

print_TF = False



