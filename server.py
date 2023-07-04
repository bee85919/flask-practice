from flask import Flask     # Flask 패키지에서 Flask 클래스를 import하여 사용할 수 있게 함
import random               # random 모듈을 import하여 사용할 수 있게 함

# Flask 클래스의 인스턴스 생성
app = Flask(__name__)

# '/' 경로에 대한 함수 등록
@app.route('/')
def index():
    return 'Welcome'

# '/create/' 경로에 대한 함수 등록
@app.route('/create/')
def create():
    return 'Create'

# '/read/<id:int>/' 경로에 대한 함수 등록
@app.route('/read/<int:id>/')
def read(id):
    print(id)
    return 'Read '+str(id)

# Flask 애플리케이션 실행
app.run(debug=True)