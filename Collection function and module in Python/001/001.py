fav_items = ["3 Idiots ", 30, 4.5, True]
print("Original list:", fav_items)

fav_items[0] = "Singham"
fav_items[1] = fav_items[1] + 1
print("Updated list:", fav_items)

del fav_items[2]
print("List after removing data usage:", fav_items)

weekend_plan = ["Watch a movie", "Go for a run", 2, "Clean the house", "Call a friend"]
print("\nOriginal weekend_plan:", weekend_plan)

removed_item = weekend_plan.pop()
print("Removed item:", removed_item)
print("Updated weekend_plan:", weekend_plan)
