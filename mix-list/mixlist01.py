#!/usr/bin/env python3

# create a list containing three items
my_list = [ "192.168.0.5", 5060, "UP" ]

# display the first item in the list
print("The first item in the list (IP): " + my_list[0] )

# display the second item in the list
print("The second item in the list (port): " + str(my_list[1]) )

# display the third item in the list
print("The last item in the list (state): " + my_list[2] )

my_list2 = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]
print("IP Addresses:", my_list2[3], "and " + my_list2 [4])

new_list = ["blue", "green", "yellow"]
print(f"Misc data: {my_list[1]}, and {new_list[2]}") 
print(f"More misc data: {my_list[2]}, {new_list[0]}, and {my_list[0]}")
