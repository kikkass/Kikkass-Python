import json

'''
Defining/declaring the dictionaries to hold group data
'''
by_age_group = {'0-20':{'Low Risk':0, 'Moderate Risk':0, 'High Risk':0, 'Already Afflicted':0},
 '21-40':{'Low Risk':0, 'Moderate Risk':0, 'High Risk':0, 'Already Afflicted':0}, 
 '41-60':{'Low Risk':0, 'Moderate Risk':0, 'High Risk':0, 'Already Afflicted':0}, 
 '61-80':{'Low Risk':0, 'Moderate Risk':0, 'High Risk':0, 'Already Afflicted':0}, 
 '81-100':{'Low Risk':0, 'Moderate Risk':0, 'High Risk':0, 'Already Afflicted':0}}
by_city = {}
by_gender = {}

def write_to_file(dicts,file_name,category):
	'''
	This function writes to a file which is passed as an argument along with the dictionary and grouping name
	'''
	with open(file_name,'w') as f:
		f.write(category + ',Low Risk,Moderate Risk,High Risk,Afflicted\n')
		for key, values in dicts.items():
			row = [key]
			for value in values.values():
				row.append(value)
			f.write(','.join(map(str,row)) + '\n')

# Read the json data
with open('patient_data.txt.') as f:
    patient_data = json.load(f)

for patient in patient_data:
	'''
	Iterate through each patient to find the appropriate grouping
	'''
	city = patient['meta']['user']['city']
	gender = patient['meta']['user']['gender']
	age = patient['meta']['user']['age']
	risk_level = patient['data']['risk']['parameters']['diabetes_risk']['level']

	# For each new City create a group
	if city not in by_city:
		by_city[city] = {'Low Risk':0, 'Moderate Risk':0, 'High Risk':0, 'Already Afflicted':0}
	# If the group is already created increment the risk_levvel value in the current group
	by_city[city][risk_level] += 1

	# For each new gender create a group
	if gender not in by_gender:
		by_gender[gender] = {'Low Risk':0, 'Moderate Risk':0, 'High Risk':0, 'Already Afflicted':0}
	# If the group is already created increment the risk_levvel value in the current group
	by_gender[gender][risk_level] += 1

	# As age group is defined globally, check for age gropu to which the age of current patient belongs
	if age < 21:
		by_age_group['0-20'][risk_level] += 1
	elif age < 41:
		by_age_group['21-40'][risk_level] += 1
	elif age < 61:
		by_age_group['41-60'][risk_level] += 1
	elif age < 81:
		by_age_group['61-80'][risk_level] += 1
	else:
		by_age_group['81-100'][risk_level] += 1

# Write into output file
write_to_file(by_city,'by_city.csv','City')
write_to_file(by_gender,'by_gender.csv','Gender')
write_to_file(by_age_group,'by_age.csv','Age Group')
