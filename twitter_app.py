# geektechstuff
# Twitter Application

from twython import Twython
#Twython is a Twitter Python library

import random

#imports the Twitter API keys

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

ids_replied_to = []
with open('ids_replied_to.txt', 'r') as filehandle:
    filecontents = filehandle.readlines()

    for line in filecontents:
        # remove linebreak which is the last character of the string
        current_place = line[:-1]
        # add item to the list
        ids_replied_to.append(current_place)

# This searches Tweets
print('')
print('GeekTechStuff Twitter Search Python Program')
print('')
search_term = input('What word should I look for? ')

results = twitter.cursor(twitter.search, q=search_term)

print('')
print('Searching Twitter...')
print('')

#These are the tweets the bot can send
rand_message = ['I am a auto tweet bot', 'Twitter is great', 'Tweet Tweet', 'I auto reply to Tweets and I was created in Python',]

for result in results:

    name = result['user']
    screen_name = name['screen_name']

    creation_date = result['created_at']

    tweet_txt = result['text']

    id = result['id']

    print('Twitter User:', screen_name)
    print('Posted:')
    print(tweet_txt)
    print('at:')
    print(creation_date)
    print('')

  
    #This posts Tweets
    id = str(id)
    if id in ids_replied_to:
        print('')
        print('Skipped as already replied to')
        print('')
        print('')
    else:
        twitter_handle = '@' + screen_name
        message = twitter_handle + " " + random.choice(rand_message)
        #twitter.update_status(status=message, in_reply_to_status_id=id)
        print("Tweeted: %s" % message)
        id = int(id)
        ids_replied_to.append(id)
        with open('ids_replied_to.txt', 'w') as filehandle:
            filehandle.writelines("%s\n" % place for place in ids_replied_to)
        # delay so that it doesn't look like the program is spamming Twitter
        time.sleep(5)



