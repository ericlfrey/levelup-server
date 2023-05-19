CREATE VIEW EVENTS_BY_USER AS
SELECT 
                ga.id gamer_id,
                u.first_name || ' ' || u.last_name AS full_name,
                e.id,
                e.date,
                e.time,
                g.title game_name
            FROM levelupapi_gamer ga
            JOIN auth_user u 
                ON u.id = ga.user_id 
            JOIN levelupapi_event_attendees ea
                ON ea.gamer_id = ga.id
            JOIN levelupapi_event e
                ON e.id = ea.event_id
            JOIN levelupapi_game g
                ON g.id = e.game_id
                ;
