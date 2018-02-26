# Sentiments Analysis using Python

## Sources
After reading [an interesting tutorial on Kaggle about Sentiments Analysis applied to American Political Speeches](http://blog.kaggle.com/2017/10/05/data-science-101-sentiment-analysis-in-r-tutorial/), I decided to create my own version.

Instead of using R, I used Python and I applied my model to French Political Speeches.

I used the lexicons available [here](https://www.kaggle.com/rtatman/sentiment-lexicons-for-81-languages), which are from the following paper : Chen, Y., & Skiena, S. (2014). Building Sentiment Lexicons for All Major Languages. In ACL (2) (pp. 383-389).

I used the speeches available on [this page](http://www.vie-publique.fr/discours/selection-discours/voeux-presidents-republique-depuis-1974-2.html).

## Code
I used a Class :
`class Speech:
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
self.ratio = (nbPositiveWords-nbNegativeWords)/nbTotalWords*100`

I obtained the following results:
![Alt text](Positivness_ratio_among_time.png?raw=true "Title")

![Alt text](Positivness_Presidents.png?raw=true "Title")


