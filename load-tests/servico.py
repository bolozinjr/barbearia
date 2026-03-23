from locust import HttpUser, task, between

class ServicoUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def testar_servicos(self):
        headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imo5Tmx5VnVkdzNVaEZaMml5X3o2WSJ9.eyJpc3MiOiJodHRwczovL2Rldi1tZ2JlMXNiOHo2Y3ZpNWh5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJMNzZ6UG9US3RORXpSVzY4clg0ZVJZRGxXMERRUGJjRkBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9hcGkuYmFyYmVhcmlhLmNvbSIsImlhdCI6MTc3NDI0MTgxNCwiZXhwIjoxNzc0MzI4MjE0LCJzY29wZSI6ImFkbWluIGZ1bmNpb25hcmlvIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwiYXpwIjoiTDc2elBvVEt0TkV6Ulc2OHJYNGVSWURsVzBEUVBiY0YiLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsImZ1bmNpb25hcmlvIl19.k611Ojss876B1NASvUlDbgfWV5dd7H__yi5CWl9VV8l96Cvv_k9nTsMo3C-NleNanUgEq7OrC_hIDPtOZak0yUTa0kLYamfGQLQOvT3vrX3rUaDqM6QIxz5o6pxRTNKAc9Pvt2U32StqmwF554CVTEoz_VVZrrUFZSWtEQmvFVaGhTuPCsVv0w2lRdojp7PllTNxqf0Tm_zkFmD614wHjCQhOJijvrXFfhTSjitgk7XhIuNJuevGO9JqDON3aHEvpqDeQFcWADj9yediXSTJm7yz-XBj9EbOTyT-YeOAT2BUcPEFLi_H_in_c3nz7Zbhu9gE6mX66LMs1qjVy_vIng'}

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