from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Chrishart!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
    
    
# @app.route('/hello')
# def hello():
#     response = make_response('Hello, Chrishart!\n')
#     response.status_code = 202
#     response.headers['content-type'] = 'text/plain'
#     return response
    

# @app.route('/greet/<name>')
# def greet(name):
#     return f'Hello, {name}!'



# @app.route('/add/<int:number1>/<int:number2>')
# def add(number1, number2):
#     return f'The sum of {number1} and {number2} is {int(number1) + int(number2)}'




# @app.route('/handle_url_params')
# def handle_params():
#     if 'greeting' in request.args.keys() and 'name' in request.args.keys():
#         greeting = request.args['greeting']
#         name = request.args.get('name')
#         return f'{greeting}, {name}!'
#     else:
#         return 'Invalid parameters'