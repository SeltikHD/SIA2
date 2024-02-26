from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class GreenhouseData(db.Model):
    __tablename__ = 'dados_periodicos'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)
    temperatura = db.Column(db.Float, nullable=False)
    umidade = db.Column(db.Float, nullable=False)
    path_image = db.Column(db.Text)
    cultura_id = db.Column(db.Integer, db.ForeignKey('cultura.id'), nullable=False)

class Cultura(db.Model):
    __tablename__ = 'cultura'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text, nullable=False)
    trefle_id = db.Column(db.Integer, nullable=False)
    condicoes_ideais = db.relationship('CondicoesIdeais', backref='cultura', lazy=True)

class CondicoesIdeais(db.Model):
    __tablename__ = 'condicoes_ideais'
    id = db.Column(db.Integer, primary_key=True)
    temperatura_min = db.Column(db.Float, nullable=False)
    temperatura_max = db.Column(db.Float, nullable=False)
    umidade_min = db.Column(db.Float, nullable=False)
    umidade_max = db.Column(db.Float, nullable=False)
    cultura_id = db.Column(db.Integer, db.ForeignKey('cultura.id'), nullable=False)

class APIKey(db.Model):
    __tablename__ = 'chave_api'
    id = db.Column(db.Integer, primary_key=True)
    chave = db.Column(db.Text, unique=True, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

class LogAcesso(db.Model):
    __tablename__ = 'log_acesso'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)
    ip = db.Column(db.String(45), nullable=False)
    chave_api_id = db.Column(db.Integer, db.ForeignKey('chave_api.id'), nullable=False)
