import collections
dic1={'a':1,'b':2}
dic2={'b':3,'d':4}
chain=collections.ChainMap(dic1,dic2)
print("All the chainmap contents are:")
print(chain.maps)
print("All keys of chainmap are:")
print(list(chain.keys()))
print("All values of chainmaps are:")
print(list(chain.values()))
