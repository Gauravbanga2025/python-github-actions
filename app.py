from flask import Flask, render_template, request
import random


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def game():
    result = ""
    computer_choice = ""
    user_choice = ""
    if request.method == "POST":
        options = ["rock", "paper", "scissors"]
        user_choice = request.form.get("choice")
        computer_choice = random.choice(options)

        if user_choice == computer_choice:
            result = "It's a tie!"

        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win! 🎉"

        else:
            result = "You lose 🤖"

    return render_template(
        "index.html", result=result,
        user=user_choice, computer=computer_choice)


if __name__ == "__main__":
    app.run(debug=True)
