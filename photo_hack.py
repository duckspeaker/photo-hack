import sys, json
from pprint import pprint
from bottle import route, run, response
sys.path.append('/home/david/photo-hack')
import backend_stuff

@route('/')
def index():
    response.content_type = 'application/json'
    venues = backend_stuff.main()
    venues_json = json.dumps(venues)
    return venues_json

@route('/hello')
def hello():
    return "Hello World!"

@route('/test')
def test():
    return 'OH MY GOD'
