from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/spam/<string:text>/<int:count>")
def spam(text="spam", count=10):
    text = " " + text
    return text * count


@app.route("/")
@app.route("/main")
def index():
    return render_template("index.html")


@app.route("/registration")
def registration():
    return render_template("form.html")


@app.route("/submit_form", methods=["POST"])
def submit_form():
    if request.method == "POST":
        value = int(request.form.get("age"))
        if value < 18:
            return f"Ваш вік менше 18, ми не зможемо <strike>обдурити вас</strike> вам допомогти"
        else:
            return render_template("scam.html")  # TODO реалізувати цей шаблон

@app.route("/zascamili", methods=["POST"])
def zascamili():
    if request.method == "POST":
        value = request.form.get("name")
        value2 = request.form.get("surname")
        value3 = request.form.get("bot")
        if value3 == "не знаю":
            return f'''Поздравляем вы не робот потому, что только робот сможет решить это.
                        Мы украли с вашей карточки все деньги,до свидания {value} {value2}!'''

if __name__ == "__main__":
    app.run(debug=True)