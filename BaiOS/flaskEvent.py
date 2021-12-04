# -*- coding : utf-8 _*_
from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def cqhttp_post():
    data = request.get_data()
    json_data = json.loads(data.decode('utf-8'))
    shortcut_do=event_itemize(json_data)
    return shortcut_do


def event_itemize(json_data):
  if '' in json_data:
    
  elif '' in json_data:
    
  elif '' in json_data:
    
  else:
    return ''
  
  return shortcut_do


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5701)
