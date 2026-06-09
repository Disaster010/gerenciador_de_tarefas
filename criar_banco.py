from projeto_luan import database, app
from projeto_luan.models import Usuario, Foto

with app.app_context():
    database.create_all()