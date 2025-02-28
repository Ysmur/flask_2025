from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def title():
    return "Missiya"

@app.route('/image_mars')
def return_sample_page():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="../static/css/style.css"/>
  </head>
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">

                    <div class="alert alert-success" role="alert">
                        <p>Вот она какая, красная планета.</p>
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
                    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" 
                    crossorigin="anonymous"></script>
                  </body>
                </html>'''

@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="../static/css/style.css"/>
                      </head>
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}!</h1>
                      <h2> Эта планета</h2>

                        <div class="alert alert-success" role="alert">
                            <p>Вот она какая, красная планета.</p>
                        </div>
                        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
                        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" 
                        crossorigin="anonymous"></script>
                      </body>
                    </html>'''



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')