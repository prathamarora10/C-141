from flask import Flask, jsonify, requests
import csv

all_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]
    
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route('/get-articles')
def get_articles():
    return jsonify({
        'data' : all_articles[0],
        'status' : 'success'
    }), 201
    
@app.route('/liked-articles', methods=["POST"])
def liked_movie():
    article = all_articles[0]
    articles = all_articles[1:]
    liked_articles.append(article)
    
    return jsonify({
        'status' : 'success'
    }), 201
    
@app.route('/not-liked-articles', methods=["POST"])
def not_liked_movie():
    article = all_articles[0]
    articles = all_articles[1:]
    not_liked_articles.append(article)
    
    return jsonify({
        'status' : 'success'
    }), 201
      
if __name__ == '__main__':
    app.run()
    