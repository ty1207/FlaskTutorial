from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world！'

@app.route('/home/')
def home():
    return 'Welecome to home!'

@app.route('/home/<int:num>')
def int(num):
    #return '数字是：{}'.format(num)
    return f'数字是：{num}'

@app.route('/home/<float:num>')
def float(num):
    return f'浮点数是：{num}'
    #return '浮点数是：{}'.format(num)

@app.route('/home/<name>')
def str(name):
    return f'名字是: {name}'
    #return '名字是:{}'.format(name)

if __name__ == '__main__':
    app.run(debug=True)

