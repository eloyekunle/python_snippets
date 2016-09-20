def crawler(page):
	startIndex = page.find('<a')
	startIndex += 9
	stopIndex = page[startIndex:].find("\"/>")
	url = page[startIndex:startIndex+stopIndex]
	return url
	

link = raw_input("Input: ")
url = crawler(link)
print url
