import requests
import urllib2, json
import HTMLParser # I'm still on Python 2
import random

def getNImagesWithDescription(s, n):
    messageText = ''
    html = HTMLParser.HTMLParser()

    # User-agent is necessary to get the links:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
    url = 'http://images.google.com/search'
    r = requests.get(url, params={'q': s, 'tbm': 'isch', 'gbv': '2'}, headers=headers)

    imageUrls = map(lambda l: urllib2.unquote(urllib2.unquote(l[:l.find('&amp;imgref')])), r.text.split('imgurl=')[1:])

    # now that I have `# coding: utf-8` in newEmail.py, it is unnecessary to .decode('unicode_escape') here, but since it took so long to get it right originally, worth saving just in case
    # imageDescs = map(lambda l: html.unescape(html.unescape(l[:l.find('"')].decode('unicode_escape'))), r.text.split('"s":"')[1:])
    imageDescs = map(lambda l: html.unescape(html.unescape(l[:l.find('"')])), r.text.split('"s":"')[1:])

    randomIndices = random.sample(xrange(10 * n), n) # 100 choose 6 had just a few too many false positives

    for i in randomIndices:
        messageText += '<br /><br />' + imageDescs[i] + ':<br />'
        messageText += '<center><img style="max-height: 480px; max-width: 480px;" src="' + imageUrls[i] + '"></center>'
        print i, imageDescs[i].encode('utf-8'), imageUrls[i].encode('utf-8')

    return messageText

def getNImages(s, n):
    html = HTMLParser.HTMLParser()

    # User-agent is necessary to get the links:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
    url = 'http://images.google.com/search'
    r = requests.get(url, params={'q': s, 'tbm': 'isch', 'gbv': '2'}, headers=headers)

    imageUrls = map(lambda l: urllib2.unquote(urllib2.unquote(l[:l.find('&amp;imgref')])), r.text.split('imgurl=')[1:])

    randomIndices = sorted(random.sample(xrange(10 * n), n)) # try only using 3n

    return [imageUrls[i] for i in randomIndices]

#getNImagesWithDescription('William III of England', 100).encode('utf-8')