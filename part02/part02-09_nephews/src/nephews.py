# Write your solution here
name = input("Please type in your name: ")
donald = ["Huey", "Dewey", "Louie"]
mickey = ["Morty", "Ferdie"]

if name in mickey:
    print("I think you might be one of Mickey Mouse's nephews.")
elif name in donald:
    print("I think you might be one of Donald Duck's nephews.")  
else: 
    print("You're not a nephew of any character I know of.")