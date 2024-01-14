from django.shortcuts import render,redirect
from .models import Topic,Room,Message,register,Profile
from .forms import Createform, ProfilePicForm
from django.contrib.auth import login
from django.db.models import Q   #This import for search box
from django.contrib.auth.decorators import login_required




def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    obj = Room.objects.filter(Q(topic__name__icontains =q) |
                              Q(name__icontains =q)|
                              Q(description__icontains=q))
    topic = Topic.objects.all()

    obj_count = obj.count()

    pro = Profile.objects.all()

    mess = Message.objects.all()

    context = {'key':obj,'topic':topic , 'obj_count':obj_count, 'pro':pro, 'mess':mess}
    return render(request,'app1/home.html',context)


def owner(request,pk):
    objs = Room.objects.get(id=pk)
    mess = objs.message_set.all().order_by('-created')

    if request.method =='POST':
        Mes = Message.objects.create(
            user=request.user,
            room = objs,
            body = request.POST.get('boo')
        )
        return redirect('owner', pk=objs.id)

    context = {'key':objs,'mess':mess}
    return render(request,'app1/owner.html',context)




def create(request):
    obj = Createform()
    if request.method=='POST':
        obj = Createform(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('home')
        
    context ={'form':obj}
    return render(request, 'app1/create.html',context)



def update(request,pk):
    obj = Room.objects.get(id=pk)
    form = Createform(instance=obj)
    if request.method=='POST':
        form = Createform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context ={'form':form}
    return render(request, 'app1/update.html',context)
        
    

def delete(request,pk):
    obj = Room.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    
    context ={'form':obj}
    return render(request, 'app1/delete.html',context)



def Register(request):
    obj = register()
    if request.method == 'POST':
        obj = register(request.POST)
        if obj.is_valid():
            check = obj.save()
            login(request, check)
            return redirect('home')

    return render(request,'app1/register.html',{'form':obj})


@login_required
def deletemessage(request,pk):
    obj = Message.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    
    context ={'form':obj}
    return render(request, 'app1/delete.html',context)



def profile_details(request):
    user = request.user

    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after profile picture change
    else:
        form = ProfilePicForm(instance=user.profile)

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'app1/profile_details.html', context)