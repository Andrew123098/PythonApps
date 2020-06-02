from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')                          # Page URL
def home():                              # Define homepage content content
    return render_template("home.html") # FILE MUST BE STORED IN A FOLDER CALLED "TEMPLATES" 

@app.route('/about/')         # Page URL
def about():                  # Define about page content
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True) # Run app in debug mode


