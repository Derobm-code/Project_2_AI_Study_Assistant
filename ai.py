from ollama import chat


class AIClient:
    def __init__(self, model: str = "llama3.2"):
        self.model = model


    def ask(self, prompt: str) -> str:
        try:
            response = chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            return response.message.content

        except Exception as e:
            return f"Something went wrong: {e}"

    def ask_structured(self, prompt: str, output_model):
        try:
            response = chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                format=output_model.model_json_schema(),
            )

            return output_model.model_validate_json(
                response.message.content
            )

        except Exception as e:
            print(f"Something went wrong: {e}")
            return None
