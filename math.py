# Создаем функцию для подсчета средней оценки за домашние задания
# по всем студентам в рамках конкретного курса
# в качестве аргументов принимает список студентов и название курса

def student_rating(student_list, course_name):

    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Создаем функцию для подсчета средней оценки за лекции всех лекторов в рамках курса
# в качестве аргумента принимает список лекторов и название курса

def lecturer_rating(lecturer_list, course_name):

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

# Создаем функцию для подсчета средней оценки за домашние задания
# по всем студентам в рамках конкретного курса
# в качестве аргументов принимает список студентов и название курса


def student_rating(student_list, course_name):

    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Создаем функцию для подсчета средней оценки за лекции всех лекторов в рамках курса
# в качестве аргумента принимает список лекторов и название курса

def lecturer_rating(lecturer_list, course_name):

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all
