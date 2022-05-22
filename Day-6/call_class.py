class Product:
	def __init__(self):
		print("Instance Created")
	def __call__(self, a, b):
		print(a * b)
ans = Product()
ans(10, 20)
# Product(30, 60)
ans(30, 60)
