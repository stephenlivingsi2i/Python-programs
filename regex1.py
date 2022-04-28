import re
import fileinput


count = 0
for line in fileinput.input(["doc.txt"]):
    #Printing ip address occured line
    x = re.search('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
    if x != None:
        print(line)

print("{} ip addresses found in the file".format(count))



