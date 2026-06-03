from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":

        altura = float(request.form['alturaimc'])
        peso = float(request.form['pesoimc'])

        imc = peso / (altura ** 2)

        return render_template('imc.html', imc=imc)

    return render_template('imc.html')


if __name__ == '__main__':
    app.run(debug=True)