## Sentiments analysis using Python applied to French political speeches
## Lexicons (positive and negative words) used : Chen, Y., & Skiena, S. (2014). Building Sentiment Lexicons for All Major Languages. In ACL (2) (pp. 383-389).

import matplotlib.pyplot as plt
import numpy as np

class Speech:
	# name of the speaker
	# year of the speech
	# nb of positive words
	# nb of negative words
	# nb total of words
	# (positive - negative)/size
    def __init__(self, name, year, nbPositiveWords, nbNegativeWords, nbTotalWords):
        self.name = name
        self.year = year
        self.nbPositiveWords = nbPositiveWords 
        self.nbNegativeWords = nbNegativeWords 
        self.nbTotalWords = nbTotalWords
        self.ratio = (nbPositiveWords-nbNegativeWords)/nbTotalWords*100 # Here, I divide by the number of words because some speeches are longer than others.

def getLexicons(positiveList, negativeList):
	## Open positive lexicon 
	positiveLex = open('positive_words_fr.txt', 'r')
	for words in positiveLex:
		word=words.rstrip("\n") # to eliminate the line break
		positiveList.append(word) # add the word to the list

	## Negative lexicon 
	negativeLex = open('negative_words_fr.txt', 'r')
	for words in negativeLex:
		word=words.rstrip("\n") # to eliminate the line break
		negativeList.append(word) # add the word to the list

	## close the files
	positiveLex.close()
	negativeLex.close()

	return positiveList, negativeList
	
def getSpeechAnalysis(speechName, name, year, positiveList, negativeList): 
	# speechName : name of the file (ex '.\speech\Macron2018.txt')
	# name : name of the speaker
	# year : year of the speech
	# positiveList, negativeList : lexicons generated before
	
	## Open the speech
	speech = open(speechName, 'r')      
	speechList = [] # create a list where we are going to put all the words
	for line in speech:
		word=line.rstrip(" ").split()    # to eliminate the unwanted blanks and turn the line into a list of words
		for element in word: # now, we have words but we have to check that their end isn't a special character
			if element[-1]=='.' or element[-1]==",": # to eliminate the point or comma at the end of the word
				element = element[:-1]
			speechList.append(element.lower()) # we add the word to the list (lowercase to ease later search)

	## Count the nb of positive words and negative words
	positiveWords = 0
	negativeWords = 0
	for words in speechList: # we browse the speech
		if positiveList.count(words)==1: # if the word is a positive one
			positiveWords+=1
		if negativeList.count(words)==1: # if the word is a negative one
			negativeWords+=1
	
	## Close the files
	speech.close()

	# we create a speech
	speechClass = Speech(name, year, positiveWords, negativeWords, len(speechList))
	return speechClass


## Initialization
positiveList = []
negativeList = []
getLexicons(positiveList, negativeList)

# list of all the speeches, speakers and years:
# if you want to add a speech, add it at the end of the array
# the speeches should be ordered by speakers : you can't add a 'Macron's speech' between two 'Hollande's speeches' for instance
Files = [
			# ['Name', year, 'speechfile'],
			[ 'Macron', 2018, 'Macron2018_voeux.txt'],
			[ 'Hollande', 2017, 'Hollande2017_voeux.txt'],
			[ 'Hollande', 2016, 'Hollande2016_voeux.txt'],
			[ 'Hollande', 2015, 'Hollande2015_voeux.txt'],
			[ 'Hollande', 2014, 'Hollande2017_voeux.txt'],
			[ 'Hollande', 2013, 'Hollande2013_voeux.txt'],
			[ 'Sarkozy', 2012, 'Sarkozy2012_voeux.txt'],
			[ 'Sarkozy', 2011, 'Sarkozy2011_voeux.txt'],
			[ 'Sarkozy', 2010, 'Sarkozy2010_voeux.txt'],
			[ 'Sarkozy', 2009, 'Sarkozy2009_voeux.txt'],
			[ 'Sarkozy', 2008, 'Sarkozy2008_voeux.txt'],
			[ 'Chirac', 2007, 'Chirac2007_voeux.txt'],
			[ 'Chirac', 2006, 'Chirac2006_voeux.txt'],
			[ 'Chirac', 2005, 'Chirac2005_voeux.txt'],
			[ 'Chirac', 2004, 'Chirac2004_voeux.txt'],
			[ 'Chirac', 2003, 'Chirac2003_voeux.txt'],
			[ 'Chirac', 2002, 'Chirac2002_voeux.txt'],
			[ 'Chirac', 2001, 'Chirac2001_voeux.txt'],
			[ 'Chirac', 2000, 'Chirac2000_voeux.txt'],
			[ 'Chirac', 1999, 'Chirac1999_voeux.txt'],
			[ 'Chirac', 1998, 'Chirac1998_voeux.txt'],
			[ 'Chirac', 1997, 'Chirac1997_voeux.txt'],
			[ 'Chirac', 1996, 'Chirac1999_voeux.txt'],
			[ 'Mitterand', 1995, 'Mitterand1995_voeux.txt'],
			[ 'Mitterand', 1994, 'Mitterand1994_voeux.txt'],
			[ 'Mitterand', 1993, 'Mitterand1993_voeux.txt'],
			[ 'Mitterand', 1992, 'Mitterand1992_voeux.txt'],
			[ 'Mitterand', 1991, 'Mitterand1991_voeux.txt'],
			[ 'Mitterand', 1990, 'Mitterand1990_voeux.txt'],
			[ 'Mitterand', 1989, 'Mitterand1989_voeux.txt'],
			[ 'Mitterand', 1988, 'Mitterand1988_voeux.txt'],
			[ 'Mitterand', 1987, 'Mitterand1987_voeux.txt'],
			[ 'Mitterand', 1986, 'Mitterand1986_voeux.txt'],
			[ 'Mitterand', 1985, 'Mitterand1985_voeux.txt'],
			[ 'Mitterand', 1984, 'Mitterand1984_voeux.txt'],
			[ 'Mitterand', 1983, 'Mitterand1983_voeux.txt'],
			[ 'Mitterand', 1982, 'Mitterand1982_voeux.txt'],
			[ 'Giscard', 1981, 'Giscard1981_voeux.txt'],
			[ 'Giscard', 1979, 'Giscard1979_voeux.txt'],
			[ 'Giscard', 1975, 'Giscard1975_voeux.txt']
		]

