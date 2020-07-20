'''
Celsius:

Celsius is a unit of measurement for temperature. It is also known as centigrade. 
It is a SI derived unit used by most of the countries worldwide.
It is named after the Swedish astronomer Anders Celsius.
Fahrenheit:
Fahrenheit is also a temperature scale. It is named on Polish-born German physicist Daniel 
Gabriel Fahrenheit. It uses degree Fahrenheit as a unit for temperature.
Conversion formula:
T(℉) = T(℃) x 9/5 + 32
T(℉) = T(℃) x 1.8 + 32
'''
print("Python program to convert Celsius to Fahrenheit:")	
#Collect input from the user 
celsius = float(input("Enter temperature in Celsius:"))

#Calculate temperature in fahrenheit 
fahrenheit = (celsius*1.8) + 32
print("%0.1f Celsius is equal to %0.1f degree fahrenheit."%(celsius,fahrenheit)) 






























