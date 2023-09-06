# write your code here
person = {
    "name":"bader",
    "age": 14,
    'hobbies':['programming','video games','hunting']

}
print(person['name'])
print(person['age'])

person['age']= 19
person["country"]= "kuwait"
print(person)
print(len(person))

person['hobbies'].append('movies')
def check_hobbies(user):
    if len(user['hobbies']) > 3:
        print('wow you are amazing')

check_hobbies(person)