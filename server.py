from flask import Flask, request, redirect
 
app = Flask(__name__)
 
 
nextId = 4

'''
- 복수의 데이터를 파이썬의 데이터로 전환했다
    - 동급의 데이터(각각의 글들)은 리스트로 표현
    - 데이터의 속성(id,title,body)은 딕셔너리로 표현
    = list + dict 
    / dict in list
'''
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]
 
 
def template(contents, content, id=None):
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
            <li><form action="/delete/{id}/" method="POST"><input type="submit" value="delete"></form></li>
        '''
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
                {contextUI}
            </ul>
        </body>
    </html>
    '''
 
 
def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags
 
 
@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')
 
 
@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}', id)
 
 
 '''
- GET: browser가 정보를 가져올 때 사용
- POST: browser가 정보를 변경할 때 사용
''' 
@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        '''
        1. 서버로 전송할 사용자의 입력 정보를 form 태그로 그룹핑한다.

        2. <form method="XXX"> 
            - 여기에선 GET을 사용한다.         
                - URL으로 입력 정보를 전달할 땐 입력 정보 노출에 주의

        3. <input type="submit"> 
            - submit 버튼 
            → form의 입력 정보 
            → form의 action 
            → method 
            → 전송
        ''' 
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    
    elif request.method == 'POST':
        '''
        1. POST: http 통신의 body를 통해 전송
            → 입력 정보를 감추고, 대용량의 데이터를 전송 할 수 있다. 

        2. browser의 요청 정보를 확인하기 위해 flask.request 모듈 이용. 

        3. request.method: browser가 전송한 method를 확인할 수 있다. 

        4. request.form['NAME']: browser가 전송한 POST 데이터를 확인할 수 있다. 
        '''
        global nextId

        title,body = request.form['title'], request.form['body']

        newTopic = {'id': nextId, 'title': title, 'body': body}        
        topics.append(newTopic)

        url = '/read/'+str(nextId)+'/'
        nextId = nextId + 1
        return redirect(url)
 
 
@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):

    if request.method == 'GET': 
        title = ''
        body = ''
        for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="title" value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>
        '''
        return template(getContents(), content)
    
    elif request.method == 'POST':

        global nextId

        title,body = request.form['title'],request.form['body']

        for topic in topics:
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body
                break

        url = '/read/'+str(id)+'/'
        return redirect(url)
 
 
@app.route('/delete/<int:id>/', methods=['POST'])
def delete(id):
    for topic in topics:
        if id == topic['id']: # 해당 id의 topic을 삭제
            topics.remove(topic)
            break
    return redirect('/')
 
 
app.run(debug=True)