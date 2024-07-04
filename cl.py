
class Language:
    def __init__(self) -> None:
        self.name = "English"
        self.spoken = "English"
        self.official = True
        self.native = True
        self.language = "English"
        
my_lang = Language()
print(f"I know how to speak {my_lang.name}")