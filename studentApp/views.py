from django.shortcuts import render,redirect
from django.views import View
from instructorApp.models import Course,Cart,Order
from instructorApp.forms import InstructorCreateForm
from instructorApp.models import User
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
import razorpay
from django.db.models import Sum

# Create your views here.




class StudentRegister(View):
    def get(self,request):
        return render(request,"student_register.html")
    
    def post(self,request):
        fname=request.POST.get("first_name")
        uname=request.POST.get("username")
        email=request.POST.get("email")
        pswrd=request.POST.get("password")
        try:
            User.objects.create_user(first_name=fname,username=uname,email=email,password=pswrd)
            messages.success(request,"Registration successful")
            print(fname, uname, email, pswrd)
            return redirect("student_log")
        except:
            messages.warning(request,"invalid input")
            print(fname, uname, email, pswrd)
            return redirect("student_reg")

class StudentLoginView(View):
    def get(self,request):
        return render(request,'student_register.html')
    
    def post(self,request):
        usrnm=request.POST.get("username")
        pswrd=request.POST.get("password")
        res=authenticate(request,username=usrnm,password=pswrd)
        if res:
            login(request,res)
            if res.role=='student':
                return redirect("student_view")
    


class StudentView(View):
    def get(self,request):
        courses=Course.objects.all()
        return render(request,"student_home.html",{'courses':courses})

class CourseDetailView(View):
    def get(self,request,**kwargs):
        course=Course.objects.get(id=kwargs.get("id"))
        return render(request,'course_detail.html',{'course':course})
    
def login_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("student_log")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

    
@method_decorator(login_required,name="dispatch")
class AddToCartView(View):
    def get(self,request,**kwargs):
        course_instance=Course.objects.get(id=kwargs.get("id"))
        user_instance=request.user
        res_instance,created=Cart.objects.get_or_create(course_instance=course_instance,user_instance=user_instance)
        print(res_instance,created)
        return redirect("student_view")
    
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("student_log")
    

@method_decorator(login_required,name="dispatch")
class CartSummary(View):
    def get(self,request):
        cart_list=Cart.objects.filter(user_instance=request.user)
        total_price=sum([item.course_instance.price for item in cart_list])
        return render(request,'cart_summary.html',{'cart_list':cart_list,'total_price':total_price})
    
class CartDeleteView(View):
    def get(self,request,**kwargs):
        Cart.objects.get(id=kwargs.get("id")).delete()
        return redirect("cart_summary")
    
class CheckOutView(View):
    def get(self,request):
        cart_list=request.user.user_cart.all()
        total_price=cart_list.aggregate(sum=Sum("course_instance__price")).get("sum") or 0
        order_instance=Order.objects.create(student=request.user,total=total_price)
        if cart_list:
            for cart in cart_list:
                order_instance.course_instances.add(cart.course_instance)
                cart.delete()
            
        return render(request,"payment.html")


