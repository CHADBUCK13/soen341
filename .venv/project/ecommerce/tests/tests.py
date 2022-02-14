from django.test import TestCase

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"The {self.name} says \"{self.sound}\""

class test_animals(TestCase):        

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal("lion","roar")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
    
    # def test_animals_cant_speak(self):
    #     """Animals that cant speak are correctly identified"""
    #     lion = Animal("lion","")
    #     self.assertEqual(lion.speak(), 'The lion says "roar"')
