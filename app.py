from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Mikal Tedros! I am adding my first code change'
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/hello')
def hello():
    return render_template('hello.html')

# Route for the home page
@app.route('/')
def home():
    message = "Welcome to My Website!"
    return render_template('home.html', message=message)

# Route for the base page
@app.route('/base')
def base():
    return render_template('base.html')

# Route for the favorite course page
@app.route('/favorite-course', methods=['GET', 'POST'])
def favorite_course():
    if request.method =='POST':
     subject = request.form['subject']
     course_number = request.form['course_number']
     message = "You entered your favorite course as: {} {}".format(subject, course_number)
     return render_template('favoritecourse.html', submitted=True, message=message)
    else:
        return render_template('favoritecourse.html', submitted=False)

# Route for the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        additional_field = request.form['additional_field']
        return render_template('contact.html', submitted=True, first_name=first_name, last_name=last_name, email=email, additional_field=additional_field)
    else:
        return render_template('contact.html', submitted=False)

if __name__ == '__main__':
    app.run()
