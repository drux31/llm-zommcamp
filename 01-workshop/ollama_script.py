from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='tinyllama', messages=[
  {
    'role': 'user',
    'content': 'how often a cow poops?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
# print(response.message.content)