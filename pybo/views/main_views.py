from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
# redirect(): 입력받은 url로 리다이렉트 해줌
    # url_for('등록된 blueprint이름.등록된 blueprint함수명'): 라우트가 설정된 함수명으로 URL을 역으로 찾아줌
    # _list()에 등록된 라우트는 @bp.route('/list/') 이므로, url_for('question._list)는 bp의 접두어(url_prefix)인 /question/와 /list/가 더해진 /question/list/ URL을 반환한다.
