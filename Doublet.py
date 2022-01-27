def readwords():
  file=open('word.txt','r')
  words=file.readlines()
  file.close()
  return words 

line=readwords()
step=[]
filtered_list=[]

def checkedin(word):
  for x in filtered_list:
    if x[0]==word:
      return 'yes'
      break
  return 'no'

def check(word):
  for x in line:
    if x.replace('\n','')==word:
      return 'yes'
      break
  return 'no'


def filtered_words(word,parent):
 if check(word)=='yes':
   if checkedin(word)=='no':
      filtered_list.append([word,parent])


def find(doublet1):
  abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for e in abc:
    filtered_words(format(doublet1[0:3])+e+format(doublet1[4:5]),doublet1)
    filtered_words(format(doublet1[0:2])+e+format(doublet1[3:5]),doublet1)
    filtered_words(format(doublet1[0:1])+e+format(doublet1[2:5]),doublet1)
    filtered_words(format(doublet1[0:0])+e+format(doublet1[1:5]),doublet1)
    filtered_words(format(doublet1[0:4])+e+format(doublet1[5:5]),doublet1)

def steps(a,b):
  for x in filtered_list:
    if (x[0]==a and x[0]!=b):
      step.append(x[1])
      steps(x[1],b)
# here you can insert 2 words
start='flour'
end='bread'

find(start)

for x in filtered_list:
  if x[0]==end:
    print('======Found======')
    print(start.upper(),' to ',end.upper())
    steps(end,start)
    break
  else:
   find(x[0])

print(step)

