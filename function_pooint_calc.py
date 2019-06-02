#2. Design a program for a Function Point calculator.
#software enginnering practicatl assignment-1
#SE CS2036
#rofi
#25-05-19

import os
import sys
from tabulate import tabulate

#showing weighting factors for UFP calculation as a table.
data = [("Inputs, EI", 3, 4, 5), ("Outputs, EO", 4, 5, 7), ("Inquiries, EQ", 3, 4, 6), ("Logical files, ILF", 7, 10, 15), ("Interface, EIF", 5, 7, 10)]
headers = ["Functional Units(weighting factors)", "Low", "Medium", "High"]
#print(tabulate(data, headers, "grid"))





#function to take no of user inputs
def input_EI():
    data = []


    #low weighting factors.
    low = int(input("How many low EI ?"))
    #data.append(low)
    wf_low = 3*low
    data.append(wf_low)

    #mid weighting factors.
    mid = int(input("How many mid EI ?"))
    #data.append(mid)
    wf_mid = 4*mid
    data.append(wf_mid)

    #mid weighting factors.
    high = int(input("How many high EI ?"))
    #data.append(high)
    wf_high = 6*high
    data.append(wf_high)

    #total weighting factor for a functional unit
    total = 0
    for i in data:
        total += i

    data.append(total)


    data = ["EI"] + data

    #converting data to tuple form
    #tmp = data
    tmp = tuple(i for i in data)
    #tpl = tuple(tmp)

    #print(tmp)
    return tmp

#function to take output
def input_EO():
    data = []


    #low weighting factors.
    low = int(input("How many low EO ?"))
    #data.append(low)
    wf_low = 4*low
    data.append(wf_low)

    #mid weighting factors.
    mid = int(input("How many mid EO ?"))
    #data.append(mid)
    wf_mid = 5*mid
    data.append(wf_mid)

    #mid weighting factors.
    high = int(input("How many high EO ?"))
    #data.append(high)
    wf_high = 7*high
    data.append(wf_high)

    #total weighting factor for a functional unit
    total = 0
    for i in data:
        total += i

    data.append(total)


    data = ["EO"] + data

    #converting data to tuple form
    #tmp = data
    tmp = tuple(i for i in data)
    #tpl = tuple(tmp)

    #print(tmp)
    return tmp

#function to take output
def input_EQ():
    data = []


    #low weighting factors.
    low = int(input("How many low EQ ?"))
    #data.append(low)
    wf_low = 3*low
    data.append(wf_low)

    #mid weighting factors.
    mid = int(input("How many mid EQ ?"))
    #data.append(mid)
    wf_mid = 4*mid
    data.append(wf_mid)

    #mid weighting factors.
    high = int(input("How many high EQ ?"))
    #data.append(high)
    wf_high = 6*high
    data.append(wf_high)

    #total weighting factor for a functional unit
    total = 0
    for i in data:
        total += i

    data.append(total)


    data = ["EQ"] + data

    #converting data to tuple form
    #tmp = data
    tmp = tuple(i for i in data)
    #tpl = tuple(tmp)

    #print(tmp)
    return tmp





#function to take output
def input_ILF():
    data = []


    #low weighting factors.
    low = int(input("How many low ILF ?"))
    #data.append(low)
    wf_low = 7*low
    data.append(wf_low)

    #mid weighting factors.
    mid = int(input("How many mid ILF ?"))
    #data.append(mid)
    wf_mid = 10*mid
    data.append(wf_mid)

    #mid weighting factors.
    high = int(input("How many high ILF ?"))
    #data.append(high)
    wf_high = 15*high
    data.append(wf_high)

    #total weighting factor for a functional unit
    total = 0
    for i in data:
        total += i

    data.append(total)


    data = ["ILF"] + data

    #converting data to tuple form
    tmp = data
    tmp = tuple(i for i in data)
    #tpl = tuple(tmp)

    #print(tmp)
    return tmp


#function to take output
def input_EIF():
    data = []


    #low weighting factors.
    low = int(input("How many low EIF ?"))
    #data.append(low)
    wf_low = 5*low
    data.append(wf_low)

    #mid weighting factors.
    mid = int(input("How many mid EIF ?"))
    #data.append(mid)
    wf_mid = 7*mid
    data.append(wf_mid)

    #mid weighting factors.
    high = int(input("How many high EIF ?"))
    #data.append(high)
    wf_high = 10*high
    data.append(wf_high)

    #total weighting factor for a functional unit
    total = 0
    for i in data:
        total += i

    data.append(total)


    data = ["EIF"] + data

    #converting data to tuple form
    #tmp = data
    tmp = tuple(i for i in data)
    #tpl = tuple(tmp)

    #print(tmp)
    return tmp


#driver code.

#headers for result table.
resultHeaders = ["Functional unit", "low", "mid", "high", "total"]
EI = input_EI()
EO = input_EO()
EQ = input_EQ()
ILF = input_ILF()
EIF = input_EIF()

UFP = EI[-1] + EO[-1] + EQ[-1] + ILF[-1] + EIF[-1]

#print(EIF[-1])
last_row = ("Unadjusted Function Point, UFP", "", "", "", UFP)

#UFP table generation
resultData = []

resultData.append(EI)
resultData.append(EO)
resultData.append(EQ)
resultData.append(ILF)
resultData.append(EIF)
resultData.append(last_row)

tmp = []
tmpH = ["Calculation Of Unadjusted Function Point, UFP"]
print(tabulate(tmp, tmpH, "grid"))
print(tabulate(resultData, resultHeaders, "grid"))


tmpH = ["Calculation Of Technical Complexity Factor, TCF"]
tmp = []
print(tabulate(tmp, tmpH, "grid"))

tcfH = ["Formula", "TCF Calculated"]
tcf = float(0.65 + 42*0.01)
tcfData = [("0.65+0.01*DI", tcf)]
print(tabulate(tcfData, tcfH, "grid"))

tmpH = [("Calculation Of Function Point, FP")]
tmp = []
print(tabulate(tmp, tmpH, "grid"))

fpH = ["Formula", "UFP", "TCF", "FP Calculated"]
fp = float(UFP*tcf)
fpData = [("FP = UFP*TCF", UFP, tcf, fp)]
print(tabulate(fpData, fpH, "grid"))
