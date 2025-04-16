from flask import Flask, jsonify, request
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

API_TOKEN = "supersecrettoken123"

# Available capital cities
capital_timezones = {
    "Washington": "America/New_York",
    "Beijing": "Asia/Shanghai",
    "Tokyo": "Asia/Tokyo",
    "Moscow": "Europe/Moscow",
    "Kinshasa": "Africa/Kinshasa",
    "Jakarta": "Asia/Jakarta",
    "Lima": "America/Lima",
    "Cairo": "Africa/Cairo",
    "Seoul": "Asia/Seoul",
    "Mexico City": "America/Mexico_City",
    "London": "Europe/London",
    "Dhaka": "Asia/Dhaka",
    "Tehran": "Asia/Tehran",
    "Bangkok": "Asia/Bangkok",
    "Hanoi": "Asia/Ho_Chi_Minh",
    "Baghdad": "Asia/Baghdad",
    "Riyadh": "Asia/Riyadh",
    "Hong Kong": "Asia/Hong_Kong",
    "Bogotá": "America/Bogota",
    "Santiago": "America/Santiago",
    "Ankara": "Europe/Istanbul",
    "Singapore": "Asia/Singapore",
    "Kabul": "Asia/Kabul",
    "Nairobi": "Africa/Nairobi",
    "Amman": "Asia/Amman",
    "Algiers": "Africa/Algiers",
    "Berlin": "Europe/Berlin",
    "Madrid": "Europe/Madrid",
    "Buenos Aires": "America/Argentina/Buenos_Aires",
    "Addis Ababa": "Africa/Addis_Ababa",
    "Kuwait City": "Asia/Kuwait",
    "Brasília": "America/Sao_Paulo",
    "Guatemala City": "America/Guatemala",
    "Pretoria": "Africa/Johannesburg",
    "Kyiv": "Europe/Kyiv",
    "Pyongyang": "Asia/Pyongyang",
    "Tashkent": "Asia/Tashkent",
    "Rome": "Europe/Rome",
    "Quito": "America/Guayaquil",
    "Yaoundé": "Africa/Douala",
    "Lusaka": "Africa/Lusaka",
    "Khartoum": "Africa/Khartoum",
    "Taipei": "Asia/Taipei",
    "Sanaa": "Asia/Aden",
    "Luanda": "Africa/Luanda",
    "Ouagadougou": "Africa/Ouagadougou",
    "Accra": "Africa/Accra",
    "Mogadishu": "Africa/Mogadishu",
    "Baku": "Asia/Baku",
    "Phnom Penh": "Asia/Phnom_Penh"
}

def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    decorator.__name__ = f.__name__
    return decorator

# Route to get time info
@app.route('/api/time/<capital>', methods=['GET'])
@token_required
def get_time(capital):
    timezone_name = capital_timezones.get(capital)
    if not timezone_name:
        return jsonify({"error": f"Capital city '{capital}' not available in database."}), 404

    now = datetime.now(ZoneInfo(timezone_name))
    utc_offset = now.utcoffset().total_seconds() / 3600
    offset_str = f"UTC{utc_offset:+.0f}"

    return jsonify({
        "capital": capital,
        "local_time": now.strftime('%Y-%m-%d %H:%M:%S'),
        "utc_offset": offset_str
    })

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

