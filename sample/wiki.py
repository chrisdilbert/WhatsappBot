import wikipedia
import wolframalpha
from googleTest import google_search

app_id = "4W6ERL-42QRJYYK8U"
client = wolframalpha.Client(app_id)
defaultMessage="Hey Ravindra is currently Busy.Meanwhile You can ask me questions. \n i.e wiki:Thomas Edison \n wiki:9+7+8"
def getAnswer(message):
    if message and message.strip().startswith('wiki:'):
       message=message.strip()
       message=message[5:]
       input = message
       input = input.lower()
       try:
          res = client.query(input)
          answer = next(res.results).text
          return answer
       except:
       	     try:
                print('Searching Wiki')
                return  wikipedia.summary(input)
       	     except:
                   try:
                      print('Searching google')
                      return google_search(input)
                   except:
       	   	              return "I don't know"

    else:
        return defaultMessage

print(getAnswer('wiki:Virat Kohali'))