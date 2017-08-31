import a
import b

print a.is_leap_year(2000)
print a.is_leap_year(2001)
print a.is_leap_year(2004)
print a.is_leap_year(2100)
    
c , i = b.newton_method(1.0, 0.0001)
print("解:",c ,"(計算回数:", i+1, ")")