MOVES = {'U':[-1,0],'D':[1,0],'L':[0,-1],'R':[0,1]}
KEYPAD = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]
KEYPAD_LENGTH = len(KEYPAD)-1

def move_by_stroke(key, curr_location):
	move = MOVES[key]
	new_location = [a+b for a,b in zip(move, curr_location)]
	if min(new_location) < 0 or max(new_location) > KEYPAD_LENGTH or get_keypad_value(new_location) == 0:
 		return curr_location
	else:
		return new_location
		
def move_list(lst, start_location):
	curr_location = start_location
	for key in lst:
		curr_location = move_by_stroke(key, curr_location)
	return curr_location
	
def move_instructions(instruction_string):
	code = []
	start_location = [2,0]
	steps = instruction_string.split('\n')
	for step in steps:
		m_lst = list(step)
		start_location = move_list(m_lst, start_location)
		code.append(get_keypad_value(start_location))
	return code

def get_keypad_value(location):
	row = KEYPAD[location[0]]
	return row[location[1]]
	
def read_from_file(fname):
	fl = open(fname)
	fl_str = fl.read()
	fl.close()
	return fl_str
		
#curr_location = [2,0]
#move_lst = ['U','L','L']
#print('Start: %s' % (get_keypad_value(curr_location)))
#print(get_keypad_value(move_by_stroke('U',curr_location)))
#print('Moves: %s' % (move_lst))
#print('End: %s' % (get_keypad_value(move_list(move_lst, curr_location))))

#test_vals = """ULL
#RRDDD
#LURDL
#UUUUD"""
#print('Code: %s' % (move_instructions(test_vals)))

print('Code for directions file: %s' % move_instructions(read_from_file('day2_directions.txt')))