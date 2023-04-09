from flask import Blueprint, render_template, redirect
from ..user.views import USERS
article = Blueprint("article", __name__, url_prefix='/article', static_folder='../static')

ARTICLES = {
    1: {
        'text': 'Text1',
        'author': 1
    },
    2: {
        'text': 'Text2',
        'author': 2
    },
    3: {
        'text': 'Text3',
        'author': 3
    }
}


@article.route('/')
def article_list():
    return render_template('articles/list.html', articles=ARTICLES)


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article = ARTICLES[pk]
    except KeyError:
        # raise NotFound(f'User id {pk} not found!')
        return redirect('/users/')
    return render_template('articles/details.html', article_text=article['text'], article_user=USERS[article['author']])
