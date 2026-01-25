def solution(bandage, health, attacks):
    max_hp = health
    current_hp = health
    bandage_time, heal_per_sec, bonus_heal = bandage

    attack_map = {a[0]: a[1] for a in attacks}
    last_attack_time = attacks[-1][0]
    
    continuous_success = 0
    
    for t in range(1, last_attack_time + 1):
        if t in attack_map:
            current_hp -= attack_map[t]
            continuous_success = 0
            
            if current_hp <= 0: return -1
        else:
            continuous_success += 1
            current_hp += heal_per_sec
            
            if continuous_success == bandage_time:
                current_hp += bonus_heal
                continuous_success = 0
            
            if current_hp > max_hp:
                current_hp = max_hp
                
    return current_hp