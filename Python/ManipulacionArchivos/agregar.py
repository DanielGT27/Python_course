with open('Python\\ManipulacionArchivos\\texto_delgt.txt','w',encoding='UTF-8') as archivo:
  
       archivo.writelines(f'Linea N#{i+1}\n' for i in range(5) )
       
       
       