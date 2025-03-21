from django.shortcuts import render
def student_list(request): 
    students = [ 
        {'name': 'Prameela', 'marks': 37}, 
        {'name': 'Mythri', 'marks': 89}, 
        {'name': 'Mahitha', 'marks': 80}, 
        {'name': 'Eshwari', 'marks': 96}, 
    ] 
    passing_marks = 40   
    return render(request, 'std_app/student_list.html', 
{'students': students, 'passing_marks': passing_marks}) 
