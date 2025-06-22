## Simulador de examen teórico de licencia de conducir
Sólo válido para la provincia de Córdoba

### Cómo lo hice?
Le pasé el PDF del manual del buen conductor (material de estudio oficial) a Gemini 2.5 pro y pedí que extraiga las preguntas junto a las respuestas correctas.
Luego generé un script de python que arma tests con cualquier cantidad de preguntas (por defecto 20, el número de pregutnas en el examen oficial).

### Para usar
1. Cloná el repo
2. Corré el script `python3 test.py --n 5` donde el parámetro `--n` define el número de preguntas
