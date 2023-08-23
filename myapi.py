import paralleldots as pd




class API:

    def __init__(self):
        pd.set_api_key('e8ZjNG8Q0fkKeJhapMIbEoZIWBRhe0exbl2r5wwzDb4' )

    def analyse(self,text):
        result= pd.sentiment(text)
        return result

