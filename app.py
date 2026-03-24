import requests

# 🔹 CONFIGURAÇÕES (vamos preencher depois)
PIPEFY_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3NzQzOTYyMTgsImp0aSI6ImFjOWE3OGNlLTk4NjUtNDY4MC04MWE2LWY2ODc1NGQ3NmNlMiIsInN1YiI6MzA2NzU2NDE5LCJ1c2VyIjp7ImlkIjozMDY3NTY0MTksImVtYWlsIjoiYW5hLm5hc2NpbWVudG9AZWRpZmlxdWVqci5jb20ifSwidXNlcl90eXBlIjoiYXV0aGVudGljYXRlZCJ9.2VY-"
PIPE_ID = "306967557"

def criar_card(nome, email, resposta):
    url = "https://api.pipefy.com/graphql"

    query = f'''
    mutation {{
      createCard(input: {{
        pipe_id: {PIPE_ID},
        fields_attributes: [
          {{field_id: "nome", field_value: "{nome}"}},
          {{field_id: "email", field_value: "{email}"}},
          {{field_id: "resposta", field_value: "{resposta}"}}
        ]
      }}) {{
        card {{
          id
        }}
      }}
    }}
    '''

    headers = {{
        "Authorization": f"Bearer {{PIPEFY_TOKEN}}",
        "Content-Type": "application/json"
    }}

    requests.post(url, json={{"query": query}}, headers=headers)


# 🔹 TESTE
criar_card("Teste automático", "teste@email.com", "Funcionou 🚀")
# teste
