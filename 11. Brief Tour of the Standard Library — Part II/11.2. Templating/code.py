from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(repr(t))
t.substitute(village='Nottingham', cause='the ditch fund')

print(repr(t))