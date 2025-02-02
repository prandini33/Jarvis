import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from commands import execute_command

class ActionAbrirNavegador(Action):
    def name(self) -> Text:
        return "action_abrir_navegador"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        execute_command("navegador")
        dispatcher.utter_message(text="Abrindo o navegador.")
        return []

class ActionAbrirTerminal(Action):
    def name(self) -> Text:
        return "action_abrir_terminal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        execute_command("terminal")
        dispatcher.utter_message(text="Abrindo o terminal.")
        return []

class ActionDesligarComputador(Action):
    def name(self) -> Text:
        return "action_desligar_computador"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        execute_command("desligar")
        dispatcher.utter_message(text="Desligando o computador.")
        return []

class ActionReiniciarComputador(Action):
    def name(self) -> Text:
        return "action_reiniciar_computador"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        execute_command("reiniciar")
        dispatcher.utter_message(text="Reiniciando o computador.")
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
