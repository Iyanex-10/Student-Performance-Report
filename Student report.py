<<<<<<< HEAD
# Generator
def get_scores(students):
    for student in students:
        name = student['name']
        for score in student['scores']:
            yield (name, score)

#Recursion
def sum_scores(scores):
    if not scores:
        return 0
    return scores[0] + sum_scores(scores[1:])

def average(scores):
    total = sum_scores(scores)
    return total / len(scores)


#Decorator
def simple_retry(func):
    def wrapper(*args, **kwargs):
        try:
            print(f"Running {func.__name__}...")
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            print("Retry once")
            return func(*args, **kwargs)
        return wrapper
@simple_retry
def get_student_average(scores):
    if not scores:
        raise ValueError("Empty score")
    return sum(scores) / len(scores)

    
#Example input
        
students = [{"name": "Alice", "scores": [70, 80, 90]}, {"name": "Bob", "scores": [60, 75,85]}]

#Decorated function to calculate average
def get_student_average(scores):
    if not scores:
        raise ValueError("Empty score")
    return average(scores)

# Print individual scores
print("Individual Scores:")
for name, score in get_scores(students): 
    print(f"{name}: {score}")

#Print average scores
print("\nAverage Scores:")
for student in students:
    avg = get_student_average(student['scores'])
=======
# Generator
def get_scores(students):
    for student in students:
        name = student['name']
        for score in student['scores']:
            yield (name, score)

#Recursion
def sum_scores(scores):
    if not scores:
        return 0
    return scores[0] + sum_scores(scores[1:])

def average(scores):
    total = sum_scores(scores)
    return total / len(scores)


#Decorator
def simple_retry(func):
    def wrapper(*args, **kwargs):
        try:
            print(f"Running {func.__name__}...")
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            print("Retry once")
            return func(*args, **kwargs)
        return wrapper
@simple_retry
def get_student_average(scores):
    if not scores:
        raise ValueError("Empty score")
    return sum(scores) / len(scores)

    
#Example input
        
students = [{"name": "Alice", "scores": [70, 80, 90]}, {"name": "Bob", "scores": [60, 75,85]}]

#Decorated function to calculate average
def get_student_average(scores):
    if not scores:
        raise ValueError("Empty score")
    return average(scores)

# Print individual scores
print("Individual Scores:")
for name, score in get_scores(students): 
    print(f"{name}: {score}")

#Print average scores
print("\nAverage Scores:")
for student in students:
    avg = get_student_average(student['scores'])
>>>>>>> 38ae9a3cb227cad17a6994253de57e96b7779328
    print(f"{student['name']} - Average: {avg: .2f}")