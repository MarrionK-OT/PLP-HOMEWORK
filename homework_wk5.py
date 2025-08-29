# Week 5 Python OOP Homework
# Student: [Your Name]
# Assignment 1: Design Your Own Class
# Assignment 2: Polymorphism Challenge

print("Week 5 Python OOP Homework")
print("=" * 40)

# =============================================================================
# Assignment 1: Custom Class Design - Smartphone Theme
# =============================================================================

class Smartphone:
    """A Smartphone class demonstrating basic OOP concepts"""
    
    def __init__(self, brand, model, storage_gb, battery_percent=100):
        # Constructor to initialize each phone with unique values
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_percent = battery_percent
        self.is_on = False
        self.apps_installed = []
    
    # Methods that define smartphone behavior
    def turn_on(self):
        if self.battery_percent > 0:
            self.is_on = True
            return f"{self.brand} {self.model} is now ON"
        else:
            return "Cannot turn on - battery dead!"
    
    def turn_off(self):
        self.is_on = False
        return f"{self.brand} {self.model} is now OFF"
    
    def install_app(self, app_name):
        if len(self.apps_installed) < 10:  # Storage limit
            self.apps_installed.append(app_name)
            return f"Installed {app_name} successfully!"
        else:
            return "Not enough storage space!"
    
    def use_phone(self, minutes):
        battery_drain = minutes * 2  # 2% per minute
        self.battery_percent = max(0, self.battery_percent - battery_drain)
        return f"Used phone for {minutes} minutes. Battery: {self.battery_percent}%"
    
    def charge(self):
        self.battery_percent = 100
        return f"{self.brand} {self.model} fully charged!"
    
    def get_info(self):
        status = "ON" if self.is_on else "OFF"
        return f"{self.brand} {self.model} ({self.storage_gb}GB) - Battery: {self.battery_percent}% - Status: {status}"


class GamingPhone(Smartphone):
    """Gaming smartphone with enhanced features - demonstrates inheritance"""
    
    def __init__(self, brand, model, storage_gb, gpu_name, refresh_rate=120):
        super().__init__(brand, model, storage_gb)  # Call parent constructor
        self.gpu_name = gpu_name
        self.refresh_rate = refresh_rate
        self.gaming_mode = False
    
    def enable_gaming_mode(self):
        if self.battery_percent > 20:
            self.gaming_mode = True
            return f"Gaming mode ON! {self.gpu_name} activated at {self.refresh_rate}Hz"
        else:
            return "Need more battery for gaming mode!"
    
    def play_game(self, game_name):
        if self.gaming_mode and self.is_on:
            self.battery_percent = max(0, self.battery_percent - 15)
            return f"Playing {game_name} with enhanced graphics! Battery: {self.battery_percent}%"
        else:
            return "Turn on gaming mode first!"


# =============================================================================
# Assignment 2: Polymorphism Challenge - Vehicle Movement
# =============================================================================

class Animal:
    """Base Animal class for polymorphism"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def move(self):
        """This method will be overridden by each animal type"""
        return f"{self.name} the {self.species} is moving"
    
    def make_sound(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def move(self):
        return f"🐕 {self.name} the {self.breed} is running and wagging tail!"
    
    def make_sound(self):
        return f"{self.name} barks: Woof woof!"


class Bird(Animal):
    def __init__(self, name, bird_type):
        super().__init__(name, "Bird")
        self.bird_type = bird_type
    
    def move(self):
        return f"🐦 {self.name} the {self.bird_type} is flying through the sky!"
    
    def make_sound(self):
        return f"{self.name} chirps: Tweet tweet!"


class Fish(Animal):
    def __init__(self, name, fish_type):
        super().__init__(name, "Fish")
        self.fish_type = fish_type
    
    def move(self):
        return f"🐟 {self.name} the {self.fish_type} is swimming underwater!"
    
    def make_sound(self):
        return f"{self.name} blows bubbles: Blub blub!"


class Snake(Animal):
    def __init__(self, name, snake_type):
        super().__init__(name, "Snake")
        self.snake_type = snake_type
    
    def move(self):
        return f"🐍 {self.name} the {self.snake_type} is slithering on the ground!"
    
    def make_sound(self):
        return f"{self.name} hisses: Ssssss!"


# =============================================================================
# TESTING AND DEMONSTRATION
# =============================================================================

def test_assignment_1():
    """Test the Smartphone classes"""
    print("\n📱 ASSIGNMENT 1: SMARTPHONE CLASS TEST")
    print("-" * 40)
    
    # Create smartphone objects with unique values
    phone1 = Smartphone("Apple", "iPhone 15", 128)
    phone2 = Smartphone("Samsung", "Galaxy S24", 256, 85)
    gaming_phone = GamingPhone("ASUS", "ROG Phone 7", 512, "Adreno 740", 165)
    
    phones = [phone1, phone2, gaming_phone]
    
    # Test basic functionality
    for phone in phones:
        print(f"\n{phone.get_info()}")
        print(f"  {phone.turn_on()}")
        print(f"  {phone.install_app('Instagram')}")
        print(f"  {phone.use_phone(5)}")
    
    # Test gaming phone specific features
    print(f"\n🎮 Gaming Phone Special Features:")
    print(f"  {gaming_phone.enable_gaming_mode()}")
    print(f"  {gaming_phone.play_game('Call of Duty Mobile')}")


def test_assignment_2():
    """Test the Animal polymorphism"""
    print("\n\n🐾 ASSIGNMENT 2: POLYMORPHISM CHALLENGE")
    print("-" * 40)
    
    # Create different animals
    animals = [
        Dog("Buddy", "Golden Retriever"),
        Bird("Charlie", "Parrot"),
        Fish("Nemo", "Clownfish"),
        Snake("Slither", "Python")
    ]
    
    # Polymorphism demo - same method name, different behavior
    print("\n🏃 How each animal moves (Polymorphism!):")
    for animal in animals:
        print(f"  {animal.move()}")
    
    print("\n🔊 How each animal sounds:")
    for animal in animals:
        print(f"  {animal.make_sound()}")


def main():
    """Main function to run all tests"""
    test_assignment_1()
    test_assignment_2()
    
    print("\n\n✅ HOMEWORK COMPLETED!")
    print("🎯 Concepts demonstrated:")
    print("  • Classes and Objects")
    print("  • Constructors (__init__)")
    print("  • Attributes and Methods") 
    print("  • Inheritance")
    print("  • Polymorphism")
    print("  • Method Overriding")


# Run the program
if __name__ == "__main__":
    main()