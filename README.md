# Proyecto de Pre-Entrega: Automatización QA con Selenium y Pytest

## Propósito del Proyecto
Este proyecto implementa la suite de pruebas automatizadas para la aplicación web [SauceDemo](https://www.saucedemo.com). Se destacan las pruebas end-to-end de autenticación de usuario, validación de catálogo e interacción con el carrito de compras.

## Tecnologías Utilizadas
- **Python 3.12+**
- **Selenium WebDriver 4+**
- **Pytest**
- **pytest-html**
- **Git & GitHub**

## Estructura del Repositorio
```
pre-entrega-automation-testing-[nombre-apellido]/
│
├── tests/
│   └── test_saucedemo.py     # Casos de prueba automatizados (Login, Catálogo, Carrito)
├── utils/
│   └── helpers.py            # Utilidades y configuración de WebDriver
├── reports/                  # Reportes HTML generados y capturas de pantalla
├── pytest.ini                # Configuración global de Pytest
├── requirements.txt          # Dependencias de Python
└── README.md                 # Documentación del proyecto
```

## Instalación y Configuración
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/pre-entrega-automation-testing-[nombre-apellido].git
   cd pre-entrega-automation-testing-[nombre-apellido]
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/macOS
   # venv\Scripts\activate   # En Windows
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución de las Pruebas
Para ejecutar la suite de pruebas y generar el reporte HTML ejecute:

```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

Una vez ejecutado, podrá consultar los resultados detallados abriendo `reports/reporte.html`.
