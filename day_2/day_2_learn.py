
# test_matrix = [1,2,3,4,5,6]

# test_matrix_1 =[7,8,9] 
# # test_matrix.extend(test_matrix_1)

# test_matrix_1.extend(test_matrix) # to ADD the element of the  list of test_matrix into the test_matrix_1 list
# test_matrix_1.sort() #sorting the elements in the list after receiving the extended file into the list
# print(test_matrix_1)
# i= input("Enter the number:") # taking input from the user by giving the syntax input and then parenthesis in which the parameter is written...
# i = int(i) #typecasting and the class is integer...
# #print(type(i))

# k=4
# o="apple"
# next_matrix=[k,o]
# print(next_matrix[0])

# print(len(next_matrix)) # it gives the length of the totAL ELEMENT IN THERE AS THEY ALL COUNT...

# another_matrix=[len(next_matrix),4,"apple"]
# print(another_matrix)

# l= ["apple","goat", "cow", "goat"]
# l.remove("goat") # if repetation occurs then the remove method works only for 1st goat which comes nearer to the start point of the list...
# print(l)

# m=[1,3,4,5,6,"football"]
# print(m[-1]) # negative indicates the list from end point...
# print(m[::-1]) #-1 dekhi SABBAI vannale tya dekhi aagadi sabbai list maa vaako ...


# test_variables=[1,6,8,9,3,0]
# test_variables.sort()
# print(test_variables)
# print(test_variables)
# print("Following is descending order")
# print(test_variables[::-1])
# var=input("input any positive number less than 5. ")
# try:

#     var=int(var)
#     if var<5: # Conditional statement...
#         print("Five is greater than two")   
#     elif var<4:
#                 print("four is greater than two")
#     elif var<3:
#                 print("three is greater than two.")
#     elif var<2:
#                 print("two is not greater than two.")
#     elif var<1:
#         print("one is less than two.")
#     else:
#                 print("Input the valid number")
# except ValueError:
#         print("print enter a valid positive integer lessss than 5...")
var = input("Input any positive number less than 5: ")

try:
    var = int(var)  # Convert the input to an integer
    if var < 0:  # Check if the number is positive
        print("The number should be positive.")
    elif var >= 5:  # Check if the number is less than 5
        print("The number should be less than 5.")
    else:  # Valid input, compare with other numbers
        if var == 2:
            print("Two is equal to two.")
        elif var < 2:
            print("The number is less than two.")
        elif var < 3:
            print("The number is less than three.")
        elif var < 4:
            print("The number is less than four.")
        else:
            print("The number is less than five but not less than four.")
except ValueError:
    print("Please enter a valid positive integer.")
