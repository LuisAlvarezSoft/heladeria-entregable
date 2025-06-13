from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import platform

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# DEste if es para que funcione en github, debido a que funciona con linux y toca indicarle unas bobadas y aja :(
if platform.system() == "Linux":
    service = Service("/snap/bin/chromium.chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
else:
    driver = webdriver.Chrome(options=options)

driver.get("http://localhost:5000")

select = Select(driver.find_element(By.ID, "sabor"))
select.select_by_visible_text("Fresa - $11")

driver.find_element(By.TAG_NAME, "button").click()

time.sleep(1)

pedidos = driver.find_elements(By.CLASS_NAME, "pedido")
assert any("Fresa" in p.text for p in pedidos), "No se encontró el pedido de Fresa"

print("Test completado sin errores.")

driver.quit()
