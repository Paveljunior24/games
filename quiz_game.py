class Question:
    """
    A class to represent a quiz question.

    Attributes:
        question (str): The text of the question.
        answer (str): The correct answer to the question.
    """
    def __init__(self, question, answer):
        """
        Initializes the Question with a question and its correct answer.

        Args:
            question (str): The text of the question.
            answer (str): The correct answer to the question.
        """
        self.question = question
        self.answer = answer.lower()

    def check_answer(self, player_answer):
        """
        Check if the provided answer is correct.

        Args:
            player_answer (str): The player's answer.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        return player_answer.lower() == self.answer


class QuizGame:
    """
    A class to represent the quiz game.

    Attributes:
        themes (dict): A dictionary containing themes and their associated questions and answers.
        questions (list): A list of Question objects for the selected theme.
    """
    themes = {
        "informatics": [
            ("What does WWW stand for?", "world wide web"),
            ("What does GPU stand for?", "graphics processing unit"),
            ("What does CPU stand for?", "central processing unit"),
            ("What does RAM stand for?", "random access memory"),
            ("What is the keyword to define a function in Python?", "def"),
            ("What data type is used to store text in Python?", "string"),
            ("Which Python data structure can store key-value pairs?", "dictionary"),
            ("What is the output of print(2 ** 3) in Python?", "8"),
            ("What keyword is used to create a loop in Python?", "for"),
            ("Which function is used to get the length of a list in Python?", "len")
        ],
        "africa": [
            ("What is the largest country in Africa by area?", "algeria"),
            ("Which river is the longest in Africa?", "nile"),
            ("Which desert is the largest in Africa?", "sahara"),
            ("What is the capital of Kenya?", "nairobi"),
            ("In which African country is the ancient city of Timbuktu located?", "mali"),
            ("What is the official language of Egypt?", "arabic"),
            ("Which African country has the most pyramids?", "sudan"),
            ("What is the currency of South Africa?", "rand"),
            ("Which African country is known as the 'Pearl of Africa'?", "uganda"),
            ("What is the largest lake in Africa?", "lake victoria")
        ],
        "biology": [
            ("What is the powerhouse of the cell?", "mitochondria"),
            ("What is the process by which plants make their food?", "photosynthesis"),
            ("Which molecule carries genetic information?", "dna"),
            ("What is the largest organ in the human body?", "skin"),
            ("Which blood cells fight infections?", "white blood cells"),
            ("What is the basic unit of life?", "cell"),
            ("What is the human body's primary source of energy?", "glucose"),
            ("Which organ is responsible for pumping blood?", "heart"),
            ("What type of blood vessels carry blood away from the heart?", "arteries"),
            ("Which organ filters waste from the blood?", "kidney")
        ]
    }

    def __init__(self, theme):
        """
        Initializes the QuizGame with a selected theme.

        Args:
            theme (str): The selected theme for the quiz.

        Raises:
            ValueError: If the selected theme is not valid.
        """
        if theme not in QuizGame.themes:
            raise ValueError("Invalid theme selected.")
        # Initialize questions based on the selected theme
        self.questions = [Question(q, a) for q, a in QuizGame.themes[theme]]

    def start(self, players):
        """
        Starts the quiz game for the given players.

        Args:
            players (list): A list of Player objects.
        """
        total_questions = len(self.questions)
        for player in players:
            print(f"\n{player.name}'s turn:")
            player.score = 0
            for question in self.questions:
                # Prompt the player for an answer
                answer = input(question.question + " (type 'stop' to quit) ").strip().lower()
                if answer == "stop":
                    print(f"{player.name} has chosen to stop the quiz.")
                    break
                if question.check_answer(answer):
                    print("Correct!")
                    player.score += 1
                else:
                    print(f"Incorrect! The correct answer is '{question.answer}'.")
            player.percentage = (player.score / total_questions) * 100
            print(f"{player.name} got {player.score} question(s) correct!")
            print(f"{player.name} got {player.percentage:.2f}%")


class Player:
    """
    A class to represent a player.

    Attributes:
        name (str): The player's name.
        score (int): The player's score.
        percentage (float): The player's score percentage.
    """
    def __init__(self, name):
        """
        Initializes the Player with a name.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.score = 0
        self.percentage = 0.0


def main():
    """
    The main function to run the quiz game.
    """
    print("Welcome to the Quiz")

    # Prompt the user to choose a theme
    theme = input(f"Choose a theme from the following options: {', '.join(QuizGame.themes.keys())} ").strip().lower()

    try:
        game = QuizGame(theme)
    except ValueError as e:
        print(e)
        return

    # Prompt the user to enter the number of players
    num_players = int(input("Enter the number of players: "))
    players = [Player(input(f"Enter the name of player {i + 1}: ")) for i in range(num_players)]

    # Start the quiz game
    game.start(players)


if __name__ == "__main__":
    main()
