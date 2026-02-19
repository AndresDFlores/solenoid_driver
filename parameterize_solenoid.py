sol_v = 12 #V
sol_a = 1.7 #A

r_ds = 0.022 #ohms
r_th = 62 #C/W


r_ds_margin = .042 #r_ds*1.2
P_lost = r_ds_margin*(sol_a**2)
T_total = (r_th*P_lost)+25

print(f'r: {r_ds_margin}')
print(f'P: {P_lost}')
print(f'T: {T_total}')
