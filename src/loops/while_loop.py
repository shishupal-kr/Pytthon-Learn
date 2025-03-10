# ---------------------------------------------
# 1. Normal while loop (Entry Controlled Loop)
# ---------------------------------------------

i = 1   # Initialize the variable
while i <= 5:    # Condition to check
    print(i)     # Print the value of i
    i += 1       # Increment the value of i by 1
# When i becomes 6, the loop will terminate automatically


# --------------------------------------------------
# 2. Infinite while loop (Runs forever until stopped)
# --------------------------------------------------
# WARNING: This loop will run forever if not stopped manually or with break.

count = 1
while True:   # This is an infinite loop
    print("Count:", count)
    count += 1
    if count > 5:    # Break the loop when count becomes 6
        break
# Without the break statement, the loop will never stop


# ---------------------------------------------------------
# 3. while loop with else block (Executes else when loop ends)
# ---------------------------------------------------------

x = 1
while x <= 3:
    print("Value of x:", x)
    x += 1
else:
    print("Loop Ended Normally")
# The else block will execute only when the loop ends normally (without break)


# ---------------------------------------------------------------
# 4. while loop with break (else block will NOT execute)
# ---------------------------------------------------------------
y = 1
while y <= 5:
    print("Y:", y)
    if y == 3:
        break  # Break the loop when y becomes 3
    y += 1
else:
    print("This line will not execute due to break")
# In this case, the else block did not execute due to break


# ---------------------------------------------------------------
# 5. while loop without body (Using pass)
# ---------------------------------------------------------------
z = 1
while z <= 3:
    pass  # This loop does nothing, it just passes
    z += 1
# Useful when you don't want the loop to do anything temporarily