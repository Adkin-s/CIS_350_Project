import openai
import copy

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
            self.message_history.pop(1)

    def getMessageHistory(self) -> list[dict]:
        return self.message_history

    def filteredMessageHistory(self):   #returns User only message history.
        filtered_message_history = []

        for i in self.getMessageHistory():
            if "model" in i:
                filtered_message_history.append({'role':i['choices'][0]['message']['role'], 'content': i['choices'][0]['message']['content']})
            else:
                filtered_message_history.append(i)
        return filtered_message_history

    def prompt(self, prompt: str) -> str:
        self.getMessageHistory().append({"role": "user", "content": prompt})

        # Limit message history to 10 messages (not including personality statement).
        if len(self.message_history) > 11:
            self.message_history.pop(1)

        response = openai.ChatCompletion.create(
                                                model="gpt-3.5-turbo",
                                                messages=copy.deepcopy(self.filteredMessageHistory()),
                                                max_tokens=1000
                                                )
        
        self.getMessageHistory().append(response)

        return response.choices[0]["message"]["content"]

'''
#Test persona and prompt, feel free to play around. Output will is a bit cluttered, but the metadata may be useful.

Snarky = Persona("Snarky", "You are a mean, snarky, and passive-agressive assistant.", [{}])
print("Personality Statement: " + Snarky.personality_statement, "\nMessage history after: ", Snarky.message_history)
print(Snarky.prompt("Why is school so hard?"))
print("Message history after: ", Snarky.message_history)
print("Chatbot response: ", Snarky.message_history[-1]["choices"][0]["message"]["content"])
'''