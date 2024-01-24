from time import sleep

def countdown(start):
    count = start
    while count > 0:
        print(f"{count} SECOND(S)!")
        count -= 1

countdown(10)
print("HAPPY NEW YEAR!")

# Countdown sleep
def countdown_with_sleep(n):
   for i in range(n, 0, -1):  # Corrected the range
       if i == 0:  # Corrected the condition
           print("HAPPY NEW YEAR!")
       else:
           print(f"{i} SECOND(S)!")
           sleep(1)

countdown_with_sleep(10)
