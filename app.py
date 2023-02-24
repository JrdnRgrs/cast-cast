from flask import Flask, render_template, request
import subprocess
import jinja2

app = Flask(__name__)

env = jinja2.Environment()
env.globals.update(zip=zip)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        cast_device = request.form['device']
        audio_url = request.form['url']
        if request.form['action'] == 'Start':
            subprocess.Popen(['catt', '-d', cast_device, 'cast', audio_url])
            message = 'Casting to device with IP ' + cast_device
        elif request.form['action'] == 'Stop':
            subprocess.Popen(['catt', '-d', cast_device, 'stop'])
            message = 'Stopped casting to device with IP ' + cast_device

    output = subprocess.check_output(['catt', 'scan']).decode('utf-8').split('\n')[1:]
    devices = [line.split(' - ')[1] for line in output if line]
    ips = [line.split(' - ')[0] for line in output if line]
    return render_template('index.html', devices=devices, ips=ips, zip=zip, message=message)


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0')