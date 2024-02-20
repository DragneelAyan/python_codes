class School:
    school = 'St. Lawrence'
    
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        
        
student1 = School('Debjit', '48')
student2 = School('Aritro', '2')

print(student1.name)
print(student2.name)
print(student1.school)

