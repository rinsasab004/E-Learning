from django.shortcuts import render
from django.views import View
from instructorApp.models import Course

# Create your views here.
class StudentView(View):
    def get(self,request):
        courses=Course.objects.all()
        return render(request,"student_home.html",{'courses':courses})
