import time

import qrcode

ran_first_time = False

def get_qr(inp):
    print("\n" + "=" * 30 + "\n")
    print(inp)
    print("\n" + "=" * 30)

    link = input()
    print("\n" + "=" * 30 + "\n")
    print("Making QR Code..")
    print("\n" + "=" * 30 + "\n")

    time.sleep(1)

    if link != "":
        ran_first_time = True
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )

        qr.add_data(link)
        qr.make(fit=True)

        # img = qr.make_image(fill_color="black", back_color="white")

        # img.save("Test_Qr.png")



        qr.print_ascii(invert=True)


        if ran_first_time == False:
            get_qr("Paste Link below to turn into a QR Code.")
        else:
            get_qr("Paste Link to make another QR Code.")
    else:
        print("Link is invalid!")



if ran_first_time == False:
    get_qr("Paste Link below to turn into a QR Code.")
else:
    get_qr("Paste Link to make another QR Code.")