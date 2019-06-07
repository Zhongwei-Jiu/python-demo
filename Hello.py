ab = {
    'Yang': 'zhongwei_jiu@qq.com',
    'Wang': 'wangbaozhi@bit.edu.cn',
    'Li': 'lishuai@bit.edu.cn',
    'Xue': 'jinqin@qq.com'
}
print("Yang's address is", ab['Yang'])
del ab['Wang']
print('\nThere are {} contacts in the adress-book\n'.format(len(ab)))

ab['Chen']='chen@bit.edu.cn'

if 'Chen' in ab:
    print("\n Chen's address is",ab['Chen'])
print(ab)
