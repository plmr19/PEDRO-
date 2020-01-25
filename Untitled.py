#!/usr/bin/env python
# coding: utf-8

# In[1]:


matemáticas de importación
 
print ( "=========================================" ) 
print ( "Calculo numérico de la regla del trapecio " ) 
imprimir ( " ======================================= == " )

n = int ( input ( "Número de segmentos =" )) 
a = float ( input ( "Límite inferior =" )) 
b = float ( input ( "Límite superior =" ))

print ( "----------------------------------------------- ----------------------------- " ) 
print ( " {0:> 10s} {1:> 20s} {2:> 20s} " . Format ( " n " ,  " integral " ,  " Et " )) 
print ( " ---------------------------- ------------------------------------------------ " )

vv = 5.7725887272

fa  =  (( a + 2 ) / a ) ** 2 
fb  =  (( b + 2 ) / b ) ** 2 
h  =  ( b - a ) / n

para  k  en  rango  ( n )  : 
    suma  =  fa 
    h  =  ( b - a ) / ( k + 1 ) 
    para  i  en  rango  ( 1 , k + 1 )  : 
        xi  =  a + i * h 
        fxi  =  (( xi + 2 ) / xi ) ** 2 
        sum  =  sum +2 * fxi
        
    sum  =  sum  +  fb 
    sum  =  h  *  sum / 2
    
    I  =  h  *  sum / 2 
    Et = abs (( vv - sum ) / vv ) * 100
    
    print ( " {0: 10d} {1: 20.9f} {2: 20.9f} " . format ( k + 1 ,  sum  ,  Et ))
    
print ( "=============================================== ======================= " ) 
print ( " El resultado es " ,  sum  ) 
print ( " El error verdadero es " ,  Et )


# In[7]:





# In[9]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




