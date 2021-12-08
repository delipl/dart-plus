import pickle

from app.main.database.database import get_db
from app.main.model.game import Game


def get_info(id):
    game = None
    db = get_db()
    cursor = db.cursor()
    query = 'SELECT * FROM games WHERE id = ?'
    cursor.execute(query, [id])
    rows = cursor.fetchall()
    if len(rows) == 0:
        return "User does not exist!"
    for i in rows:
        game = Game(i[0], i[1], i[2], i[3], i[4], i[5], pickle.loads(i[6]), pickle.loads(i[7]))
    player = None
    players = []
    main_dictionary = {}
    for p in game.players:
        if 0 < p.attempts < 4:
            player = p
            break
    if player is None:
        player = game.players[0]

    game.players.remove(player)
    for p in game.players:
        dictionary = {"nick": p.nick, "points": p.points}
        players.append(dictionary)

    main_dictionary["nick"] = player.nick
    main_dictionary["points"] = player.points
    main_dictionary["attempts"] = player.attempts
    lastThrows = 0
    for i in range(3 - player.attempts):
        if len(player.throws) > 0:
            lastThrows = lastThrows + player.throws[len(player.throws) -1 - i].getScore()
    main_dictionary["lastThrows"] = lastThrows
    main_dictionary["players"] = players
    return main_dictionary
