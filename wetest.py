import itchat

itchat.auto_login()
# res = itchat.get_friends()
data = itchat.search_friends(remarkName='xzll')
# print(type(res))
# with open('user_list.js','w+') as f:
#     f.write(res)
# print(res)
print(data)