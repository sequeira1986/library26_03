class Author_nov:
    def __init__(self, IdAuthori, name, Bio):
        self.IdAuthori = IdAuthori
        self.name = name
        self.Bio = Bio

    def __str__(self):
        return f"ID: {self.IdAuthori}, Name: {self.name}, Bio: {self.Bio}"


