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
