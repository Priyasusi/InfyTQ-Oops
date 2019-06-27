'''OOPR-Assgn-13
Write a python program to find out if a given classroom is present in the left wing of a university building.
Implement the class, Classroom given below.
Method/Attribute description:30 min
classroom_list: Static list which store the name of the class rooms in the left wing
search_classroom(class_room): Static method which search for the given class room in the classroom_list.
If found, return "Found". Else, return -1
Note: Perform case insensitive string comparison 

For testing:
Invoke search_classroom(class_room) static method on class, Classroom by passing the name of the class room to be searched
Display appropriate message based on the return value of search_classroom(class_room)'''
class Classroom:
    classroom_list=["ECE_A","ECE_B","ECE_C"]
    @staticmethod
    def search_classroom(class_room):
        if(class_room.upper() in Classroom.classroom_list):
            return "Found"
        else:
            return -1
print(Classroom.search_classroom("ECE_C"))
