import gradio as gr
import os
from qa_model import get_answer

# Load document safely
file_path = os.path.join("data", "document.txt")

if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} not found")

with open(file_path, "r", encoding="utf-8") as f:
    context = f.read()

def answer_question(question):
    if not question.strip():
        return "Please enter a question"
    return get_answer(question, context)

demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(label="Ask Question"),
    outputs=gr.Textbox(label="Answer"),
    title="Question Answering System"
)

demo.launch()
