class Plant:


    def __init__(self, name: str, age: int, height: float) -> None:

        self.name = name
        self.age = age
        self.height = height

    def __str__(self) -> str:

        return f"{self.name}, возраст {self.age} лет, высота {self.height} м."

    def __repr__(self) -> str:
       
        return f"Plant(name={self.name}, age={self.age}, height={self.height})"

    def grow(self, growth: float) -> None:
       
        self.height += growth
        print(f"{self.name} выросло на {growth} м. Теперь его высота {self.height} м.")

    def get_age(self) -> int:
       
        return self.age


class Flower(Plant):
  

    def __init__(self, name: str, age: int, height: float, color: str, is_blooming: bool = False) -> None:
       
        super().__init__(name, age, height)
        self.color = color
        self.is_blooming = is_blooming

    def __str__(self) -> str:
        
        blooming_status = "цветет" if self.is_blooming else "не цветет"
        return f"{self.name} ({self.color}), возраст {self.age} лет, высота {self.height} м., {blooming_status}."

    def __repr__(self) -> str:
       
        return f"Flower(name={self.name}, age={self.age}, height={self.height}, color={self.color}, is_blooming={self.is_blooming})"

    def bloom(self) -> None:
        
        if not self.is_blooming:
            self.is_blooming = True
            print(f"{self.name} начал цвести!")
        else:
            print(f"{self.name} уже цветет.")

    def wither(self) -> None:
       
        if self.is_blooming:
            self.is_blooming = False
            print(f"{self.name} завял.")
        else:
            print(f"{self.name} уже не цветет.")

    def grow(self, growth: float) -> None:
        
        super().grow(growth)
        if self.height > 0.5 and not self.is_blooming:
            self.bloom()