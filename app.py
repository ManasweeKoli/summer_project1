from flask import Flask,render_template,url_for,redirect,session,make_response
import mysql.connector as mysql
from flask import request
import os


app=Flask(__name__)
app.secret_key = os.urandom(24)


conn=mysql.connect(host='localhost',database='summer_project',user='root',password='manas@2002')
cursor=conn.cursor()


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/activity')
def activity():
    return render_template("activity.html")  

@app.route('/feedback')
def feedback():
    return render_template("feedback.html") 

@app.route('/testimonials')
def testimonials():
    return render_template("testimonials.html")     

@app.route('/ent')
def ent():
    return render_template("virtual_tour.html")           

@app.route('/music')
def music():
    return render_template("music.html")  

@app.route('/diary')
def diary():
    return render_template("mydiary.html")

@app.route('/books')
def books():
    return render_template("books3.html")

@app.route('/ex_kids')
def ex_kids():
    return render_template("exercise_kids.html")  

@app.route('/ex_adults')
def ex_adults():
    return render_template("exercise_adults.html")  

@app.route('/ex_old')
def ex_old():
    return render_template("exercise_old.html")  

@app.route('/pop')
def pop():
    return render_template("pop.html") 

@app.route('/sour')
def sour():
    return render_template("sour.html")  

@app.route('/christmas')
def christmas():
    return render_template("christmas.html") 

@app.route('/disney')
def disney():
    return render_template("disney.html")     

@app.route('/bollywood')
def bollywood():
    return render_template("bollywood.html")   

@app.route('/worship')
def worship():
    return render_template("worship.html")  

@app.route('/games')
def games():
    return render_template("games.html")  

@app.route('/doodle_art')
def doodle_art():
    return render_template("doodle_art.html")

@app.route('/hangman')
def hangman():
    return render_template("hangman.html")   

@app.route('/snake_game')
def snake_game():
    return render_template("snake_game.html")                                        

@app.route('/feed',methods=['POST'])
def feed():
    name=request.form.get('name')
    email=request.form.get('email')
    comments=request.form.get('comments')
    ratings=request.form.get('ratings')
    
    cursor.execute("""INSERT INTO `feedback`(`name`,`email`,`comments`,`ratings`) VALUES
                   ('{}', '{}', '{}', '{}') """.format(name,email,comments,ratings))

    conn.commit() 

    
    return render_template("feedback_success.html") 

if __name__=="__main__":
  app.run(debug=True)   