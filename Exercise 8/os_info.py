"""
OperatingSystemInfo Class

A class for obtaining information about the operating system.

"""

import platform

class OperatingSystemInfo:
    """
    OperatingSystemInfo class provides information about the operating system.

    Attributes:
    - os_name: Name of the operating system (e.g., 'Windows', 'Linux').
    - os_version: Version of the operating system.
    - architecture: System architecture (e.g., '32-bit', '64-bit').

    Methods:
    - display_info: Display information about the operating system.
    """

    def __init__(self):
        """
        Constructor for OperatingSystemInfo.

        Initializes attributes with information about the operating system.
        """
        self.os_name = platform.system()
        self.os_version = platform.version()
        self.architecture = platform.architecture()

    def display_info(self):
        """
        Display information about the operating system.
        """
        print(f"Operating System: {self.os_name}")
        print(f"Version: {self.os_version}")
        print(f"Architecture: {self.architecture[0]}-bit")

if __name__ == "__main__":
    # Example usage of OperatingSystemInfo
    os_info = OperatingSystemInfo()
    os_info.display_info()
