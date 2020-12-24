# bounce.py
#
# Exercise 1.5
height = 100 # meters

for bounce_cnt in range(1,11):
    height = height * 0.6 # reduce height to 3/5 each bounce
    print(bounce_cnt, height)
