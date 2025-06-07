from flask import Flask, render_template, jsonify
import speedtest

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test_speed")
def test_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()  # Choose the best server based on ping
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping
        server = st.results.server['name']
        isp = st.results.client['isp']

        return jsonify({
            'download_speed': f"{download_speed:.2f} Mbps",
            'upload_speed': f"{upload_speed:.2f} Mbps",
            'ping': f"{ping:.0f} ms",
            'server': server,
            'isp': isp
        })
    except speedtest.SpeedtestException as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
