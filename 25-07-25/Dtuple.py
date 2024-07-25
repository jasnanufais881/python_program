
def Convert(tup, di):
	for a, b in tup:
		di.setdefault(a, []).append(b)
	return di

tups = [("jasna", 25), ("arya", 22), ("nufais", 30),
		("izan", 3), ("shamila", 24), ("shami", 26)]
dictionary = {}
print(Convert(tups, dictionary))