## Results
# array where we are going to put all the results:
speeches = []
# we apply the function to all the speeches
sizeOfFiles = len(Files)
for i in range(sizeOfFiles-1, -1, -1): # browse all the array from end to beginning
	speeches.append(getSpeechAnalysis('.\speech\\'+Files[i][2], Files[i][0], Files[i][1], positiveList, negativeList))
	
# we fill up the informations for all the presidents
iFiles = 0

# do the grouping
Result = []
nameOfSpeaker = "" # at the beginning, the speaker is not defined 
ratio = []
year = []
while (iFiles<sizeOfFiles):
	if nameOfSpeaker!=speeches[iFiles].name: # if the speaker changes
		if (len(nameOfSpeaker)>0): # if the speaker is defined (that doesn't happen when nameOfSpeaker = "")
			Result.append([nameOfSpeaker, ratio, year]); # we add its name, its ratio list and year list 
		nameOfSpeaker=speeches[iFiles].name # we change the name of the actual speaker
		ratio = [] # we reinitialize the ratio list
		year = [] # same for the year
	ratio.append(speeches[iFiles].ratio) # if the speaker is still the same, we add the ratio to its ratio list
	year.append(speeches[iFiles].year) # same for the year
	iFiles+=1
Result.append([nameOfSpeaker, ratio, year]); # we add the last speaker's parameters to the List

# we create a list with all the ratios
Ratio = []
for i in range(0, len(Result)):
	for j in range(0, len(Result[i][1])):
		Ratio.append(Result[i][1][j])
	

# we calculate the moving average and also two limits (inf and sup)
movingAverage = []
movingAverageInf = []
movingAverageSup = []
for i in range(2, len(Ratio)):
	movingAverage.append((Ratio[i-2]+Ratio[i-1]+Ratio[i])/3)
	movingAverageInf.append((Ratio[i-2]+Ratio[i-1]+Ratio[i])/3-0.5)
	movingAverageSup.append((Ratio[i-2]+Ratio[i-1]+Ratio[i])/3+0.5)

# we create a list with the same size than the moving average
yearsMovingAv = [speeches[i].year for i in range(2,sizeOfFiles)]	

# first figure : 
plt.figure(1)
plt.plot(yearsMovingAv, movingAverage, 'b', label='Moving Average')
plt.plot(yearsMovingAv, movingAverageInf, 'b--')
plt.plot(yearsMovingAv, movingAverageSup, 'b--')
color = ['magenta', 'black', 'yellow', 'blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
iColor = 0


for i in range(0, len(Result)):
	if (iColor>=len(color)):
		iColor=0
	plt.scatter(Result[i][2],Result[i][1], c = color[iColor], label=Result[i][0]) 
	iColor+=1

plt.legend()
plt.title('Positiveness ratio in speeches depending on the year')
plt.show()

# second figure :
RatioList = [] 
for i in range(0, len(Result)):
	RatioList.append(Result[i][1])
fig, ax = plt.subplots()
fig.canvas.draw()
labels = [item.get_text() for item in ax.get_xticklabels()]

for i in range(0, len(Result)):
	labels[i]=Result[i][0]

plt.boxplot(RatioList)
ax.set_xticklabels(labels)
plt.title('Positiveness ratio in speeches')
plt.show()
