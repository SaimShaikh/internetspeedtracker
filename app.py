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
        print("Testing internet speed...")
        download_speed = st.download() / 1000000  # Convert to Mbps
        upload_speed = st.upload() / 1000000  # Convert to Mbps
        ping = st.results.dict()['ping']
        server = st.results.dict()['server']['name']
        isp = st.results.dict()['client']['isp']
        return jsonify({
            'download_speed': f"{download_speed:.2f} Mbps",
            'upload_speed': f"{upload_speed:.2f} Mbps",
            'ping': f"{ping} ms",
            'server': server,
            'isp': isp
        })
    except speedtest.SpeedtestException as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)