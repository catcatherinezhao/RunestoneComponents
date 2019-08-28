# Python script to create any number of instances of TIE in a Runestone page.

file = open("_sources/index.rst", "w")

for i in range(100):
	file.write(".. tie:: %s\n  :feedback:\n  :output:\n  :error:\n\n" % ("uniqueId" + str(i)))

file.close()