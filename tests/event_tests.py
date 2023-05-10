import json
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import Event, Gamer
from rest_framework.authtoken.models import Token


class EventTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'gamers', 'game_types', 'games', 'events']

    def setUp(self):
        self.gamer = Gamer.objects.first()
        token = Token.objects.get(user=self.gamer.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_game(self):
        """
        Ensure we can create a new game.
        """
        # Define the endpoint in the API to which
        # the request will be sent
        url = "/events"

        # Define the request body
        data = {
            "description": "Let's Play Clue!",
            "date": "2023-05-23",
            "time": "17:15",
            "organizer": 1,
            "game": 1
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["description"], "Let's Play Clue!")
        self.assertEqual(json_response["date"], "2023-05-23")
        self.assertEqual(json_response["time"], "17:15:00")

    def test_get_event(self):
        """
        Ensure we can get an existing game.
        """

        # Seed the database with a game
        event = Event()
        event.game_id = 1
        event.organizer_id = 1
        event.description = "Lorem Ipsum"
        event.date = "2023-05-23"
        event.time = "17:15"

        event.save()

        # Initiate request and store response
        response = self.client.get(f"/events/{event.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["description"], "Lorem Ipsum")
        self.assertEqual(json_response["date"], "2023-05-23")
        self.assertEqual(json_response["time"], "17:15:00")

    # def test_change_game(self):
    #     """
    #     Ensure we can change an existing game.
    #     """
    #     game = Game()
    #     game.gametype_id = 1
    #     game.skill_level = 5
    #     game.title = "Sorry"
    #     game.maker = "Milton Bradley"
    #     game.number_of_players = 4
    #     game.gamer_id = 1
    #     game.save()

    #     # DEFINE NEW PROPERTIES FOR GAME
    #     data = {
    #         "gameTypeId": 1,
    #         "skillLevel": 2,
    #         "title": "Sorry",
    #         "maker": "Hasbro",
    #         "numberOfPlayers": 4
    #     }

    #     response = self.client.put(f"/games/{game.id}", data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #     # GET game again to verify changes were made
    #     response = self.client.get(f"/games/{game.id}")
    #     json_response = json.loads(response.content)

    #     # Assert that the properties are correct
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(json_response["title"], "Sorry")
    #     self.assertEqual(json_response["maker"], "Hasbro")
    #     self.assertEqual(json_response["skill_level"], 2)
    #     self.assertEqual(json_response["number_of_players"], 4)
