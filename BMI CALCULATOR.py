'''BMI = Mass of person /  (height)2 
where,
Mass in Kilograms(Kg), height in meters(m)'''


# importing modules
from pywebio.input import *
from pywebio.output import *


# classify and compute BMI
class calculation:

	# defining method
	def BMIcalculator(self, Height, Mass):
		
		# compute BMI
		BMI = (Mass)/(Height*Height)
		
		# classify
		for t1, t2 in [(16, 'severely underweight'), 
					(18.5, 'underweight'), 
					(25, 'normal'), (30, 'overweight'), 
					(35, 'moderately obese'), 
					(float('inf'), 'severely obese')]:
		
			if BMI <= t1:
				put_text('Your BMI is', BMI, 'and the person is :', t2)
				break


# height input
Height = input("Please enter height in meters(m)", type=FLOAT)

# Mass input
Mass = input("Please enter Mass/Weight in Kilograms(Kg)", type=FLOAT)

obj = calculation()
obj.BMIcalculator(Height, Mass)


