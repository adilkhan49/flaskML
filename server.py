import numpy as np
from flask import Flask, request, jsonify
import os
import joblib

app = Flask(__name__)
model = joblib.load(open('LassoLars.pkl','rb'))

@app.route('/api',methods=['POST'])

def predict():
	data = request.get_json(force=True)
	input = data['exp']
	print(input)

	prediction = model.predict(np.array(input))
	output = prediction[0]

	print(output)
	return jsonify(output)


if __name__ == '__main__':
    app.run(port=5005, debug=True)


    
# def init():
#     global model
#     # AZUREML_MODEL_DIR is an environment variable created during deployment.
#     # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
#     # For multiple models, it points to the folder containing all deployed models (./azureml-models)
#     model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'LassoLars.pkl')
#     model = joblib.load(model_path)

# def run(raw_data):
#     data = np.array(json.loads(raw_data)['data'])
#     # make prediction
#     y_hat = model.predict(data)
#     # you can return any data type as long as it is JSON-serializable
#     return y_hat.tolist()