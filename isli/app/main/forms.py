# coding:utf-8
from flask.ext.wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class EditUserInfoForm(FlaskForm):
    ilsi_source = StringField(u'源', validators=[DataRequired()])
    ilsi_target = StringField(u'目标', validators=[DataRequired()])
    ilsi = StringField(u'ILSI码', validators=[DataRequired()])
    # email = StringField(u'电子邮件', validators=[DataRequired(), Length(1, 64), Email()])
    # password = PasswordField(u'密码确认', validators=[DataRequired()])
