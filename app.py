from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, DateField, BooleanField
from wtforms.validators import DataRequired, NumberRange
import click
from werkzeug.security import generate_password_hash
from flask.cli import with_appcontext

# Flask uygulamasını ve SQLAlchemy objesini oluşturma
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/QMDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'thesecretkey'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'  # Tablo adını belirtin
    ID = db.Column(db.Integer, primary_key=True)  # ID sütunu
    NAME = db.Column(db.String(50), nullable=False)  # NAME sütunu
    SURNAME = db.Column(db.Text, nullable=False)  # SURNAME sütunu
    AUTH = db.Column(db.Integer, nullable=True)  # AUTH sütunu, not null kısıtlaması yok
    YON = db.Column(db.Integer, nullable=True)  # YON sütunu, not null kısıtlaması yok
    SKILL = db.Column(db.Integer, nullable=True)  # SKILL sütunu, not null kısıtlaması yok
    username = db.Column(db.String(255), unique=True, nullable=False)  # username sütunu


class CallQueue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)

class Evaluations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    representative = db.Column(db.String(100), nullable=False)
    evaluation_date = db.Column(db.Date, nullable=False)
    call_queue = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    call_date = db.Column(db.Date, nullable=False)
    opening_and_welcome = db.Column(db.Integer, nullable=False)
    effective_listening_and_understanding = db.Column(db.Integer, nullable=False)
    analysis_and_effective_questioning = db.Column(db.Integer, nullable=False)
    speech_and_sounds = db.Column(db.Integer, nullable=False)
    confident_and_courteous_tone = db.Column(db.Integer, nullable=False)
    problem_ownership = db.Column(db.Integer, nullable=False)
    empathy = db.Column(db.Integer, nullable=False)
    time_and_stress_management = db.Column(db.Integer, nullable=False)
    correct_routing = db.Column(db.Integer, nullable=False)
    information_sharing_and_persuasion = db.Column(db.Integer, nullable=False)
    proper_closing_announcement = db.Column(db.Integer, nullable=False)
    information_given_to_related_team = db.Column(db.Integer, nullable=False)
    inappropriate_ending = db.Column(db.Boolean, nullable=False)
    no_or_incorrect_recording = db.Column(db.Boolean, nullable=False)
    rude_or_aggressive_behavior = db.Column(db.Boolean, nullable=False)
    no_contact_number_update = db.Column(db.Boolean, nullable=False)
    customer_hung_up_but_line_left_open = db.Column(db.Boolean, nullable=False)
    kvkk_compliance = db.Column(db.Boolean, nullable=False)
    indifferent_and_insensitive_behavior = db.Column(db.Boolean, nullable=False)
    interrupting_talking_simultaneously = db.Column(db.Boolean, nullable=False)
    late_or_inappropriate_greeting = db.Column(db.Boolean, nullable=False)
    distracted_during_call = db.Column(db.Boolean, nullable=False)
    noises_during_call = db.Column(db.Boolean, nullable=False)
    sharing_personal_information = db.Column(db.Boolean, nullable=False)
    sharing_incorrect_information = db.Column(db.Boolean, nullable=False)
    comments = db.Column(db.Text, nullable=True)



