# 20ce005
# Yash Bhalgamiya

# A:Write a Python script to check whether a given key already exists in a dictionary.

dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F':6}
def is_key_present(key):
  if key in dic:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present('A')
is_key_present('a')

# B:Write a Python script to merge two Python dictionaries.

dicA={ 'a':1, 'b':2 }
dicB={'c':3, 'd':4 }
dicMerge=dicA.copy()
dicMerge.update(dicB)
print(dicMerge)

# c:Write a Python program to sum all the items in a dictionary.

dic = {'a': 220, 'b': 110}
print("Total Sum of values in the dictionary:", sum(dic.values()))

# D:Write a Python script to add a key to a dictionary.

dic = {'a': 100, 'b': 200}
dic.update({'c': 300})
print(dic)

# E:Write a Python script to concatenate dictionaries to create a new one.
#Sample Dictionary:
#dic1={1:10, 2:20}
#dic2={3:30, 4:40} dic3={5:50,6:60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)