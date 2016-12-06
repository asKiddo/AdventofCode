from operator import itemgetter

def most_letter(str):
	cnts = [ (l, str.count(l)) for l in set(str) ]
	s = sorted(cnts, key=itemgetter(1), reverse=True)
	return s[0][0]

fl = open('day6_input.txt')
fl_str = fl.read()
fl.close()

lst = fl_str.split('\n')
wrd = ''

for i in range(len(lst[0])):
	str = [x[i] for x in lst]
	wrd += most_letter(str)

print(wrd)