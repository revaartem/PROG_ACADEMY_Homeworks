
class TextMethods:
    """
    Class allows you to get statistics about .txt file.
    """

    def __init__(self, file_name):
        """

        :param file_name: name of file in format {name}.txt
        """
        self.file_name = file_name

    def characters(self):
        """

        :return: Quantity of characters in file.
        """
        res = 0
        with open(self.file_name, mode='r') as file:
            for line in file:
                res += len(line)
        return res

    def characters_without_spaces(self):
        """

        :return: Quantity of characters without spaces in file.
        """
        res = 0
        with open(self.file_name, 'r') as file:
            for line in file:
                words_list = line.strip().split(' ')
                new_line_without_spaces = "".join(words_list)
                res += len(new_line_without_spaces)
        return res

    def words(self):
        """

        :return: Quantity of words in file.
        """
        res = 0
        with open(self.file_name, 'r') as file:
            for line in file:
                words_list = line.strip().split()
                res += len(words_list)
        return res

    def sentences(self):
        """

        :return: Quantity of sentences in file.
        """
        res = 0
        with open(self.file_name, 'r') as file:
            for line in file:
                x = line.strip().split(". ")
                if len(x) == 1 and x[0] == '':
                    continue
                res += len(x)
        return res
