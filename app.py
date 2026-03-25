import requests

PIPEFY_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3NzQ0MDkwMjksImp0aSI6IjdmNjdkMTI2LTYxYWMtNGQ1Zi04M2Y1LTcxOWNkZGI1NGU2OCIsInN1YiI6MzA2NzU2NDE5LCJ1c2VyIjp7ImlkIjozMDY3NTY0MTksImVtYWlsIjoiYW5hLm5hc2NpbWVudG9AZWRpZmlxdWVqci5jb20ifSwidXNlcl90eXBlIjoiYXV0aGVudGljYXRlZCJ9.2rfii5au0v12Pj6Kb2YkuNOzw2RiMR_qMOLkKT9zTsBSGspf7fDCuY1AsaFfy7gF74Xlt0f-OwXu9UMofQL19A"
PIPE_ID = "306967557"

url = "https://api.pipefy.com/graphql"

query = f"""
mutation {{
  createCard(input: {{
    pipe_id: {PIPE_ID},
    title: "Teste automático"
  }}) {{
    card {{
      id
      title
    }}
  }}
}}
"""

headers = {{
    "Authorization": f"Bearer {{PIPEFY_TOKEN}}",
    "Content-Type": "application/json"
}}

response = requests.post(url, json={{"query": query}}, headers=headers)

print(response.text)
