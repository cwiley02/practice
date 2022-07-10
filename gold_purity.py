# Code to test gold purity of 22K (> 91.7%) and 24K (>= 99.9%)

purity = float(input())
if purity >= 75.0 and purity < 83.3:
    print("18K")
if purity >= 83.3 and purity < 91.7:
    print("20K")
if purity >= 91.7 and purity < 99.9:
    print("22K")
if purity > 99.9:
    print("24K")