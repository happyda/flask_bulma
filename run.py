# coding:utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'WELCOME TO FLASK'
    subtitle = '祝你有美好的一天'
    description = '有好事會發生'
    footer = 'FOOTER TEXT'
    return render_template('index.html', title=title, subtitle=subtitle, description=description, footer=footer)

@app.route('/do_something', methods=['POST'])
def do_something():
    msg = '大家好我是小神通！'
    print(msg)
    return msg

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True,host='0.0.0.0',port=5000)
