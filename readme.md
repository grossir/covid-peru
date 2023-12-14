# Covin Perú

Datos obtenidos por solicitudes de acceso a la información sobre el Covid en Perú.

Se puede encontrar análisis y gráficos realizados sobre estos datos en mi Substack

A continuación, algunos comentarios sobre los datos

## Datos obtenidos por transparencia

### merma_factor_perdida

Documentos sobre el factor perdida de las vacunas Covid obtenidos por Transparencia

### esavis

Informes internos producidos por el CDC sobre **ESAVI**: Eventos Supuestamente Atribuidos a la Vacunación o Inmunización. Para obtener algunos tuve que apelar al Tribunal de Transparencia

### esavi_subregistro

Datos de países latinoamericanos y la OPS para comparar tasas de reporte de ESAVI por vacuna Covid.

### olas

Informes internos producidos por el CDC sobre la posibilidad de nuevas olas Covid, y sus recomendaciones. Contienen muchas sobre estimaciones y recomendaciones alarmistas

### documentos

Documentos de interés varios 

### documentos_judiciales

Sentencias relacionadas a temas de la vacunación forzada

### aduanas

Sobre los precios filtrados de las vacunas


## Datos abiertos

### Sinadef


Muertos por todas las causas

**Sin ID_PERSONA**

[Home](https://www.datosabiertos.gob.pe/dataset/informaci%C3%B3n-de-fallecidos-del-sistema-nacional-de-defunciones-ministerio-de-salud/resource)
[Datos](https://cloud.minsa.gob.pe/s/nqF2irNbFomCLaa/download)


**Con ID_PERSONA**

[Home](https://www.datosabiertos.gob.pe/dataset/sinadef-certificado-defunciones)



----------------

### Sinadef (solo muertos por Covid)

Muertos por Covid, con todos los campos del registro Sinadef

[Home](https://www.datosabiertos.gob.pe/dataset/fallecidos-por-covid-19-ministerio-de-salud-minsa/resource/4b7636f3-5f0c-4404-8526)
[Datos](https://cloud.minsa.gob.pe/s/xJ2LQ3QyRW38Pe5/download)


----------------

### Fallecidos, hospitalizados, vacunados (CDC)

Todos en esta archivo fallecieron.

Es el archivo fuente del gráfico borrado por el Minsa

Sin embargo, contiene menos muertos que la cuenta general en SINADEF (alrededor de 100k / 200k)

Los muertos del último periodo (mitad del 2022 en adelante) si están completos, comparable con el SINADEF (me di cuenta al hacer el estudio del engaño de Cevallos). Esto le da aún más fuerza al gráfico

[Home](https://www.datosabiertos.gob.pe/dataset/fallecidos-hospitalizados-y-vacunados-por-covid-19)
[Datos](https://cloud.minsa.gob.pe/s/8EsmTzyiqmaySxk/download)

#### Problemas de consistencia

Algunos que tienen flag_vacuna == 0 tiene fecha de dosis 1 o dosis 2 o dosis 3. ¿Serán vacunados en el extranjero? ¿Error de tipeo? Hay que controlar eso al momento de hacer las cuentas


----------------

### Vacunación

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

----------------

### Pruebas Positivas

Tiene ID_PERSONA

[Home](https://www.datosabiertos.gob.pe/dataset/casos-positivos-por-covid-19-ministerio-de-salud-minsa)
[Datos](https://cloud.minsa.gob.pe/s/AC2adyLkHCKjmfm/download)

-----------------

### Pruebas PCR - INS

Puede servir para complementar el analisis de "pandemia de los vacunados", parece que contiene datos de *todas* las pruebas, no solo positivas.

[Home](https://www.datosabiertos.gob.pe/dataset/dataset-de-pruebas-moleculares-del-instituto-nacional-de-salud-para-covid-19-ins)
