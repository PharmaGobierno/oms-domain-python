from enum import Enum


class OrderTypes(str, Enum):
    REMISSION = "REMISSION"


class RemissionEvents(str, Enum):
    INTEGRATED = "INTEGRATED"
    TRANSPORT_ARRIVAL = "TRANSPORT_ARRIVAL"
    PARTIAL_WITH_REJECTION = "PARTIAL_WITH_REJECTION"
    PARTIAL_COMPLETE = "PARTIAL_COMPLETE"
    COMPLETE = "COMPLETE"
    REJECTED = "REJECTED"


class ResmissionMigrationOrigins(str, Enum):
    FIRESTORE = "FIRESTORE"
    BLUEYONDER = "BLUEYONDER"
