from django.shortcuts import render,redirect
from .models import ChatRoom, ChatMessage
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



def index(request):
    user = request.user
    chatrooms = ChatRoom.objects.all()
    context = {'chatrooms': chatrooms,'user':user}
    return render(request, 'chatapp/index.html', context)


def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)[0:30]
    context = {'chatroom': chatroom, 'messages': messages}
    return render(request, 'chatapp/room.html', context)

