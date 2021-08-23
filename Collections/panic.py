phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist = plist[1:8]
plist.pop(2)
plist.insert(2, plist.pop(3))
plist[4:6]=plist[:3:-1]
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
