import gradio as gr

def respond(message):
    return "You said: " + message  # Replace this with your own logic

iface = gr.Interface(
    fn=respond,
    inputs=gr.Textbox(lines=2, placeholder="Type something..."),
    outputs="text",
    title="My Chat App",
    description="Send me a message!",
    theme="soft",
)

iface.launch()
import gradio as gr
import random

# Keep a random number between 1 and 20
secret_number = random.randint(1, 20)

def guess_number(user_guess):
    global secret_number
    try:
        guess = int(user_guess)
    except ValueError:
        return "Please enter a valid number."

    if guess < secret_number:
        return "Too low! Try again."
    elif guess > secret_number:
        return "Too high! Try again."
    else:
        secret_number = random.randint(1, 20)  # Reset for next game
        return "🎉 Correct! I've thought of a new number now."

iface = gr.Interface(
    fn=guess_number,
    inputs=gr.Textbox(lines=1, placeholder="Enter a number between 1-20"),
    outputs="text",
    title="Guess the Number Game",
    description="Can you guess the number I'm thinking of? Enter your guess below!",
)

iface.launch()
