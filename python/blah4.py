

level = input("Easy, medium, or hard difficulty?: ")

while level not in ["easy", "medium", "hard"]:
        level = input("You gotta choose easy, medium, or hard...")


if level == "easy":
        tries = 5