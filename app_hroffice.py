from flask import Flask, render_template, url_for, request, flash, redirect, session, make_response, jsonify
import mimetypes
import os
import psycopg2
import csv
from io import StringIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234asdfasdfasdf'
mimetypes.add_type('application/javascript', '.js')


def _get_connect_db():
  conn = psycopg2.connect(host="localhost",
                          database=os.environ['POSTGRES_DB'],
                          user=os.environ['USERNAME_DB'],
                          password=os.environ['PASSWORD_DB'])
  return conn



def get_connect_db():
  conn = psycopg2.connect(host="localhost",
                          database='hroffice',
                          user='hruser',
                          password='hruser')
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
  conn = get_connect_db()
  cur = conn.cursor()

  table = 'office'


  print('----------  office -----------')
  if request.method == 'POST':
    item = request.get_json() # получаем данные от клиента {'pk':'v1', 'c2': 'v2',...}

    item_columns = tuple(item.keys()) # преобразуем Ключи к виду ('pk', 'c2', 'c3', ...)
    item_columns = item_columns
    item_columns = (',').join(item_columns) # преобразуем последов. ключей (колонок) 'c2, c3, ...,cn'

    item_values = tuple(item.values()) # преобразуем Значен к виду ('v1', 'v2', 'v3', ...)

    # формируем запрос INSERT INTO table (c1, c2, c3) VALUES (v1, v2, v3);
    sql = f"INSERT INTO {table} (" + item_columns + ") "
    sql =  sql + 'VALUES (' + ('%s,' * len(item_values)).strip(',') + ");"
    cur.execute(sql, item_values)
    conn.commit()
    print('---------- POST office -----------')
  
  if request.method == 'PUT':
    item = request.get_json() # получаем данные от клиента {'pk':'v1', 'c2': 'v2',...}
    item_columns = tuple(item.keys()) # преобразуем Ключи к виду ('c1', 'c2', ..., pk)
    pk_name = item_columns[-1] + '=%s;' # извлекаем pk=%5
    item_columns = item_columns[:-1] # удаляем pk из последов Ключей
    item_columns = ('=%s,').join(item_columns) + '=%s' # преобразуем последов. ключей (колонок) 'c2=%s, c3=%s, ...'

    item_values = tuple(item.values()) # преобразуем Значен к виду ('v1', 'v2', 'v3', ...)
    pk_value = item_values[-1] # извлекаем Знач vpk
    item_values = item_values[:-1] # удаляем Знач vpk из основной послед

    # формируем запрос UPDATE table SET c1=v1, c2=v2 WHERE id=2;
    sql = f"UPDATE {table} SET " + item_columns  # "UPDATE table SET c2=%s, c3=%s"
    sql = sql + ' WHERE ' + pk_name            # "UPDATE table SET c2=%s, c3=%s WHERE pk=%s;" 
    cur.execute(sql, (*item_values, pk_value)) # "UPDATE table SET c2=%s, c3=%s WHERE pk=%s;", (v2, v3, vpk)
    conn.commit()
    print('---------- PUT office -----------')
    flash('Соообщение PUT')

  
  if request.method == 'DELETE':
    item = request.get_json() # получаем данные от клиента {'pk2':'v1', 'pk2': 'v2',...}
    item_columns = tuple(item.keys()) # преобразуем Ключи к виду ('pk1', 'pk2', 'pk3', ...)
    item_columns = ('=%s AND ').join(item_columns) + '=%s;' # преобразуем последов. ключей 'pk1=%s AND c3=%s...'

    item_values = tuple(item.values()) # преобразуем Значен к виду ('v1', 'v2', 'v3', ...)

    # формируем запрос DELETE FROM table WHERE id=1 and k=2;
    sql = f"DELETE FROM {table}"  # "UPDATE table SET c2=%s, c3=%s"
    sql = sql + ' WHERE ' + item_columns            # "UPDATE table SET c2=%s, c3=%s WHERE pk=%s;" 

    print(sql)
    print()
 
    cur.execute(sql, item_values) # "DELETE FROM table WHERE pk1=%s AND pk2=%s;", (v1, v2)
    conn.commit()
    print('---------- DELETE office -----------')
    flash('Соообщение DELETE')

  cur.execute('SELECT * FROM office;')
  offices = cur.fetchall()
  cur.close()
  conn.close()
  return render_template('office.html', offices=offices)


