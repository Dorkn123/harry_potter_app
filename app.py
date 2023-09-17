from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/philosophers_stone')
def philosophers_stone():
    return render_template('philosophers_stone.html')

@app.route('/chamber_of_secrets')
def chamber_of_secrets():
    return render_template('chamber_of_secrets.html')

@app.route('/prisoner_of_azkaban')
def prisoner_of_azkaban():
    return render_template('prisoner_of_azkaban.html')

@app.route('/goblet_of_fire')
def goblet_of_fire():
    return render_template('goblet_of_fire.html')

@app.route('/order_of_the_phoenix')
def order_of_the_phoenix():
    return render_template('order_of_the_phoenix.html')

@app.route('/half_blood_prince')
def half_blood_prince():
    return render_template('half_blood_prince.html')

@app.route('/deathly_hallows')
def deathly_hallows():
    return render_template('deathly_hallows.html')

if __name__ == '__main__':
    app.run(debug=True)
