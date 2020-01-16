from app.bowling_api import BowlingScore


def check_input(value):
    if isinstance(value, int):
        return 0 <= value <= 10
    else:
        return False


class BowlingGame:
    def __init__(self):
        self.score = BowlingScore()

    def launch(self):
        for i in range(10):
            print('Round ', i, ': Enter your score')
            self.request_score()
        print('> Total score', self.score.sum())

    def request_score(self):
        score_val1 = int(input('first shot :'))
        while not check_input(score_val1):
            score_val1 = int(input('Wrong value, Enter your score:'))

        score_val2 = 0
        if not score_val1 == 10:
            score_val2 = int(input('second shot :'))
            while (not check_input(score_val2)) or score_val1 + score_val2 > 10:
                score_val2 = int(input('Wrong value, re-enter second shot:'))

        self.score.add(score_val1, score_val2)
        print('Current score : ', self.score.sum())


if __name__ == "__main__":
    game = BowlingGame()
    game.launch()
