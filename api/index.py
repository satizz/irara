from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://avnadmin:AVNS__XMFENAQ3Jjq2nY86ul@traffic-irara.e.aivencloud.com:12679/defaultdb?sslmode=require'  # Replace username and password with your PostgreSQL credentials
db = SQLAlchemy(app)


class AccidentReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    severity = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=True)
    weather_condition = db.Column(db.String(50), nullable=True)
    road_condition = db.Column(db.String(50), nullable=True)
    casualties = db.relationship('Casualty', backref='accident', lazy=True)
    cause = db.Column(db.Text, nullable=True)
    num_vehicles_involved = db.Column(db.Integer, nullable=False, default=1)


class Casualty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    accident_id = db.Column(db.Integer,
                            db.ForeignKey('accident_report.id'),
                            nullable=False)


# Update the form.html to include input fields for accident details
@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        # Save new accident report to database
        accident = AccidentReport(
            location=request.form['location'],
            date=datetime.strptime(request.form['date'], '%Y-%m-%d'),
            time=datetime.strptime(request.form['time'], '%H:%M').time(),
            severity=request.form['severity'],
            description=request.form['description'],
            weather_condition=request.form['weather_condition'],
            road_condition=request.form['road_condition'],
            cause=request.form['cause'],
            num_vehicles_involved=int(request.form['num_vehicles_involved']))

        db.session.add(accident)

        if 'casualty_name' in request.form:
            for i in range(len(request.form.getlist('casualty_name'))):
                casualty = Casualty(
                    name=request.form.getlist('casualty_name')[i],
                    age=int(request.form.getlist('casualty_age')[i]),
                    gender=request.form.getlist('casualty_gender')[i])
                accident.casualties.append(casualty)
                db.session.add(casualty)

        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('form.html')


@app.route('/')
def index():
    accidents = AccidentReport.query.all()
    return render_template('./index.html', accidents=accidents)


if __name__ == "__main__":
    app.run()
