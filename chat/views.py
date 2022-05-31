from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse


def ChatVox_Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            login(request,user)
            # messages.success(request,'Login')
            return redirect(reverse('home'))
        else:
            messages.error(request,'UserName and password is incorrect')

    return render(request,'myapp/ChatVox_Login.html')


def home_Chat(request):
    if request.method == "POST":
        room = request.POST['room_name']
        username = request.POST['username']

        if Room.objects.filter(name=room).exists():
            return redirect('/'+room+'/?username='+username)
        else:
            new_room = Room.objects.create(name=room)
            new_room.save()
            return redirect('/'+room+'/?username='+username)
    return render(request,'myapp/home.html')



def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'myapp/room.html', {'username': username, 'room': room, 'room_details': room_details })


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))














































































# def checkview(request):
#     room = request.POST['room_name']
#     username = request.POST['username']

#     if Room.objects.filter(name=room).exists():
#         return redirect('/'+room+'/?username='+username)
#     else:
#         new_room = Room.objects.create(name=room)
#         new_room.save()
#         return redirect('/'+room+'/?username='+username)

# def send(request):
#     message = request.POST['message']
#     username = request.POST['username']
#     room_id = request.POST['room_id']

#     new_message = Message.objects.create(value=message, user=username, room=room_id)
#     new_message.save()
#     return HttpResponse('Message sent successfully')

# def getMessages(request, room):
#     room_details = Room.objects.get(name=room)

#     messages = Message.objects.filter(room=room_details.id)
#     return JsonResponse({"messages":list(messages.values())})