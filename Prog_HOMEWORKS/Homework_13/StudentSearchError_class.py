class StudentSearchError(Exception):
    def __init__(self):
        self.message = None

    def __str__(self):
        return 'This student is not in this group!'