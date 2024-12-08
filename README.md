

---

# Sistema de Alertas Globales Ambientalistas con Flask

## Descripción del Proyecto

Este es un sistema web desarrollado en **Python** utilizando el framework **Flask**, diseñado para proporcionar información sobre proyectos amigables con el medio ambiente y daños ambientales en nuestro planeta. 
El usuario puede seleccionar una región o país, y el sistema mostrará automáticamente los datos en una tabla, proporcionando una experiencia interactiva y fácil de usar. Toda la información se obtiene a través de APIs especializadas.

---

## APIs Utilizadas

- 🌍 **API para Obtener la Lista de Países**  
  [World Bank API](https://search.worldbank.org/api/v3/wds?format=json&fct=count_exact,lang_exact&rows=0)

- 🌍♻️ **API para Obtener la Lista de Proyectos Ambientales en Cada País**  
  [World Bank API](https://search.worldbank.org/api/v3/wds?format=json&q&fl=docdt,count,display_title,pdfurl)

- 🌋🌊🌍 **API para Obtener la Lista de Tsunamis, Erupciones Volcánicas, y Terremotos por Región o País**  
  [NOAA API](https://www.ngdc.noaa.gov/hazel/view/swagger)

---


## Tecnologías Utilizadas

- **Python**  
- **Flask**  
- **APIs REST**  
- **HTML/CSS** 

---



