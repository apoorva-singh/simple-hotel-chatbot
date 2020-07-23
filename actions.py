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

		return ["guest_count", "room_type"]

	def slot_mappings(self) -> Dict[Text, Any]:

		return {"guest_count": self.from_entity(entity="guest_count", intent=["booking", "inform"]), "room_type": self.from_entity(entity="room_type", intent=["booking","inform"])}

	def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:

		guest_count = tracker.get_slot('guest_count')

		buttons = []
		buttons.append({"title": "Simple"})
		buttons.append({"title": "Deluxe"})

		message = "You can choose from the following category of rooms: {}".format(button_name)
		dispatcher.utter_message(message)

		room_type = tracker.get_slot('room_type')

		return []


class CleanRoom(FormAction):

	def name(self) -> Text:

		return "clean_room"

	@staticmethod
	def required_slots(tracker: Tracker) ->List[Text]:

		return ["time"]

	def slot_mappings(self) -> Dict[Text, Any]:

		return {"time": self.from_entity(entity="time", intent=["room_cleaning", "inform"])}

	def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:

		time = tracker.get_slot('time')

		message = "I have scheduled a cleaning for {}".format(time)
		dispatcher.utter_message(message)

		return []
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
