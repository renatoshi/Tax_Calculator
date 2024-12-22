from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_tax():
    total_with_tax = None
    if request.method == 'POST':
        try:
            amout = float(request.form['amount'])
            tax_rate = float(request.form['tax_rate'])
            total_with_tax = amout + (amout * tax_rate / 100)
        except ValueError:
            total_with_tax = "Invalid amount"
    return render_template('index.html', total_with_tax=total_with_tax)


if __name__ == '__main__':
    app.run(debug=True)