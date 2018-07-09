#07 序列：计算生肖、星座
#1.序列的切片操作

#shengxiao = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
#print (shengxiao[0:6])
#公元1年是鸡年，可以调换生肖顺序
shengxiao = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = 2018
print (year,'是',shengxiao[year % 12],'年')
#2.序列的成员关系判断
print('猪' in shengxiao)#输出true
print('猪' not in shengxiao)#输出false
#3.序列连接
print(shengxiao[0] + shengxiao[3])
print('郝桐的生肖在里面===>' + shengxiao )
#4.序列重复
print(shengxiao * 4)

