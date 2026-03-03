import gradio as gr
from qa_model import get_answer

# Load document
with open("data/document.txt", "r", encoding="utf-8") as f:
    context = f.read()

def answer_question(question):
    if question.strip() == "":
        return "Please enter a question"
    return get_answer(question, context)

demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(label="Ask Question"),
    outputs=gr.Textbox(label="Answer"),
    title="Question Answering System"
)

demo.launch()