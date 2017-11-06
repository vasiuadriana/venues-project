class InvalidUserSelectionError(Exception):
    def __init__(self, message):
        super(InvalidUserSelectionError, self).__init__(message)
