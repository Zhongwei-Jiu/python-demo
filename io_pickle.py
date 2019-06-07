import pickle
shoplistfile = 'shoplist.data'
shoplist = ['好apple','mango','carrot']
f=open(shoplistfile,'wb')
pickle.dump(shoplist,f)
f.close()

del shoplist
f=open(shoplistfile,'rb')
shoplist=pickle.load(f)
print(shoplist)


import io
f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"I好magine non-English language here")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text)
