from this import d


class Action:

    
    def __init__(self, query) -> None:
        self.query = query
    
    def setaction(self, sender_id, action: str):
        self.query.set_action(sender_id, action)
    
    

