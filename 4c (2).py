cm=('sand','cement','bricks','water')
cmat=input("Enter the constructino material:")
cm=cm+(cmat,)
print(cm)
print("length of the list:",len(cm))
print("maximum of the list:",max(cm))
print("minimum of the list:",min(cm))
print("indexing:",cm[3])
print("cement" in cm)
print("multiplication of list element:",cm*2)
