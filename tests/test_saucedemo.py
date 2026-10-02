import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import get_driver, save_screenshot

class TestSauceDemo:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """
        Fixture que inicializa el navegador antes de cada prueba y lo cierra al finalizar.
        """
        self.driver = get_driver(headless=True)
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    @pytest.mark.smoke
    def test_login_exitoso(self):
        """
        Caso de Prueba 1: Automatización de Login.
        Navega a saucedemo.com, ingresa credenciales válidas y valida la redirección con esperas explícitas.
        """
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        
        # Localización de campos e ingreso de datos
        username_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_input.send_keys("standard_user")
        
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        
        # Validación mediante espera explícita
        self.wait.until(EC.url_contains("/inventory.html"))
        assert "/inventory.html" in driver.current_url, "Falló la redirección a la página de inventario."

    @pytest.mark.smoke
    def test_navegacion_y_catalogo(self):
        """
        Caso de Prueba 2: Navegación y Verificación del Catálogo.
        Valida título de la página, presencia de productos, extrae datos del primer ítem y verifica elementos de UI.
        """
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        
        # Login previo
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Validación del título
        title_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.title"))
        )
        assert title_element.text == "Products", f"El título esperado era 'Products', se obtuvo '{title_element.text}'."
        
        # Verificación de catálogo
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No se encontraron productos visibles en el catálogo."
        
        # Nombre y precio del primer artículo
        first_product_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        first_product_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text
        
        assert first_product_name != "", "El nombre del producto no debe estar vacío."
        assert first_product_price != "", "El precio del producto no debe estar vacío."
        
        # Verificación de elementos clave de la interfaz
        assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed(), "Menú hamburguesa no disponible."
        assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed(), "Filtro de productos no disponible."

    @pytest.mark.smoke
    def test_interaccion_carrito(self):
        """
        Caso de Prueba 3: Interacción con el Carrito.
        Añade un producto al carrito, verifica el contador badge, navega al carrito y valida la presencia del artículo.
        """
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        
        # Login previo
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Añadir primer producto al carrito
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//button[contains(@data-test, 'add-to-cart')])[1]"))
        )
        add_btn.click()
        
        # Espera explícita para confirmar badge numérico
        badge = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert badge.text == "1", f"Contador del carrito debería ser '1', se obtuvo '{badge.text}'."
        
        # Navegar al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.wait.until(EC.url_contains("/cart.html"))
        
        # Comprobar que el producto aparezca en el carrito
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 1, "El carrito debería listar 1 producto."
