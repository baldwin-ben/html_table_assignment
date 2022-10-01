from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)

@app.route('/')
def hello():
    print("Hello")
    return "Hello World!"

@app.route('/tables')
def render_table():
    users_info = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("index.html", users_info = users_info) #we can reset the variable name but we dont need to. This allows us to access the user_info dictionary in our html.



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.