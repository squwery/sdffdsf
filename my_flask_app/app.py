from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f'Имя: {name}, Email: {email}, Сообщение: {message}')
        return redirect(url_for('success'))
    return render_template('form.html')

@app.route('/success')
def success():
    return 'Форма успешно отправлена!'

if __name__ == '__main__':
    app.run(debug=True)