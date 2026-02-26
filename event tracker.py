entered_persons = set()
rejected_persons = set()

num_persons = 5

print("Event Tracker: Enter 5 persons\n")

for i in range(num_persons):
    name = input("Enter name of person " + str(i + 1) + ": ").strip()
    
    if name in entered_persons:
        print("Entry rejected! ", name, "has already entered.")
        rejected_persons.add(name)
    else:
        print("Entry accepted! Welcome", name)
        entered_persons.add(name)

print("\n--- Event Entry Summary ---")
print("Persons entered successfully (", len(entered_persons), "):", ', '.join(entered_persons))
print("Persons rejected (", len(rejected_persons), "):", ', '.join(rejected_persons))
print("Total persons who entered:", len(entered_persons))
print("Total persons rejected / duplicate entries:", len(rejected_persons))
print("Total persons not entered:", num_persons - len(entered_persons))
