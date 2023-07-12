import os
import random
import json
import pickle
import numpy as np
import nltk
import sys
import re

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from database import db

names = ['luke skywalker','c-3po','darth vader','owen lars','beru whitesun lars','r5-d4','biggs darklighter','anakin skywalker','shmi skywalker','cliegg lars','r2-d2','palpatine','padmé amidala','jar jar binks','roos tarpals','rugor nass','ric olié','quarsh panaka','gregar typho', 'cordé']
not_nouns = ['specie', 'height', 'vehicles', 'starships', 'planet', 'planets', 'day', 'population', 'father']

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

def find_similar_name(name):
  if (len(name) > 0):
    for n in names:
      if n.lower() in name.lower():
        return n

  return name

def not_found_handle():
  return "apologies", " "

def category_not_determined():
  return "apologies", " "

def classify_noun(noun):
  similar_name = find_similar_name(noun).lower()
  print("similar name", similar_name)
  rgx = re.compile(f'{similar_name}', re.IGNORECASE)
  people = db.peoples.find_one({"name": rgx})
  if people:
    return "peoples", similar_name
  
  species = db.species.find_one({"name": similar_name})
  if species:
    return "species", similar_name

  vehicles = db.vehicles.find_one({"name": similar_name})
  if vehicles:
    return "vehicles", similar_name

  planets = db.planets.find_one({"name": similar_name})
  if planets:
    return "planets", similar_name

  return None, None

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
  noun = extract_noun(nltk_results)

  if isinstance(noun, list):
    result_noun = noun = " ".join(noun)
    category, similar_name = classify_noun(result_noun)
    rgx = re.compile(f'{similar_name}', re.IGNORECASE) 
    query = { "name": rgx }
  else:
    category = classify_noun(noun.lower())
    rgx = re.compile(f'{noun.lower()}', re.IGNORECASE) 
    query = { "name": rgx }
    
  tag = intents_list[0]['intent']
  
  if category:
    collection = db[category]
    query_res = collection.find_one(query)
    
    if tag in [ 'vehicles', 'starships', 'films', 'species', 'residents']:
      sub_res = []
      if tag == 'residents':
        sub_collection = db['peoples']
      else:
        sub_collection = db[tag]
        
      ar = query_res[tag]

      for a in ar:
        sub_query = { "url": a }
        if tag in 'films':
          sub_res.append(sub_collection.find_one(sub_query)["title"])
        else:
          sub_res.append(sub_collection.find_one(sub_query)["name"])
      res = sub_res

      if len(sub_res) == 0:
        tag, res = not_found_handle()

    elif tag in [ 'homeworld' ]:
        sub_collection = db['planets']
        sub_query = { "url": query_res[tag] }
        sub_res = sub_collection.find_one(sub_query)["name"]
        res = sub_res

    else:
      if tag in query_res:
        res = query_res[tag]
  else:
    tag, res = not_found_handle()
  
  # else:
  #   tag, res = category_not_determined()

  list_of_intents = intents_json['intents']
  result = find_result(tag, res, list_of_intents, noun)

  return result

def extract_noun(nltk_results):
  nouns = []

  for nltk_result in nltk_results:
    if isinstance(nltk_result, Tree):
      name = ' '.join([nltk_result_leaf[0] for nltk_result_leaf in nltk_result.leaves()])
      nouns.append(name)
      print('Type:', nltk_result.label(), 'Name:', name)
    elif isinstance(nltk_result, tuple) and nltk_result[1].startswith('NN'):
      noun = nltk_result[0]
      if noun.lower() not in not_nouns:
        nouns.append(noun)
        print('Noun:', noun)
  return nouns

def find_result(tag, res, list_of_intents, character):
  for intent in list_of_intents:
    if intent['tag'] == tag:
      if isinstance(res, list):
        if (len(res) == 1):
          res = ", ".join(res)
          result = random.choice(intent['responses']['singular'])
        else:
          res = ", ".join(res)
          result = random.choice(intent['responses']['multiple'])
      else:
        result = random.choice(intent['responses']['singular'])
      result = result.replace("{name}", character)
      result = result.replace("{response}", res)
  return result

if __name__ == '__main__':
  print('GO, BOT IS RUNNING')
  counter = 0
  max_iterations = 2

  while counter < max_iterations:
    message = input('')
    ints = predict_class(message)
    print('message', message)
    print('ints', ints)
    res = get_response(ints, intents, message)
    print(res)
    counter += 1
