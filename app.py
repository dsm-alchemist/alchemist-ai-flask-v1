from flask import Flask, render_template, request
import os

app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/multiFileUploads', methods = ['POST'])
def multi_upload_file():
  if request.method == 'POST':
    upload = request.files.getlist("file[]")
    for f in upload:
      f.save('./uploads/' + f.filename)

    return render_template('check.html')


if __name__ == '__main__':
  app.run()