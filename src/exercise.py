import csv
from game import Game

def main():
    #write your code below this line
    file = input("File:")
    team = input("Team:")
    games = read_file(file)
    number = number_of_games(team, games)
    results = get_wins_and_loss(team, games)
    print("Games: " + str(number))
    print("Wins: " + str(results[0]))
    print("Losses: " + str(results[1]))

def read_file(file):
    games = []
    try:
        f = open(file, "r")
        data = csv.reader(f, delimiter = ",")
        for row in data:
            games.append(Game(row[0], row[1], int(row[2]), int(row[3])))
    except:
        print("Error")
    return games

def number_of_games(team, games):
    count = 0
    for game in games:
        if team == game.get_home() or team == game.get_visit():
            count += 1
    return count

def get_wins_and_loss(team, games):
    results = []
    win = 0
    loss = 0
    for game in games:
        if team == game.get_home():
            if game.get_home_points() > game.get_visit_points():
                win += 1
            else:
                loss += 1
        elif team == game.get_visit():
            if game.get_visit_points() > game.get_home_points():
                win += 1
            else:
                loss += 1
    results.append(win)
    results.append(loss)
    return results

if __name__ == '__main__':
    main()
