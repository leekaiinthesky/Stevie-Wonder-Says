# coding: utf-8
import argparse
import quickstart
import sendEmail
import generateGoogleImagesContent as im
from pyteaser import SummarizeUrl

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('prodString')
args = parser.parse_args()

if args.prodString == 'production':
    production = True
else:
    production = False

# more ideas - ebay stuff, random amazon reviews, guest post from bitofnews bot from my friend Bonnie
# the best thing about ebay... all this memorabilia about so-and-so
# after we run out of monarchs, do one on monarch butterflies, then one on charmin toilet paper, then one on nomes and mention nomarch

with open('listOfMonarchs.txt') as f:
    monarchs = set(f.read().splitlines())

with open('featuredMonarchs.txt') as f:
    featured = set(f.read().splitlines())

with open('chosenMonarch.txt') as f:
    s = f.read()

wikipediaUrl = 'http://en.wikipedia.org/wiki/' + s.replace(' ', '_')

sender = 'Stevie Wonder Says <steviewondersays@gmail.com>'
subject = s + ' (production = False) (' + str(len(monarchs) - len(featured) - 1) + ' features queued)'
to = 'free.leekai@gmail.com'

if production == True:
    to = 'Stevie Wonder Says <steviewondersays@googlegroups.com>'
    subject = s

messageText = "Today's subject is " + s + '.<br /><br />Did you know...?<br /><br />'

imageUrls = im.getNImages(s, 5)
sentences = SummarizeUrl(wikipediaUrl)

for i in xrange(5):
    messageText += sentences[i].encode('utf-8') + '<br /><br />'
    messageText += '<center><img style="max-height: 480px; max-width: 480px;" alt="one of the best pictures of ' + s + '"" src="' + imageUrls[i].encode('utf-8') + '" /></center><br /><br />'

messageText += "That's all for now. Have a great week!<br /><br />Long live the queen,<br />Steve"

# feel free to write back with feedback or suggestions on how to improve my newsletter

message = sendEmail.CreateHTMLMessage(sender, to, subject, messageText)
sendEmail.SendMessage(quickstart.gmail_service, 'me', message)

### Below is for posting to Tumblr
postToTumblr = production # or hard code if necessary
if postToTumblr == True:
    tumblrEmail = '5v0tjjeaateiq@tumblr.com'
    message = sendEmail.CreateMessage(sender, tumblrEmail, subject, messageText + " #" + s)
    sendEmail.SendMessage(quickstart.gmail_service, 'me', message)

if production == True:
    with open('featuredMonarchs.txt', 'a') as f:
        f.write(s + '\n')
