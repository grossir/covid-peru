# Covin Perú

Análisis y gráficos sobre el Covin en Perú
Pueden encontrar la publicación y discusiones en mi [Twitter](https://twitter.com/gjrossir)

### Productos

[Gráfico borrado por el Minsa: Visualización de fallecidos por Covin según estado de vacunación](https://datawrapper.dwcdn.net/naPx1/)


### Datos

#### Sinadef


Muertos por todas las causas

**Sin ID_PERSONA**

[Home](https://www.datosabiertos.gob.pe/dataset/informaci%C3%B3n-de-fallecidos-del-sistema-nacional-de-defunciones-ministerio-de-salud/resource)
[Datos](https://cloud.minsa.gob.pe/s/nqF2irNbFomCLaa/download)


**Con ID_PERSONA**

[Home](https://www.datosabiertos.gob.pe/dataset/sinadef-certificado-defunciones)




#### Sinadef (solo muertos por Covid)

Muertos por Covid, con todos los campos del registro Sinadef

[Home](https://www.datosabiertos.gob.pe/dataset/fallecidos-por-covid-19-ministerio-de-salud-minsa/resource/4b7636f3-5f0c-4404-8526)
[Datos](https://cloud.minsa.gob.pe/s/xJ2LQ3QyRW38Pe5/download)


#### Fallecidos, hospitalizados, vacunados (CDC)

Todos en esta archivo fallecieron.

Es el archivo fuente del gráfico borrado por el Minsa

Sin embargo, contiene menos muertos que la cuenta general en SINADEF (alrededor de 100k / 200k)

Los muertos del último periodo (mitad del 2022 en adelante) si están completos, comparable con el SINADEF (me di cuenta al hacer el estudio del engaño de Cevallos). Esto le da aún más fuerza al gráfico

[Home](https://www.datosabiertos.gob.pe/dataset/fallecidos-hospitalizados-y-vacunados-por-covid-19)
[Datos](https://cloud.minsa.gob.pe/s/8EsmTzyiqmaySxk/download)


#### Vacunación

Posible de ligar con los otros archivos a través de ID_PERSONA

He encontrado 2 versiones

Demasiadas filas, dificil de cargar en memoria de la compu aunque tenga ~16GB de RAM. Lo ideal sería cargarlo a una BD y sacar los fragmentos que interesen
También, si solo interesa saber cuantas dosis tiene una persona, se puede proyectar el ID_PERSONA antes de cargar los datos usando:

```
awk -F, '{print $2}' vacunas_covid.csv > vacunas_proyeccion.csv
awk -F, '{print $1}' 2022_01_24_TB_VACUNACION_COVID19/TB_VACUNACION_COVID19.csv > vacunas_proyeccion.csv
```

54M regisros


[Home](https://www.datosabiertos.gob.pe/dataset/vacunaci%C3%B3n-contra-covid-19-ministerio-de-salud-minsa)
[Datos](https://cloud.minsa.gob.pe/s/To2QtqoNjKqobfw/download)

Nombre del archivo: vacunas_covid.7z

--------------

[Home](https://www.datosabiertos.gob.pe/dataset/vacunacion)
[Datos](https://cloud.minsa.gob.pe/s/oHF5JSLEk8KzpPW/download)

Nombre del archivo: TB_VACUNACION

Parece mas ligero que el otro, puras fechas e ints, ni siquiera tiene el nombre de la vacuna en strings

head -n 2
```
id_persona,id_vacunados_covid19,fecha_vacunacion,id_eess,id_centro_vacunacion,id_vacuna,id_grupo_riesgo,dosis,edad
28192674,20698369,17/09/2021,2495,102495,6,23,1,37
```

#### Pruebas Positivas

Tiene ID_PERSONA

[Home](https://www.datosabiertos.gob.pe/dataset/casos-positivos-por-covid-19-ministerio-de-salud-minsa)
[Datos](https://cloud.minsa.gob.pe/s/AC2adyLkHCKjmfm/download)

