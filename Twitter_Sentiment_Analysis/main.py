from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100 * float(part/float(whole))

ACCESS_TOKEN = '1196957825613926400-vm74Byrqytgd51yjEzgPIGdJkbqHBu'

ACCESS_TOKEN_KEY = 'xUBLFSdqn1ZVRnIGWWq0wAmZjPqS0G7OU3tSwuOqq2qB0'

API_SECRET_KEY = 'JPiqdnCecLgD4fFu1A2RRyQzJEmOvhMwo8H8FRyObJBOk5JqSx'

API_KEY='ekl1Zd8vwuOlpE6OX6bs2jhC1'

auth = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_KEY)
api=tweepy.API(auth)

searchTerm = input("Enter keyword to search: ")
numberTweets = int(input("Enter how many tweets to analyze: "))

tweets = tweepy.Cursor(api.search, q=searchTerm).items(numberTweets)


positive =  0 
negative =  0
neutral =   0
polarity =  0

for tweet in tweets: 
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    
    
    if (analysis.sentiment.polarity == 0):
        neutral +=1 
    elif (analysis.sentiment.polarity < 0.00):
         negative +=1 
    elif (analysis.sentiment.polarity > 0.00):
        positive +=1 

positive = percentage(positive, numberTweets)
negative= percentage(negative, numberTweets)
neutral = percentage(neutral, numberTweets)
total_polarity = neutral + positive + negative
average_polarity = percentage(total_polarity, numberTweets)


positive=format(positive, '.2f')
negative=format(negative, '.2f')
neutral=format(neutral, '.2f')
average_polarity=format(polarity, '.2f')

if (polarity == 0):
    print ('Neutral')
elif (polarity >= 1):
    print('Positive')
elif (polarity <= -1):
    print("Negative")
    
    
print(average_polarity)

labels = ['Positive ['+str(positive)+'%]', 'Neutral ['+str(neutral)+'%]', 'Negative ['+str(negative)+'%]']

sizes= [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)

plt.legend(patches, labels, loc='best')
plt.title('How People are reacting to '+searchTerm+' by analyzing '+str(numberTweets)+' Tweets')

plt.axis('equal')
plt.tight_layout()
plt.show()
