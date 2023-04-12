from flask import Flask
from flask import render_template
from peewee import *
app = Flask(__name__)

db = SqliteDatabase('foreclosures.db')

class Notice(Model):
    id = IntegerField(unique=True)
    zip = CharField()
    month = DateField()
    notices = IntegerField()

    class Meta:
        table_name = "notices"
        database = db

@app.route("/")
def index():
    notice_count = Notice.select().count()
    all_zips = (Notice.select(Notice.zip).distinct())
    template = 'index.html'
    return render_template(template, count = notice_count, all_zips = all_zips)

@app.route('/zipcode/<slug>')
def detail(slug):
    zipcode = slug
    notices = Notice.select().where(Notice.zip==slug)
    total_notices = Notice.select(fn.SUM(Notice.notices).alias('sum')).where(Notice.zip==slug).scalar()
    notice_json = []
    for notice in notices:
        notice_json.append({'x': str(notice.month.year) + ' ' + str(notice.month.month), 'y': notice.zip, 'heat': notice.notices})
    return render_template("detail.html", zipcode=zipcode, notices=notices, notices_count=len(notices), total_notices = total_notices, notice_json = notice_json)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)