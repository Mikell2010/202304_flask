from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'Bunny bob was here'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] =0
    session['count'] +=1
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route("/incrementa_en_dos")
def incrementa_en_dos():
    session["count"] += 2
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True, port=5001) 