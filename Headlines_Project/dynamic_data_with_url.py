from flask import Flask, render_template

import feedparser

app = Flask(__name__)

rss_feeds = {   'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
                'cnn': 'http://rss.cnn.com/rss/edition.rss',
                'fox': 'http://feeds.foxnews.com/foxnews/latest',
                'iol': 'http://www.iol.co.za/cmlink/1.640'
            }

@app.route('/')
@app.route('/<publication>')
def get_news(publication = 'bbc'):
    feed = feedparser.parse(rss_feeds[publication])
    return render_template('home4.html',articles = feed['entries'])

if __name__ == '__main__':
    app.run(debug = True)