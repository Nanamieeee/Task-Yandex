from flask import Flask

app = Flask(__name__)


@app.route('/')
def sy():
    return 'Миссия Колонизация Марса'
@app.route('/index')
def countdown():
    return 'И на Марсе будут яблони цвести!'
@app.route('/promotion')
def add():
    return ''.join('Человечество вырастает из детства.<p>Человечеству мала одна планета.<p>'
            'Мы сделаем обитаемыми безжизненные пока планеты.<p>И начнем с Марса!<p>Присоединяйся!')
@app.route('/image_mars')
def title():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.jpg" alt=", но не нашлась">
                    <h3>Жди нас, Марс!</h3>
                  </body>
                </html>"""
@app.route('/promotion_image')
def promotion_image():
    return """<!doctype html>
                <link rel="stylesheet" href="/static/img/style.css">
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1 class='color1'>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.jpg" alt=", но не нашлась">
                    <h1 class='color2'>Человечество вырастает из детства.</h1>
                    <h1 class='color4'>Человечеству мала одна планета.</h1>
                    <h1 class='color3'>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                    <h1 class='color5'>И начнем с Марса!</h1>
                    <h1 class='color6'>Присоединяйся!</h1>
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
