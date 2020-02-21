# Python program to explain os.path.isdir() method 
	
# importing os.path module 
import os.path 
	

	
# Path 
path = '\\\s-user\TECHNOLOGY'
path2 = '\\\s-user\public\ceyhun'
	
# Check whether the 
# specified path is an 
# existing directory or not 
isdir = os.path.isdir(path) 
isdir2 = os.path.isdir(path2) 
print(path,isdir) 
print(path2,isdir2)
