import random
import time

class Problem:
    """
    A class to represent a math problem.

    Attributes:1
        left (int): The left operand.
        right (int): The right operand.
        operator (str): The operator.
        expression (str): The expression as a string.
        answer (int): The correct answer to the expression.
    """
    OPERATORS = ["+", "-", "*"]
    MIN_OPERAND = 3
    MAX_OPERAND = 12

    def __init__(self):
        """
        Initializes the Problem with randomly generated operands and operator.
        """
        self.left = random.randint(self.MIN_OPERAND, self.MAX_OPERAND)
        self.right = random.randint(self.MIN_OPERAND, self.MAX_OPERAND)
        self.operator = random.choice(self.OPERATORS)
        self.expression = f"{self.left} {self.operator} {self.right}"
        self.answer = eval(self.expression)

class Player:
    """
    A class to represent a player.

    Attributes:
        name (str): The player's name.
        wrong_answers (int): The number of wrong answers.
        total_time (float): The total time taken to complete the problems.
    """
    def __init__(self, name):
        """
        Initializes the Player with a name and default values for wrong answers and total time.
        """
        self.name = name
        self.wrong_answers = 0
        self.total_time = 0.0

class Game:
    """
    A class to represent the math quiz game.

    Attributes:
        total_problems (int): The total number of problems.
        players (list): A list of Player objects.
    """
    TOTAL_PROBLEMS = 10

    def __init__(self):
        """
        Initializes the Game with an empty list of players.
        """
        self.players = []

    def add_player(self, name):
        """
        Adds a new player to the game.

        Args:
            name (str): The name of the player.
        """
        self.players.append(Player(name))

    def start(self):
        """
        Starts the game for all players.
        """
        input("Press enter to start ")
        for player in self.players:
            print(f"\n{player.name}'s turn:")
            print("-----------------")
            start_time = time.time()
            for i in range(self.TOTAL_PROBLEMS):
                problem = Problem()
                while True:
                    guess = input(f"Problem #{i + 1}: {problem.expression} = ")
                    if guess == str(problem.answer):
                        break
                    player.wrong_answers += 1
            end_time = time.time()
            player.total_time = round(end_time - start_time)
            print(f"Nice work {player.name}! You finished in {player.total_time} seconds with {player.wrong_answers} wrong answers!")

    def display_results(self):
        """
        Displays the results for all players.
        """
        print("\n-----------------")
        print("Game Results:")
        for player in self.players:
            print(f"{player.name}: {player.total_time} seconds, {player.wrong_answers} wrong answers")

def main():
    """
    The main function to run the game.
    """
    game = Game()
    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        name = input(f"Enter the name of player {i + 1}: ")
        game.add_player(name)

    game.start()
    game.display_results()

if __name__ == "__main__":
    main()
