
list_number =[1,2,3,4,5]
list_number.append(6)
print(list_number)

list_num = [1,2,3,4,5]
list_num.append(5)
print(list_num)

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list1.append(list2)
print(list1)

list3 = [1,2,3,4,5]
list4 = [6,7,8,9,10]
list3.extend(list4)
print(list3)

list5 = [1,2,3,4,5]
list5.insert(3,3.5) #accepte 2 argumment becerful!!!
print(list5)


num_list = [10,20,30,40,50,60]
num_list.remove(20)
print(num_list)

num_list = [10,20,30,40,50,60,60,60]
num_list.remove(60)
print(num_list)

num_list = [10,20,30,40,50,60]
#num_list.pop(1)  return the index o 1 from the list that's mean return 20
num_list.pop() #that return ti last element in the list

num_list.clear()
print(num_list)


num_list = [23,39,74,923,92,64,10]
num_list.sort()
print(num_list)

num_list = [23,39,74,923,92,64,10]
number_sorted = sorted(num_list)
print(num_list)
print(number_sorted)

num_list = [23,39,74,923,92,64,10]
num_list.reverse()
print(num_list)
