import random

name = input("Enter your hero name:")
player_hp = 100
score = 0
inventory = []
rooms = ["North", "South", "East", "West"]

enemy_room = random.choice(rooms)
enemy_alive = True

print("\n===================================")
print("WELCOME TO THE DUNGEON", name)
print("===================================")

while player_hp > 0:
    print("\n========== MENU ==========")
    print("1. Move")
    print("2. Check HP")
    print("3. Check Inventory")
    print("4. Show Score")

    menu = input("Enter your choice: ")
    if menu == "1":
        print("\nRooms:", rooms)
        room = input("Choose a room: ").title()
        if room not in rooms:
            print("Invalid room!")
            continue

        print("\nYou entered the", room, "room.")
        if room == enemy_room and enemy_alive:
            print("\nA Goblin appears!")
            enemy_hp = 50
            while enemy_hp > 0 and player_hp > 0:
                print("\nYour HP:", player_hp)
                print("Goblin HP:", enemy_hp)

                print("\n1. Attack")
                print("2. Use Potion")
                print("3. Run")

                action = input("Choose: ")
                if action == "1":
                    damage = random.randint(10,20)
                    enemy_hp -= damage
                    print("You attacked for", damage)

                    if enemy_hp <= 0:
                        print("Goblin defeated!")
                        score += 50
                        inventory.append("Potion")
                        enemy_alive = False
                        print("You found a Potion!")
                        break

                    goblin_attack = random.randint(5,12)
                    player_hp -= goblin_attack
                    print("Goblin attacks for", goblin_attack)

                elif action == "2":
                    if "Potion" in inventory:
                        inventory.remove("Potion")
                        player_hp += 30
                        if player_hp > 100:
                            player_hp = 100

                        print("Potion used!")
                        print("HP =", player_hp)

                    else:
                        print("No Potion available.")

                elif action == "3":
                    print("\nYou escaped from the Goblin!")
                    break

                else:
                    print("Invalid choice.")

        else:

            print("The room is empty.")

    elif menu == "2":
        print("Current HP:", player_hp)
    elif menu == "3":
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            print("Inventory:", inventory)
    elif menu == "4":
        print("Current Score:", score)
    else:
        print("Invalid choice.")

    if enemy_alive == False:
        print("\nA Dragon appears as the Final Boss!")
        dragon_hp = 100

        while dragon_hp > 0 and player_hp > 0:
            print("\nYour HP:", player_hp)
            print("Dragon HP:", dragon_hp)

            print("\n1. Attack")
            print("2. Use Potion")
            print("3. Run")

            choice = input("Choose: ")
            if choice == "1":
                damage = random.randint(15,25)
                dragon_hp -= damage
                print("You dealt", damage, "damage.")
                if dragon_hp <= 0:
                    print("\nYou defeated the Dragon!")
                    score += 100
                    print("Final Score:", score)
                    print("YOU WIN!")
                    exit()

                dragon_attack = random.randint(10,20)
                player_hp -= dragon_attack
                print("Dragon attacks for", dragon_attack)

            elif choice == "2":
                if "Potion" in inventory:
                    inventory.remove("Potion")
                    player_hp += 30
                    if player_hp > 100:
                        player_hp = 100
                    print("Potion used.")

                else:
                    print("No Potion!")

            elif choice == "3":
                print("You cannot run from the Dragon!")
            else:
                print("Invalid choice.")

print("\nGAME OVER!")
print("Final Score:", score)