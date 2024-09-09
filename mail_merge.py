class MailMerge:
    def names(self):
        """_Open txt of invited people and return the names_

        Returns:
            _list_: _Names_
        """
        with open("./Input/Names/invited_names.txt", "r") as file:
            names = file.readlines()
        return names

    def letter(self)-> str:
        """_Open txt for example output and return str of the letter_

        Returns:
            str: _example of output letter_
        """
        with open("./Input/Letters/starting_letter.txt", "r") as file:
            letter = file.read()
        return letter

    def mail_merge(self):
        """_Get the list of names and example letter, iterate through the names and write the ready to send letter_
        """
        names = self.names()
        names = [name.removesuffix("\n") for name in names]
        letter = self.letter()

        for name in names:
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
                output_letter = letter.replace("[name]", name)
                file.write(output_letter)
