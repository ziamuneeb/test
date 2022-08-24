from flask import Flask
import os 

app = Flask(__name__)
value_1 = os.environ.get('v_1')
value_2 = os.environ.get('v_2')

@app.route('/')
def welcome():
    return 'Hello Muneeb {} and {}'.format(value_1,value_2)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)