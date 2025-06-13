from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("http://localhost:5000")

select = Select(driver.find_element(By.ID, "sabor"))
select.select_by_visible_text("Fresa - $11")

driver.find_element(By.TAG_NAME, "button").click()

time.sleep(1)

pedidos = driver.find_elements(By.CLASS_NAME, "pedido")
assert any("Fresa" in p.text for p in pedidos), "No se encontró el pedido de Fresa"

print("Test completado sin errores.")

driver.quit()
