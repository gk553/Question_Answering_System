from transformers import pipeline
import traceback

# Load model once
try:
    qa_pipeline = pipeline(
        task="question-answering",
        model="distilbert-base-cased-distilled-squad",
        tokenizer="distilbert-base-cased-distilled-squad"
    )
except Exception as e:
    print("Model loading error:", str(e))
    qa_pipeline = None


def get_answer(question, context):
    if not question.strip():
        return "Please enter a valid question."

    if not context.strip():
        return "Context is empty."

    if qa_pipeline is None:
        return "Model not loaded properly."

    try:
        context = context[:512]  # prevent overflow

        result = qa_pipeline(
            question=question,
            context=context
        )

        return result.get('answer', "No answer found.")

    except Exception:
        return traceback.format_exc()
