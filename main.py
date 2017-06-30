from flask import Flask, redirect, url_for, request, render_template, send_from_directory, make_response
from pprint import pprint
from config import DevConfig

app = Flask(__name__,
            static_url_path='/static',  # how to get static files' url
            static_folder='public')     # static files' location
app.config.from_object(DevConfig)


@app.route('/')
def index():
  return 'Chong Test'

@app.route('/variable/<test>')
def variableTest(test):
  return test

@app.route('/setVarType/<int:num>')
def setVariableTypeTest(num):
  return str(num)


@app.route('/admin')
def admin():
  return 'admin'

@app.route('/guest/<name>')
def guest(name):
  return 'test %s' % name

# url_for(funcName)
# -> get the url by funcName
@app.route('/user/<name>')
def check_user(name):
  if name == 'admin':
    return redirect(url_for('admin'))
  else:
    return redirect(url_for('guest', name=name))

# request
@app.route('/login/<test>', methods=['POST', 'GET'])
def login(test):
  if request.method == 'POST':
    # form data:
    # request.form[name]
    return 'post'
  else:
    return 'get'

@app.route('/index/<name>')
def renderIndex(name):
  # render engine is jinga2
  return render_template('index.html', name = name)

# test request query string
@app.route('/queryString')
def queryString():
  print(request.args)
  print(request.form)
  print(request.cookies)
  return 'query string test'

# cookies test
@app.route('/setCookies/<data>')
def setCookies(data):
  resp = make_response('set cookies finished')
  resp.set_cookie('cookie_test', data)
  return resp

if __name__ == '__main__':
  app.run(debug = True)