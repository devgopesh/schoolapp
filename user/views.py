from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .forms import AssignmentForm
from .models import Assignment


# Create your views here.

def base(request):

    if request.method == 'POST':
        selected_option = request.POST["option"] 
        if selected_option == "teacher":
            return render(request, 'home.html')
            
        elif selected_option == 'student':
            st = User.objects.all()
            return render(request, 'student.html', {'st':st})
        else:
            return HttpResponse(404)




    return render(request, 'base.html')


def basic(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':


        val3 = request.POST['username']
        val4 = request.POST['password']

        user = auth.authenticate(username=val3, password=val4)

        if user is not None:
            auth.login(request, user)
            # print(request.user)
            id=request.user.id
            # print(type(pk))
            # print(pk)
            return redirect("user:list", id=id)
        else:
            return redirect('user:login')

    else:
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        val1 = request.POST['first_name']
        val2 = request.POST['last_name']
        val3 = request.POST['username']
        val4 = request.POST['password']
        val5 = request.POST['confirm']

        if val4 == val5:
            if User.objects.filter(username=val3).exists():
                msg = 'username taken'
                
                return render(request, 'register.html', {'msg':msg})
            else:


                user = User.objects.create_user(username = val3, password = val4, first_name = val1, last_name = val2)
                user.save()
                # pk = user.instance.pk
                return redirect("user:login")

        else:
            return redirect('user:register')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



def assign(request):
    form = AssignmentForm
    if request.method == "POST":

        user = request.user
        x = (User.objects.all())
        print(user)
        print(x)
        if user in x:
            # userid = request.user.id

            form = AssignmentForm(request.POST or None)
            if form.is_valid():
                form.save()
                form.user = user
                form.save()

                id = request.user.id

                # obj = User.objects.get(pk=request.user.id)
                # print(obj).values()
                # obj.user_id.add(request.user.id)
                # obj.save()
                # print(obj)
                # v = {
                # 'form':form,
                # 'userid':userid
                # }
                # form.save()
                
                # order = request.user.assignment.order_set.all()
                # print(order)
                # pk = form.instance.pk
                # print(pk)

                
                
                return redirect('user:list', id=id)
            
            return redirect("user:assign")
        else:
            return redirect('user:login')
       

    return render(request, 'assign.html', {'form':form})
            
def list(request, id):
    obj = Assignment.objects.filter(id=id).all()
    print(obj)
    obj1 = Assignment.objects.all()
    print(obj1.values())
    #  print(request.user)
    # id = request.user.id
    # obj = request.user.user.assignment_set.all()
    # obj1 = User.objects.get(pk=id)
    # print(obj1)
    # print()
    # obj = Assignment.objects.filter(user=request.user)
    # user=request.user
    # print(Assignment.user.id)
    # if pk:
    # u = User.objects.get(pk=pk)
    # obj=u.q.all()
    # print(u)
    # obj = Assignment.objects.filter(user__pk=u.pk)
    # else:
    #     obj = request.user
    # print(request.user.id)
    # obj = list(filter(lambda: Assignment.user.id==request.user.id, object))
    print((obj).values())

    # print(obj.assignment.ques)


    return render(request, 'list.html', {'obj':obj})






def student(request):
    st = User.objects.all()
    return render(request, 'student.html', {'st':st})

        


        
        