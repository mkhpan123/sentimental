from flask import Flask, request, jsonify, render_template
from src.helper import pre_process
from keras.models import load_model

# Create the app object
app = Flask(__name__)

# Load model
model = load_model('model/model_lstm1.h5')

# Define home route
@app.route('/')
def index():
    return render_template('index.html')

# For prediction
@app.route('/predict', methods=['GET','POST'])
def predict():
    tweet = request.form['tweet']
    #tweets will be the set tht has given the tweet
    tweet = pre_process(tweet) #convert to 200 length list of integer
    pred = model.predict(tweet)
    mx = max(pred[0])
    a = pred[0][0]
    b = pred[0][1]
    c = pred[0][2]
    return render_template('index.html', prediction_textb=f'Positive {b*100:.1f}%\nNeutral {a*100:.1f}%\nNegative {c*100:.1f}%')
    #if mx == b:
    #    return render_template('index.html', prediction_textb=f'Positive {b*100}%')
    #elif mx == a:
    #    return render_template('index.html', prediction_texta=f'Neutral {a*100}%')
    #elif mx == c:
    #    return render_template('index.html', prediction_textc=f'Negative {c*100}%')
    

# To initiate Flask app
if __name__ == '__main__':
    app.run(debug=True)