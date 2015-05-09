
import data_load
import indexer
import shelve
from datetime import datetime

def search(fortune_shelve):
    dt1 = datetime.now()
    dt2 = datetime.now()

    print("Reading shelve data:")
    word_dic = shelve.open(fortune_shelve)
    
    while(True):
        query = input("\nquery:").lower()  
        query = set(query.split())

        if "and" in (query):
            query.remove("and")
            if "or" in (query):
                query.remove("or")
            print (query)

            foundSet = set()
            for quote in (data_list):
                if query[0] in quote and query[0] in quote:
                    foundSet  = foundSet | set(word_dic[quote])
                    print("Execution time:", dt2.microsecond - dt1.microsecond)
                else:
                    foundSet = indexer.finalList
                    for quote in query:
                        if quote not in (word_dic).key():
                                foundSet = set()
                                break
                        else: foundSet = foundSet & set(word_dic[quote])

        elif "or" in (query) and "and" not  in (query):
            query.remove("or")
            print (query)
     
            for quote in (data_list):
                for (value) in (query):
                    found_at = quote.find(value)
                    if( found_at > 0):
                        print(quote)
            print("Execution time:", dt2.microsecond - dt1.microsecond)
     
        else:
            print (query)

            for quote in (data_list):
                if query[0] in quote and query[0] in quote:
                    print(quote)
            print("Execution time:", dt2.microsecond - dt1.microsecond)
            word_dic.close()
     
