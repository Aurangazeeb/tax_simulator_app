from flask import Flask, render_template, request, redirect, url_for
from calculator_logic import find_take_home_OR
api = Flask(__name__)

tax_inputs = {}

@api.route('/welcome/')
def hello_world():
    # if request.method == 'GET':
    return render_template('tax_welcomepage.html')

@api.route('/tax_simulator/') #canonical url /link/ = /link
def tax_simulator():
    return render_template('tax_inputpage.html')

@api.route('/tax_inputs/', methods = ['POST'])
def display_inputs():
    # if request.method == 'POST':
    user_formdata = request.form
    global tax_inputs
    tax_inputs = request.form
    return render_template('tax_read.html', user_data = user_formdata)

@api.route('/tax_payable/', methods = ['POST'])
def final_action():
    if request.form['submit'] == 'ok':
        # user_formdata2 = request.form
        # global tax_inputs
        # print(tax_inputs)
        # take_home, annual_tax_amt = find_take_home_OR(float(user_formdata2['gsalary']), user_formdata2['pfmode'])
        take_home, annual_tax_amt = find_take_home_OR(float(tax_inputs['gsalary']), int(tax_inputs['pfmode']))
        return render_template('tax_payable.html', take_home = take_home, annual_tax_amt = annual_tax_amt, name = tax_inputs['name'])
    else:
        return redirect(url_for('tax_simulator'))

if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0')