
#### About
This is a RESTful parser of Metacritic site for a top PS3 games.
```/games``` - returns all top PS3 games on metacritic page
Request: ```curl -XGET http://127.0.0.1:5000/games```
Example ouput:
```json

[
    {
        "score": 86,
        "title": "The Legend of Heroes: Trails of Cold Steel"
    },
    {
        "score": 83,
        "title": "Steins;Gate"
    }
]
```

```/games/TITLE_OF_GAME_GOES_HERE``` - returns JSON for a specific job that matches the corresponding job title.

Request: ```curl -XGET http://127.0.0.1:5000/games/The%20Awakened%20Fate:%20Ultimatum```
Example output:
```json
[
    {
        "score": 65,
        "title": "The Awakened Fate: Ultimatum"
    }
]
```
#### How to install and run
It needs ```python2.7``` to be installed for a successful run.
```bash
git clone git@github.com:beastea/gaikai-parser.git
cd gaikai-parser
pip install -r requirements.txt
python gaikai_app.py
```
By default application starts and runs on port 5000 of localhost. You can change the behavior by adding parameters to run function of application.
For example:
```python
if __name__ == '__main__':
    app.run(port=5010,host='127.0.0.1')
```
Run app on localhost on port 5010.
#### Tests
```bash
py.test -v
```
