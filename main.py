from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import requests

APP_NAME = "GOAT AI"
# New API Key
API_KEY = "AQ.Ab8RN6LFS6Rgr0ea1Zk-zG-00Pw0_gL4Mvo894EY2iC5Bn9Whw"

# Gemini 3.6 Flash Endpoint
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={API_KEY}"

class GoatAIApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.chat_label = Label(text=f"[color=00ffff]{APP_NAME} IS ONLINE[/color]\n", markup=True, size_hint_y=None)
        self.chat_label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        
        self.scroll = ScrollView(size_hint=(1, 0.8))
        self.scroll.add_widget(self.chat_label)
        self.layout.add_widget(self.scroll)
        
        input_layout = BoxLayout(size_hint=(1, 0.2), spacing=5)
        self.user_input = TextInput(hint_text="Ask something, Sir...", multiline=False)
        send_btn = Button(text="Send", size_hint=(0.3, 1), background_color=(0, 0.7, 1, 1))
        send_btn.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_btn)
        self.layout.add_widget(input_layout)
        
        return self.layout

    def send_message(self, instance):
        query = self.user_input.text.strip()
        if query:
            self.chat_label.text += f"\n[b]You:[/b] {query}"
            self.user_input.text = ""
            payload = {
                "contents": [
                    {
                        "parts": [
                            {"text": f"You are {APP_NAME}, a smart AI assistant. Speak concise Roman Urdu and English. Address user as Sir.\n\nUser: {query}"}
                        ]
                    }
                ]
            }
            headers = {
                "Content-Type": "application/json"
            }
            try:
                res = requests.post(URL, json=payload, headers=headers).json()
                reply = res['candidates'][0]['content']['parts'][0]['text']
                self.chat_label.text += f"\n[color=00ff00][b]{APP_NAME}:[/b] {reply}[/color]\n"
            except Exception as e:
                self.chat_label.text += f"\n[color=ff0000]Error: {e}[/color]\n"

if __name__ == '__main__':
    GoatAIApp().run()
  
