import csv
from flask import Flask,jsonify

all_articles,liked_articles,unliked_articles = [],[],[]

with open("articles.csv","r",encoding = 'utf-8') as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    all_articles = data[1:]

app = Flask(__name__)

@app.route('/get-articles')
def get_articles():
    return jsonify({
        "data" : all_articles[0],
        "status" : "Success"
    })

#Api 2
@app.route('/liked-article',methods = ['POST'])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status" : "Success"
    }),201

#Api 3
@app.route('/unliked-article',methods = ["POST"])
def unliked_article():
    article = all_articles[0]
    unliked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status" : "Success"
    }),201

if (__name__ == "__main__"):
    app.run(debug= True,port= 9090)