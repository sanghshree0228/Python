import pickle
import os
import shelve

def data_processed(path, fortune_shelve):
	f = open(path, "rb")	
	data_list = pickle.load(f)

	word_dic = shelve.open(fortune_shelve)	

	global finalList
	finalList = []	

	for item in data_list:
	
		i = item[1]	
		quote = item[0]	
		finalList.append(i)

		words = set(quote.split())	
		for word in words:
			word = word.decode('utf-8').lower()	
			if word in word_dic.keys():
				word_dic[word].append(i) 
			else:
				word_dic.update({word:[i]})
			word_dic.sync()
	finalList = set(finalList)	
	f.close()
	word_dic.close()
	
