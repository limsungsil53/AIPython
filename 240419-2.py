#split
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

data = "John,30,Engineer\nAlice,25,Designer\nBob,22,Artist"
lines = data.split("\n")
print(lines)
for line in lines:
 fields = line.split(",")
 print("Name:", fields[0], "Age:", fields[1], "Occupation:", fields[2])


