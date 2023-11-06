import openai

#TODO Add error handling for no response from API.

# Dev note, this is a test API key. It is not the real one, if you need to test this, please use your own (https://platform.openai.com/) or ask Eli in-person.
openai.api_key = "OPENAI_API_KEY"

class Persona():
    def __init__(self, name: str, personality_statement: str, message_history: list[dict]) -> None:
        self.name = name
        self.message_history = message_history
        self.personality_statement = personality_statement
        
        # Checks if first message is the persona statement of the AI.
        if self.message_history[0] != {"role": "system", "content": self.personality_statement}: 
            self.message_history.insert(0, {"role": "system", "content": self.personality_statement})

    def updateDB(self, email, message_history) -> None:
        pass
        #TODO make this function update the database with the message history.
    
    def prompt(self, prompt: str) -> str:
        formattedPrompt = {"role": "user", "content": prompt}
        self.message_history.append(formattedPrompt)

        # Limit message history to 10 messages.
        if len(self.message_history) > 11:
            self.message_history.pop(1)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.message_history,
            maximum_tokens=50
            )
        
        self.message_history.append(response)
        #TODO updateDB() with message history.

        return response.choices[0]["message"]["content"]
    