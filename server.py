from flask import Flask     # Flask 패키지에서 Flask 클래스를 import하여 사용할 수 있게 함
import random               # random 모듈을 import하여 사용할 수 있게 함

# Flask 클래스의 인스턴스 생성
app = Flask(__name__)

# 아래 코드는 복수의 데이터를 파이썬의 데이터로 전환
# 동급의 데이터(각각의 글들)은 리스트로 표현
# 데이터의 속성(id, title, body)은 딕셔너리로 표현
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

# '/' 경로에 대한 함수 등록
@app.route('/')
def index():
    # HTML 코드를 동적으로 생성하고 있는 모습
    # 토픽 리스트에서 <li> 태그 문자열을 생성
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    # 페이지 본문 문자열 반환
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {liTags}
            </ol>
            <h2>Welcome</h2>
            Hello, Web
        </body>
    </html>
    '''

# '/create/' 경로에 대한 함수 등록
@app.route('/create/')
def create():
    return 'Create'

# '/read/<id>/' 경로에 대한 함수 등록
@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read '+str(id)

# Flask 애플리케이션 실행
app.run(debug=True)