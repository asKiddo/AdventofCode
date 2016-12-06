from hashlib import md5

door = 'ffykfhsq'.encode('utf-8')
password = []
i = 0

while len(password) < 8:
	hash = md5(door + str(i).encode('utf-8')).hexdigest()
	if hash.startswith('00000'):
		password.append(hash[5])
		print(hash)
	i += 1

print(''.join(password))