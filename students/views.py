from django.shortcuts import render
from .models import Student

def dashboard(request):
    return render(request, 'dashboard.html')

def student_login(request):
    roll = request.GET.get('roll_no')
    student = None
    if roll:
        try:
            student = Student.objects.get(roll_no=roll)
        except Student.DoesNotExist:
            student = None
    return render(request, 'student_login.html', {'student': student})
def home(request):
    return render(request, 'student_portal/index.html')


def leaderboard(request):
    top_students = sorted(Student.objects.all(), key=lambda x: x.total(), reverse=True)[:3]
    return render(request, 'leaderboard.html', {'top_students': top_students})
