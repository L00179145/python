#############################
List Comprehensions
###########################

# Create a list of temperature in kelvin
temperature_in_kelvin = [200, 400, 273, 1200, 220, 700, 520, 900, 1000, 1130]
print('***************************************************************************')

# Convert Kelvin to Celsius
temperature_in_celsius = [round(temp - 273.15, 2) for temp in temperature_in_kelvin]
print('Temperature in Celsius:', temperature_in_celsius)
print('***************************************************************************')

# Convert Kelvin to Fahrenheit
temperature_in_fahrenheit = [round((temp - 273.15) * 9/5 + 32, 2) for temp in temperature_in_kelvin]
print('Temperature in Fahrenheit:', temperature_in_fahrenheit)

print('***************************************************************************')
