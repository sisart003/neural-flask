from flask import Flask, render_template, redirect, url_for
# request, make_response

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = 'Chrishart E. Estrada'
    myresult = 10 + 20
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    return render_template('index.html', value=myvalue, result=myresult, mylist=mylist)

@app.route('/nextpage')
def nextpage():
    some_text = 'Hello, World!'
    return render_template('nextpage.html', some_text=some_text)

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat_string')
def repeat_string(s, n=2):
    return s * n


@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s))


@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('nextpage'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
    
# topics covered -> HTML Templates, Jinja2, Filters, Template Inheritance, Redirects, URL Building, Static Files, Error Handling, and more.
    
    
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