from flask import Flask,render_template

skills_app=Flask(__name__)

@skills_app.route("/")
def homepage(): 
    return render_template('homepage.html',pagetitle='Home Page')


@skills_app.route("/About")
def about(): 
    
    return "Hello from about page " 

if __name__ =="__main__":
    skills_app.run(debug=True,port=2040)