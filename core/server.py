from flask import Flask, render_template, request, redirect, session, url_for

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


if __name__=="__main__":
    app.run(debug=True, port=5001) 