import flask

App = flask.Flask(__name__)


@App.route('/')
def index():
    every = []
    with open("persistence/KongkhaiStore.txt", "r") as m:
        for line in m:
            e = eval(line)
            every.append(e)
    return flask.render_template('ProdList.html', every=every)


if __name__ == "__main__":
    App.run(port="80")
