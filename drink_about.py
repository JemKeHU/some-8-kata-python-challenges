def people_with_age_drink(age):
    
    if age > 21:
        return "drink whisky"
    if age < 21 and age >= 18:
        return "drink beer"
    if age < 18 and age > 14:
        return "drink coke"
        
    return "drink toddy"

print(people_with_age_drink(13))
print(people_with_age_drink(17))
print(people_with_age_drink(18))
print(people_with_age_drink(20))
print(people_with_age_drink(30))