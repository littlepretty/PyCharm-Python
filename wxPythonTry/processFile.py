__author__ = 'YJQ'

import fileinput

new_file = open("result.txt",'w+')

for line in fileinput.input("hello.txt"):
    line.strip()
    new_line=line.replace("YJQ","ZHB")
    new_file.write(new_line)


new_file.close()

