from enum import Enum

class ModeType(Enum):
    """
    Enum representing different modes of operation.
    
    Attributes:
        VIDEO: Represents video file mode.
        CAMERA: Represents real-time camera mode.
    """
    VIDEO = 'video'
    CAMERA = 'camera'
