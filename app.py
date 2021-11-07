from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
# print(app)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    # print(page_name)
    return render_template(page_name)


def write_to_file(data):
    with open('./database.txt', mode='a+', encoding='utf-8') as f:
        email = data['email']
        subject = data['subject']
        message = data['message']
        f.write(f'\n{email} {subject}: {message}')


def write_to_csv(data):
    with open('./database.csv', mode='a', newline='', encoding='utf-8') as file_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        print([email, subject, message])
        csv_writer = csv.writer(
            file_csv,  delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@ app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thank.html')
        except:
            return "did not save to database"
    else:
        return 'form wrong. try again'


# @app.route('/index.html')
# def home():
#     return render_template('index.html')


# @app.route('/works.html')
# def work():
#     return render_template('works.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')
