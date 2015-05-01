# Word frequency count

def count_frequency(mylist):
	dictionary = {}

	for words in mylist:
		key = words
		if(dictionary.get(key) == None):
			dictionary[key] = 1
		else:
			dictionary[key] = dictionary[key] + 1
		
	return dictionary

mylist=["one", "two", "eleven", "one", "three", "two", "eleven", "three", "seven", "eleven"]

print(count_frequency(mylist))
