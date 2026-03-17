from transformers import pipeline

# Load pretrained QA model
qa_pipeline = pipeline(
    task="question-answering",
    model="distilbert-base-cased-distilled-squad",
    tokenizer="distilbert-base-cased-distilled-squad"
)

def get_answer(question, context):
    # Handle empty input
    if not question.strip():
        return "Please enter a valid question."

    if not context.strip():
        return "Context is empty."

    try:
        result = qa_pipeline(
            question=question,
            context=context
        )
        return result.get('answer', "No answer found.")
    except Exception as e:
        return f"Error: {str(e)}"
