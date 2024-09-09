class MailMerge:
    def names(self):
        with open("./Input/Names/invited_names.txt", "r") as file:
            names = file.readlines()
        return names

    def letter(self):
        with open("./Input/Letters/starting_letter.txt", "r") as file:
            letter = file.read()
        return letter

    