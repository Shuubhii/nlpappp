from paralleldots.config import set_api_key
from paralleldots.paralleldots_apis import get_sentiment as sentiment
import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key('e8ZjNG8Q0fkKeJhapMIbEoZIWBRhe0exbl2r5wwzDb4')

    def analyse(self,text):
        result= paralleldots.sentiment(text)
        return result
    
    def ner(self,text):
        result= paralleldots.ner(text)
        return result

    def emotion(self,text):
        result=paralleldots.emotion(text)
        return result