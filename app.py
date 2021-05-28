from flask import Flask, render_template, request
from reading import value


app = Flask(
        __name__,
        template_folder="./client/templates",
        static_folder="./client/static"
    )

@app.route('/', methods=['GET', 'POST'])

def weather():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        file = request.form['file']
        fps = request.form['fps']
        # result = value(file, fps)
        return render_template(
            'index.html',
            result=file,
            file=file)

    
if __name__ == "__main__":
    app.run(debug=True)