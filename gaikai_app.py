#!/usr/bin/env/ python

import flask
import json
from lxml import html
import requests

app = flask.Flask(__name__)

def get_data(url='http://www.metacritic.com/game/playstation-3'):
    headers = {'User-agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.content)
    games = tree.xpath('//div/div/div/h3/a/text()')
    ranks = tree.xpath('//li/div/div/div/div/a/span/text()')
    return tuple(map(None, games, [int(i) for i in ranks]))

def to_json(data):
    return json.dumps(data, indent=4)

def resp(code, data):
    return flask.Response(
        status=code,
        mimetype="application/json",
        response=to_json(data)
    )

@app.route('/')
def root():
    return flask.redirect('/games', code=302)

@app.route('/games', methods=['GET'])
def get_gameslist():
    gameslist = []
    for game, rank in get_data():
        gameslist.append({"title": game, "score": rank})
    return resp(200, gameslist)

@app.route('/games/<path:gamename>', methods=['GET'])
def get_game(gamename):
    gameinfo = []
    for game,rank in get_data():
        if game == gamename:
            gameinfo.append({"title": game, "score": rank})
    return resp(200, gameinfo)

@app.errorhandler(400)
def page_not_found(error):
    return resp(400, {})

@app.errorhandler(404)
def not_found(error):
    return resp(400, {})

@app.errorhandler(405)
def not_found(error):
    return resp(400, {})

if __name__ == '__main__':
    app.run()
