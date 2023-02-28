# create Application instance
# Application instance is an object of Flask Class
# so import Flask class
# Flask Class will take an argument that is Name of the current module
# standard way to represent current module name is __name__

from flask import Flask

AI=Flask(__name__)

# create one view function and decoorate it with routemethod of AI

@AI.route('/wish')
def wish():
    return 'This is my first flask view function'
@AI.route('/second')
def second():
    return 'Second view function'

if __name__=='__main__':
    AI.run(debug=True,host='192.168.43.53',port=5001)