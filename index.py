from flask import Flask, jsonify, request
from flask.ext.cors import CORS
import engine

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def index():
	file = request.files["imageLoader"]
	return engine.main(file)
	
if __name__ == '__main__':
	app.run(debug=True)
