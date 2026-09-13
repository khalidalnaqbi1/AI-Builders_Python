students = [
    {"name": "Lara",  "age": 23, "track": "AI",   "hours_studied": 40, "scores": [85, 90, 78]},
    {"name": "Omar",  "age": 31, "track": "Data", "hours_studied": 12, "scores": [60, 55, 70]},
    {"name": "Rim",   "age": 27, "track": "AI",   "hours_studied": 55, "scores": [95, 88, 92]},
    {"name": "Karim", "age": 19, "track": "Web",  "hours_studied": 8,  "scores": [50, 65, 40]},
    {"name": "Nour",  "age": 25, "track": "AI",   "hours_studied": 30, "scores": [75, 80, 85]},
    {"name": "Sami",  "age": 35, "track": "Data", "hours_studied": 48, "scores": [88, 91, 79]},
]


#  Part 1: Exploring the Data (accessing nested structures)
# 1. Print the name of the first student and the name of the last student.

# print(students[0]["name"])
# print(students[-1]["name"])

# # 2. Print Rim's scores. (Find her record, then access the `scores` key.)

# print(students[2])
# print(students[2]["scores"])

# # 3. Loop through all students and print one line per student: `Lara is 23 years old and studies AI`.

# for x in students:  
#  print(f'{x["name"]} is {x["age"]} years old and studies {x["track"]} .')




# Part 2: Filtering (the most common data operation)
# 4. Use a loop to build a new list containing only the students in the  AI track. Print how many there are.
# newlist= []
# for i in students:
#     if i["track"] =="AI":
#         newlist.append(i)
# print(len(newlist))



# 5. Now do the same thing with a list comprehension in a single line. Confirm you get the same result.
# newlist1=[x for x in students if x["track"]== "AI"]
# print(len(newlist1))

# 6. Build a list of the **names** of all students who studied more than 30 hours.
# names=[]
# for n in students:
#     if n["hours_studied"] > 30:
#         names.append(n["name"])
        
# print(names)

# names1= [i["name"] for i in students if i["hours_studied"] > 30]
# print(names1)
# # 7. Build a list of students who are older than 24 AND in the AI track. (Combining conditions is everyday work.)
# student=[]
# for s in students:
#     if s["age"] > 24 and s["track"] =="AI":
#         student.append(s["name"])
# print(student)


# student1=[a["name"] for a in students if a["age"] > 24 and a["track"] =="AI"]
# print(student)



# Part 3: Aggregating (turning many records into one number)
# 8. Calculate the average age of all students.
tot_ages= 0
# for a in students:
#     tot_ages+= a["age"]
# average= tot_ages/len(students)
# print(average)
# # 9. Calculate the total hours studied across the whole cohort.
# tot_hours= 0 
# for h in students:
#     tot_hours+= h["hours_studied"]
# print(tot_hours)

# 10. Find the student who studied the most hours. Print their name and hours. (Hint: loop and track the max as you go.)

# max_student = students[0] #assune
# for s in students: 
#     if s["hours_studied"] > max_student["hours_studied"]:
#         max_student = s  
# print(max_student["name"],max_student["hours_studied"])



# 11. For each student, their final grade is the average of their `scores`. Print each student's name and their final grade, rounded to 1 decimal.

# for s in students:
#     score= sum(s["scores"])
#     avg= score / len(s["scores"])
#     print(f"{s['name']} {avg:.1f}")


# Part 4: Transforming (reshaping data into something new)
# 12. Write a list comprehension that produces a new list of dictionaries, each with only two keys: `name` and `average_score`. This is exactly how you'd prepare data for a report or a model.
# new_students=[{"name":s["name"], "average_score":  sum(s["scores"]) / len(s["scores"])} for s in students]
# print(new_students)

# 13. Build a dictionary that maps each track to the number of students in it, like `{"AI": 3, "Data": 2, "Web": 1}`.
# track ={}
# for t in students:
#     current_track = t["track"]
    
#     if current_track not in track:
#         track[current_track]= 1
#     else :
#         track[current_track]+=1
# print(track)
# # 14. Create a set of all the unique tracks in the dataset. Explain in a comment why a set is the right tool here instead of a list.

# set_track= {t["track"] for t in students}
# print(set_track)

# set is collection that not allow a duplication records as well its unchangable tool compaired to the list collection .


# Part 5 : Reusable Functions (don't repeat yourself)
# 15. Write a function `filter_by_track(students, track)` that returns all students in a given track. Test it with `"AI"` and `"Data"`.
# def students_track(s)
# def filter_by_track (students,track):
#     match=[] 
#     for i in students:
#         a= i["track"]
#         if a == track :
#             match.append(i["name"])
#     return(match) 

# ai_students =filter_by_track(students,"AI")
# print(ai_students)

# ai_students =filter_by_track(students,"Data")
# print(ai_students)
    


# # 16. Write a function `average_score(student)` that takes one student dictionary and returns their average score.
# def  average_score(student):
#             sum_score= sum(student["scores"])
#             avg= sum_score / len(student["scores"])
#             return(avg)


# avg_Sami=  average_score(students[5])
# print(avg_Sami)

# # 17. Write a function `top_student(students)` that returns the name of the student with the highest average score. (Use the function from #16 inside it — functions calling functions.)

# def top_student(students):
    
#     highest = students[0]#assume
#     for a in students:
#         if average_score(a) > average_score(highest):
#             highest= a
#     return(highest["name"])

# t= top_student(students)
# print(t)
            

# # 18. Write a function `summary(students)` that returns a dictionary with three keys: `total_students`, `average_age`, and `tracks` (the set of unique tracks). One function, full overview.
# def summary(students):
#     total_students = len([i["name"] for i in students])
#     total_avg = sum([i["age"] for i in students])/total_students
#     unique_track = set([i["track"] for i in students])
#     new={
#         "total_students": total_students, 
#         "average_age":total_avg,
#         "tracks":unique_track 
#     }
#     return new

# s=summary(students)
# print(s)



# Bonus — Mini Data Pipeline
# 19. Write a function `report(students, min_hours)` that:
#    - filters the students who studied at least `min_hours`,
#    - for each one calculates their average score,
#    - returns a list of dictionaries with `name` and `average_score`,
#    - sorted from highest score to lowest.

def report(students, min_hours):
    #filters the students who studied at least `min_hours
    passed=[]
    for i in students:
        study= i["hours_studied"] 
        if study >= min_hours:
    # for each one calculates their average score        
            students_sum_score= sum(i["scores"])
            avg_score= students_sum_score / len(i["scores"])
    #returns a list of dictionaries with `name` and `average_score
            new_dic={
                "name":i["name"], 
                "average_score":avg_score 
            }
            passed.append(new_dic) 
    #sorted from highest score to lowest. 
    sorted_report = sorted(passed, key=lambda x: x["average_score"], reverse=True)
    
    # Return the final sorted list
    return sorted_report
s= report(students,12)
print(s)
        
