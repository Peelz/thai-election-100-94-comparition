# 94%
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

# 100%
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

comparations = {
    "ปชร": ["7,939,937", "8,433,137"],
    "พท": ["7,423,361", "7,920,630" ],
    "อนม": ["5,871,137", "6,265,950" ],
    "ปชป": ["3,704,654", "3,947,726" ],
    "ภทพ": ["3,512,446", "3,732,883" ],
}

people = 0
for party in comparations:
    print (party, end=": ")
    old, new = comparations[party]
    diff = int(new.replace(",", ""))-int(old.replace(",", ""))
    print (old, new, diff)
    people += diff
print ("total voted different: ", people, "from 35532647" )

