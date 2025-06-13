from locust import HttpUser, task, between
import random

sabores = [1, 2, 3]  # IDs de helados

class ClienteHeladeria(HttpUser):
    wait_time = between(1, 3)  # Espera entre peticiones

    @task(2)
    def ver_pagina_inicio(self):
        self.client.get("/")

    @task(3)
    def ordenar_helado(self):
        sabor_id = random.choice(sabores)
        self.client.post("/ordenar", data={"sabor": sabor_id})
