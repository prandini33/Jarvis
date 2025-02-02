# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import subprocess

class ActionAbrirTerminal(Action):
    def name(self) -> Text:
        return "action_abrir_terminal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Lógica para abrir terminal
        try:
            subprocess.Popen(["x-terminal-emulator"])  # Linux
            # subprocess.Popen(["wt"])  # Windows Terminal
            dispatcher.utter_message(text="Terminal aberto com sucesso!")
        except Exception as e:
            dispatcher.utter_message(text="Desculpe, não consegui abrir o terminal.")
        
        return []

class ActionAjustarVolume(Action):
    def name(self) -> Text:
        return "action_ajustar_volume"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        volume = tracker.get_slot("volume")
        # Implemente a lógica real de ajuste de volume aqui
        dispatcher.utter_message(response="utter_volume_ajustado", volume=volume)
        return []

# actions.py
class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        last_message = tracker.latest_message.get('text')
        
        # Lógica de recuperação
        if "terminal" in last_message:
            dispatcher.utter_message("Você quer que eu abra o terminal?")
        else:
            dispatcher.utter_message("Desculpe, não entendi. Poderia reformular?")
        
        return []