import openai

openai.api_key = ""

def get_filme_sinopse(titulo, ano, diretor):
    prompt = f"Crie uma sinopse em apenas 200 caracteres para o filme '{titulo}' do ano {ano}, dirigido por {diretor}"

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content