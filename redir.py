from flask import Flask,redirect
import index

app = Flask(__name__)

@app.route('/register/<param>')
def register_route(param):
    id = index.dbinsert(param)
    return 'Hello ' + param + id

@app.route('/micro.ly/<param>')
def redirect_route(param):
    id = index.dbgetdecodedurl(param)
    print(id)
    return redirect('https://www.google.com')


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=8088)