class StudentAddError(Exception):
    def __init__(self):
        self.message = None

    def __str__(self):
        """

        :return: Error message
        """
        return 'This student is already in this group or reached max group size!'
