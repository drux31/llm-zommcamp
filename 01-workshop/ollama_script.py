from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='tinyllama', messages=[
  {
    'role': 'user',
    'content': 'what is a flower?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
# print(response.message.content)