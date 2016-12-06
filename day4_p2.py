def caeser_shift(s, shift):
	return ''.join(chr(((ord(c) - ord('a') + shift) % 26) + ord('a')) for c in s)

def unshift_str(enc_str):
	lst = enc_str.split('-')
	str = "".join(lst[0:-1])
	return caeser_shift(str, int(lst[-1][-10:-7]))

#test_str = 'aczupnetwp-dnlgpyrpc-sfye-dstaatyr-561[patyc]'
#print(unshift_str(test_str))

fl = open('day4_rooms.txt')
fl_str = fl.read()
fl.close()

fl = open('day4_room_names.txt','w')
for room in fl_str.split('\n'):
	fl.write("%s\n" % unshift_str(room))