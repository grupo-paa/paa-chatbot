import os
import random
import json
import pickle
import numpy as np
import requests
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import load_model

lemmatizer = WordNetLemmatizer()

intents_path = os.path.join(os.path.dirname(__file__), 'intents.json')
with open(intents_path) as file:
  intents = json.load(file)

words_path = os.path.join(os.path.dirname(__file__), 'words.pkl')
with open(words_path, 'rb') as file:
  words = pickle.load(file)

classes_path = os.path.join(os.path.dirname(__file__), 'classes.pkl')
with open(classes_path, 'rb') as file:
  classes = pickle.load(file)

model_path = os.path.join(os.path.dirname(__file__), 'chatbot_model.h5')
model = load_model(model_path)

def clean_up_sentence(sentence):
  sentence_words = nltk.word_tokenize(sentence)
  sentence = [lemmatizer.lemmatize(word) for word in sentence_words]

  return sentence_words

def bag_of_words(sentence):
  sentence_words = clean_up_sentence(sentence)
  bag = [0] * len(words)
  for w in sentence_words:
    for i, word in enumerate(words):
      if word == w:
        bag[i] = i
  return np.array(bag)

def predict_class(sentence):
  bow = bag_of_words(sentence)
  res = model.predict(np.array([bow]))[0]

  ERROR_THRESHOLD = 0.25
  results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

  results.sort(key=lambda x: x[1], reverse=True)
  return_list = []
  for r in results:
    return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
  return return_list

def get_response(intents_list, intents_json, message):
  
  nltk_results = ne_chunk(pos_tag(word_tokenize(message)))
  character = ''
  for nltk_result in nltk_results:
    if type(nltk_result) == Tree:
      name = ''
      for nltk_result_leaf in nltk_result.leaves():
        name += nltk_result_leaf[0] + ' '
      character = name
      print ('Type: ', nltk_result.label(), 'Name: ', name)
  
  print(intents_list)
  tag = intents_list[0]['intent']
  url = f"https://swapi.dev/api/people/?search={character}"
  res = requests.get(url)
  print(res.json()['results'][0][tag])
  list_of_intents = intents_json['intents']
  for i in list_of_intents:
    if i['tag'] == tag:
      result = random.choice(i['responses'])
      break
  return result


if __name__ == '__main__':
  print('GO, BOT IS RUNNING')
  counter = 0
  max_iterations = 5

  while counter < max_iterations:
    message = input('')
    ints = predict_class(message)
    print('message', message)
    print('ints', ints)
    res = get_response(ints, intents, message)
    print(res)
    counter += 1
