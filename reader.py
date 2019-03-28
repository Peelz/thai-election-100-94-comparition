import matplotlib.pyplot as plt
import numpy as np
tt = 0

old_total = 32706921 #32,706,921

# ประชารัฐ
# 7,939,937	
# พท
# 7,423,361
# อคม
# 5,871,137
# ปชป
# 3,704,654
# ภทพ
# 3,512,446	

# ประชารัฐ
# 8,433,137
# พท
# 7,920,630
# อนม
# 6,265,950
# ปชป
# 3,947,726
# ภทพ
# 3,732,883



with open('raw_data.txt', 'r') as f :
    data = f.read().split()
    for line in data:
        tt += int(line.replace(",",""))
        
display_data = {
    "new": tt,
    "old(94%): ": old_total,
    "div: ": (tt-old_total)
}
print(tt)
# l = [tt, old_total, tt-old_total]
# x = np.arange(3) 
# plt.bar(x, height=l)
# plt.ylabel('some numbers')
# plt.xticks(x, ["new",'old','dif'])
# plt.show()