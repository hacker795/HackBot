import gradio as gr
import openai
import os

# Set up OpenAI API credentials
openai.api_key = "your-api-key"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated response from the API response
    generated_text = response.choices[0].text.strip()

    return generated_text

# Define custom HTML and CSS for the interface
html = """
<div class="chat-container">
    <div class="chat-header">
        <h1>ChatGPT</h1>
    </div>
    <div class="chat-history">
        <div class="chat-message">
            <div class="chat-message-text">Hi, how can I help you today?</div>
            <div class="chat-message-time">1:00 PM</div>
        </div>
    </div>
    <div class="chat-input-container">
        <input type="text" id="chat-input" placeholder="Type your message here...">
        <button id="chat-submit">Send</button>
    </div>
</div>
"""

css = """
.chat-container {
    max-width: 400px;
    margin: 0 auto;
    font-family: Arial, sans-serif;
    background-color: #f7f7f7;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.chat-header {
    padding: 10px;
    background-color: #007bff;
    color: #fff;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

.chat-history {
    padding: 10px;
    max-height: 300px;
    overflow-y: scroll;
}

.chat-message {
    margin-bottom: 10px;
}

.chat-message-text {
    display: inline-block;
    background-color: #fff;
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 5px;
    max-width: 80%;
}

.chat-message-time {
    display: inline-block;
    font-size: 12px;
    color: #999;
    margin-left: 10px;
}

.chat-input-container {
    padding: 10px;
    background-color: #fff;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
}

#chat-input {
    padding: 10px;
    border: none;
    border-radius: 5px;
    width: 80%;
    margin-right: 10px;
}

#chat-submit {
    padding: 10px;
    border: none;
    background-color: #007bff;
    color: #fff;
    border-radius: 5px;
    cursor: pointer;
}
"""

# Define the Gradio interface
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.inputs.Textbox(label=""),
    outputs=gr.outputs.Textbox(label=""),
    title="HackBot",
    description="An AI chatbot created by Twinkle",
    examples=[["Hi, how are you?"]],
    allow_flagging=False,
    layout="vertical",
    theme="default",
    css=css,
    live=True,
    capture_session=True
)

interface.launch()
