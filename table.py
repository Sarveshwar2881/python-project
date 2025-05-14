
# print("hi this my table ")

# i=1
# while i<=10:
#     j=1
#     while j<=10:
#         print(i*j ,end="\t")
#         j=j+1
#     print()
#     i=i+1
# Gap de de ke table.
# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print(i * j, end="\t")  
#         j = j + 1
#     print()  
#     i = i + 1

index = 0

print("Odd numbers:")
while index < len(numbers):
    if numbers[index] % 2 != 0:
        print(numbers[index])
    index += 1



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
index = 0
while index < len(my_list):
  number = my_list[index]
  if number % 2 == 0:
    print(f"{number} is even")
  else:
    print(f"{number} is odd")
  index += 1

  def calculate_ticket_price(age, day_of_week):
  """
  Calculates the ticket price based on age and day of the week.

  Args:
    age: The age of the person.
    day_of_week: The day of the week (e.g., "Monday", "Tuesday", "Wednesday").

  Returns:
    The ticket price in rupees.
  """

  if age < 18:
    ticket_price = 8
  else:
    ticket_price = 12

  if day_of_week == "Wednesday":
    ticket_price -= 2

  return ticket_price

# Example usage:
age = 17
day = "Monday"
price = calculate_ticket_price(age, day)
print(f"Ticket price for a {age} year old on {day}: {price} rupees")

age = 20
day = "Wednesday"
price = calculate_ticket_price(age, day)
print(f"Ticket price for a {age} year old on {day}: {price} rupees")