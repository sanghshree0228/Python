import Searcher
import data_load
import indexer

data = indexer.data_processed("raw_data.pickle", "fortune_shelve") 
Searcher.search("fortunes_shelve")
