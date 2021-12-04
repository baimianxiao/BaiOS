# -*- coding : utf-8 _*_
from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def cqhttp_post():
    data = request.get_data()
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)
    if 'message_type' in json_data:
        print(json_data['raw_message'])
    return ""


# def event_itemize(json_data):
# if
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5701)
