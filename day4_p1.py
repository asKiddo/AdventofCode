from operator import itemgetter

def order_letters(encrypted_name):
	lst = encrypted_name.split('-')
	str = "".join(lst[0:-1])
	cnts = [ (l, str.count(l)) for l in set(str) ]
	s = sorted(cnts, key=itemgetter(0))
	s = sorted(s, key=itemgetter(1), reverse=True)
	return [ x[0] for x in s]
	
#test_str='totally-real-room-200[decoy]'
#print(order_letters(test_str))
#print("".join(order_letters(test_str))[0:4] == test_str[-6:-2])

fl = open('day4_rooms.txt')
fl_str = fl.read()
fl.close()

sum_sector_ids = 0
for room in fl_str.split('\n'):
	if "".join(order_letters(room))[0:4] == room[-6:-2]:
		sum_sector_ids += int(room[-10:-7])

print(sum_sector_ids)