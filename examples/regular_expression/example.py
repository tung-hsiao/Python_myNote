# -*- coding: utf-8 -*-

import re

# * 前一個字元或括號內字元出現 0次或多次
# + 前一個字元或括號內字元出現 1次或多次
# [] 括號內的任一字元
# \ 跳脫字元
# . 任何單一字元 (符號, 數字, 空格)
# ? 
# \d

print("----- re.search -----\n")
# re.search
# ============================
needle = "abc"
haystack = "abcdefg"
res = re.search(needle, haystack).group()
print(res)    # abc

needle = "bc"
haystack = "abcdefg"
res = re.search(needle, haystack).group()
print(res)    # bc


needle = "PSNR = \d* dB"
haystack = "PSNR = 40 dB"
res = re.search(needle, haystack).group()
print(res)    # PSNR = 40 dB

needle = "\d* dB"
haystack = "PSNR = 40 dB"
res = re.search(needle, haystack).group()
print(res)    # 40 dB

needle = "PSNR = [+-]\d* dB"
haystack = "PSNR = +40 dB"
res = re.search(needle, haystack).group()
print(res)    # PSNR = 40 dB

# .*
needle = "PSNR = [+-]\d* dB.*"
haystack = "PSNR = +40 dB. [Log] This part is the log we want and has no same pattern -#?,"
res = re.search(needle, haystack).group()
print(res)


print("\n----- re.search -----\n")
# re.findall
# ============================

# 括號、問號
needle = "PSNR = [+-]?\d* dB"
haystack = "PSNR = +40 dB.\nPSNR = -41 dB.\nPSNR = 42 dB."
res = re.findall(needle, haystack)
print(res[0])    # PSNR = +40 dB
print(res[1])    # PSNR = -41 dB
print(res[2])    # PSNR = 42 dB

needle = "PSNR = [+-]?\d* dB"
haystack = "PSNR = +40 dB. [Log] This part is the log we DON't need -#?,\nPSNR = -41 dB"
res = re.findall(needle, haystack)
print(res[0])    # PSNR = +40 dB
print(res[1])    # PSNR = -41 dB

# 文字、括號
haystack = "[Log] Step1, Step2, Step3, Step4, Step5"
needle = 'Step[1-3]'
res = re.findall(needle, haystack)
print(res)    # ['Step1', 'Step2', 'Step3']

# 跳脫字元
haystack = 'please print all the start: *******'
needle = '\*+'
res = re.findall(needle, haystack)
print(res[0])

# 條件式搜尋
haystack = "[Log] Step1, Step2, Step3, Step4, Step5, StepA, StepB"
needle = "Step[1-3]|\[Log\]"
res = re.findall(needle, haystack)
print(res)    # ['[Log]', 'Step1', 'Step2', 'Step3']

