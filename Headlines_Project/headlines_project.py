from flask import Flask

import feedparser

app = Flask(__name__)

bbc_feed = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route('/')
def get_news():
    feed = feedparser.parse(bbc_feed)
    first_article = feed['entries'][10]
    return """<html>
            <body>
                <h1> BBC Headlines </h1>
                <b>{0}</b><br/>
                <i>{1}<i><br/>
                <p>{2}<p><br/>
            </body>
            </html>""".format(first_article.get('title'),
                              first_article.get('published'),
                              first_article.get('summary'))

if __name__ == '__main__':
    app.run(debug = True)
