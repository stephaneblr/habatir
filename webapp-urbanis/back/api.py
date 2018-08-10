from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'webapp'
app.config['MYSQL_DATABASE_HOST'] = 'db'

mysql.init_app(app)


def do_query(query):
    cur = mysql.connect().cursor()
    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return r


@app.route('/sujets')
def get_sujets():
    return jsonify(do_query('select * from webapp.sujet'))


@app.route('/variables')
def get_variables():
    return jsonify(do_query('select * from webapp.variable'))


def get_base_query():
    return """SELECT txt.id_txt, txt.txt, lois.id_loi, lois.description as description_loi, lois.lien FROM webapp.txt 
              LEFT JOIN webapp.lois ON webapp.lois.id_loi = txt.loi 
              LEFT JOIN webapp.regle ON webapp.regle.txt=webapp.txt.id_txt """


class ObjectContientVariable(object):
    id_regle = 0
    id_variable = []

    def __init__(self, id_regle, id_variable):
        self.id_regle = id_regle
        self.id_variable = []
        self.id_variable.append(id_variable)

    def __eq__(self, other):
        return self.id_regle == other.id_regle

    def is_valid(self, param):
        return param in self.id_variable


def group_variable_by_regle(result):
    list_object_cv = []
    for i in range(len(result)):
        object = ObjectContientVariable(result[i]['id_regle'], result[i]['id_variable'])
        if object not in list_object_cv:
            list_object_cv.append(object)
        else:
            index = list_object_cv.index(object)
            list_object_cv[index].id_variable.append(object.id_variable[0])
    return list_object_cv


def filter_regle(args, list_args):

    result = do_query('SELECT * FROM contientvariable WHERE contientvariable.id_variable IN (' + args + ');')
    list_regle = group_variable_by_regle(result)

    for i in range(len(list_args)):
        list_regle[:] = [x for x in list_regle if x.is_valid(list_args[i])]

    args = ''
    for i in range(len(list_regle)):
        if args:
            args += ','
        args += str(list_regle[i].id_regle)
    return args


def get_option2_query(options):
    args = ''
    list_args = []
    for i in range(len(options)):
        if options[i]['option'] != 2:
            continue
        if args:
            args += ','
        args += str(options[i]['id'])
        list_args.append(options[i]['id'])
    if not args:
        return args
    args = filter_regle(args, list_args)
    if not args:
        args = '-1'
    return 'WHERE webapp.regle.id_regle IN (' + args + ') '


def get_option1_query(options):
    args = ''
    for i in range(len(options)):
        if options[i]['option'] != 1:
            continue
        if args:
            args += ','
        args += str(options[i]['id'])
    if not args:
        return args
    return 'regle.contrainte IN (' + args + ') '


def get_option3_query(options):
    args = ''
    for i in range(len(options)):
        if options[i]['option'] != 3:
            continue
        if args:
            args += ','
        args += str(options[i]['id'])
    if not args:
        return args
    return 'regle.change_def IN (' + args + ') '


def get_c1_query(c1):
    if c1 == 0:
        return ''
    return 'webapp.regle.sujet = ' + str(c1) + ' '


def add_operator(condition, is_something_to_add):
    if not is_something_to_add:
        return ''
    if not condition:
        return 'WHERE '
    return 'AND '


@app.route('/search', methods=['POST'])
def post():
    try:
        c1 = request.json['c1']
        c2 = request.json['c2']

        base_query = get_base_query()
        query_opt1 = get_option1_query(c2)
        query_opt2 = get_option2_query(c2)
        query_opt3 = get_option3_query(c2)
        query_c1 = get_c1_query(c1)

        base_query += query_opt2
        base_query += add_operator(query_opt2, query_opt1)
        base_query += query_opt1
        base_query += add_operator(query_opt2 + query_opt1, query_opt3)
        base_query += query_opt3
        base_query += add_operator(query_opt2 + query_opt1 + query_opt3, query_c1)
        base_query += query_c1
        base_query += ';'
        print base_query
        return jsonify(do_query(base_query))
    except Exception as e:
        print e
        return jsonify(str(e))


if __name__ == '__main__':
    app.run(debug=True)
