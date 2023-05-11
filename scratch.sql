SELECT 
    g.id,
    g.title,
    g.maker,
    g.skill_level,
    g.number_of_players,
    g.game_type_id,
    u.first_name || ' ' || u.last_name AS full_name,
    ga.id
FROM levelupapi_gamer ga
JOIN auth_user u 
    ON u.id = ga.user_id 
JOIN levelupapi_game g 
    ON g.gamer_id = ga.id
