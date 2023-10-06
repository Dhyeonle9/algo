blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

blood_dict = {
    'A': 0,
    'O': 0, 
    'B': 0, 
    'AB': 0
}
for i in blood_type:
    if i in blood_dict.keys():
        blood_dict[i] += 1
    else:
        continue
print(blood_dict)

#강사님 솔루션
blood_dict = {
    'A': 0,
    'O': 0, 
    'B': 0, 
    'AB': 0
}

for blood in blood_type:
    blood_dict[blood] += 1
print(blood_dict)

######################################
location_list = ['서울', '부산', '부산', '서울', '대전', '광주', '제주']

location_dict = {}

for location in location_list:
    if location in location_dict.keys():
        location_dict[location] += 1
    else:
        location_dict[location] = 1
print(location_dict)