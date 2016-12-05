moves = {'U':[-1,0],'D':[1,0],'L':[0,-1],'R':[0,1]}
keypad = [[1,2,3],[4,5,6],[7,8,9]]
KEYPAD_LENGTH = len(keypad)-1

def move_by_stroke(key, curr_location):
	move = moves[key]
	new_location = [a+b for a,b in zip(move, curr_location)]
	if max(new_location) > KEYPAD_LENGTH or min(new_location) < 0:
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
	start_location = [1,1] #Always start on 5
	steps = instruction_string.split('\n')
	for step in steps:
		m_lst = list(step)
		start_location = move_list(m_lst, start_location)
		code.append(get_keypad_value(start_location))
	return code

def get_keypad_value(location):
	row = keypad[location[0]]
	return row[location[1]]
	
def read_from_file(fname):
	fl = open(fname)
	fl_str = fl.read()
	fl.close()
	return fl_str
		
#curr_location = [1,1]
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