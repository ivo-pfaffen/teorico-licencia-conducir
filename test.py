import csv
import random
import argparse
import sys

def cargar_preguntas(csv_path):
    preguntas = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            if fila['question'] and fila['correct_answer']:
                preguntas.append(fila)
    return preguntas

def mostrar_pregunta(pregunta, n):
    print(f"\nPregunta {n}: {pregunta['question']}")
    opciones = {'a': pregunta['option_a'], 'b': pregunta['option_b'],
                'c': pregunta.get('option_c', ''), 'd': pregunta.get('option_d', '')}
    for k, v in opciones.items():
        if v:
            print(f"  {k}) {v}")
    return opciones

def main():
    parser = argparse.ArgumentParser(description="Test interactivo de preguntas.")
    parser.add_argument('-n', '--num', type=int, default=20, help="Cantidad de preguntas a presentar.")
    parser.add_argument('--csv', type=str, default='preguntas.csv', help="Ruta al archivo CSV con las preguntas.")
    args = parser.parse_args()

    preguntas = cargar_preguntas(args.csv)

    if args.num > len(preguntas):
        print(f"Solo hay {len(preguntas)} preguntas disponibles en el CSV.")
        sys.exit(1)

    seleccionadas = random.sample(preguntas, k=args.num)
    puntaje = 0

    for i, pregunta in enumerate(seleccionadas, start=1):
        opciones = mostrar_pregunta(pregunta, i)
        respuesta = input("Tu respuesta: ").strip().lower()
        while respuesta not in opciones or not opciones[respuesta]:
            print("Opción inválida.")
            respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == pregunta['correct_answer'].lower():
            puntaje += 1
            print("✔ Correcto!")
        else:
            print(f"✘ Incorrecto. Respuesta correcta: {pregunta['correct_answer']}")

    print(f"\nPuntaje final: {puntaje}/{args.num}")

if __name__ == "__main__":
    main()
