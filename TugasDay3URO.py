import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in input().split()]
connection = []
for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]
    connection.append([zone_1,zone_2])

base = -1 # owner base/my base
opponentBase = -1 # enemy base

def gerak(x):
    a = []
    for i in range(len(connection)):
        if x == connection[i][0]:
            a.append(connection[i][1])
        if x == connection[i][1]:
            a.append(connection[i][0])
    return a
            

# game loop
while True:
    my_platinum = int(input())  # your available Platinum
    d = [] # visible zone
    e = [] # pods
    f = [] # zone owner
    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]
        if visible:
            if owner_id == 0 and base == -1:
                base = z_id
            elif owner_id == 1 and opponentBase == -1:
                opponentBase = z_id
        if pods_p0 > 0:
            e.append([z_id,pods_p0])
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print(connection, file=sys.stderr)
    print(visible, file=sys.stderr)
    print(e, file=sys.stderr)
    print(gerak(e[0][0]), file=sys.stderr)
    for i in range(len(e)):
        m = e[i][1]
        n = e[i][0]
        o = random.choice(gerak(n))
        print(str(m) + " " + str(n) + " " + str(o), end=" ")
    # first line for movement commands, second line no longer used (see the protocol in the statement for details)

    print()
    print("WAIT")
