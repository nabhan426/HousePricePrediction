from flask import Flask ,request , jsonify ,render_template
import util


app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route('/')
def home():
    return render_template("app.html") 

@app.route('/get_location_names')
def get_location():
    response= jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin',"*")


    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    if request.method == 'POST':
        data = request.form
    else:
        data = request.args
    total_sqft = float(data['total_sqft'])
    location = data['location']
    bhk = int(data['bhk'])
    bath = int(data['bath'])
   

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__=="__main__":
    app.run(debug=True)
