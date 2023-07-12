import re
m_lines  = open('./movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
m_conversations = open('./movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')
idLine = {}
for line in m_lines:
    new_line = line.split(' +++$+++ ')
    if(len(new_line) == 5):
        idLine[new_line[0]] = new_line[4]
# Creating list of all conversations
conversations_ids = []
for conversation in m_conversations[:-1]:
	_conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
	conversations_ids.append(_conversation.split(","))
        
q=[]
a=[]
for conversation in conversations_ids:
     for i in range(len(conversation)-1):
          q.append(idLine[conversation[i]])
          a.append(idLine[conversation[i+1]])

# doing a first cleaning of the texts
def clean_text(text):
	text = text.lower()
	text = re.sub(r"i'm", "i am", text)
	text = re.sub(r"he's", "he is", text)
	text = re.sub(r"she's", "she is", text)
	text = re.sub(r"that's", "that is", text)
	text = re.sub(r"what's", "what is", text)
	text = re.sub(r"where's", "where is", text)
	text = re.sub(r"\'ll", " will", text)
	text = re.sub(r"\'ve", " have", text)
	text = re.sub(r"\'re", " are", text)
	text = re.sub(r"\'d", " would", text)
	text = re.sub(r"won't", "will not", text)
	text = re.sub(r"can't", "can not", text)
	text = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", text)
	return text

clean_questions = list(map(clean_text, q))
clean_answers =  list(map(clean_text, a))

wordCounter = {}

for i in clean_questions:
    for word in i.split():
        if word not in wordCounter:
            wordCounter[word] = 1
        else:
            wordCounter[word]+=1
for i in clean_answers:
    for word in i.split():
        if word not in wordCounter:
            wordCounter[word] = 1
        else:
            wordCounter[word]+=1

minimum = 20
qWordInt = {}
nWord=0
aWordInt = {}
for word,count in wordCounter.items():
    if count > minimum:
        qWordInt[word] = nWord
        qWordInt[word] = nWord
        nWord+=1
    
tokens = ['<PAD>', '<EOS>', '<OUT>', '<SOS>']
for token in tokens:
	qWordInt[token] = len(qWordInt)+1
	aWordInt[token] = len(aWordInt) + 1