class EvaluationForm(FlaskForm):
    representative = SelectField('Müşteri Temsilcisi', coerce=int, validators=[DataRequired()])
    evaluation_date = DateField('Değerlendirme Tarihi', format='%Y-%m-%d', validators=[DataRequired()])
    call_queue = SelectField('Çağrı Kuyruğu', coerce=int, validators=[DataRequired()])
    phone_number = StringField('Görüşme Yapılan Numara', validators=[DataRequired()])
    call_date = DateField('Çağrı Tarihi', format='%Y-%m-%d', validators=[DataRequired()])
    opening_and_welcome = IntegerField('Açılış ve Karşılama', validators=[NumberRange(min=0, max=5)], default=5)
    effective_listening_and_understanding = IntegerField('Etkin Dinleme ve Anlama', validators=[NumberRange(min=0, max=15)], default=15)
    analysis_and_effective_questioning = IntegerField('Analiz ve Etkin Soru Sorma', validators=[NumberRange(min=0, max=15)], default=15)
    speech_and_sounds = IntegerField('Görüşme Kirliliği Yaratacak Söylem ve Sesler', validators=[NumberRange(min=0, max=10)], default=10)
    confident_and_courteous_tone = IntegerField('Kendinden Emin, Canlı ve Nezaketli Ses Tonu', validators=[NumberRange(min=0, max=10)], default=10)
    problem_ownership = IntegerField('Abonenin Sorununun Sahiplenilmesi', validators=[NumberRange(min=0, max=5)], default=5)
    empathy = IntegerField('Empati', validators=[NumberRange(min=0, max=5)], default=5)
    time_and_stress_management = IntegerField('Süre ve Stres Yönetimi', validators=[NumberRange(min=0, max=5)], default=5)
    correct_routing = IntegerField('Doğru Yönlendirme', validators=[NumberRange(min=0, max=10)], default=10)
    information_sharing_and_persuasion = IntegerField('Bilgiyi Anlaşılır Biçimde Paylaşma, İkna Etme', validators=[NumberRange(min=0, max=10)], default=10)
    proper_closing_announcement = IntegerField('Uygun Kapanış Anonsu Verildi mi?', validators=[NumberRange(min=0, max=5)], default=5)
    information_given_to_related_team = IntegerField('İlgili/ Yönlendirilen Ekipleİlgili Bilgi Verildi mi?', validators=[NumberRange(min=0, max=5)], default=5)
    inappropriate_ending = BooleanField('Sürece uygun olmayan şekilde çağrıyı sonlandırdı (Çağrı Puanı 0)', default=False)
    no_or_incorrect_recording = BooleanField('Kayıt almadı, hatalı kayıt aldı (Çağrı Puanı 0)', default=False)
    rude_or_aggressive_behavior = BooleanField('Azarlama, kaba ve ukala konuşma, bağırma (Çağrı Puanı 0)', default=False)
    no_contact_number_update = BooleanField('İrtibat numarası almama/ güncellememe (Çağrı Puanı 0)', default=False)
    customer_hung_up_but_line_left_open = BooleanField('Müşteri kapattı ancak MT hattı açık bıraktı (Çağrı Puanı 0)', default=False)
    kvkk_compliance = BooleanField('KVKK Uyum  (Çağrı Puanı 0)', default=False)
    indifferent_and_insensitive_behavior = BooleanField('İlgisiz ve duyarsız davranış (Çağrı Puanı -%50 Düşer)', default=False)
    interrupting_talking_simultaneously = BooleanField('Söz kesme, aynı anda konuşma (Çağrı Puanı -%50 Düşer)', default=False)
    late_or_inappropriate_greeting = BooleanField('Çağrıyı geç ya da uygunsuz karşılama (gülme, esneme vs) (Çağrı Puanı -%50 Düşer)', default=False)
    distracted_during_call = BooleanField('Görüşme esnasında farklı bir ekranla, içerikle ilgilenme (Çağrı Puanı -%50 Düşer)', default=False)
    noises_during_call = BooleanField('Yemek, sakız vb. nedenlerle çağrıya yanşayan sesler (Çağrı Puanı -%50 Düşer)', default=False)
    sharing_personal_information = BooleanField('Kendi kişisel bilgilerini müşteri ile paylaşma (Çağrı Puanı -%50 Düşer)', default=False)
    sharing_incorrect_information = BooleanField('Şirket prosedür ve mevzuata aykırı bilgi paylaşma (Çağrı Puanı -%50 Düşer)', default=False)
    comments = TextAreaField('Açıklamalar')



@app.route('/evaluation', methods=['GET', 'POST'])
def evaluation():
    form = EvaluationForm()
    # AUTH değeri 0 olan temsilcileri veritabanından al ve formdaki representative alanı için seçenekleri ayarla
    representatives = User.query.filter_by(AUTH=0).all()
    form.representative.choices = [(rep.ID, f'{rep.NAME} {rep.SURNAME}') for rep in representatives]

    if form.validate_on_submit():
        evaluation = Evaluation(
            # Değerlendirici ID'sini belirtin (evaluator_id değeri burada belirtilmelidir)
            evaluator_id=...,
            representative_id=form.representative.data,
            evaluation_date=form.evaluation_date.data,
            call_queue_id=form.call_queue.data,
            phone_number=form.phone_number.data,
            call_date=form.call_date.data,
            comments=form.comments.data,
            # ... diğer puanlama alanlarını buraya ekleyin
        )
        db.session.add(evaluation)
        db.session.commit()
        flash('Değerlendirme başarıyla kaydedildi!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('evaluation.html', form=form)


@app.route('/dashboard')
def dashboard():
    evaluations = Evaluation.query.all()
    return render_template('dashboard.html', evaluations=evaluations)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)