#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    n, hp = map(int, input().split())
    swing_damage_list = []
    throw_damege_list = []
    
    for _ in range(n):
        swing_damage, throw_damage = map(int, input().split())
        swing_damage_list.append(swing_damage)
        throw_damege_list.append(throw_damage)

    swing_damage_list.sort()
    throw_damege_list.sort()
    max_swing_damage = swing_damage_list[-1]

    will_throw_list = [damage for damage in throw_damege_list if damage > max_swing_damage]
   
    all_damage = sum(will_throw_list) 
    answer = len(will_throw_list)
    if all_damage > hp:
       for damage in will_throw_list:
            if all_damage - damage < hp:
                print(answer)
                return
            all_damage -= damage
            answer -= 1
    else:
        print(answer + ((hp - all_damage) + (max_swing_damage - 1)) // max_swing_damage)

if __name__=="__main__":
    solve()
