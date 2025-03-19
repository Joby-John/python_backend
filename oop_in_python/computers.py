class Computer:

    monitor = "Dell"

    def __init__(self, processor, ram, storage):
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def config(self):
        print(f"Config is {self.processor, self.ram, self.storage}")
    
    def update(self):
        self.processor = input("Enter the processor: ")

    def compare(self, otherComputer):
        return self.processor == otherComputer.processor


computer1 = Computer("Intel i5", "16GB", "1TB")
computer2 = Computer("Ryzen 3", "32GB", "1TB")

computer1.update()

computer1.config()
computer2.config()

print(computer1.monitor)



print(computer1.compare(computer2))