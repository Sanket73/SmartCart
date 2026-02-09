info = [
    ("Sanket","Math"),
    ("Raj","Science"),
    ("Sanket","Science"),
    ("Aniket","English"),
    ("Rahul","Math"),
]

'''
unique_courses = set()
for tup in info:
    unique_courses.add(tup[1])
print(unique_courses)

for courses,name in info:
    if(courses == "Math"):
        print(name)
'''
dict = {}
for name,courses in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(courses)
    else:
        dict[name].add(courses)
print(dict)