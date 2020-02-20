class Utils:
    """Utilitary class for collecting miscelaneous methods and logic
    """
    def __init__(self, version='0.0'):
        """
        :param version: Version of auxiliary methods
        :ivar version: Internal aux version
        """
        self.version = version

    def get_version(self):
        """
        This method returns the version number

        >>> get_version()
        0.0
        """
        return self.version