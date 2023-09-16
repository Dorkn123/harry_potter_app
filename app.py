from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book1')
def book1():
    return render_template('philosophers_stone.html')

@app.route('/book2')
def book2():
    return render_template('book2.html')

@app.route('/book3')
def book3():
    return render_template('book3.html')

@app.route('/book4')
def book4():
    return render_template('book4.html')

@app.route('/book5')
def book5():
    return render_template('book5.html')

@app.route('/book6')
def book6():
    return render_template('book6.html')

@app.route('/book7')
def book7():
    return render_template('book7.html')

if __name__ == '__main__':
    app.run(debug=True)