@app.route('/employer', methods=['GET','POST','PUT', 'DELETE'])
def employer():
  conn = get_connect_db()
  cur = conn.cursor()

  table = 'employer'

  print('----------  employer -----------')
  if request.method == 'POST':
    item = request.get_json() # получаем данные от клиента {'pk':'v1', 'c2': 'v2',...}

    item_columns = tuple(item.keys()) # преобразуем Ключи к виду ('pk', 'c2', 'c3', ...)
    item_columns = item_columns
    item_columns = (',').join(item_columns) # преобразуем последов. ключей (колонок) 'c2, c3, ...,cn'

    item_values = tuple(item.values()) # преобразуем Значен к виду ('v1', 'v2', 'v3', ...)

    # формируем запрос INSERT INTO table (c1, c2, c3) VALUES (v1, v2, v3);
    sql = f"INSERT INTO {table} (" + item_columns + ") "
    sql =  sql + 'VALUES (' + ('%s,' * len(item_values)).strip(',') + ");"

    cur.execute(sql, item_values)
    conn.commit()
    print('---------- POST employer -----------')
  
  if request.method == 'PUT':
    item = request.get_json() # получаем данные от клиента {'pk':'v1', 'c2': 'v2',...}
    item_columns = tuple(item.keys()) # преобразуем Ключи к виду ('pk', 'c2', 'c3', ...)
    pk_name = item_columns[-1] + '=%s;' # извлекаем pk=%5
    item_columns = item_columns[:-1] # удаляем pk из последов Ключей
    item_columns = ('=%s,').join(item_columns) + '=%s' # преобразуем последов. ключей (колонок) 'c2=%s, c3=%s, ...'

    item_values = tuple(item.values()) # преобразуем Значен к виду ('v1', 'v2', 'v3', ...)
    pk_value = item_values[-1] # извлекаем Знач vpk
    item_values = item_values[:-1] # удаляем Знач vpk из основной послед

    # формируем запрос UPDATE table SET c1=v1, c2=v2 WHERE id=2;
    sql = f"UPDATE {table} SET " + item_columns  # "UPDATE table SET c2=%s, c3=%s"
    sql = sql + ' WHERE ' + pk_name            # "UPDATE table SET c2=%s, c3=%s WHERE pk=%s;" 
    print(sql,(*item_values, pk_value) )
    cur.execute(sql, (*item_values, pk_value)) # "UPDATE table SET c2=%s, c3=%s WHERE pk=%s;", (v2, v3, vpk)
    conn.commit()
    print('---------- PUT employer -----------')
  
  if request.method == 'DELETE':
    item = request.get_json() # получаем данные от клиента {'pk2':'v1', 'pk2': 'v2',...}
    item_columns = tuple(item.keys()) # преобразуем Ключи к виду ('pk1', 'pk2', 'pk3', ...)
    item_columns = ('=%s AND ').join(item_columns) + '=%s;' # преобразуем последов. ключей 'pk1=%s AND c3=%s...'

    item_values = tuple(item.values()) # преобразуем Значен к виду ('v1', 'v2', 'v3', ...)

    # формируем запрос DELETE FROM table WHERE id=1 and k=2;
    sql = f"DELETE FROM {table}"  # "UPDATE table SET c2=%s, c3=%s"
    sql = sql + ' WHERE ' + item_columns            # "UPDATE table SET c2=%s, c3=%s WHERE pk=%s;" 

    print(sql)
    print()
 
    cur.execute(sql, item_values) # "DELETE FROM table WHERE pk1=%s AND pk2=%s;", (v1, v2)
    conn.commit()
    print('---------- DELETE employer -----------')

  cur.execute('SELECT * FROM employer;')
  employers = cur.fetchall()
  cur.execute('SELECT * FROM office;')
  offices = cur.fetchall()
  cur.close()
  conn.close()
  return render_template('employer.html', employers=employers, offices=offices)



