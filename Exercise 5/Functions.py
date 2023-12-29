##############################
Functions
##############################


# Calculate average score in last 10 exams
def last_10_exams_score(*scores):
    average_score = 0
	
	
# For loop to calculate the average score
    for score in scores:
        average_score += score / number_of_exams
    
    return average_score

print('Average score in last 10 exams:', last_10_exams_score(80, 92, 75, 88, 95, 60, 78, 85, 90, 88))
