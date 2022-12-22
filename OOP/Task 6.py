# Реализовать систему хранения информации о футбольном чемпионате. Информация опирается на следующие основные классы:
# Team (команда), Player (игрок), Match (матч). Эти классы связаны друг с другом посредством ассоциации.
#
# Атрибуты классов
#
# Team
#
# id — уникальный численный идентификатор
# name — имя
# players — игроки, играющие за данную команду в рамках чемпионата
#
# Player
#
# id — уникальный численный идентификатор
# name — имя
# team – команда
#
# Match
#
# id — уникальный численный идентификатор
# date — дата
# location — место
# result — счёт
# team1 — первая команда
# team2 — вторая команда
# players – игроки, участвовавшие в матче.
#
# Реализовать возможность сохранения записей в файл, а также возможность поиска информации о матчах в
# указанные даты (предусмотреть возможность поиска по временному периоду) с выводом информации по командам и
# игрокам, участвовавшим в матчах.

# По поводу методов классов. Например, у Матча можно реализовать метод для добавления игроков, участвующих в матче.
# Команде можно создать метод Трансфер с логикой для добавления и удаления игроков из команды (можно также
# предварительно создать класс Бюджет и использовать здесь его). Для Игрока можно реализовать метод добавления
# сыгранных матчей. Можно и другие методы придумать – я написал первое, что пришло в голову.
# Создавать классы без методов не имеет никакого практического смысла

from random import randint


class Player:

    def __init__(self, identifier, name, team=None, matches=None):
        self.identifier = identifier
        self.name = name
        self.team = team
        self.matches = matches if matches else []

    def add_match(self, match):
        self.matches.append(match)

    def add_team(self, team):
        self.team = team


class Team:

    def __init__(self, identifier, name, players=None, matches=None):
        self.identifier = identifier
        self.name = name
        self.matches = matches if matches else []
        self.players = players if players else []

    def transfer(self, player, action='add'):
        if action == 'add':
            self.players.append(player)
        else:
            ind = None
            for i, p in enumerate(self.players):
                if p.identifier == player.identifier:
                    ind = i
                    break
            if ind is not None:
                self.players = self.players[:ind] + self.players[ind + 1:]

    def add_match(self, match):
        self.matches.append(match)


class Match:

    def __init__(self, identifier, date, location, team1, team2):
        self.identifier = identifier
        self.date = date
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.players = []
        self.team1_score = None
        self.team2_score = None

    def get_result(self):
        return f'{self.team1}:{self.team1_score}, {self.team2}:{self.team2_score}'

    def play(self, players):
        self.players = players
        self.team1_score = randint(0, 9)
        self.team2_score = randint(0, 9)
        self.team1.add_match(self)
        self.team2.add_match(self)
        for p in self.players:
            p.add_match(self)


def search_matches(date, matches):
    results = []
    for match in matches:
        if match.date == date:
            results.append(match)
    return results


def write_to_file(path, match):
    with open(path, 'a') as file:
        for p in match.players:
            file.write(p.name + '\n')
        file.write(match.team1.name)
        file.write(match.team2.name)
