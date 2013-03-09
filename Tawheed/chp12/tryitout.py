#Question 1
print "Enter 5 names: "
name_list = []

for i in range(5):
    name = raw_input()
    name_list.append(name)


print "The sorted list is ", sorted(name_list)

print "The original list is ", name_list

print "The thrird name you typed is ", name_list[2]

replace = int(raw_input("Replace one name. Which one (1-5): ")) - 1
new_name = raw_input("New name: ")

name_list[replace] = new_name
print "The names are ", name_list[0], " ", name_list[1]," ", name_list[2]," ",name_list[3], " ",name_list[4]

