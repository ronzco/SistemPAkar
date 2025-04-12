from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def diagnose():
    diagnosis = None
    if request.method == 'POST':
        demam = 'demam' in request.form
        batuk = 'batuk' in request.form
        pilek = 'pilek' in request.form
        sakit_tenggorokan = 'sakit_tenggorokan' in request.form

        if demam and batuk and pilek:
            diagnosis = "Anda kemungkinan terkena FLU."
        elif sakit_tenggorokan and pilek:
            diagnosis = "Anda kemungkinan terkena RADANG TENGGOROKAN."
        else:
            diagnosis = "Gejala tidak cukup untuk diagnosis tertentu."

    return render_template('index.html', diagnosis=diagnosis)

if __name__ == '__main__':
    app.run(debug=True)
