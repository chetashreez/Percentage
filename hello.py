from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        english = int(request.form['english'])
        hindi = int(request.form['hindi'])
        math = int(request.form['math'])
        science = int(request.form['science'])
        social_science = int(request.form['social_science'])

        total_marks = english + hindi + math + science + social_science
        percentage = (total_marks / 500) * 100
        return render_template('result.html', percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True)
