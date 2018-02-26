# Sentiments Analysis using Python

## Sources
After reading [an interesting tutorial on Kaggle about Sentiments Analysis applied to American Political Speeches](http://blog.kaggle.com/2017/10/05/data-science-101-sentiment-analysis-in-r-tutorial/), I decided to create my own version.

Instead of using R, I used Python and I applied my model to French Political Speeches.

I used the lexicons available [here](https://www.kaggle.com/rtatman/sentiment-lexicons-for-81-languages), which are from the following paper : Chen, Y., & Skiena, S. (2014). Building Sentiment Lexicons for All Major Languages. In ACL (2) (pp. 383-389).

I used the speeches available on [this page](http://www.vie-publique.fr/discours/selection-discours/voeux-presidents-republique-depuis-1974-2.html).

## Code
I used a Class `Speech` which contains the following:
- name of the speaker (Here, the name of the President)
- year of the speech
- number of positive words in the speech
- number of negative words in the speech
- number of words in the speech
- a ratio, (number of positive words - number of negative words)/(number of words).

I created a function `getLexicons(positiveList, negativeList)` which put all the positive words from the positive lexicon into a list, and put all the negative words from the negative lexicon into another list.

I then created another function `getSpeechAnalysis(speechName, name, year, positiveList, negativeList)` which return a speech class with all the information we need (number of words, number of positive/negative words...).

Then, after initializing the environment with the first function, I applied this last function to a list of speeches (the end-of-the-year speech given by the Frencg President).

## Results
I obtained the following results:
- On this graphe, we can see the positivness ratio evolving among time. We can see where the different Presidents position themselves compared  to the moving average. 
![Alt text](Positivness_ratio_among_time.png?raw=true "Title")

- On this graphe, I draw a boxplot for every President. Thus, we can see the median, the first and third quartile, the maximum and the minimum for every President.
![Alt text](Positivness_Presidents.png?raw=true "Title")


