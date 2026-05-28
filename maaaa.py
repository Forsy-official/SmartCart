import flask
app = flask.Flask("__main__")
from maw import get_info_patyorka
from maw import get_info_lenta
from maw import get_info_magnit


def p():
    a = [
        "Хлеб белый",
        "Молоко 3.2%",
        "Яйца куриные (десяток)",
        "Сахар-песок",
        "Соль поваренная",
        "Картофель",
        "Лук репчатый",
        "Морковь",
        "Яблоки",
        "Бананы",
        "Куриное филе",
        "Гречневая крупа",
        "Рис длиннозерный",
        "Подсолнечное масло",
        "Чай чёрный"
    ]

    answer = []
    for i in a:
        try:
            answer.append(get_info_patyorka(i))
        except Exception as e:
            print(e)
    return answer

def l():
    a = [
        "Хлеб белый",
        "Молоко 3.2%",
        "Яйца куриные (десяток)",
        "Сахар-песок",
        "Соль поваренная",
        "Картофель",
        "Лук репчатый",
        "Морковь",
        "Яблоки",
        "Бананы",
        "Куриное филе",
        "Гречневая крупа",
        "Рис длиннозерный",
        "Подсолнечное масло",
        "Чай чёрный"
    ]

    answer = []
    for i in a:
        try:
            answer.append(get_info_lenta(i))
        except Exception as e:
            print(e)
    return answer

def m():
    a = [
        "Хлеб белый",
        "Молоко 3.2%",
        "Яйца куриные (десяток)",
        "Сахар-песок",
        "Соль поваренная",
        "Картофель",
        "Лук репчатый",
        "Морковь",
        "Яблоки",
        "Бананы",
        "Куриное филе",
        "Гречневая крупа",
        "Рис длиннозерный",
        "Подсолнечное масло",
        "Чай чёрный"
    ]

    answer = []
    for i in a:
        try:
            answer.append(get_info_magnit(i))
        except Exception as e:
            print(e)
    return answer

@app.route('/main')
def main():
    tovar = f()
    return flask.render_template("main.html",text=tovar, filteres=filteres)


def filteres(filter):
    tovar = f()
    ls = []
    for element in tovar:
        if element["shop"] == filter:
            ls.append(element)

    return ls



app.run(debug=True, port="8080")
