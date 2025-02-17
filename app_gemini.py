from google import genai
from google.genai import types
question = ["AGE","gender","education"]
options = [["17 to 20","21 to 30"],["male","female"],["undergraduate","postgraduate"]]
def getGeminiResponse(question,options):
    client = genai.Client(api_key="AIzaSyAmgD8UCMqU6Q8PexJGF67TZwWZl1Pd0WY")

    prompt = "Help me fill this form giving human-like reliable responses assuming you are a random person everytime by choosing the options and return only the option number instead of values in the pattern [question number].[space][answer]\n"
    for i in range(len(question)):
        prompt=prompt+str(i+1)+question[i]+"\n"
        
        prompt=prompt+"Choices: "+str(options[i])+"\n"


    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt
    )
    responseContent = response.text
    print(responseContent)
    ans=[]
    for i in range(len(responseContent)):
        if responseContent[i].isdigit() and responseContent[i+1]=="." and responseContent[i+3].isdigit():
            ans.append(int(responseContent[i+3])-1)
    # print(get_parsed_response.get_parsed_response(responseContent))
    print(ans)
    return ans