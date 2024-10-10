from datetime import datetime
from flask import Flask, render_template
from lib.models import db, Sessao, DadoPeriodico, Cultura, SessaoIrrigacao
from dotenv import load_dotenv
import os
import base64

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)

@app.route('/')
def index():
    sessoes_info = []

    # Consulta todas as sessões
    sessoes = Sessao.query.all()

    for sessao in sessoes:
        # Último dado periódicos da sessão
        ultimo_dado = DadoPeriodico.query.filter_by(sessao_id=sessao.id).order_by(DadoPeriodico.data_hora.desc()).first()

        # Verifica a cultura associada
        cultura = Cultura.query.get(sessao.cultura_id)

        # Verifica se a sessão está sendo irrigada
        irrigacao = SessaoIrrigacao.query.filter_by(sessao_id=sessao.id).order_by(SessaoIrrigacao.data_inicio.desc()).first()
        esta_irrigando = irrigacao.status if irrigacao else False

        # Cálculo de tempo de cultivo (considerando a data de início da irrigação como início do cultivo)
        tempo_cultivo = None
        if irrigacao and irrigacao.data_inicio:
            tempo_cultivo = (datetime.now() - irrigacao.data_inicio).days

        # Prepara a imagem em base64
        imagem_base64 = None
        if ultimo_dado and ultimo_dado.imagem:
            imagem_base64 = base64.b64encode(ultimo_dado.imagem).decode('utf-8')

        # Adiciona as informações de cada sessão
        sessoes_info.append({
            'sessao_nome': sessao.nome,
            'cultura_nome': cultura.nome if cultura else 'Sem cultura',
            'tempo_cultivo': tempo_cultivo,
            'ocupada': bool(cultura),
            'esta_irrigando': esta_irrigando,
            'temperatura': ultimo_dado.temperatura if ultimo_dado else 'N/A',
            'umidade_ar': ultimo_dado.umidade_ar if ultimo_dado else 'N/A',
            'umidade_solo': ultimo_dado.umidade_solo if ultimo_dado else 'N/A',
            'imagem_base64': imagem_base64
        })

    print(sessoes_info)
    return render_template('index.html', sessoes_info=sessoes_info)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registrar')
def registrar():
    return render_template('registrar.html')

if __name__ == '__main__':
    app.run(debug=True)
