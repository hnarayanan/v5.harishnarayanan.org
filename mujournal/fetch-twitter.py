#!/usr/bin/env python

import tweepy
import re
import codecs
from itertools import groupby

consumer_key = 'eeH4kHYeep7cQ1OWDxV3sw'
consumer_secret = 'ayu6R3ZpxNqjGM9s3q414BjP1grpaPJTbtDW9rK6IM'

access_token_key = '566067400-tgBEIo8iAgATIYtia7rxyyJ2nsPr3D0qGTwdNsn8'
access_token_secret = 'SJ0m55TpGrCfhwZ3zS88Tc6KUOdwik4tg3BSmAWWgl8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

def format_text(tweet):
    formatted_text = tweet.text
    formatted_text = re.sub(r'\n', r' ', formatted_text)
    formatted_text = re.sub(r'---', r'&#8212;', formatted_text)
    formatted_text = re.sub(r'--', r'&#8210;', formatted_text)
    formatted_text = re.sub(r'@([A-Za-z0-9_]+)', r'<a href="http://twitter.com/\1">@\1</a>', formatted_text)
    formatted_text = re.sub(r'(https?://t.co/[A-Za-z0-9_]+)', r'<a href="\1">\1</a>', formatted_text)
    formatted_text = re.sub(r'\B#(\w*[a-zA-Z]+\w*)', r'<a href="https://twitter.com/search?q=%23\1&amp;src=hash">#\1</a>', formatted_text)
    return formatted_text

def format_date(date):
    formatted_date = date.strftime("%A, %B %d, %Y")
    return formatted_date

def format_time(tweet):
    formatted_time = tweet.created_at.strftime("%I:%M <small>%p</small>")
    return formatted_time

def format_url(tweet):
    formatted_url = 'https://twitter.com/copingbear/status/' + tweet.id_str
    return formatted_url

recent_tweets = api.user_timeline(count=500)
output = codecs.open('tweets.html', 'w', 'utf8')
output.truncate()

for date, group in groupby(recent_tweets, lambda x: x.created_at.date()):
    output.write('                <div class="daygroup">\n')
    output.write('                  <h2>' + format_date(date) + '</h2>\n')

    for tweet in group:
        formatted_text = format_text(tweet)
        formatted_time = format_time(tweet)
        formatted_url = format_url(tweet)
        output.write('                  <p class="muj-entry">' + formatted_text + '<br /><span class="timestamp"><a href="' + formatted_url + '">' + formatted_time + '</a></span></p>\n')
    output.write('                </div>\n')

output.close()
