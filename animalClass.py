import sys

class Animal:

	def print(self):
		print("This is my favorite animal!")
		print(f"Number of eyes = {self.neyes}")
		print(f"Length of arms = {self.larms}")
		print(f"Length of legs = {self.llegs}")
		print(f"Tail = {self.tail}")
		print(f"Furry = {self.furry}")

	def __init__(self, neyes=int, larms=float, llegs=float, tail=bool, furry=bool):
		self.neyes = neyes
		self.larms = larms
		self.llegs = llegs
		self.tail = tail
		self.furry = furry


def main():
	neyes = int(2)
	larms = float(10)
	llegs = float(15)
	tail = bool(True)
	furry = bool(True)


	myAnimal = Animal(neyes = neyes, larms = larms, llegs = llegs, tail = tail, furry = furry)
	myAnimal.print()


if __name__ == "__main__":
	main()