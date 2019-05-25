from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import requests

app = Flask(__name__)


@app.route("/", methods=['GET'])
def main():
    return render_template('curr.html')


@app.route("/convert", methods=['POST'])
def convert():
    res = request.form
    value = requests.get('https://www1.oanda.com/rates/api/v2/rates/spot.json?api_key=bI7O5G3ryIAHJN5E2ICXsLlb&base='+res[1].value+'&quote='+res[2].value+'')
    json_object = value.json
    changed = float(json_object['quotes']['midpoint'])
    result = current * changed
    return render_template('curr1.html', result=result, fromm=res["froma"], toc=res["toc"], current=res["current"])



if __name__ == '__main__':
    app.run(debug=True)
