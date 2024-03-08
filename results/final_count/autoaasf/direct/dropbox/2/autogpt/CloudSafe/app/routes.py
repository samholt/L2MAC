from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@app.route('/generate_share_link', methods=['POST'])
def generate_share_link():
    file_id = request.form['file_id']
    expiry_time = int(request.form['expiry_time'])
    password = request.form['password']
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiry_time)
    token = s.dumps({'file_id': file_id, 'password': password}).decode('utf-8')
    share_link = url_for('shared_file', token=token, _external=True)
    return jsonify({'share_link': share_link})


@app.route('/shared_file/<token>', methods=['GET', 'POST'])
def shared_file(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        abort(404)
    file_id = data['file_id']
    password = data['password']
    if request.method == 'POST':
        entered_password = request.form['password']
        if entered_password == password:
            return send_from_directory(app.config['UPLOAD_FOLDER'], file_id, as_attachment=True)
        else:
            flash('Incorrect password')
    return render_template('shared_file.html')
