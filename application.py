from flask import Flask, render_template, request
from gen_response import generate_responses
import os

app=Flask(__name__)
form_link = None
port=int(os.environ.get('PORT',5001))
@app.route("/",methods=["GET", "POST"])
def index():
  return render_template('index.html')
@app.route("/generate_responses",methods=["GET","POST"])
def generate():
  if request.method == "POST":
    no_of_resp=int(request.form['resp'])
    form_link=request.form['link']
  
  try:
    generate_responses(no_of_resp,form_link)
    return "SUCCESS"
  except:
    return "ERROR"
if __name__=='__main__':
  app.run(host='0.0.0.0',port=port)