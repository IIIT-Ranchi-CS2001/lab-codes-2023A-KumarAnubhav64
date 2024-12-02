# Solving the provided questions

# Q1: Find the number of palindrome words in a sentence without using any function
def count_palindromes(sentence):
    count = 0
    words = sentence.split()  # Split the sentence into words
    for word in words:
        word = word.lower()  # Case insensitive check
        is_palindrome = True
        for i in range(len(word) // 2):
            if word[i] != word[len(word) - i - 1]:
                is_palindrome = False
                break
        if is_palindrome:
            count += 1
    return count

# Q2: List comprehension to get multiple inputs from keyboard
#      Finding the mean, median, and mode of the list

def get_stats_from_input():
    # Input multiple values from the user
    nums = [int(i) for i in input("Enter space-separated integers: ").split()]

    # Calculating mean
    mean = sum(nums) / len(nums)

    # Calculating median
    sorted_nums = sorted(nums)
    n = len(nums)
    if n % 2 == 0:
        median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    else:
        median = sorted_nums[n // 2]

    # Calculating mode
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    mode = max(frequency, key=frequency.get)

    return {"mean": mean, "median": median, "mode": mode}

# Q3: Create a list of course codes and course names, and then merge them into a list
def create_course_list():
    course_codes = ['CS1001', 'CS1002', 'CS1003']
    course_names = ['Python', 'Data Structures', 'Algorithms']

    combined_courses = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]
    return combined_courses

# Q4: Set operations on singers and dancers
def perform_set_operations():
    # Set comprehension to generate singers and dancers
    singers = {input("Enter singer name: ") for _ in range(int(input("Number of singers: ")))}
    dancers = {input("Enter dancer name: ") for _ in range(int(input("Number of dancers: ")))}

    # All artists (union)
    all_artists = singers | dancers

    # Allrounders (intersection)
    allrounders = singers & dancers

    # Dancers but not singers (difference)
    dancers_not_singers = dancers - singers

    # Singers but not dancers (difference)
    singers_not_dancers = singers - dancers

    # Dancers but not singers combined with singers but not dancers (symmetric difference)
    exclusive = singers ^ dancers

    return {
        "all_artists": all_artists,
        "allrounders": allrounders,
        "dancers_not_singers": dancers_not_singers,
        "singers_not_dancers": singers_not_dancers,
        "exclusive": exclusive
    }

# Putting together the functions to format them in a notebook
import nbformat as nbf

# Creating a new notebook
nb = nbf.v4.new_notebook()

# Adding cells for each question in the notebook

# Q1
nb['cells'].append(nbf.v4.new_code_cell("""
# Q1: Count palindrome words in the given sentence
sentence = input('Enter a sentence: ')
count_palindromes(sentence)
"""))

# Q2
nb['cells'].append(nbf.v4.new_code_cell("""
# Q2: Get list of integers and find mean, median, mode
get_stats_from_input()
"""))

# Q3
nb['cells'].append(nbf.v4.new_code_cell("""
# Q3: Combine course codes and names
create_course_list()
"""))

# Q4
nb['cells'].append(nbf.v4.new_code_cell("""
# Q4: Perform set operations on singers and dancers
perform_set_operations()
"""))

# Save the notebook to a file
with open('Experiment_5.ipynb', 'w') as f:
    nbf.write(nb, f)

"Experiment_5.ipynb file has been created with the solutions."
