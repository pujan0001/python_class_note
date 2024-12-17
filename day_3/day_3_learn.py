#we are going to learn tuples

a=("apple","banana","cat")
print(a[0])

print(a.count("apple"))
print(len(a))

#next data tyoe

b={"name": "Rahul","last_name": "Sharma"}

print(b["name"],b["last_name"])

next_variable={"values":[1,2,3,4]}
print(next_variable['values'])
print("\n")
print("\n")
print(len(next_variable['values']))

test_1= {"values":(1,2,3,4)}
print(test_1["values"][0])

#unpacking
e, f, g = (1,2,3)

print(e,f,g)

test_2 =[{"name":"rahul","last_name":"sharma"},2,"apple"]
print(test_2[0]["name"])

test_3={"list_key":[1,2,3,4],"tuple_key":(4,5,6,7),"string_key":"apple","int_key":4}
test_3["list_key"]="random_apple"

print(test_3)

#take values from user and store it on list add it on dictionary and index it

#a= input()
#a=int(a)
#b=[]
#c={}
#print()

#user_values=[]
#indexed_dict={}

#num_values=int(input("How many numbers would you like to enter "))

a={1,2,3,4} #this is set
print(len(a))

b=set ([1,2,3,3])
print(b)

b.remove(2)

print(b)


#all datatypes are mutable but tuple datatype is immutable

b.add(5)
print(b)

test_5={"first":[(list({1,0,9,5}))], "second":"hello"}
#print(test_5["first"][0][0][0])

test_6={"name":"rahul","last_name":"sharma","age":30}
#print(test_6.keys())
user_keys = test_6.keys() # this returns a list of keys

user_values=list(test_6.values())
#print(f"Hello your {user_keys[0]is {user_values[0]}}")

test_7= {"name":"hari","age":30,"subject":"cs"}
print(f"previous dict was{test_7}")
test_7.update({"age":31,"subject":"aiml"})
print(f"New one is {test_7}")



test_7.pop("age")

print(test_7)