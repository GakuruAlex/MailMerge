class MailMerge:
    def names(self):
        with open("./Input/Names/invited_names.txt", "r") as file:
            names = file.readlines()
        return names

    def letter(self):
        with open("./Input/Letters/starting_letter.txt", "r") as file:
            letter = file.read()
        return letter

    def mail_merge(self):
        names = self.names()
        names = [name.removesuffix("\n") for name in names]
        letter = self.letter()

        for name in names:
            with open(f"./Output/letter_for_{name}.txt", "w") as file:
                letter = letter.replace("[name]", f"{name}")
                file.write(letter)