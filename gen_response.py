from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
import os
import app_gemini
def generate_responses(total_responses,form_link):
  options = webdriver.ChromeOptions()
  options._binary_location = os.environ.get('GOOGLE_CHROME_BIN')
  options.add_argument("--headless")
  options.add_argument("--disable-dev-shm-usage")
  options.add_argument("--no-sandbox")
  
  driver= webdriver.Chrome(options=options,service=os.environ.get('CHROMEDRIVER_PATH'))
  questionsBucket = []
  optionsBucket = []
  try:
    form_page = driver.get(form_link)
    time.sleep(3)
    try:
      questions1 = driver.find_elements(By.CLASS_NAME,"Qr7Oae")
      for question in questions1:
        
        radiobuttons = question.find_elements(By.CLASS_NAME,"aDTYNe.snByac.OvPDhc.OIC90c")
        rangebuttons = question.find_elements(By.CLASS_NAME,"Zki2Ve")
        if rangebuttons==[] and radiobuttons==[]:
          continue
        else:
          questionsBucket.append(question.text.split("\n")[0])

        try:

          if radiobuttons!=[]:
            temp=[]
            for btn in radiobuttons:
                temp.append(btn.text)
            optionsBucket.append(temp)
            continue
        except:
          print("no radio buttons")
        try:
          
          if rangebuttons!=[]:
            temp=[]
            for btn in rangebuttons:
              temp.append(btn.text)
            optionsBucket.append(temp)
            continue
        except:
          print("no range buttons")
    except:
      print("")
  except:
    print("cant getttuu")
  time.sleep(2)
  print(questionsBucket,optionsBucket,"got ittt")
  while total_responses:
    responseAnswers = app_gemini.getGeminiResponse(questionsBucket,optionsBucket)
    resp_ptr=0
    form_page = driver.get(form_link)
    time.sleep(3)
    try:
      questions = driver.find_elements(By.CLASS_NAME,"Qr7Oae")
      for question in questions:
        
        radiobuttons = question.find_elements(By.CLASS_NAME,"aDTYNe.snByac.OvPDhc.OIC90c")
        rangebuttons = question.find_elements(By.CLASS_NAME,"Zki2Ve")
        if radiobuttons==[] and rangebuttons==[]:
          continue
        try:
          if radiobuttons!=[]:
            temp=[]
            
            rand_choice=responseAnswers[resp_ptr]
            resp_ptr+=1
            radiobuttons[rand_choice].click()
            continue
        except:
          print("no radio buttons")
        
        try:

          rand_choice=responseAnswers[resp_ptr]
          resp_ptr+=1
          rangebuttons[rand_choice].click()
          continue
        except:
          print("no range buttons")
      try:
        SubmitBtn = driver.find_element(By.CLASS_NAME,"uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd")
        SubmitBtn.click()
      except:
        print("no Submit BTN")
    except:
      print("cant get")
    total_responses-=1
    time.sleep(1)
    
# generate_responses(3,"https://docs.google.com/forms/d/e/1FAIpQLSdpb6AOaXRNqBa6VPCGjcs-v6QcQ12KHBHCpduiS18hoEM4Gw/viewform")
