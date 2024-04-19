#enumerate
list=['Python', 'Java', 'JavaScript']
newlist=[(idx, lang) for idx, lang in enumerate(list)] 
print(newlist)