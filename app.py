from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Game Logic (Modify this to match your script)
number_to_guess = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def guess_number():
    message = ""
    if request.method == "POST":
        try:
            user_guess = int(request.form["guess"])
            if user_guess < number_to_guess:
                message = "Too low! Try again."
            elif user_guess > number_to_guess:
                message = "Too high! Try again."
            else:
                message = "Congratulations! You guessed it!"
        except ValueError:
            message = "Invalid input. Please enter a number."
    
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
