class Game:
    all = []

    def __init__(self, title):
        self._title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        player_results = [result for result in self.results() if result.player == player]
        if not player_results:
            return 0
        total_score = sum(result.score for result in player_results)
        return total_score / len(player_results)


class Player:
    all = []

    def __init__(self, username):
        self._username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set([result.game for result in self.results()]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self._score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        pass
