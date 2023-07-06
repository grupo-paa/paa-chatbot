import random
import json
import pickle
import numpy as np
import nltk
import matplotlib.pyplot as plt

from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
  for pattern in intent['patterns']:
    word_list = nltk.word_tokenize(pattern)
    words.extend(word_list)
    documents.append((word_list, intent['tag']))

    if intent['tag'] not in classes:
      classes.append(intent['tag'])

lemmatizer = WordNetLemmatizer()
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters]

words = sorted(set(words))
classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)

for document in documents:
  bag = []
  word_patterns = document[0]
  word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]

  for word in words:
    bag.append(1) if word in word_patterns else bag.append(0)

  output_row = list(output_empty)
  output_row[classes.index(document[1])] = 1
  training.append([bag, output_row])

random.shuffle(training)
training = np.array(training, dtype=object)

train_x = list(training[:, 0]) # features of the training data
train_y = list(training[:, 1]) # labels for the training data

model = Sequential()

# the second parameter (len(train_x[0]),) is empty because it represents a single-dimensional input
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu')) # fully connected layer in the neural network
model.add(Dropout(0.2)) # prevent overfitting
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(len(train_y[0]), activation='softmax')) # The number of neurons in this layer is determined by the number of classes in train_y

sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.h5')
print('Done')

def loss_chart():
  plt.plot(hist.history['loss'])
  plt.title('Training Loss')
  plt.xlabel('Epochs')
  plt.ylabel('Loss')
  plt.show()

def accuracy_chart():
  plt.plot(hist.history['accuracy'])
  plt.title('Training Accuracy')
  plt.xlabel('Epochs')
  plt.ylabel('Accuracy')
  plt.show()

loss_chart()
accuracy_chart()
