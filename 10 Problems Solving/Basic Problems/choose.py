import random

class Chooser:
    """
    A class to randomly select numbers from a list without repetition.
    """
    def __init__(self, numbers):
        self.numbers = numbers
        self.choosen = []
    
    def choose(self, count):
        """
        Randomly select 'count' numbers from the list without repetition.
        
        Args:
            count (int): Number of items to select
            
        Returns:
            list: List of selected numbers
        """
        while len(self.choosen) < count:
            number = random.choice(self.numbers)
            # TODO: Implement the logic to using remove and append
            # self.numbers.remove(number)
            # self.numbers.append(number)
            if number not in self.choosen:
                self.choosen.append(number)
        return self.choosen
    
    
    def reset(self):
        """
        Reset the selected numbers list.
        """
        self.choosen = []
    
    def __str__(self):
        """
        Return a string representation of the selected numbers.
        """
        return str(self.choosen)
    
    def __repr__(self):
        """
        Return a string representation of the Chooser object.
        """
        return f"Chooser({self.numbers})"

if __name__ == "__main__":
    chooser = Chooser([1, 2, 3, 4, 5])
    print(chooser.choose(3))
    print(chooser)
    print(repr(chooser))
    chooser.reset()
    print(chooser.choose(2))
    print(chooser)
    print(repr(chooser))

