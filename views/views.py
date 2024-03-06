import os
import re

import requests
from flask import (Flask, flash, make_response, redirect, render_template,
                   request, session, url_for)

from app import *

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET'])
def UploadGet():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def UploadPost():
    print('!!')

    file = request.files['file']
    if file.filename == '' :
        flash('No image selected for uploading')
        return redirect(request.url)   
    
    else:
        file.save(file.filename)
    return render_template('upload.html')