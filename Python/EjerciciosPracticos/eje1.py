# a) Diferencia en procentaje entre el curso actual y :

# El más rápido de los cursos :

curso_actual = 1.5
cusro_rapido = 2.5

diferencia =  cusro_rapido - curso_actual

porcentaje_1 = (diferencia * 100) // cusro_rapido


print("---------------------------")

print(f'La diferencia de duración entre el curso más rápido y el actual es del: {int(porcentaje_1)} porciento')

#  El más lento de otros cursos 

curso_lento = 7

diferencia_curso_lento =  curso_lento - curso_actual

porcentaje_2 = (diferencia_curso_lento * 100) // curso_lento

print(f'La diferencia entre el curso más lento y el curso actual es del : {int(porcentaje_2)} poricento')

# Promedio de los cursos

promedio_cursos = 4 

diferencia_promedio = promedio_cursos - curso_actual

porcentaje_3 = (diferencia_promedio * 100) // promedio_cursos

print(f'la diferencia entre el promedio de los cursos y el curso actual es del: {int(porcentaje_3)} porciento')


# b) Porcentaje de material inservible que se reduce en :
# El promedio de los cursos :

crudo_promedio = 5

material_inservible_promedio = crudo_promedio - promedio_cursos

porcentaje_4 = (material_inservible_promedio * 100) // crudo_promedio

print("---------------------------")

print(f'El porcentaje de material inservible es del : {int(porcentaje_4)} poricento , en el promedio de los cursos')
# El curso actual :


crudo_curso_actual = 3.5

material_inservible = crudo_curso_actual - curso_actual

porcentaje_5 = (material_inservible*100)// crudo_curso_actual



print(f'El porcentaje de material inservible es del : {int(porcentaje_5)} porciento , en el promedio de los cursos')

 
# c ) Ver 10 horas de este curso a cuanto equivaldra en otros cursos , al reves ?

# Equivalencia con el curso rápido :


equivalencia_cursos_promedio = (10 * promedio_cursos) // curso_actual

print("---------------------------")

print(f' La duración de otros cursos es de {float(equivalencia_cursos_promedio)} horas si equivale a 10 horas del curso de dalto')

equivalencia_curso_actual = curso_actual *100 // promedio_cursos / 10

print(equivalencia_curso_actual)