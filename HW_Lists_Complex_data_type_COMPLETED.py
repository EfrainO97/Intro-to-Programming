#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""BMI 6018 Fall 2026

Instructions: 

For this assignment, please return all answers as variables in your
.py  (or .ipynb) file. You will quickly note that you will need to find answers outside the
class lectures. This is not an accident! You will need to become professionally
comfortable with looking things up via the python docs and google. 

Ensure that all variables are labelled according to the example. IE the answer
to problem 1 part c should be labelled "one_c". While all questions are answerable
with a single line of code, you are free to use helper variables so long as they
are helpfully/informatively named. 

I should be able to open your .py (or .ipynb) file and run it without errors. I will **not** be 
debugging your code for you. If your file does not run, it will **not** be graded. 
If you are unsure if your file will run, open up a chpc terminal and test it there.

For this assignment, please only use base python files types. That is: there 
should be no import calls in your file save my use of sys at the end.

Example Problem

0.a Create a list of strings
0.b Using a str method, capitalize one of the elements in the list using a slice
0.c Coerce one character of one element of the list to display as a hex

zero_a = ['first','second','third','fourth','fifth']
zero_b = zero_a[1].upper()
zero_c = hex(ord(zero_a[1][1]))

#Problem 1: Lists, Sets and Coersion

1.a Create a list of integers no fewer than 10 items from 0 to 9.
 .b Add 3 to the 5th indexed element
 .c Coerce all elements in the list to floats using list comprehension
 .d Coerce the list to a set
 .e Using a method, append int 10 to the set
 .f Using a method, pop an item from the set
 .g Using a length counting function, count the number of items in the set
 .h Check if the number of items in the set is the same as the 
    number of items in the list
 .i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
 .j Coerce 1.i to a set
 .k Count the number of elements in the 1.j



Problem 2: Dictionary woes

2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named 
    two_a, ensure the key names are the same as the dictionary names.
 .b Using keys, retrieve the Dango's name from 2.a
 .c Using keys, update the value of Mochi's year to 2018. This should not be a variable
    and should simply update 2.a.
 .d Manually create a dictionary that has a single level and contains each patient
    as the key and the year as the value. Set Mochi's year to 2019.'
 .e Coerce the keys of 2.d into a list
 .f Coerce the values of 2.d into a list
 .g Use the zip function to combine 2.e and 2.f into a dictionary again


two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}



Problem 3: Set combinations

Given the predefined sets below and using set methods
3.a Is set E a subset of set A
 .b Is set E a strict subset of set A
 .c Create a set that is the intersection of set A and set B
 .d Create a set that is the union of sets C, D and E
 .e add 9 to the set
 .f Using == compare this set to the list in one_a
 .g Explain why they are not the same. What would you need to change if you
    wanted this to be True?


three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}



Problem 4: Changing variable types

For each step you will modify a variable, then append the type of the variable
to a list. Do not recreate the list variable, it should be a running list of 
types.

4.a Create a variable of type int with the value of 8
 .b Create an empty list 
 .c Using type(), add the type of 4.a to this list
 .d Add 0.39 to 4.c
 .e append the type of 0.39 to the list
 .f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no 
    decimal places, and append to list.
 .g append the type to the list


Problem 5: More variable type changes

Continue from where you left off in Problem 4.

5.a Manually create a dictionary where the values are items in the list from where we left in 
    problem 4, and the keys should be their index in the list. Print the dictionary.
 .b Add 300 and coerce it into a string
 .c append the type to the list
 .d slice the string up to the 2nd element
 .e append the type to the list
 .f use list comprehension to convert this into a new list of integers
 .g append the type to the list
 .h append the type of three_setA to the list
