# LIST PART (SLICE)

# name[m:n] returns elements with indices m...(n-1)
# name[:n] returns elements with indices 0...(n-1)
# name[m:] returns elements with indices m...end
# -1 = last, -2 = second last, -3 = third last
# therefore name[-3:] returns -3,-2,-1

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

# name[m:n:h] where h is step
print(players[::2])
#! step can be negative, -1, for example
#! then new list will be reversed

# slice can be used in a FOR loop
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
