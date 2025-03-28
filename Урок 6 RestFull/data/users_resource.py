from flask_restful import reqparse, abort, Api, Resource
from . import db_session
from .users import User
from flask import jsonify


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    if type(news_id) == int:
        news = session.query(User).get(news_id)
    if not news:
        abort(404, message=f"User {news_id} not found")


class UsersResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        user = session.query(User).get(news_id)

        return jsonify({'users': user.to_dict(
            only=('surname', 'name', 'age'))})

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        users = session.query(User).get(news_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})