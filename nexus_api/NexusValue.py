


class NexusValue:
    uid: str
    value: float

    def __init__(self, Uid, Value):
        self.uid = Uid
        self.value = Value


    def __repr__(self):
        return f"[uid: {self.uid}, value: {self.value}]"
    

