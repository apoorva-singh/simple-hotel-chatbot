# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

class BookRoom(FormAction):

	def name(self) -> Text:

		return "book_room"

	@staticmethod
	def required_slots(tracker: Tracker) ->List[Text]:

		return ["guest_count"]

	def slot_mappings(self) -> Dict[Text, Any]:

		return {"guest_count": self.from_entity(entity="guest_count", intent=["booking", "inform"])}

	def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:

		guest_count = tracker.get_slot('guest_count')

		buttons = []
		buttons.append({"title": "Simple"})
		buttons.append({"title": "Deluxe"})

		if button_name == "Simple":
			message = "Your booking of {} simple rooms has been made successfully".format(guest_count)
		else:
			message = "Your booking of {} deluxe rooms has been made successfully".format(guest_count)

		dispatcher.utter_message(message)


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
