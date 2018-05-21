bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[2])
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[1].title() + "."
print(message)

names = ['Korea', 'America', 'Japan', 'England']
print(names[0])
print(names[1])
print(names[-1])

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles[0] = 'ducati'
print(motocycles)
motocycles.append('ducati')
print(motocycles)

motocycles = []

motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('ducati')

print(motocycles)

del motocycles[0]
print(motocycles)

popped_motocycle = motocycles.pop()
print(motocycles)
print(popped_motocycle)

motocycles = ['honda', 'yamaha', 'suzuki']
last_owned = motocycles.pop()
print("The last motocycles I owned was a " + last_owned.title() + ".")

motocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocycles)
too_expensive = 'ducati'
motocycles.remove(too_expensive)
print(motocycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
