import sys
import json
import os
import pip

#import pandas as pd
#from azure.datalake.store import core, lib
#from flask import Flask
#from flask_restplus import Resource, Api, fields, abort

def wsgi_app(environ, start_response):
    installed_packages = pip.get_installed_distributions()
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
         for i in installed_packages])
    print(installed_packages_list)


    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    response_body = 'Hello World {} - {}'.format(sys.version, installed_packages_list)
    yield response_body.encode()


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
    