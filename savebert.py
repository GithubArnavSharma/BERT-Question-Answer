import pickle
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer

model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

pickle.dump(model, open('QAModel', 'wb'))
pickle.dump(tokenizer, open('tokenizer', 'wb'))
