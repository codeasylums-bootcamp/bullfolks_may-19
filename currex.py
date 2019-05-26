#importing required libraries
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import requests

#naming a flask
app = Flask(__name__)

#giving the flask routes-what happens in home page
@app.route("/", methods=['GET'])
def main():
    return render_template('curr.html')

#what happens during when Convert button is clicked
@app.route("/convert", methods=['GET','POST'])
def convert():
    if request.method == 'POST':
        current = request.form['amount']
        fromm = request.form['fromm']
        toc = request.form['toc']
        value = requests.get('https://www1.oanda.com/rates/api/v2/rates/spot.json?api_key=bI7O5G3ryIAHJN5E2ICXsLlb&base='+fromm+'&quote='+toc+'').json()
        changed = value['quotes'][0]['midpoint']
        result = float(current) * float(changed)
        return render_template('curr1.html', result=result, fromm=fromm, toc=toc, current=current)
    else:
        return render_template('curr1.html')

#main menu
if __name__ == '__main__':
    app.run(debug=True)
