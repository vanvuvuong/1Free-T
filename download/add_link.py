with open('link_summary', 'r+') as f:
	body = f.read()
list_link = body.split ('\n')

post = open('post_test', 'r+')
post_with_link = open ('post_test_with_link', 'a+')
while True:
	line = post.readline()
	if not line:
		break
	if "Post" in line:
		post_with_link.write(line)
		index = int(line.split(' ')[-1])
		post_with_link.write(list_link[index])
		post_with_link.write('\n')
	else:
		post_with_link.write(line)



