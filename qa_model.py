import re

2

B STOP_WORDS =

4

'the', 'is', 'at', 'which', 'on', ,'and', 'a', 'an', 'in', 'of', 'to', 'for', 'what', 'who', 'when', 'where', 'why', 'how', 'does', 'do', 'did', 'is', 'are', 'was', 'were', 'will', 'can', 'could', 'should', 'your', 'with', 'from', 'by', 'that', 'this', 'it', 'its', 'as', 'about'

def normalize_text(text):

I

return re.findall(r"\w+", text.lower())

def best_sentence(question, context):

question_tokens = [tok for tok in normalize_text(question) if tok not in STOP_WORDS]

if not question_tokens:

return None
sentences = re.split(r'(?<=[.!?])\s+', context.strip())

best = None

best_score = 0

for sentence in sentences:

I

sentence_tokens = set(normalize_text(sentence))

score = sum(1 for token in question_tokens if token in sentence_tokens)

if score > best_score:

best_score = score

best = sentence

return best if best_score > ◊ else sentences [0] if sentences else None
def get_answer(question, context):

if not question or not question.strip():

return "Please enter a valid question."

if not context or not context.strip():

return "Context is empty."

answer = best_sentence(question, context)

if answer:

return answer.strip()

return "No answer found."