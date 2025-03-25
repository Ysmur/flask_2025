from data import db_session, jobs_api
from flask import Flask, render_template, redirect

app = Flask(__name__)


def main():
    db_session.global_init("db/mars_explorer.db")
    app.register_blueprint(jobs_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()