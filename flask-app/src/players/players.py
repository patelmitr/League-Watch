from db import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


players = Blueprint('players', __name__)

# Get all players from the DB
@players.route('/players', methods=['GET'])
def get_players():
    cursor = db.get_db().cursor()
    cursor.execute('select first_name, last_name, salary, team_id, player_id, player_number, position, points, assists, steals, blocks, rebounds, turnovers, games_played from players')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get player detail for player with particular userID
@players.route('/players/<playerID>', methods=['GET'])
def get_customer(playerID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from players where player_id = {0}'.format(playerID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get player detail for players with particular number of points
@players.route('/players/<points>', methods=['GET'])
def get_customer(points):
    cursor = db.get_db().cursor()
    cursor.execute('select * from players where points = {0}'.format(points))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get player detail for players with particular number of assists
@players.route('/players/<assists>', methods=['GET'])
def get_customer(assists):
    cursor = db.get_db().cursor()
    cursor.execute('select * from players where assists = {0}'.format(assists))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get player detail for players with particular number of steals
@players.route('/players/<steals>', methods=['GET'])
def get_customer(steals):
    cursor = db.get_db().cursor()
    cursor.execute('select * from players where steals = {0}'.format(steals))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get player detail for players with particular number of blocks
@players.route('/players/<blocks>', methods=['GET'])
def get_customer(blocks):
    cursor = db.get_db().cursor()
    cursor.execute('select * from players where blocks = {0}'.format(blocks))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get player detail for players with particular number of rebounds
@players.route('/players/<rebounds>', methods=['GET'])
def get_customer(rebounds):
    cursor = db.get_db().cursor()
    cursor.execute('select * from players where rebounds = {0}'.format(rebounds))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

#POST a player in the DB
@players.route('/players', methods=['POST'])
def add_new_product ():
    # access json data from, request object.
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    first_name = req_data ['first _name']
    last_name = req_data['last_name']
    salary = req_data['salary']
    team_id = req_data ['team_id']
    player_id = req_data['player_id']
    player_number = req_data['player_number']
    position = req_data ['position']
    points = req_data['points']
    assists = req_data['assists']
    steals = req_data ['steals']
    blocks = req_data['blocks']
    rebounds = req_data['rebounds']
    turnovers = req_data['turnovers']
    games_played = req_data['games_played']

    # construct the insert statement
    insert_stmt = 'INSERT INTO players (first_name, last_name, salary, team_id, player_id, player_number, position, points, assists, steals, blocks, rebounds, turnovers, games_played) VALUES ("'
    insert_stmt += first_name + '", "' + last_name + str(salary) + str(team_id) + str(player_id) + str(player_number) + str(position) + str(points) + str(assists) + str(steals) + str(blocks) + str(rebounds) + str(turnovers) + str(games_played) + ')'

    current_app.logger.info(insert_stmt)

    # execute the query
    cursor = db.get_db().curser()
    cursor.execute(insert_stmt)
    db.get_db().commit()
    return 'Success!'

#TODO
# Put a player in the DB
@players.route('/players', methods=['PUT'])
def get_customer(playerID):
    cursor = db.get_db().cursor()
    cursor.execute('insert first_name, last_name, salary, team_id, player_id, player_number, position, points, assists, steals, blocks, rebounds, turnovers, games_played from players')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response