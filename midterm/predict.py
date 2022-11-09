import pickle
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from flask import Flask
from flask import request
from flask import jsonify

from common import config

app = Flask('match')

def load_model():
    with open(config['vectorizer_file_name'], 'rb') as stream:
        vectorizer = pickle.load(stream)
    with open(config['model_file_name'], 'rb') as stream:
        model = pickle.load(stream)
    return vectorizer, model

vectorizer, model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict(vectorizer.transform([data]))[0]
    return jsonify({'request': data, 'result': prediction})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)