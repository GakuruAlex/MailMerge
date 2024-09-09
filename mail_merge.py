class MailMerge:
    def names(self):
        with open("./Input/Names/invited_names.txt", "r") as file:
            names = file.readlines()
        return names

    