''' 파이썬 클래스는 타입을 만들어내는 도구입니다. int, float, str과 같이 여러분의 새로운 타입을 만들 수 있습니다.
'''

# 251
print('@251')
'''
파이썬에서 클래스는 개체를 만드는 템플릿입니다. 클래스는 속성과 메서드로 구성됩니다. 속성은 개체에 대한 데이터를 저장하는 데 사용되는 변수이고 메서드는 개체에 대한 작업을 수행하는 데 사용되는 함수입니다.

객체는 클래스에 의해 생성된 개체입니다. 객체는 클래스의 속성과 메서드를 가질 수 있습니다.

인스턴스는 클래스의 특정 객체입니다. 인스턴스는 클래스의 속성과 메서드를 가질 수 있습니다.

예를 들어 다음 코드는 Car라는 클래스를 만듭니다.

Python
class Car:
    make = "Honda"
    model = "Civic"
    color = "Red"

    def drive(self):
        print("The car is driving.")

    def stop(self):
        print("The car is stopping.")
코드를 사용할 때는 주의하시기 바랍니다. 자세히 알아보기
Car 클래스는 다음과 같은 속성과 메서드를 가집니다.

make: 자동차 제조업체의 이름
model: 자동차 모델의 이름
color: 자동차 색상
drive(): 자동차를 운전하는 메서드
stop(): 자동차를 멈추는 메서드
다음 코드는 Car 클래스의 인스턴스를 만듭니다.

Python
my_car = Car()
코드를 사용할 때는 주의하시기 바랍니다. 자세히 알아보기
my_car 객체는 Car 클래스의 속성과 메서드를 가질 수 있습니다. 예를 들어 다음 코드는 my_car 객체를 사용하여 자동차를 운전합니다.

Python
my_car.drive()
코드를 사용할 때는 주의하시기 바랍니다. 자세히 알아보기
다음 코드는 my_car 객체를 사용하여 자동차를 멈춥니다.

Python
my_car.stop()
'''

# 252
print('@252')
class Human:
	pass

# 253
print('@253')
kim = Human()

# 254
print('@254')
class Human:
	def __init__(self):
		print('hi')
kim = Human()

# 255, 256
print('@255, 256')
class Human:
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex
kim = Human('kim', 24, 'man')
print(kim.name)
print(kim.age)
print(kim.sex)

# 257
print('@257')
class Human:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex
		
	def who(self):
		print('name :',self.name,'age :',self.age,'sex :',self.sex)
		
kim = Human('kim',24,'man')
kim.who()

# 258
print('@258')
class Human:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex
		
	def who(self):
		print('name :',self.name,'age :',self.age,'sex :',self.sex)
	
	def setInfo(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex
kim = Human('Unknown', 'Unknown', 'Unknown')
kim.who()
kim.setInfo('kim', 26, 'man')
kim.who()

# 259
print('@259')
'''클래스 소멸자'''
class Human:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex
		
	def __del__(self):
		print('do not tell anyone about my death')
		
	def who(self):
		print('name :',self.name,'age :',self.age,'sex :',self.sex)
	
	def setInfo(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex
kim = Human('kim', 26, 'man')
kim.who()
del kim

# 260
print('@260')
'''다시보기'''
