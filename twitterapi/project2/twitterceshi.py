# export GOOGLE_APPLICATION_CREDENTIALS="/media/sf_dropbox_ec602/ec602/pelagic-force-326821-5dc70bdbd2e9.json"
# First step is export the google credential in terminal.
import googleceshi as analyze
import tweepy


consumer_key = "nYEgZs6LnnNLSd8iA2Q2Rf5w0"
consumer_secret = "5tzcEpKRCXqkrgNuDllGRJ29lmRqW6lHjmvSuLXLiJH5RVg5Da"
access_key = "1440789160151826439-BFerR9hb6QX0RLDVl8rEBw9yp8fqst"
access_secret = "oAy9lXxrdILDlOETri8jHpOqlVSwN95eWM4eKRL5H7tcr"


def get_tweets(typein):

    avgscore = 0
    avemagitued = 0
    count = 0
    input_str = ""
    strtolist = typein.split()

    for i in strtolist:
        input_str = input_str + i


    #authorize twitter, initialize tweepy

    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    results = api.search_tweets(q=input_str, count=500, lang = "en")

    for k in results:
        print(k.user.screen_name, ":", k.text, "\n")
        output = analyze.analyze_sentiment(k.text)
        avgscore = avgscore + output[0]
        avemagitued = avemagitued + output[1]
        count = count + 1

    avgscore = avgscore / count
    avemagitued = avemagitued / count

    print("The name of the game is: {}".format(input_str))

    print("The average sentiment score is:", avgscore)
    print("The average sentiment magnitude is:", avemagitued)

    if (avgscore <= -0.5):
        print("The feedback of the game %s is not that good" %input_str)
    elif ((avgscore > -0.5) & (avgscore < 0.5)):
        print("The feedback of the game %s is about average" %input_str)
    elif (avgscore >= 0.5):
        print("The feedback of the game %s is pretty good" %input_str)

if __name__ == '__main__':
    get_tweets(input("Enter keywords for twitter search: "))