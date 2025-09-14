def bin(t):
    a=t[::-1]
    bin_str=a
    decimal_num = int(bin_str, 2)
    print("Decimal:", decimal_num)
t="00011001"
bin(t)


#here use python builtin int() to convert binary to decimal
#00011001 this will gget reversed and converted into decimal 
