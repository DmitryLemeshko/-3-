import sys
 
result = []
for line in sys.stdin:
    result.append(line)
    for i in enumerate(result):
        list(i)
        if line[1] == line.upper():
            print(sorted((i[0], '-', i[1])))