@app.route('/childemployer', methods=['GET','POST','PUT', 'DELETE'])
def childemployer():
  conn = get_connect_db()
  cur = conn.cursor()

  table = 'children_employer'

  print('----------  childemployer -----------')
  if request.method == 'POST':
    item = request.get_json() # получаем данные от клиента {'pk':'v1', 'c2': 'v2',...}

    item_columns = tuple(item.keys()) # преобразуем Ключи к виду ('pk', 'c2', 'c3', ...)
    item_columns = item_columns
    item_columns = (',').join(item_columns) # преобразуем последов. ключей (колонок) 'c2, c3, ...,cn'

    item_values = tuple(item.values()) # преобразуем Значен к виду ('v1', 'v2', 'v3', ...)

    # формируем запрос INSERT INTO table (c1, c2, c3) VALUES (v1, v2, v3);
    sql = f"INSERT INTO {table} (" + item_columns + ") "
    sql =  sql + 'VALUES (' + ('%s,' * len(item_values)).strip(',') + ");"

    cur.execute(sql, item_values)
    conn.commit()
    print('---------- POST childemployer -----------')
  
  if request.method == 'PUT':
    item = request.get_json() # получаем данные от клиента {'pk':'v1', 'c2': 'v2',...}
    item_columns = tuple(item.keys()) # преобразуем Ключи к виду ('pk', 'c2', 'c3', ...)
    pk_name = item_columns[-2] + '=%s AND ' # извлекаем pk=%5
    pk_name2 = item_columns[-1] + '=%s;'
    item_columns = item_columns[:-2] # удаляем pk из последов Ключей
    item_columns = ('=%s,').join(item_columns) + '=%s' # преобразуем последов. ключей (колонок) 'c2=%s, c3=%s, ...'

    item_values = tuple(item.values()) # преобразуем Значен к виду ('v1', 'v2', 'v3', ...)
    pk_value = item_values[-2] # извлекаем Знач vpk
    pk_value2 = item_values[-1] # извлекаем Знач vpk
    item_values = item_values[:-2] # удаляем Знач vpk из основной послед

    # формируем запрос UPDATE table SET c1=v1, c2=v2 WHERE id=2;
    sql = f"UPDATE {table} SET " + item_columns  # "UPDATE table SET c2=%s, c3=%s"
    sql = sql + ' WHERE ' + pk_name + pk_name2   # "UPDATE table SET c2=%s, c3=%s WHERE pk=%s;" 

    cur.execute(sql, (*item_values, pk_value, pk_value2)) # "UPDATE table SET c2=%s, c3=%s WHERE pk=%s;", (v2, v3, vpk)
    conn.commit()
    print('---------- PUT childemployer -----------')
  
  if request.method == 'DELETE':
    item = request.get_json() # получаем данные от клиента {'pk2':'v1', 'pk2': 'v2',...}
    item_columns = tuple(item.keys()) # преобразуем Ключи к виду ('pk1', 'pk2', 'pk3', ...)
    item_columns = ('=%s AND ').join(item_columns) + '=%s;' # преобразуем последов. ключей 'pk1=%s AND c3=%s...'

    item_values = tuple(item.values()) # преобразуем Значен к виду ('v1', 'v2', 'v3', ...)

    # формируем запрос DELETE FROM table WHERE id=1 and k=2;
    sql = f"DELETE FROM {table}"  # "UPDATE table SET c2=%s, c3=%s"
    sql = sql + ' WHERE ' + item_columns            # "UPDATE table SET c2=%s, c3=%s WHERE pk=%s;" 
    cur.execute(sql, item_values) # "DELETE FROM table WHERE pk1=%s AND pk2=%s;", (v1, v2)
    conn.commit()
    print('---------- DELETE childemployer -----------')


  cur.execute('SELECT * FROM employer;')
  employers = cur.fetchall()
  cur.execute(f'SELECT * FROM {table};')
  children = cur.fetchall()
  cur.close()
  conn.close()

  return render_template('childemployer.html', children=children, employers=employers)


