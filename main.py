try:
   import qrcode

   qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=15,
      border=2,
   )
   qr.add_data('http://mongodb-learning.vercel./')
   qr.make(fit=True)

   img = qr.make_image(fill_color="black", back_color="white")
   img.save(input("dosya_adi: "))
except:
   print("Boş dosya adı girilemez")