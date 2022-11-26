x = float(input('x->'))

y = float(input('y->'))

z = float(input('z->'))

print('#>--------------<#')
print('#> vodafone 1.5 <#')
print('#> lifecell 2.0 <#')
print('#> kyivstar 3.4 <#')
print('#>--------------<#')


action= input ('operator->')

if action == 'vodafone':

    print (f'({x} * 3600 + {y} * 60 + {z}) * 1,5')