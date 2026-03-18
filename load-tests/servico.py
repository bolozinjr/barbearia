from locust import HttpUser, task, between

class ServicoUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def testar_servicos(self):
        headers = {'Authorization': 'Bearer SEU_TOKEN_AQUI'}

        payload = {
            "nome": "Corte Moderno",
            "descricao": "Corte de cabelo com degradê",
            "preco": 35.00,
            "duracaoMinutos": 45,
            "ativo": True
        }

        with self.client.post("/servicos", json=payload, headers=headers, catch_response=True) as response:
            if response.status_code == 201 or response.status_code == 200:
                response.success()
            else:
                response.failure(f"Falha no POST: {response.status_code}")

        self.client.get("/servicos", headers=headers)