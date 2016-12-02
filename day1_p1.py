directions = ['N','E','S','W']
increments = {'N':[0,1],'E':[1,0],'S':[0,-1],'W':[-1,-0]}
rotations = {'R':1,'L':-1}

def move(direction, length):
	return [x * length for x in increments[direction]]

def turn(curr_direction, rotation):
	curr_dir = directions.index(curr_direction)
	return directions[(curr_dir + rotations[rotation]) % 4]

def follow_directions(step_lst):
	curr_dir = 'N'
	curr_local = [0,0]
	for step in step_lst:
		rotate = step[0]
		length = int(step[1:])
		curr_dir = turn(curr_dir, rotate)
		how_far = move(curr_dir, length)
		curr_local = [a+b for a,b in zip(curr_local, how_far)]
	return curr_local

def calc_distance(location):
	return abs(location[0])+abs(location[1])
	
def convert_file_to_list(filename):
	fl = open(filename)
	fl_str = fl.read()
	fl.close()
	return fl_str.split(', ')
	
def calc_and_print(directions):
	distance = calc_distance(follow_directions(directions))
	print('Directions: %s \nDistance: %s' % (directions, distance))

dir1 = 	['R2','L3']
calc_and_print(dir1)

dir1 = ['R2','R2','R2']
calc_and_print(dir1)

dir1 = ['R5','L5','R5','R3']
calc_and_print(dir1)

dir1 = convert_file_to_list('day1_directions.txt')
calc_and_print(dir1)