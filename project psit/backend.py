import pymysql
from flask import Flask, render_template, request, make_response

app = Flask(__name__)
conn = pymysql.connect('localhost', 'root', '', 'db_food')


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/input_name", methods=['POST'])
def member():
    if request.method == "POST":
        username = request.form['username']
        cur = conn.cursor()
        cur.execute('select * from dbrestaurant')
        rows = cur.fetchall()
        queue = 0
        if len(rows) == 0:
            queue = 0
        else:
            queue = len(rows)
        resp = make_response(render_template('/menupage/menupage.html', name=username, queue=queue))
        resp.set_cookie('name', username)
        return resp


@app.route("/input_admin", methods=['POST'])
def admin():
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        if name == "admin" and password == "3114":
            return render_template('/choose.html')
        else:
            return render_template('/index.html')


@app.route("/admin")
def linkadmin():
    cur = conn.cursor()
    cur.execute('select * from dbrestaurant')
    rows = cur.fetchall()
    return render_template('/adminpage.html', rows=rows, num=[i for i in range(1, len(rows)+1)])


@app.route("/choose")
def linkchoose():
    return render_template('/choose.html')


@app.route("/adding")
def linking():
    return render_template('/adding.html')


@app.route("/delete/<string:id_data>", methods=['GET'])
def delete(id_data):
    cur = conn.cursor()
    cur.execute("delete from dbrestaurant where id=%s", (id_data))
    conn.commit()
    cur = conn.cursor()
    cur.execute('select * from dbrestaurant')
    rows = cur.fetchall()
    return render_template('/adminpage.html', rows=rows, num=[i for i in range(1, len(rows)+1)])


@app.route("/home")
def home():
    return render_template('/index.html')


@app.route("/menupage")
def menupage():
    return render_template('/menupage/menupage.html')


@app.route('/input', methods=['POST'])
def funcinput():
    valuemoney = {
        "kaprolmukob": ["45", "mukob"],
        "kaprolpig": ["40", "pig"],
        "kaprolsquit": ["50", "squit"],
        "omelet": ["25", "egg"],
        "friegg": ["25", "egg"],
        "ricekareechimp": ["40", "chimp"],
        "ricekareechicken": ["40", "chicken"],
        "ricekareemukob": ["40", "mukob"],
        "firricechimp": ["45", "chimp"],
        "firricechicken": ["40", "chicken"],
        "padciewchimp": ["45", "chimp"],
        "padciewchicken": ["40", "chicken"],
        "padciewpig": ["40", "pig"],
        "makaronechimp": ["45", "chimp"],
        "makaronechicken": ["40", "chicken"],
        "makaronepig": ["40", "pig"],
        "mamapadseafood": ["45", "seafood"],
        "mamapadpig": ["40", "pig"],
        "mamapadmukob": ["45", "mukob"],
        "spaseafood": ["45", "seafood"],
        "spamukob": ["45", "mukob"],
        "spapig": ["40", "pig"],
    }
    viewmoney = 0
    sqlnamefood = ""
    food = request.form.getlist('food')
    for i in valuemoney:
        if i in food:
            viewmoney += int(valuemoney[i][0])
    for i in food:
        sqlnamefood += i + " "
    resp = make_response(render_template('menupage/submitpage.html', valuefood=food, valuemoney=valuemoney, money=viewmoney))
    resp.set_cookie('sqlnamefood', sqlnamefood)
    return resp


@app.route('/submit', methods=['POST'])
def submitingredent():
    if request.method == "POST":
        with conn.cursor() as cursor:
            username = request.cookies.get('name')
            sqlnamefood = request.cookies.get('sqlnamefood')
            sql = "Insert into `dbrestaurant` (`name`, `food`) values(%s, %s)"
            cursor.execute(sql, (username, sqlnamefood))
            conn.commit()
        return render_template('/success.html')
    else:
        return render_template('/unseccess.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
