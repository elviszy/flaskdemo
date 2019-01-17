from flask import Blueprint,request,session,render_template,redirect
from flaskdemo.utils.md5 import md5





acct = Blueprint('acct',__name__)

@acct.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    # 获取用户名与密码
    username = request.form.get('user')
    password = request.form.get('pwd')

    re_passwd = md5(password)
    # 去数据库中校验用户名与密码
    import pymysql
    conn = pymysql.Connect(host='127.0.0.1',user='root',password='',database='flaskdemo',charset='utf8')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select id,nickname from userinfo where user =%(us)s and pwd =%(pw)s',{'us':username,'pw':re_passwd})
    data = cursor.fetchone()
    cursor.close()
    conn.close()

    if not data:
        return render_template('login.html',error='用户名或密码错误')

    # session['user_info'] = {'id':data['id'],'nickname':data['nickname']}
    session['user_info'] = data
    return redirect("/home")




inx = Blueprint('inx',__name__)

@inx.before_request
def process_request():
    if not session.get('user_info'):

        return redirect('/login')
    return None

@inx.route('/home')
def index():
    return render_template('index.html')


