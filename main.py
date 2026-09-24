from ai import AIClient

from models import InterviewQuestions

from ai import AIClient

from prompt import (
    explain_concept_prompt, generate_exercises_prompt, summarize_prompt, generate_questions_prompt
)

ai = AIClient()

def get_non_empty_input(message: str) -> str:
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Please enter something.\n")


def main():
    menu = """

=========================
AI STUDY ASSISTANT
=========================

1. Explain concept
2. Generate interview questions
3. Summarize text
4. Create coding exercise
5. Exit
"""
    while True:
        print(menu)
        choice = input("Choose: ").strip()

        if choice == "1":
            topic = get_non_empty_input("Concept to explain: ")
            prompt = explain_concept_prompt(topic)
        elif choice == "2":
            topic = get_non_empty_input("Topic for interview questions: ")
            prompt = generate_questions_prompt(topic)

            result = ai.ask_structured(
                prompt, InterviewQuestions
            )

            if result is None:
                print("No structured response was returned.")
                input("Press Enter to return to the menu...")
                continue

            # print("\nAI:")
            # print("\nDEBUG")
            # print(type(result))
            # print(result)
            # print(result.model_dump())

            for i, question in enumerate(result.questions, start=1):
                print(f"\nQuestion {i}:")
                print(question.question)
                print(f"\nTesting: {question.testing}")
                print(f"\nModel answer: {question.model_answer}")

            print()
            input("Press Enter to return to the menu...")
            continue

        elif choice == "3":
            text = get_non_empty_input("Text to summarize: ")
            prompt = summarize_prompt(text)
        elif choice == "4":
            topic = get_non_empty_input("Topic for coding exercise: ")
            prompt = generate_exercises_prompt(topic)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")
            continue

        answer = ai.ask(prompt)

        print("\nAI:")
        print(answer)
        print()

        input("Press Enter to return to the menu...")

if __name__ == "__main__":
    main()

