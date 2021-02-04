from flask import Flask

app = Flask("app")
#app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/home/')
def home():
    return 'Welecome to home!'

#输入整数
@app.route('/home/<int:num>')
def int(num):
    #return '数字是：{}'.format(num)
    return f'数字是：{num}'

#输入浮点数
@app.route('/home/<float:num>')
def float(num):
    return f'浮点数是：{num}'
    #return '浮点数是：{}'.format(num)

#输入字符串
@app.route('/home/<name>')
def str(name):
    return f'名字是: {name}'
    #return '名字是:{}'.format(name)

#不用装饰器，用add_url_role写法
def url():
    return "欢迎使用add_url_role方式!"
app.add_url_rule('/add_url_role','url',url)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8800,debug=True)

