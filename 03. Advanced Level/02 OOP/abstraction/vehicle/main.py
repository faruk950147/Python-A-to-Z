class Car:
    def __init__(self, name, color):
        # ===========================
        # Attributes (state of the car)
        # ===========================
        self.name = name            # Car name
        self.color = color          # Car color
        self.speed = 0              # Current speed
        self.acceleration = False   # Is accelerating?
        self.braking = False        # Is braking?
        self.start = False          # Is engine started?
        self.stop = False           # Is engine stopped?
        self.gear = 0               # Current gear

    # ===========================
    # Public Methods (Interface)
    # ===========================
    def start(self):
        """Start the car"""
        self._ignite_engine()       # Call hidden implementation
        print(f"{self.name} started.")

    def stop(self):
        """Stop the car"""
        self._stop_engine()         # Call hidden implementation
        print(f"{self.name} stopped.")

    def accelerate(self):
        """Accelerate the car"""
        self._accelerate()          # Call hidden implementation
        print(f"{self.name} accelerated.")

    def brake(self):
        """Brake the car"""
        self._brake()               # Call hidden implementation
        print(f"{self.name} braked.")

    def change_gear(self, gear):
        """Change the gear of the car"""
        self._change_gear(gear)     # Call hidden implementation
        print(f"{self.name} changed gear to {gear}.")

    # ===========================
    # Hidden Implementation (Abstraction)
    # ===========================
    def _ignite_engine(self):
        """Hidden method to ignite the engine"""
        print("Engine ignited!")

    def _stop_engine(self):
        """Hidden method to stop the engine"""
        print("Engine stopped!")

    def _accelerate(self):
        """Hidden method to increase speed"""
        print("Accelerating!")

    def _brake(self):
        """Hidden method to slow down or stop"""
        print("Braking!")

    def _change_gear(self, gear):
        """Hidden method to change gear internally"""
        print(f"Gear changed to {gear}!")
