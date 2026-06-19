from projeto_luan import app, bcrypt, database
from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from projeto_luan.form import FormLogin, FormCriarConta
from projeto_luan.models import Usuario


@app.route('/', methods=['GET', 'POST'])
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario)
            return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('homepage.html', form=formlogin)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    formcriarconta = FormCriarConta()

    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data).decode('utf-8')
        usuario = Usuario(username=formcriarconta.username.data,
                          email=formcriarconta.email.data,
                          senha=senha)

        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', id_usuario=usuario.id))

    return render_template('criarconta.html', form=formcriarconta)


@app.route('/perfil/<id_usuario>')
@login_required
def perfil(id_usuario):
    if int(id_usuario) == (current_user.id):
        # o usuário está vendo o perfil dele
        return render_template("perfil.html", usuario=current_user)
    else:
        # Está vendo perfil de outra pessoa
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('perfil.html', usuario=usuario)

