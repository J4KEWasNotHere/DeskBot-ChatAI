import time
import requests
import urllib.parse

class ChatBot:
    def __init__(self):
        self.restrictions = (
            "avoid harmful, unethical, illegal, or inappropriate content. "
            "If the input is harmful or inappropriate, respond only with "
            "'Let's move onto another topic.'"
        )

        self.motive = "helpful"
        self.conversation_history = []
        self.max_history_messages = 4 
        self.api_url = "https://text.pollinations.ai/" # this is the chat generation api 'endpoint.'
    
    def get_response(self, message: str) -> str:
        start_time = time.time()

        # Commands
        if message.lower().startswith("/m:"):
            return self._set_motive(message)
        elif message.lower().startswith("/r"):
            return self._reset_conversation()
        elif message.lower().startswith("/help"):
            return "Available commands:\n/m: [motive] - Set the bot's motive or personality.\n/r - Reset the conversation history.\n/help - Show this help message."
        
        self.conversation_history.append(f"< User: {message}")
        self._check_history_limit()

        prompt = self._create_prompt(message)

        response = self._call_api(prompt)
        if not response.startswith("Error:"):
            self.conversation_history.append(f"You: {response} >")
            self._check_history_limit()

        elapsed_time = time.time() - start_time
        
        return f"{response}   ({elapsed_time:.1f}s)"
    
    def _set_motive(self, message: str) -> str:
        self.motive = message[3:].strip()
        return f"Motive set to '{self.motive}'"
    
    def _reset_conversation(self) -> str:
        self.conversation_history = []
        return "Conversation history reset!"
    
    def _create_prompt(self, message: str) -> str:
        history = " | ".join(self.conversation_history)
        return (
            f"{message} | \n"
            f"(your restrictions are {self.restrictions})\n"
            f"your motive or personality is: {self.motive}\n"
            f"chat-history: {history})\n"
        )
    
    def _check_history_limit(self):
        while len(self.conversation_history) > self.max_history_messages:
            self.conversation_history.pop()
    
    def _call_api(self, prompt: str) -> str:
        try:
            encoded_prompt = urllib.parse.quote(prompt)
            url = f"{self.api_url}{encoded_prompt}"
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            return f"Error: Failed to get response - {str(e)}"


if __name__ == "__main__":
    bot = ChatBot()