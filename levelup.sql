SELECT * FROM auth_user;
SELECT * FROM authtoken_token;
SELECT * FROM levelupapi_gamer;
SELECT * FROM levelupapi_game;

UPDATE  levelupapi_event
SET game_id = 3
WHERE id = 3;
