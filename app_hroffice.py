from flask import Flask, render_template, url_for, request, flash, redirect, session, make_response, jsonify
import mimetypes, os, psycopg2, json

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234asdfasdfasdf'
mimetypes.add_type('application/javascript', '.js')


def get_connect_db():
  conn = psycopg2.connect(host="localhost",
                          database=os.environ['POSTGRES_DB'],
                          user=os.environ['USERNAME_DB'],
                          password=os.environ['PASSWORD_DB'])
  return conn

@app.route('/test')
def test():
  conn = get_connect_db()
  cur = conn.cursor()
  cur.execute('SELECT * FROM office;')
  offices = cur.fetchall()
  cur.close()
  conn.close()
  return render_template('test.html', offices=offices)



@app.route('/index', methods=['GET','POST'])
@app.route('/', methods=['GET','POST'])
def index():
  msg = ''
  if request.method == 'POST':
    print(request.form)
    if request.form['role_'] == 'hr' and \
        request.form['passw'] == '123':
      return render_template('menu2.html')

    elif  request.form['role_'] == 'manager' and \
        request.form['passw'] == '321':
      return render_template('menu1.html')

    else:
      msg = 'Какая-то ошибка'

  return render_template('index.html', message=msg)


@app.route('/menu1')
def menu1():
  return render_template('menu1.html')


@app.route('/menu2')
def menu2():
  return render_template('menu2.html')


# @app.route('/office/<int:id>', methods=['DELETE'])
@app.route('/office', methods=['GET','POST','PUT', 'DELETE'])
def office():
  print('----------  office -----------')
  if request.method == 'POST':
    print(request.get_json())
    print('---------- POST office -----------')
    flash('Соообщение POST')

  
  if request.method == 'PUT':
    print(request.get_json())
    print('---------- PUT office -----------')
    flash('Соообщение PUT')

  
  if request.method == 'DELETE':
    print(request.get_json())
    print('---------- DELETE office -----------')
    flash('Соообщение DELETE')

  return render_template('office.html')


@app.route('/employer', methods=['GET','POST','PUT', 'DELETE'])
def emploer():
  print('----------  emploer -----------')
  if request.method == 'POST':
    print(request.get_json())
    print('---------- POST emploer -----------')
    flash('Соообщение POST')

  
  if request.method == 'PUT':
    print(request.get_json())
    print('---------- PUT emploer -----------')
    flash('Соообщение PUT')

  
  if request.method == 'DELETE':
    print(request.get_json())
    print('---------- DELETE emploer -----------')
    flash('Соообщение DELETE')

  return render_template('employer.html')



@app.route('/childemployer', methods=['GET','POST','PUT', 'DELETE'])
def childemployer():
  print('----------  childemployer -----------')
  if request.method == 'POST':
    print(request.get_json())
    print('---------- POST childemployer -----------')
    flash('Соообщение POST')

  
  if request.method == 'PUT':
    print(request.get_json())
    print('---------- PUT childemployer -----------')
    flash('Соообщение PUT')

  
  if request.method == 'DELETE':
    print(request.get_json())
    print('---------- DELETE childemployer -----------')
    flash('Соообщение DELETE')

  return render_template('childemployer.html')


@app.route('/download/<path>')
def child_group_office_item(path=None):
  print('------ /download/<path> ------')
  print(f'========== ${path} ===========')
  data = {"message": "This has custom headers", "m": "Ters", "n": "NNnn"}
  response = make_response(jsonify(data), 200)
  # response.headers["X-Custom-Header"] = "FlaskApp"
  return response
  # return {"a":123, "b": "adf"}   # json.dumps('{"a":"12", "b":"c"}')


@app.route('/chooseoffice')
def child_group_office(path=None):
  print('------ chooseoffice ------')
  print(f'========== ${path} ===========')
  return render_template('chooseoffice.html')


@app.route('/listdb')
def listDB():
  return render_template('listdb.html')


@app.route('/download')
def download():
  print('========== DownLoad ==========')
  return render_template('listdb.html')


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html'), 404

















if __name__ == "__main__":
  app.run(debug=True)














# @app.route('/office/<int:id>', methods=['DELETE'])
# @app.route('/office', methods=['GET','POST','PUT'])
# def office(id=None):
#   conn = get_connect_db()
#   cur = conn.cursor()

#   conn.close()
#   if request.method == 'POST':
#     print(request.get_json())
#     print('---------- POST -----------')
#     flash('Соообщение POST')

  
#   if request.method == 'PUT':
    # const user = { "name": "Ivan", "age": 25 }; console.log(user["age"]); console.log(user.age)
    # UPDATE users SET name = 'Ivan', age = 30 WHERE id = 5;
    
    # import json
    # json_data = '{"name": "Ivan", "age": 30, "city": "Moscow"}'
    # data = json.loads(json_data)
    # for key, value in data.items():
    # print(f"{key} = {value}")


  #   print(request.get_json())
  #   cur.execute(f'UPDATE office SET name = "Ivan"  WHERE office_number=${id};')
  #   print('---------- PUT -----------')
  #   flash('Соообщение PUT')

  
  # if request.method == 'DELETE':
  #   print(id)
  #   cur.execute(f'DELETE * FROM office WHERE office_number=${id};')
  #   print('---------- DELETE -----------')
  #   flash('Соообщение DELETE')

  
  # cur.execute('SELECT * FROM office;')
  # offices = cur.fetchall()
  # cur.close()
  # conn.close()


  # return render_template('office.html', offices=offices)





















