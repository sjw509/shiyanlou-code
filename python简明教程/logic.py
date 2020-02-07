print(5 and 4) #首先判断5，肯定为true，那么最终结果取决于and后面的布尔值，4的布尔值为true，整个表达式为true，返回4
print(0 and 4 )# 判断0 为false ，最终结果取决于and 前面的布尔值，表达式为false，返回0
print (False or 3 or 0) # 0为false，3为true，or只要有一个为true，整个表达式为true，返回3
print (2 > 1 and not 3> 5 or 4) # 2>1 结果为true ; true and not 3 = false； false 》5 = false；false or 4 =true 
