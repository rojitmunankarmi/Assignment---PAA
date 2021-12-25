# # ##########
# # 1. Write a Python program to multiplies all the items in a list.git init

# # def multiply_list(items):
# #     a = 1
# #     for x in items:
# #         a *= x
# #     return a 
# # print(multiply_list([1,2,7]))


# ##########
# # 2. Write a Python program to get the smallest number from a list.
# # a = [20,30,440,4,550,6,54,3,3,22]
# # print(min(a))


# ##########
# # 3. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# # l = ['dfd','k','5' "ffsd","hggsdfh"]
# # count = 0
# # for i in l :
# #     if len(l)>2:
# #         if i[0]==i [len(i)-1]:
# #             count +=1
# # print (count)


# ##########
# # 4. Write a Python program to check a list is empty or not.
# List = [1,2]
# if len(List)==0:
# 	print("The list is empty.")
# else:
# 	print("The list is not empty.")


# ##########
# # 5. Write a Python program to print a specified list after removing the 4th elements.
# # a = [20,40,50,7,2]
# # print(a)
# # a.remove(7)
# # print(a)


# ##########
# # 6. Write a Python program to select an item randomly from a list.
# # import random
# # a=[1,2,3,4,5,6,7,8,9,0]
# # ran=random.choice(a)
# # print(ran)


# ##########
# # 7. Write a Python program to add an item in a tuple
# # tup=(5,12,44)
# # print(tup)
# # tup= tup+(5,)
# # print(tup)


# ##########
# # 8. Write a Python program to convert a tuple to a string.

# # def convertTuple(tup):
# # 		# initialize an empty string
# # 	str = ''
# # 	for item in tup:
# # 		str = str + item
# # 	return str


# # # Driver code
# # tuple = ('S', 'P', 'I', 'D', 'E', 'R', 'M', 'A', 'N')
# # str = convertTuple(tuple)
# # print(str)



# # ##########
# # # 9. Write a Python program to create the colon of a tuple.
# # from copy import deepcopy
# # #create a tuple
# # tuplex = ("HELLO", 5, [],) 
# # print(tuplex)
# # #make a copy of a tuple using deepcopy() function
# # tuplex_colon = deepcopy(tuplex)
# # tuplex_colon[2].append(50)
# # print(tuplex_colon)
# # print(tuplex)


# ##########
# # 10. Write a Python program to iteration over sets
# # a= {1,2,2,3,3,4,5,6,6,7,7,7,8,8,9}
# # for i in a:
# #     print(i)


# #########
# # 11. Write a Python program to remove an item from a set if it is present in the set.
# # a= {1,2,3,'coding','hello world','javascript'}
# # print(a)
# # if 'coding' in a:
# #     a.remove('coding')
# #     print(a)
# # else:
# #     print("not present")
    

# ##########
# # 12. Write a Python program to update list element in a set.
# # a= {0,1,2,3,"hello","ohh","python"}
# # a.update({"Hello","Sir"})
# # print(a)


# ##########
# # 13. Write a Python script to concatenate following dictionaries to create a new one.
# # Sample Dictionary: dic1= {1:10, 2:20} dic2= {3:30, 4:40} dic3= {5:50,6:60}
# # dic1= {1:10, 2:20}
# # dic2= {3:30, 4:40}
# # dic3= {5:50,6:60}
# # print(dic1,':',dic2,':',dic3)

# # dic1.update(dic2)
# # dic1.update(dic3)

# # print (dic1)


# ##########
# # 14. Write a Python script to check if a given key already exists in a dictionary.
# # d={1:"hello",2:"i",3:"am",4:"avicek"}
# # if 5 in d:
# #     print("present")
# # else:
# #     print("not present")


# ##########
# # 15. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# # a={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:8**2,9:9**2,10:100,11:11**2,12:12**2,13:2**13,14:14**2,15:15**2}
# # print(a)
