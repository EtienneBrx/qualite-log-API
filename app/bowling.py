from app.bowling_api import BowlingScore


class BowlingGame:
    def __init__(self):
        self.score = BowlingScore()
        pass

    def launch(self):
        for i in range (10):
            self.request_score()

    def request_score(self):
        pass
        # print('Enter your score')
        # score_val1 = input('first shot :')
        # while not self.check_input(score_val1):
        #     score_val1 = input('Wrong, Enter your score:')
        #
        # score_val2 = 0
        # if not score_val1 == 10:
        #     score_val2 = input('second shot :')
        #     while not self.check_input(score_val2):
        #         score_val2 = input('Wrong, Enter your score:')
        #
        # self.score.add(score_val1, score_val2)

    def check_input(self):
        pass

