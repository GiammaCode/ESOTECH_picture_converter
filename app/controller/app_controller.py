from app.model.converter import ConverterModel


class AppController:
    def __init__(self, view):
        self.view = view
        self.model = ConverterModel()

    def start_conversion(self):
        input_folder = self.view.get_input_folder()
        output_folder = self.view.get_output_folder()

        if not input_folder or not output_folder:
            self.view.show_error("Seleziona entrambe le cartelle prima di procedere!")
            return

        success = self.model.convert_heic_to_jpg(input_folder, output_folder)

        if success:
            self.view.show_message("Conversione completata con successo!")
        else:
            self.view.show_error("Nessun file HEIC trovato nella cartella di origine.")
