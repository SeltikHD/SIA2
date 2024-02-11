from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sklearn.linear_model import LinearRegression
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)


class GreenhouseData(db.Model):
    __tablename__ = 'dados'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)
    temperatura = db.Column(db.Float, nullable=False)
    umidade = db.Column(db.Float, nullable=False)
    path_image = db.Column(db.Text)


@app.route('/')
def index():
    # Exemplo de consulta ao banco de dados para obter os dados mais recentes
    latest_data = GreenhouseData.query.order_by(
        GreenhouseData.timestamp.desc()).first()

    # Exemplo de previsão de temperatura usando regressão linear
    temperatures = [data.temperatura for data in GreenhouseData.query.all()]
    humilities = [data.umidade for data in GreenhouseData.query.all()]
    X = [[temp] for temp in temperatures]
    if len(X) == 0:
        predicted_humidity = 0
    else:
        y = humilities
        model = LinearRegression()
        model.fit(X, y)
        predicted_humidity = model.predict([[latest_data.temperatura]])[0]

    # Exemplo de detecção de anomalias (temperatura abaixo de 10 graus)
    anomalies = GreenhouseData.query.filter(
        GreenhouseData.temperatura < 10).all()

    # Exemplo de reconhecimento de imagem usando OpenCV
    #if latest_data.path_image:
    #    img = cv2.imread(latest_data.path_image)
        # Implemente aqui o código para reconhecimento de imagem
        # (por exemplo, detecção de plantas, pragas, ou doenças)

    return render_template('index.html', latest_data=latest_data, predicted_humidity=predicted_humidity, anomalies=anomalies)


if __name__ == '__main__':
    app.run(debug=True)
