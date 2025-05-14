import numpy as np

def proportional_navigation(missile, target, nav_constant, dt):
    rel_pos = target.pos - missile.pos
    rel_vel = target.vel - missile.speed * np.array([np.cos(missile.heading), np.sin(missile.heading)])
    
    los_angle = np.arctan2(rel_pos[1], rel_pos[0])
    los_rate = (rel_vel[0] * rel_pos[1] - rel_vel[1] * rel_pos[0]) / np.linalg.norm(rel_pos)**2
    
    turn = nav_constant * los_rate
    turn = np.clip(turn, -missile.max_turn, missile.max_turn)
    
    missile.heading += turn * dt
    missile.pos += missile.speed * np.array([np.cos(missile.heading), np.sin(missile.heading)]) * dt
