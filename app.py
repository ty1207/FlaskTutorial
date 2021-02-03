from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world！'

@app.route('/home/<int:age>')
def int(age):
    return '年龄是：{}'.format(age)

@app.route('/home/<float:num>')
def float(num):
    return '浮点数是：{}'.format(num)

#@app.route('/home/<name>')
#def string(name):
#    return '名字是：{}'.format(name)

@app.route('/home/<name>')
def str(name):
    return f'名字是 {name}'

@app.route('/home/')
def home():
    return 'Welecome to home!'

if __name__ == '__main__':
    app.run(debug=True)

