#Import neccessary modules
import numpy as np
import torch
import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

#Load the Question Answering Model and the Tokenizer
model = pickle.load(open('C:/Users/arnie2014/Desktop/QAModel', 'rb'))
tokenizer = pickle.load(open('C:/Users/arnie2014/Desktop/tokenizer', 'rb'))

#Render the home template from index.html 
@app.route('/')
def home():
    return render_template('index.html')

#Function that inputs question and its context and outputs an answer 
def predict_result(question, paragraph):
  #Encode the question + [SEP] + paragraph 
  encoding = tokenizer.encode_plus(text=question,text_pair=paragraph)
  inputs = encoding['input_ids'] #Tokenized word ids to represent every word 
  sentence_embedding = encoding['token_type_ids'] #Classify each word as 0(question) or 1(passage)
  tokens = tokenizer.convert_ids_to_tokens(inputs) #Transform the input ids into a list of words and seperators

  #Get the scores of each word on the probability of them being the start or end word
  start_scores, end_scores = model(input_ids=torch.tensor([inputs]), token_type_ids=torch.tensor([sentence_embedding]), return_dict=False) 
  #Get the index of the start and the end 
  start_index = torch.argmax(start_scores)
  end_index = torch.argmax(end_scores)

  #Using the tokens(as the index is based off of them), get the answer
  answer = ' '.join(tokens[start_index:end_index+1])

  #The tokens are encoded in such a way where seperations are added through ##, so removing that will make the answer cleaner
  clean_answer = ''
  for word in answer.split():
    if word[0:2] == '##':
      clean_answer += word[2:]
    else:
      clean_answer += ' ' + word
  clean_answer = ' '.join(clean_answer.split())

  #Return the cleaned answer
  return clean_answer

#Function for the /predict task, which takes a question and input passgae and using the predict_result function to return predictions
@app.route('/predict',methods=['POST'])
def predict():
    question = str(request.json['question'])
    paragraph = str(request.json['paragraph'])
    answer = predict_result(question, paragraph)
    return jsonify({'result': answer})

#Run the app
if __name__ == "__main__":
    app.run(debug=True)
