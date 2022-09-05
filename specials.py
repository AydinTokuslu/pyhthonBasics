class Movie():
    def __init__(self,title,director, duration) -> None:
        self.title=title
        self.director=director
        self.duration=duration
        print('movie objesi oluşturuldu')

    def __str__(self) -> str:
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

m=Movie('film adı', 'yönetmen adı', 120)

print(m)
print(len(m))