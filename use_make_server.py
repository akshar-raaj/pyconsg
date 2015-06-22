from wsgiref.simple_server import make_server
from dj.wsgi import application

httpd = make_server('localhost', 8051, application)

print "Server running at http://localhost:8051"
httpd.serve_forever()