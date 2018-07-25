from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    un = "Enter a number"
    if "first" in request.args:
        un = "{}".format(int(request.args['first']) * int(request.args['second']))
    deux = "Enter a second number"
    if "second" in request.args:
        deux = format(request.args['second'])

    return render_template('webhtml2.html').format(un, deux)


app.run(debug=True, port=8080)
