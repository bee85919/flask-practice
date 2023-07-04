from flask import Flask

app = Flask(__name__)

# 아래 코드는 복수의 데이터를 파이썬의 데이터로 전환
# 동급의 데이터(각각의 글들)은 리스트로 표현
# 데이터의 속성(id, title, body)은 딕셔너리로 표현
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

# HTML 템플릿 생성 함수
def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
        </body>
    </html>
    '''

# 토픽 리스트 HTML 생성 함수 # dynamic
def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

# 메인 페이지 라우팅 
@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

# 독립된 페이지 라우팅 
@app.route('/read/<int:id>/')
def read(id):
    # 토픽 제목과 내용을 찾기 위해 리스트를 순회
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    # 작성된 제목과 내용을 템플릿에 적용
    return template(getContents(), f'<h2>{title}</h2>{body}')

# 새 페이지 생성 라우팅 
@app.route('/create/')
def create():
    return 'Create'

# Flask 애플리케이션 실행
app.run(debug=True)
