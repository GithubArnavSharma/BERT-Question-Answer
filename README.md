# BERT-Question-Answer
BERT is a Bidirectional Encoder Representation from Transformers which consists of encoders pre-trained with the task to understand human language. BERT was initially pre-trained simultaneously based on predicting whether two sentences are continous and completing fill in the blank questions. The Question Answering BERT was a fine tuned version of BERT which is able to highlight answers to a question from a given passage. It does this by training a start and end vector, and along with BERT's representation of every word, it computes the dot product followed by a softmax activation over all the dot products for all the words. The purpose of this is to compute the probability of a word being the start or end word of the answer. 

This project involved using BERT pre-trained off of the Stanford Question Answering Dataset to create a local server website to test out BERT. The trask was done using Python's Flask, HTML, CSS, and Javascript. The results of the website:

https://user-images.githubusercontent.com/77365987/119275524-74112280-bbca-11eb-90f5-2d21f737e9d1.mov
