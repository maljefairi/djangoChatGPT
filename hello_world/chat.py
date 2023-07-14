# hello_world/chat.py

import os
import openai
from .models import ChatMessage

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt4(session, user_message):
    # Get previous messages
    previous_messages = ChatMessage.objects.filter(session=session)
    messages = [{
        "role": msg.role,
        "content": msg.content
    } for msg in previous_messages]

    # Add user's current message
    messages.append({
        "role": "user",
        "content": user_message
    })

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=256
    )

    # Return the assistant's message
    return response['choices'][0]['message']['content']
