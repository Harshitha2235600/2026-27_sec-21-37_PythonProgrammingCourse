#write a python program that create a student dictionary(name,age,course),updates age and adds city
# Example solution: create, access and update a dictionary
student = {
    "name": "harshitha",
    "age": 20,
    "course": "Python",
}
print("Student:", student)
print("Name:", student["name"])

student["age"] = 21
student["city"] = "Vijayawada"
print("Updated:", student)