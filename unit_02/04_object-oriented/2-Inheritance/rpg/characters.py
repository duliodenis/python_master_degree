class Character:
    def __init__(self, name="", **kwargs):
        if not name:
            raise ValueError("'name' is required")
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)
