## booking happy path 1
* greet
  - utter_greet
* mood_great
  - utter_good_to_hear
  - utter_help
* booking
  - book_room
  - form{"name": "book_room"}
  - form{"name": null}
  - utter_booking_confirmation
  - utter_goodbye

## booking happy path 2
* booking
  - book_room
  - form{"name": "book_room"}
  - form{"name": null}
  - utter_booking_confirmation
  - utter_goodbye

## room cleaning happy path 1
* greet
  - utter_greet
* mood_great
  - utter_good_to_hear
  - utter_help
* room_cleaning
  - clean_room
  - form{"name": "clean_room"}
  - form{"name": null}
  - utter_goodbye

## room cleaning happy path 2
* room_cleaning
  - clean_room
  - form{"name": "clean_room"}
  - form{"name": null}
  - utter_goodbye

## room cleaning happy path 3
* greet
  - utter_help
* room_cleaning
  - clean_room
  - form{"name": "clean_room"}
  - form{"name": null}
  - utter_goodbye

## check in path 
* check_in
  - utter_check_in_time

## check out path
* check_out
  - utter_check_out_time

## cancel reservation path
* do_cancel_reservation
  - utter_reservation_cancel

## cancellation policy path
* cancellation_policy
  - utter_cancel_policy

## restaurant availavility enquiry path
* restaurant_enquiry
  - utter_restaurant

## breakfast time enquiry path
* breakfast_time
  - utter_time_for_breakfast

## restaurant timing path
* restaurant_timing
  - utter_time_of_restaurant

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
