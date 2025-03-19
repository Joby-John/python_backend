class Computer:

    def __init__(self, processor, ram, storage):
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def config(self):
        print(f"{self.processor, self.ram, self.storage}")

computer1 = Computer("1TB", "16GB", "1TB")
computer2 = Computer("1TB", "32GB", "1TB")

computer1.config()
computer2.config()