"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from levelupreports.views.helpers import dict_fetch_all


class UserEventList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            db_cursor.execute("""
            SELECT 
                id,
                date,
                time,
                game_name,
                gamer_id,
                full_name
            FROM
                EVENTS_BY_USER
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            events_by_user = []

            for row in dataset:
                event = {
                    "id": row['id'],
                    "date": row['date'],
                    "time": row['time'],
                    "game_name": row['game_name']
                }

                # See if the gamer has been added to the games_by_user list already
                user_dict = None
                for user_event in events_by_user:
                    if user_event['gamer_id'] == row['gamer_id']:
                        user_dict = user_event

                if user_dict:
                    # If the user_dict is already in the games_by_user list, append the game to the games list
                    user_dict['events'].append(event)
                else:
                    # If the user is not on the games_by_user list, create and add the user to the list
                    events_by_user.append({
                        "gamer_id": row['gamer_id'],
                        "full_name": row['full_name'],
                        "events": [event]
                    })

        # The template string must match the file name of the html template
        template = 'users/list_with_events.html'

        # The context will be a dictionary that the template can access to show data
        context = {
            "userevent_list": events_by_user
        }

        return render(request, template, context)
