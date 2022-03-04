from http import server
from flask import Flask, render_template, request, redirect, session
import datetime

# x = datetime.datetime.now()
# print(x)
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe' 

fruits = [
    {'name' : 'apple', 'quantity' : 0},
    {'name' : 'raspberry', 'quantity' : 0},
    {'name' : 'strawberry', 'quantity' : 0},
    # {'raspberry' : request.form["raspberry"]},
    # {'strawberry' : request.form["strawberry"]}
]

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    fruits[0]['quantity'] = request.form['apple']
    fruits[1]['quantity'] = request.form['raspberry']
    fruits[2]['quantity'] = request.form['strawberry']
    # fruits = [
    #     {'apple' : request.form["apple"]},
    #     {'raspberry' : request.form["raspberry"]},
    #     {'strawberry' : request.form["strawberry"]}
    # ]
        # {'fruit_name' : 'apple', 'quantity' : request.form["apple"]},
        # {'fruit_name' : 'blackberry', 'quantity' : request.form["blackberry"]},
        # {'fruit_name' : 'raspberry', 'quantity' : request.form["raspberry"]},
        # {'fruit_name' : 'strawberry', 'quantity' : request.form["strawberry"]}
    
    session['firstName'] = request.form['first_name']
    session['lastName'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    # session['apple'] = request.form['apple']
    # session['blackberry'] = request.form['blackberry']
    # session['raspberry'] = request.form['raspberry']
    # session['strawberry'] = request.form['strawberry']
    print(request.form)
    # print(session["raspberry"])
    return redirect('/checkout')
    # render_template("checkout.html", fruits=fruits)

@app.route('/checkout')         
def check_out():
    quantity = int(fruits[0]["quantity"]) + int(fruits[1]["quantity"]) + int(fruits[2]["quantity"])
    time = datetime.datetime.now()
    x = (time.strftime("%b-%d-%y"))
    return render_template("checkout.html", fruits=fruits, time=x, quantity=quantity)

if __name__=="__main__":   
    app.run(debug=True)    