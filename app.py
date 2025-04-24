from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///VitalSync.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
app.app_context().push

class Medication(db.Model):
    Time=db.Column(db.String(10), nullable=False)
    Medication=db.Column(db.String(100), primary_key=True, nullable=False)

    def __repr__(self):
        return "Test('%s %s')" % (self.Time, self.Medication)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dash.html")

@app.route('/appointments')
def appointments():
    return render_template("appointments.html")

@app.route('/contact')
def contact():
    return render_template("dash.html")

@app.route('/update', methods=['GET', 'POST'])
def update(med1):
    if request.method=='POST':
        time1 = request.form['time1']
        med1 = request.form['med1']
        medication = Medication.query.filter_by(med1=med1).first()
        medication.time1 = time1
        medication.med1 = med1
        db.session.add(medication)
        db.session.commit()
        return redirect("/appointments")

if __name__=="__main__":
    app.run(debug=True)