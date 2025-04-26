from flask import Flask, request, render_template
import pickle
import numpy as np

model = pickle.load(open('titanic_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = np.array(features).reshape(1, -1)
    
    prediction = model.predict(final_features)
    
    output = 'Survived' if prediction[0] == 1 else 'Did not Survive'

    return render_template('index.html', prediction_text=f'Prediction: {output}')

if __name__ == "__main__":
    app.run(debug=True)
