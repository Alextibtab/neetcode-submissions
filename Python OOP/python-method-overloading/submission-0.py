class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, a: str, b: str = None) -> str:
        if b:
            return a+b
        return a.upper()



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
