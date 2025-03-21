import pandas as pd
import os
import uuid
from flask import Flask, render_template, request, Response, send_from_directory, jsonify

# request, make_response, redirect, url_for

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
    

# commits -> Forms, POST, File Upload, Excel, Pandas, JSON Response, File Download, File Handling
    
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



# @app.route('/nextpage')
# def nextpage():
#     some_text = 'Hello, World!'
#     return render_template('nextpage.html', some_text=some_text)

# @app.template_filter('reverse_string')
# def reverse_string(s):
#     return s[::-1]

# @app.template_filter('repeat_string')
# def repeat_string(s, n=2):
#     return s * n


# @app.template_filter('alternate_case')
# def alternate_case(s):
#     return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s))


# @app.route('/redirect_endpoint')
# def redirect_endpoint():
#     return redirect(url_for('nextpage'))

# @app.route('/file_upload', methods=['POST'])
# def file_upload():
#     file = request.files['file']
    
#     if not file:
#         return "No file uploaded", 400
    
#     if file.content_type == 'text/plain':
#         return file.read().decode('utf-8')
    
#     elif file.content_type in ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.ms-excel']:
#         df = pd.read_excel(file)
#         return df.to_html()
    
#     return "Unsupported file type", 400


# @app.route('/convert_csv' , methods=['POST'])
# def convert_csv():
#     file = request.files['file']
#     df = pd.read_excel(file)
    
#     response = Response(
#         df.to_csv(),
#         mimetype = 'text/csv',
#         headers = {
#             'Content-Disposition': 'attachment; filename=converted.csv'
#         }
#     )
    
#     return response


# @app.route('/convert_csv_two', methods=['POST'])
# def convert_csv_two():
#     file = request.files['file']
#     df = pd.read_excel(file)
    
#     if not os.path.exists('downloads'):
#         os.makedirs('downloads')
    
#     filename = f'{uuid.uuid4()}.csv'
#     df.to_csv(os.path.join('downloads', filename))
    
#     return render_template('download.html', filename=filename)

        
# @app.route('/download/<filename>')
# def download(filename):
#     return send_from_directory('downloads', filename, download_name="converted.csv")


# @app.route('/handle_post', methods=['POST'])
# def handle_post():
#     greeting = request.json['greeting']
#     name = request.json['name']
    
#     with open('file.txt', 'w') as f:
#         f.write(f'{greeting}, {name}!')
        
#     return jsonify({'message': 'Written to file'})