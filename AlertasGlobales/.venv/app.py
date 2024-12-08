from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    countries = []
    documents = []

    # Hacer la solicitud para obtener los países solo una vez (esto debería estar en la primera carga)
    response = requests.get('https://search.worldbank.org/api/v3/wds?format=json&fct=count_exact,lang_exact&rows=0')
    if response.status_code == 200:
        data = response.json()
        count_exact = data.get('documents', {}).get('facets', {}).get('count_exact', {})

        for key, value in count_exact.items():
            country_name = value.get('name', 'Sin nombre')  # Ajusta la clave si es necesario
            if country_name:
                countries.append(country_name)

    if request.method == 'POST':
        # Obtener el país seleccionado
        selected_country = request.form.get('selectCountry')

        # Hacer la solicitud a la API con el término seleccionado (esto cambiará según el país seleccionado)
        api_url = f"https://search.worldbank.org/api/v3/wds?format=json&qterm={selected_country}&fl=docdt,count,display_title,pdfurl"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            documents = data.get('documents', {}).values()

    return render_template('environmental projects.html', countries=countries, documents=documents)


if __name__ == '__main__':
    app.run(debug=True)
