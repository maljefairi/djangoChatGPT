# hello_world/views.py

from django.shortcuts import render, redirect
from .models import ChatSession, ChatMessage, DefaultChatSettings
from .forms import ChatForm  # Make sure you have created a form
from .chat import chat_with_gpt4  # Make sure you have created a function named chat_with_gpt4

def index(request):
    # You can pass variables to your template via context if you need to
    context = {}
    return render(request, 'hello_world/index.html', context)
# views.py

def sessions_view(request):
    if 'session_id' in request.GET:
        session_id = request.GET['session_id']
        if ChatSession.objects.filter(id=session_id).exists():
            request.session['chat_session'] = session_id
        return redirect('chat_view')

    sessions = ChatSession.objects.all()
    return render(request, 'sessions.html', {'sessions': sessions})

def chat_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data.get('message')
            # Get session_id from session, create a new one if it doesn't exist
            session_id = request.session.get('chat_session', None)
            if session_id is None:
                session = ChatSession.objects.create()
                request.session['chat_session'] = session.id
            else:
                session = ChatSession.objects.get(id=session_id)
            # Create a new ChatMessage with user's message
            ChatMessage.objects.create(session=session, role="user", content=user_message)
            # Chat with GPT-4 and get a response
            assistant_message = chat_with_gpt4(session, user_message)
            # Create a new ChatMessage with assistant's message
            ChatMessage.objects.create(session=session, role="assistant", content=assistant_message)
            return redirect('chat_view')
    else:
        form = ChatForm()
        # Get session_id from session, create a new one if it doesn't exist
        session_id = request.session.get('chat_session', None)
        if session_id is None:
            session = ChatSession.objects.create()
            request.session['chat_session'] = session.id
        else:
            session = ChatSession.objects.get(id=session_id)

    # Get all messages
    messages = session.messages.all()

    return render(request, 'chat.html', {'form': form, 'messages': messages})

