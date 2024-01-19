import qrcode
from PIL import Image

def generate_qr_code(data, size_cm=1.5, output_file='qrcode.png', dpi=300):
    # Convertir la taille en pixels en fonction de la résolution DPI
    size_pixels = int(size_cm * dpi / 2.54)

    # Générer le code QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Redimensionner l'image en utilisant la résolution DPI
    img = img.resize((size_pixels, size_pixels), Image.ANTIALIAS)

    # Sauvegarder l'image
    img.save(output_file, dpi=(dpi, dpi))

if __name__ == "__main__":
    # Informations pour le code QR
    qr_data = """
    Nom : DIABY
    Prénoms : Abdoulaye
    Fonction : E-Commercial Partner
    Identifiant : 2024EC72@167
    Code exploitant : SPST04403 Z
    Validité de la carte : 17/01/2026
    Manager de la Région du PORO
    Département : Korhogo
    Commune : Korhogo
    Sous-préfecture : Korhogo
    Phone : 0747717830
    WhatsApp : 0747717830
    """

    # Générer le code QR avec les informations
    generate_qr_code(qr_data)
    print("Code QR généré avec succès.")
