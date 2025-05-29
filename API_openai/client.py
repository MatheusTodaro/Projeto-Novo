import openai

openai.api_key = "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"

def get_filme_sinopse(titulo, ano, diretor):
    prompt = f"Crie uma sinopse em apenas 200 caracteres para o filme '{titulo}' do ano {ano}, dirigido por {diretor}"

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content