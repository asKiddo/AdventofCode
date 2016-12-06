from hashlib import md5

door = 'ffykfhsq'.encode('utf-8')
password = [None]*8
i = 0

while None in password:
	hash = md5(door + str(i).encode('utf-8')).hexdigest()
	if hash.startswith('00000'):
		position = int(hash[5], 16)
		if position < 8 and password[position] is None:
			password[position] = hash[6]
			print(hash)
	i += 1

print(''.join(password))