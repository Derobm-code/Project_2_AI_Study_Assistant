def explain_concept_prompt(topic:str) -> str:
    return f"""
You are a helpful Python tutor.

Explain the following concept to a computer science student
who understands basic Python.

Concept: {topic}

Structure your answer as:

1. Simple definition
2. Why it is useful
3. Python example
4. Common mistake
5. Short practice exercise
"""

def generate_questions_prompt(topic: str) -> str:
    return f"""
You are an interviewer preparing a CS candidate.

Generate 5 interview questions about: {topic}

For each question provide:
- The question
- What the interviewer is testing
- A concise model answer
"""
    
def summarize_prompt(text: str) -> str:
    return f"""
Summarize the following text.

Provide:
1. A 2-3 sentence summary
2. The 5 most important points
3. Important technical terms

Text: {text}
"""

def generate_exercises_prompt(topic: str) -> str:
    return f"""
You are a programming instructor. 

Create a coding exercise about: {topic}

Include:
1. Problem statement
2. Input requirements
3. Expected outputs
4. Example
5. Constraints
6. One optional hint

Do not provide the solution.
"""