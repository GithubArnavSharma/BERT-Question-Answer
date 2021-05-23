import numpy as np
import torch
import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

model = pickle.load(open('C:/Users/arnie2014/Desktop/QAModel', 'rb'))
tokenizer = pickle.load(open('C:/Users/arnie2014/Desktop/tokenizer', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

def predict_result(question, paragraph):
  encoding = tokenizer.encode_plus(text=question,text_pair=paragraph)
  inputs = encoding['input_ids']
  sentence_embedding = encoding['token_type_ids'] 
  tokens = tokenizer.convert_ids_to_tokens(inputs)

  start_scores, end_scores = model(input_ids=torch.tensor([inputs]), token_type_ids=torch.tensor([sentence_embedding]), return_dict=False)
  start_index = torch.argmax(start_scores)
  end_index = torch.argmax(end_scores)

  answer = ' '.join(tokens[start_index:end_index+1])

  clean_answer = ''
  for word in answer.split():
    if word[0:2] == '##':
      clean_answer += word[2:]
    else:
      clean_answer += ' ' + word
  clean_answer = ' '.join(clean_answer.split())

  return clean_answer

@app.route('/predict',methods=['POST'])
def predict():
    question = str(request.json['question'])
    paragraph = str(request.json['paragraph'])
    answer = predict_result(question, paragraph)
    return jsonify({'result': answer})

if __name__ == "__main__":
    app.run(debug=True)
