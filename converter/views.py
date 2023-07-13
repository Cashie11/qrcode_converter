from django.shortcuts import render
import qrcode
from io import BytesIO
from django.core.files import File
import uuid
from .models import QRCode

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def generate_qr(request):
    if request.method == 'POST':
        data = request.POST.get('data')  # Assuming you have a form field with the name 'data'
        
        # Create a new QRCode instance and save the data
        qr_code = QRCode(data=data)
        qr_code.save()

        # Generate the QR code image
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(data)  # Use the user input as the data for the QR code
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image in memory
        qr_image = BytesIO()
        img.save(qr_image)
        qr_image.seek(0)

        # Generate a unique filename for the QR code image
        filename = f'qr_code_{uuid.uuid4().hex}.png'

        # Create a Django file from the saved QR code image
        qr_code.code.save(filename, File(qr_image))

        return render(request, 'qr.html', {'qr_code': qr_code})

    return render(request, 'generate.html')