@app.route('/download/<int:path>')
def child_group_office_item(path=None):
  print('------ /download/<path> ------')
  print(f'========== ${path} ===========')

  conn = get_connect_db()
  cur = conn.cursor()


  sql = 'SELECT e.office_number, ch.child_birth_cert_number, ' \
                               ' ch.employer_number, ' \
                               ' ch.child_name, ' \
                               ' EXTRACT(YEAR FROM ch.child_birth_year), ' \
                               ' ch.child_gender ' \
                               'FROM children_employer ch ' \
         'INNER JOIN employer e ON ch.employer_number = e.employer_number AND ' \
         'e.office_number IN (SELECT office_number FROM office o WHERE o.office_number=%s );'

  print(sql)
  print()
  cur.execute(sql, (path,)) # "UPDATE table SET c2=%s, c3=%s WHERE pk=%s;", (v2, v3, vpk)
  children_emp_office = [('номер отд.','Номер свид. о рожд.','имя ребенка','год рожд. реб.','пол реб.')]
  children_emp_office = children_emp_office + cur.fetchall()
  print(type(child_group_office))
  cur.close()
  conn.close()

  response = make_response(jsonify(children_emp_office), 200)
  return response



@app.route('/chooseoffice')
def child_group_office():
  conn = get_connect_db()
  cur = conn.cursor()
  cur.execute('SELECT * FROM office;')
  offices = cur.fetchall()
  cur.close()
  conn.close()
  print('------ chooseoffice ------')
  return render_template('chooseoffice.html', offices=offices)


@app.route('/listdb')
def listDB():
  conn = get_connect_db()
  cur = conn.cursor()

  table1 = 'office'
  table2 = 'employer'
  table3 = 'children_employer'

  sql = 'SELECT t1.office_number, t1.office_name, t2.employer_number, t2.employer_surname, ' \
        't2.employer_firstname, t2.employer_patronymic, t2.employer_gender, t2.employer_length_work, ' \
        't3.child_birth_cert_number, t3.child_name, t3.child_birth_year, t3.child_gender ' \
        f'FROM {table1} t1 LEFT JOIN {table2} t2 ON ' \
        f't1.office_number=t2.office_number LEFT JOIN {table3} t3 ON ' \
         't2.employer_number=t3.employer_number ORDER BY  t1.office_number, t2.employer_number ;' 

# кол-во детей у родителей
# employer_surname employer_number	employer_surname	employer_firstname	employer_patronymic	employer_gender	employer_length_work	office_number	count	employer_number
  sql_count_ch = 'select  e.employer_number, e.employer_surname, e.employer_firstname, e.employer_patronymic, ' \
                'e.office_number, ch.count_ch from employer e ' \
                'join (select count(*) as count_ch, ce.employer_number from children_employer ce group by ce.employer_number) ' \
                'as ch on e.employer_number = ch.employer_number; '

  sql_office_child = 'select o.office_number,	o.office_name,	ch_in_off from office o ' \
  'join (select sum(am_ch) as ch_in_off,e.office_number  from employer e ' \
  'join (select count(*) as am_ch, ce.employer_number from children_employer ce group by ce.employer_number) as ch ' \
  'on e.employer_number = ch.employer_number group by e.office_number) as total_ch ' \
  'on total_ch.office_number = o.office_number ;'

  cur.execute(sql)
  alldb = cur.fetchall()

  cur.execute(sql_count_ch)
  count_ch = cur.fetchall()

  cur.execute(sql_office_child)
  office_child = cur.fetchall()

  cur.close()
  conn.close()
  return render_template('listdb.html',alldb=alldb, count_ch=count_ch, office_child=office_child)


@app.route('/download')
def download():
  data = [{"a":"1", "b":"2"},
          {"a":"3", "b":"4"}]
  
  output = StringIO()
  writer = csv.DictWriter(output, fieldnames=["a", "b"])

  writer.writeheader()
  writer.writerows(data)

  output.seek(0)

  response = make_response(output.getvalue())

  response.headers["Content-Disposition"] = "attachment; filename=hroffice_data.csv"
  response.headers["Content-type"] = "text/csv"
  


  print('========== DownLoad ==========')
  return response


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





















