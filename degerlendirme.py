from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class DegerlendirmeForm(FlaskForm):
    musteri_temsilcisi = StringField('Müşteri Temsilcisi', validators=[DataRequired()])
    degerlendiren = StringField('Değerlendiren', validators=[DataRequired()])
    gsm = StringField('GSM', validators=[DataRequired()])
    cagri_tarihi = StringField('Çağrı Tarihi', validators=[DataRequired()])
    degerlendirme_tarihi = StringField('Değerlendirme Tarihi', validators=[DataRequired()])
    cagri_puani = IntegerField('Çağrı Puanı', validators=[DataRequired()])
    aciklamalar = TextAreaField('Açıklamalar')

    submit = SubmitField('Gönder')
