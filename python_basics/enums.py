
# from enum import Enum

# class DroneStage(Enum):
#     ACT_IDLE        = 0
#     ACT_PLACEHOLDER = 1
#     ACT_NAVIGATE    = 2
#     ACT_SAFETY      = 3
#     ACT_LANDING     = 4
#     ACT_TRACKING    = 5
#     ACT_MISSION     = 6
#     ACT_INSPECT     = 7
#     ACT_TAKEOFF     = 8
#     ACT_FLAG_POLE   = 9
#     ACT_MAPPING     = 10
#     ACT_CIRCLE      = 11
#     ACT_AVOID       = 12
#     ACT_RND         = 13



# droneStage = '231'
# if droneStage is not None and isinstance(droneStage, int):
#     droneStage = droneStage >> 4

#     # Make sure droneStage is on of the DroneStage enum values
#     values = [member.value for member in DroneStage]
#     if droneStage not in values:
#         print("Got no valid drone stage: " %droneStage)
#         droneStage = None
# else:
#     print("Got invalid drone stage: %s" %droneStage)
#     droneStage = None




from enum import Enum

class EventTypes(Enum):
    UNKNOWN = "base.unknown"
    ERROR   = "base.error"
    INFO    = "base.info"
    EVENT   = "base.event"

    def __str__(self):
        return self.value

# Usage
print(type(EventTypes.UNKNOWN))  # Output: <enum 'EventTypes'>
print(EventTypes.UNKNOWN)  # Output: base.unknown
print(EventTypes.ERROR)    # Output: base.error
print(EventTypes.INFO)     # Output: base.info
print(EventTypes.EVENT)    # Output: base.event
