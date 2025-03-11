import os
from PIL import Image
import pillow_heif


class ConverterModel:
    def __init__(self):
        pass

    def convert_heic_to_jpg(self, input_folder, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        files = [f for f in os.listdir(input_folder) if f.lower().endswith('.heic')]
        total_files = len(files)

        if total_files == 0:
            print("Nessun file HEIC trovato nella cartella.")
            return False  # Per notificare alla view che non ci sono file

        for index, filename in enumerate(files, 1):
            heic_path = os.path.join(input_folder, filename)
            jpg_filename = os.path.splitext(filename)[0] + '.jpg'
            jpg_path = os.path.join(output_folder, jpg_filename)

            try:
                # Leggi il file HEIC
                heif_file = pillow_heif.read_heif(heic_path)

                # Crea immagine PIL
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw"
                )

                # Salva in JPG
                image.save(jpg_path, "JPEG")

                print(f"[{index}/{total_files}] Convertito: {filename}")
            except Exception as e:
                print(f"Errore nella conversione di {filename}: {e}")

        return True
