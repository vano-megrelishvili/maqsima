class Vigenere:

    MATRIX = [[j % 26 + 65 for j in range(i, i + 26)] for i in range(26)]

    @classmethod
    def adding_char(cls, data, char, is_lower=False):
        # returning incremented data regarding to the type

        if is_lower:
            char = char.lower()

        data_type = type(data)
        if data_type == str:
            return data + char
        elif data_type == list:
            return data + [char]
        elif data_type == tuple:
            return data + (char,)

    @classmethod
    def match_data_length(cls, data, keyword):
        # repeating keyword until it matches the data’s length

        need_break, main_keyword = False, keyword
        while not need_break:
            for letter in main_keyword:
                if len(keyword) >= len(data):
                    need_break = True
                else:
                    keyword = cls.adding_char(keyword, letter.upper(), letter.islower())

        return keyword

    @classmethod
    def change_input(cls, data):
        # translate from string to list or tuple

        default_data = data
        for char in ['[', ']', '(', ')', ',', "'", '"', ' ']:
            data = data.replace(char, '')

        if '(' in default_data:
            result = ()
            for letter in data:
                result += (letter,)
            return result
        elif '[' in default_data:
            return [letter for letter in data]

        return data

    @classmethod
    def check_char(cls, char):
        # checking if char is a letter
        if ord(char) not in range(65, 91):
            raise ValueError(f"wrong character(or one of them): '{char}'")

    """
    Main methods!
    """

    @classmethod
    def encrypt(cls, data, keyword):
        # encrypting data

        keyword = cls.match_data_length(data, keyword)
        result = type(data)()
        for index, letter in enumerate(data):
            cls.check_char(letter.upper())
            cls.check_char(keyword[index].upper())
            result = cls.adding_char(result, chr(cls.MATRIX[ord(letter.upper()) - 65][ord(keyword[index].upper())
                                                                                      - 65]), letter.islower())

        return result

    @classmethod
    def decrypt(cls, encrypted_data, keyword):
        # decrypting data

        keyword = cls.match_data_length(encrypted_data, keyword)
        result = type(encrypted_data)()
        for index, letter in enumerate(encrypted_data):
            cls.check_char(letter.upper())
            cls.check_char(keyword[index].upper())
            result = cls.adding_char(result, chr(cls.MATRIX[ord(keyword[index].upper()) - 65].index(ord(letter.upper()))
                                                 + 65), letter.islower())

        return result


if __name__ == "__main__":

    try:

        action_input = input("which one do you want , encryption or decryption ?(use upper case)/\nyou can also input"
                             " data as a char tuple or list , just make sure the format is right, \nand the code will "
                             "use only the inserted type of data to perform tasks\n(type E or D): ")
        data_input, keyword_input = Vigenere.change_input(input("input data: ")), Vigenere.change_input(input(
            "input keyword: "))

        if len(data_input) == 0 or len(keyword_input) == 0:
            raise ValueError("input shouldn't be empty")

        if action_input == "E":
            print("encrypted data: ", Vigenere.encrypt(data_input, keyword_input))
        elif action_input == "D":
            print("decrypted data: ", Vigenere.decrypt(data_input, keyword_input))
        else:
            print("wrong input")

    except (TypeError, ValueError) as error:
        print(error)