"""

#Start your assignment here
print("Assignment 3")



# In[ ]:


#Problem 1: Lists, Sets and Coersion
#1.a
one_a = [0,1,2,3,4,5,6,7,8,9]
print(one_a)
#1.b
one_b = one_a[5]+3
print(one_b)
#1.c
one_c =[float(x) for x in one_a]
print(one_c)
#1.d
one_d = set(one_c)
print(one_d)
#1.e
one_d.add(10)
one_e = one_d
print(one_e)
#1.f
one_f = one_d.pop()
print(one_f)
#1.g
one_g = one_d
print(len(one_g))
#1.h
one_h = len(one_d) == len(one_c)
print(one_h)
#1.i
one_i = list(one_d) + one_a
print(one_i)
#1.j
one_j = set(one_i)
print(one_j)
#1.k
one_k = len(one_j)
print(one_k)

#Problem 2: Dictionary woes
#2.a
two_patient_dictionary_kinoko = {
    "name": "Kinoko",
    "year": 2021
}

two_patient_dictionary_dango = {
    "name": "Dango",
    "year": 2019
}

two_patient_dictionary_mochi = {
    "name": "Mochi",
    "year": 2020
}

two_a = {
    "two_patient_dictionary_kinoko": two_patient_dictionary_kinoko,
    "two_patient_dictionary_dango": two_patient_dictionary_dango,
    "two_patient_dictionary_mochi": two_patient_dictionary_mochi
}

print(two_a)
#2.b
two_b = two_a["two_patient_dictionary_dango"]["name"]
print(two_b)
#2.c
two_a["two_patient_dictionary_mochi"]["year"] = 2018
print(two_a["two_patient_dictionary_mochi"])
#2.d
two_d = {
    "Kinoko": 2021,
    "Dango": 2019,
    "Mochi": 2019
}

print(two_d)
#2.e
two_e = list(two_d.keys())
print(two_e)
#2.f
two_f = list(two_d.values())
print(two_f)
#2.g
two_g = dict(zip(two_e, two_f))
print(two_g)

#Problem 3: Set combinations
three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}
#3.a
three_a = three_setE.issubset(three_setA)
print(three_a)
#3.b
three_b = three_setE < three_setA
print(three_b)
#3.c
three_c = three_setA.intersection(three_setB)
print(three_c)
#3.d
three_d = three_setC.union(three_setD, three_setE)
print(three_d)
#3.e
three_d.add(9)
three_e = three_d
print(three_e)
#three_d already contains a 9, sets can not have duplicates so nothing changed.
#3.f
three_f = (three_d == one_a)
print(three_f)
#3.g
three_g = "They are not the same becuase three_d is a set and one_a is a list. Addtionally, one_a is 0-9 while three_d is 1-9. To make them the same you would have to change either one_a to a set or three_d to a list, list(three_d) or set(one_a). Then you would need to add a 0 to the list three_d or remove the 0 from the set one_a, three_d.insert(1, 0) or one_a.remove(0)."
print(three_g)
#Problem 4: Changing variable types
#4.a
four_a = 8
#4.b
four_b = []
#4.c
four_b.append(type(four_a))
four_c = four_b
print(four_c)
#4.d
four_d = four_a + 0.39
print(four_d)
#4.e
four_b.append(type(four_d))
four_e = four_b
print(four_e)
#4.f
four_f = round(four_d ** -10)
four_b.append(four_f)
print(four_b)
#4g
four_b.append(type(four_f))
four_g = four_b
print(four_g)

#Problem 5: More variable type changes

#5.a
five_a = {0: four_b[0], 1: four_b[1], 2: four_b[2], 3: four_b[3]}
print(five_a)
#5.b
five_b = str(four_f + 300)
print(five_b)
#5.c
four_b.append(type(five_b))
five_c = four_b
print(five_c)
#5.d
five_d = five_b[:2]
print(five_d)
#5.e
four_b.append(type(five_d))
five_e = four_b
print(five_e)
#5.f
five_f = [int(char) for char in five_d]
print(five_f)
#5.g
four_b.append(type(five_f))
five_g = four_b
print(five_g)
#5.h
four_b.append(type(three_setA))
five_h = four_b
print(five_h)




# In[ ]:




