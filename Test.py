# myArray = [[1], [3, 3, 3, 4, 3, 3, 3]]
# for row in myArray:
#     for col in row:
#         print(col, end=' ')
#     print()

#Phil, how come this^ doesn't print like the one below
#It was originially just print(col), I added the row, to it for troubleshooting

# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for row in a:
#     for elem in row:
#         print(elem, end=' ')
#     print()
#
# list1 = ["cory", "edgar", "gel", "kuhu", "tanner"]
#
# list1.append('stinky')
# print(list1)
#
# list1.reverse()
# print(list1)
#
# name =input("Which name would you like to enter?")
# list1.insert(1, name)
#
# print(sorted(list1))

list1 = [1,2,3,4]
tuple1 = (1,2,3,4,5)

list1.extend(list(tuple1))

print(tuple1)
print(list1)