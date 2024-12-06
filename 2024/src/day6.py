###################################
# READ DATA INPUT
###################################
def read_file_input (file_name: str):

    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    lines.remove("")
    text_file.close()
    return lines

def read_input (file_name: str):
    lines = read_file_input(file_name)
    return [list(line) for line in lines]

###################################
# Initiate Position
###################################
def get_current_position(map: list, search: str):

    for line in map:
        if any(e == search for e in line):
            x = line.index(search)
            y = map.index(line)

    return (x,y)

def get_obstacle_position(map: list, search: str):

    obstacles = []
    for line in map:
        if any(e == search for e in line):
            x = line.index(search)
            y = map.index(line)
            obstacles.append((x,y))
    return obstacles

def move_up():
    return

def move_down():
    return

def move_left():
    return

def move_right():
    return
def start_moving(map : list, obstacles : list, current_position : tuple, direction: str):

    MIN_X = 0
    MIN_Y = 0
    MAX_X = len(map[0]) - 1
    MAX_Y = len(map) - 1

    print (f'Map Size: {MAX_X + 1} x {MAX_Y + 1}')
    print ('Obstacles position: ', obstacles)
    print ('Current position: ', current_position)
    print ('Current direction: going', direction)

    if direction == "UP":
        # this function should move up untill obstacles on a way or end of the map
        # should return how many spaces moved
        # should retunr next action = "end" or "turn"
        # shoud return new position
        move_up()
    elif direction == "DOWN":
        move_down()
    elif direction == "LEFT":
        move_left()
    else:        
        move_right()
    
    return 0


def start():

    map = read_input("./2024/data/day6_test_input.txt")    
    #print(map)    
    current_position = get_current_position(map, "^")
    #print(current_position)
    obstacles = get_obstacle_position(map, "#")
    #print(obstacles)
    direction = "UP"
    start_moving(map, obstacles, current_position, direction)
    
    return 0

# Start Finding Solution
how_many_places = start()