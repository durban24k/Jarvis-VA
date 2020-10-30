import JarvisAI
import re
import pprint
import random

obj=JarvisAI.JarvisAssistant()

def t2s(text):
     obj.text2speech(text)

while True:
     res=obj.mic_input()

     if re.search('what can you do', res):
          li_commands = {
               "open websites": "Example: 'open youtube.com",
               "time": "Example: 'what time it is?'",
               "date": "Example: 'what date it is?'",
               "launch applications": "Example: 'launch chrome'",
               "tell me": "Example: 'tell me about India'",
               "weather": "Example: 'what weather/temperature in Mumbai?'",
               "news": "Example: 'news for today' ",
          }
          ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
          I can open websites for you, launch application and more. See the list of commands-"""
          print(ans)
          pprint.pprint(li_commands)
          t2s(ans)