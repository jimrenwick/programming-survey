#!/usr/bin/python

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting

PORT = 80
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", PORT)
handler.cgi_directories = ["/cgi-bin"]

httpd = server(server_address, handler)
print "serving at port", PORT
httpd.serve_forever()

