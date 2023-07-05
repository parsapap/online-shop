from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'Your code is :{code}'
        }
        response = api.sms_send(params)
        print(response)

    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
