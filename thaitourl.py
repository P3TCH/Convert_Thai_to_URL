def thaitourl(thaitext):
	return_text = ''
	thai_all = ['%A1', '%A2', '%A3', '%A4', '%A5', '%A6', '%A7', '%A8', '%A9', '%AA', '%AB', '%AC', '%AD', '%AE', '%AF', '%B0', '%B1', '%B2', '%B3', '%B4', '%B5', '%B6', '%B7', '%B8', '%B9', '%BA', '%BB', '%BC', '%BD', '%BE', '%BF', '%C0', '%C1', '%C2', '%C3', '%C4', '%C5', '%C6', '%C7', '%C8', '%C9', '%CA', '%CB', '%CC', '%CD', '%CE', '%CF', '%D0', '%D1', '%D2', '%D3', '%D4', '%D5', '%D6', '%D7', '%D8', '%D9', '%DA', '%DB', '%DC', '%DD', '%DE', '%DF', '%E0', '%E1', '%E2', '%E3', '%E4', '%E5', '%E6', '%E7', '%E8', '%E9', '%EA', '%EB', '%EC', '%ED', '%EE', '%EF', '%F0', '%F1', '%F2', '%F3', '%F4', '%F5', '%F6', '%F7', '%F8', '%F9', '%FA', '%FB']
	for i in thaitext:
		if ord(i) > 3584 and ord(i) < 3677:
			i = thai_all[ord(i) - 3585]
		return_text += i

	return return_text

def urltothai(url):
	return_url = ''
	thai_all = ['%A1', '%A2', '%A3', '%A4', '%A5', '%A6', '%A7', '%A8', '%A9', '%AA', '%AB', '%AC', '%AD', '%AE', '%AF', '%B0', '%B1', '%B2', '%B3', '%B4', '%B5', '%B6', '%B7', '%B8', '%B9', '%BA', '%BB', '%BC', '%BD', '%BE', '%BF', '%C0', '%C1', '%C2', '%C3', '%C4', '%C5', '%C6', '%C7', '%C8', '%C9', '%CA', '%CB', '%CC', '%CD', '%CE', '%CF', '%D0', '%D1', '%D2', '%D3', '%D4', '%D5', '%D6', '%D7', '%D8', '%D9', '%DA', '%DB', '%DC', '%DD', '%DE', '%DF', '%E0', '%E1', '%E2', '%E3', '%E4', '%E5', '%E6', '%E7', '%E8', '%E9', '%EA', '%EB', '%EC', '%ED', '%EE', '%EF', '%F0', '%F1', '%F2', '%F3', '%F4', '%F5', '%F6', '%F7', '%F8', '%F9', '%FA', '%FB']
	i = 0
	while i < len(url):
		if url[i:i+3] in thai_all:
			indexnumber = str(thai_all.index(url[i:i+3]) + 3585)
			return_url += chr(int(indexnumber))
			i += 2
		else:
			return_url += url[i]
		i += 1

	return return_url

def __main__():
	print('================================================')
	print('   Welcome to Thai Character to URL Converter')
	print('                Create by: P3TCH')
	print('================================================')
	print()
	print('Select Option: ')
	print('1. Convert Thai Character to URL')
	print('2. Convert URL to Thai Character')
	print()
	choice = input('Enter your choice (1 or 2): ')
	while choice != '1' and choice != '2':
		print('Invalid Choice')
		choice = input('Enter your choice (1 or 2): ')
	print()
	if choice == '1':
		thaitext = input('Enter Thai Character: ')
		print()
		print('URL is: ')
		print(thaitourl(thaitext))
	elif choice == '2':
		url = input('Enter URL: ')
		print()
		print('Thai Character is: ')
		print(urltothai(url))

if __name__ == '__main__':
	__main__()

