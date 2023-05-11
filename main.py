from flask import Flask
from flask import redirect, url_for, render_template, request
from flask import session
import database as db
import nlp

# create the flask app
app = Flask(__name__)

# set the session key
app.secret_key = 'session75444u1703'

# create the databasae object
dbo = db.DataBase()


# login route
@app.route('/')
def login():
    return render_template('login.html')


# Registration route
@app.route('/register')
def register():
    return render_template('registration.html')


# perform login
@app.route('/perform_login', methods=['POST'])
def perf_login():
    email = request.form.get('email')
    password = request.form.get('password')

    # check for the profile
    response = dbo.check_login(email, password)

    # check for the response and display the message
    if response:
        session['email'] = email
        session['username'] = dbo.get_profile(email)
        details = session['username']
        print(session)
        return render_template('profile.html', message=details)

    else:
        msg = 'Incorrect Details, Check Username/Password'
        return render_template('login.html', error=msg)


# perform registration
@app.route('/perform_registration', methods=['POST'])
def perf_registration():

    email = request.form.get('email')
    password = request.form.get('password')
    user_name = request.form.get('user_name')

    # insert into the data
    response = dbo.insert_into_db(email, user_name, password)

    # check for the response and display the message
    if response:
        msg = 'Registration Successful, Proceed with Login'
        return render_template('login.html', message=msg)

    else:
        msg = 'Email already Exists, Try with a new Email ID'
        return render_template('registration.html', message=msg)


# do logout
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))


# set api key
@app.route('/set_api')
def api():
    print(session)
    return render_template('set_api.html')


# insert the api key into the database
@app.route('/perform_api', methods=["POST"])
def perf_api():
    key = request.form.get('key')
    if 'email' in session:
        print('Inside if')
        email = session['email']
        response = dbo.insert_api(email, key)
        if response:
            return render_template('profile.html')
        else:
            print('Inside else')
            return redirect('/set_api')

    else:
        return redirect(url_for('login'))


# page for sentiment analysis
@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')


# perform sentiment analysis
@app.route('/perform_sentiment', methods=['POST'])
def perf_sentiment():
    text = request.form.get('text')

    if session:
        email = session['email']
        key = dbo.get_api(email)

        if len(key) != 0:
            result = nlp.sentiment_analysis(text, key)

            return render_template('sentiment.html', result=result)

        else:
            error = 'The API key is not set'
            return render_template('sentiment.html', error=error)


# page for named entity recognition


@app.route('/ner')
def ner():
    return render_template('ner.html')


# perform named entity recognition
@app.route('/perform_ner', methods=['POST'])
def perf_ner():
    text = request.form.get('text')

    if session:
        email = session['email']
        key = dbo.get_api(email)

        if len(key) != 0:
            result = nlp.named_entity_recognition(text, key)

            return render_template('ner.html', result=result)

        else:
            error = 'The API key is not set'
            return render_template('ner.html', error=error)


# page for abuse detection
@app.route('/abuse_detection')
def abuse_detection():
    return render_template('abuse.html')


# perform abuse detection
@app.route('/perform_abuse', methods=['POST'])
def perf_abuse():
    text = request.form.get('text')

    if session:
        email = session['email']
        key = dbo.get_api(email)

        if len(key) != 0:
            result = nlp.abuse_detection(text, key)

            return render_template('abuse.html', result=result)

        else:
            error = 'The API key is not set'
            return render_template('abuse.html', error=error)


# page for similarity score
@app.route('/similarity')
def similarity():
    return render_template('similarity.html')


# perform abuse detection
@app.route('/perform_similarity', methods=['POST'])
def perf_similarity():
    text1 = request.form.get('text1')
    text2 = request.form.get('text2')

    if session:
        email = session['email']
        key = dbo.get_api(email)

        if len(key) != 0:
            result = nlp.similarity_score(text1, text2, key)

            return render_template('similarity.html', result=result)

        else:
            error = 'The API key is not set'
            return render_template('similarity.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
