import openai
import os

# Configura tu clave de API de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')  # Asegúrate de definir esta variable de entorno

def refinar_resumen(resumen, indicaciones_openai):
    try:
        # Llama a la API de OpenAI para refinar el resumen
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Usa el modelo de chat adecuado
            messages=[
                {"role": "system", "content": "Eres un asistente de redacción que mejora textos."},
                {"role": "user", "content": f"{indicaciones_openai}\n\nTexto original:\n{resumen}\n\nTexto refinado:"}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Extrae y devuelve el texto refinado
        return response.choices[0].message['content'].strip()

    except Exception as e:
        raise ValueError(f"Error al refinar el resumen: {e}")
