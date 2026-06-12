from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from projeto_luan.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")


class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    confirmacao_senha = PasswordField("Confirme a senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado. Faça login para continuar")













