import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(headless=True):
    """
    Inicializa y configura la instancia de Selenium WebDriver para Chrome.
    """
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    return driver

def save_screenshot(driver, name="screenshot"):
    """
    Guarda una captura de pantalla en la carpeta reports/ para documentación o evidencia.
    """
    reports_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    filepath = os.path.join(reports_dir, f"{name}.png")
    driver.save_screenshot(filepath)
    return filepath
