'''
Modules used: json to parse json file as list of dictionary
'''
import json

def getValues(patient_data):
	'''
	This functions iterate through each value recursively untill it reaches a value which is not a dictionary
	'''
	values = []
	for value in patient_data.values():
		if type(value) == dict:
			values = values + getValues(value)
		else:
			values.append(value)
	return values

# Read the json file and store the file as a list of objects
with open('patient_data.txt.') as f:
    patient_data = json.load(f)

# Open a file to write
with open('table.csv','w') as f:
	f.write('ID,Age,Gender,City,Height,Weight,Hip,Waist,Pulse,Temperature,SpO2,bp_s,bp_d,Fasting Glucose,Random Glucose,HbA1c,Risk Score,Risk Level,\n')

	for patient in patient_data:
		
		lab_data = getValues(patient)

		# Filter the output and write only parameter values
		required_data = lab_data[:5] + lab_data[6:21:2] + lab_data[21:]
		f.write(','.join(map(str,required_data)) + ',\n')
