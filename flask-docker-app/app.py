"""
Простое Flask веб-приложение для демонстрации Continuous Delivery.
"""
from flask import Flask, jsonify, render_template_string
import os
import platform
from datetime import datetime

app = Flask(__name__)

# HTML шаблон главной страницы
HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Docker App</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(4px);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
        }
        .info-box {
            background: rgba(255, 255, 255, 0.2);
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin: 5px;
            transition: background 0.3s;
        }
        .btn:hover {
            background: #45a049;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            font-size: 0.9em;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Flask Docker Application</h1>
        <div class="info-box">
            <h3>Информация о приложении</h3>
            <p><strong>Статус:</strong> ✅ Работает</p>
            <p><strong>Версия:</strong> 1.0.0</p>
            <p><strong>Технологии:</strong> Flask + Docker + CI/CD</p>
        </div>
        <div class="info-box">
            <h3>API Endpoints</h3>
            <p><a href="/api/health" class="btn">GET /api/health</a></p>
            <p><a href="/api/info" class="btn">GET /api/info</a></p>
            <p><a href="/api/time" class="btn">GET /api/time</a></p>
        </div>
        <div class="footer">
            <p>DevOps Практическая работа | Continuous Delivery Demo</p>
        </div>
    </div>
</body>
</html>
"""


@app.route('/')
def home():
    """Главная страница приложения"""
    return render_template_string(HOME_TEMPLATE)


@app.route('/api/health')
def health():
    """Endpoint для проверки здоровья приложения"""
    return jsonify({
        'status': 'healthy',
        'message': 'Application is running successfully',
        'timestamp': datetime.now().isoformat()
    })


@app.route('/api/info')
def info():
    """Endpoint с информацией о системе"""
    return jsonify({
        'application': 'Flask Docker App',
        'version': '1.0.0',
        'python_version': platform.python_version(),
        'platform': platform.system(),
        'hostname': platform.node(),
        'environment': os.environ.get('ENVIRONMENT', 'development')
    })


@app.route('/api/time')
def current_time():
    """Endpoint для получения текущего времени"""
    now = datetime.now()
    return jsonify({
        'current_time': now.isoformat(),
        'date': now.strftime('%Y-%m-%d'),
        'time': now.strftime('%H:%M:%S'),
        'timezone': 'UTC'
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
