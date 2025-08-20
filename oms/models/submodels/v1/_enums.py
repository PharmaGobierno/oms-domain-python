from enum import Enum

class EvidenceType(str, Enum):
    JPEG = "JPEG"
    PNG = "PNG"
    PDF = "PDF"
    B64_IMAGE = "B64_IMAGE"
