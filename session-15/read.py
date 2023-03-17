file = open("demo.txt", "r")
print(file.readable())
print(file.read(6))
print(file.readline())

file.seek(0)
lines = file.readlines()
for line in lines:
  print(line)

file.close()


file = open("sign-of-four.txt", "r")
lines = file.readlines()
for line in lines:
  print(line)
file.close()
