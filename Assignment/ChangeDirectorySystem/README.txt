I am trying to create a cd (in terminal) type functionality using python program.
here the root path is "/" and path seperator is also "/"
old_path = Path('/a/b/c/d')
create class Path which has two methods
under the methode cd passing an argument that is new-path and after spiliting the new_path by using
 '/' delimiter and stored it into a new list
split the old path by using split function with'/' delimiter
ensuring current path  is equal to new path length

if new path is equal to .. then remove elements index wise from new list

do reversing of old list
now old list and new list are of the same type
with the help of join() function concatenate by using '/' delimiter



