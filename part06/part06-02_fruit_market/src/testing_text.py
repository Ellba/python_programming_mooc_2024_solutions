text = "this, is, nice, text"
print(text.split(',')) # list
print(text.replace(',', '')) # str
print(text.strip()) # str

text2 = 'Pancakes\n15\nmilk\neggs\nflour\nsugar\nsalt\nbutter\n\nMeatballs\n45\nmince\neggs\nbreadcrumbs\n\nTofu rolls\n30\ntofu\nrice\nwater\ncarrot\ncucumber\navocado\nwasabi\n\nCake pops\n60\nmilk\nbicarbonate\neggs\nsalt\nsugar\ncardamom\nbutter\n'
#print(text2.replace('', ' '))
print(text2.split('\n\n'))
new = []
for i in text2.split('\n\n'):
    new.append(i.split('\n'))
print(new)
# new_lst = new_str.split('  ')
# print(new_lst)
# for i in new_lst:
#     print(i)