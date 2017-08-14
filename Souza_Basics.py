# # #
# Souza_Basics
#  
#  Contains useful classes and methods
#  
#  Author: Vinicius "vdsbt33" de Souza
# # #
# Example:
#  
#  stdout = String()
#  author = Person('Vinicius de Souza', 'Male', Date(1998, 7, 22), 'Brazilian')
#  print(author.toString())
#  
#  Output:
#  
#  Name: Vinicius de Souza 
#  Gender: Male 
#  Birth Date: 1998 July 22nd 
#  Nationality:: Brazilian
# # #


# C #
# Color
# Contains the values to change string color
# * Values can be used without instancing this class
class String:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'
	

	# F #
	# Msg_Error
	# Exibits the given string with an error header
	def Msg_Error(self, string, header):
		print(String.RED + ('=' * 3) + header + ('=' * 3) + String.END + '\n%s\n' % (string) +  String.RED + ('=' * 3) + header + ('=' * 3) + String.END)

	# F #
	# PrintC
	# Prints a string with the given color
	def PrintC(self, string, colorValue):
		print(colorValue + string + self.END)

	# F #
	# CString
	# Returns a colored string
	def CString(self, string, colorName):
		colorDict = {
			'P':	self.PURPLE,
			'C':	self.CYAN,
			'D':	self.DARKCYAN,
			'B':  self.BLUE,
			'G':	self.GREEN,
			'Y':	self.YELLOW,
			'R':	self.RED,
			'_B':	self.BOLD,
			'_U':	self.UNDERLINE,
			'_E':	self.END
		}

		if colorName.upper() in colorDict:
			return "%s%s%s" % (colorDict[colorName.upper()], string, self.END)

		return "%s%s" % (self.END, string)

# C #
# Date
# A class to objects in date format
class Date:
	
	# M #
	# __init__(self, year, month, day)
	# Constructor of the class
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day
	
	# M #
	# toShortString(self)
	# Returns a string with the short date
	def toShortString(self):
		if self.month <= 9:
			shortMonth = "%s%s" % ('0', self.month)
		else:
			shortMonth = self.month
		return "%s/%s/%s" % (self.year, shortMonth, self.day)
	
	# M #
	# toFullString(self)
	# Returns a string with the full date
	def toFullString(self):
		monthDict = {
			1:  'January',
			2:  'February',
			3:  'March',
			4:  'April',
			5:  'May',
			6:  'June',
			7:  'July',
			8:  'August',
			9:  'September',
			10: 'October',
			11: 'November',
			12: 'December'
		}
		
		if (self.day == 1 or self.day == 11 or self.day == 21 or self.day == 31):
			daySufix = 'st'
		elif (self.day == 2 or self.day == 12 or self.day == 22):
			daySufix = 'nd'
		elif (self.day == 3 or self.day == 13 or self.day == 23):
			daySufix = 'rd'
		else:
			daySufix = 'th'
		return "%s %s %s%s" % (self.year, monthDict[self.month], self.day, daySufix)

# C #
# Person
# Saves data from a person
class Person:
	
	# M #
	# __init__(self, name, gender, birthDate, nationality)
	# Constructor of the class
	def __init__(self, name, gender, birthDate, nationality):
		self.name = name
		self.gender = gender
		self.birthDate = birthDate
		self.nationality = nationality

	# F #
	# toString(self)
	# Returns the data of the Person as a colored String
	def toString(self):
		stdout = String()
		return "\n%s %s \n%s %s \n%s %s \n%s: %s" % (stdout.CString('Name:', 'b'), self.name, stdout.CString('Gender:', 'b'), self.gender, stdout.CString('Birth Date:', 'b'), self.birthDate.toFullString(), stdout.CString('Nationality:', 'b'), self.nationality)


# End
