from pyfcm import FCMNotification


# Create your views here.
# push_service = FCMNotification(api_key)

# registration_ids = 'd_ZMOQY3dcDv5zYonrdZW_:APA91bF-7bGLegQDquNhE9iehDVaIGyYhywz7HvIAZ8nCojfGM8UMqGndvzU1A0E827a3aRKCSinWaYogMOpFnE5NHXOf-ehFZhTKCwQGQIWhhAfxkki8FaRZYVBw_n67XluXMYJESI9'
# message_title = "Kausha"
# message_body = "appointment at 12pm 9619363353"
# # result = push_service.notify_multiple_devices(
# #     registration_ids=registration_ids, message_title=message_title, message_body=message_body)

# # result = push_service .notify_single_device(
# # registration_id=registration_ids, message_title=message_title, message_body=message_body)
# data_message = {
#     "title": 'Sample Title',
#     'body': 'Sample Body'

# }
# result = push_service.single_device_data_message(
#     registration_id=registration_ids, data_message=data_message)

# send notifications to almost multiple cliets
# send notifications to single device
# additions btns on the clients and admins tab.
# on clients book a appointment today and on admins and stff book appointment today.


class Notify:
    def __init__(self, registeration_ids):
        self.registration_ids = registeration_ids
        self.push_service = FCMNotification(
            "AAAAH6Bum4k:APA91bHvgeQKjdTk58PEJZu80LfyvwtWOOBNxRvUVxLZX84sCVpIBG-Tl2IU5GTlI96LcKj4AVAJ8Jrd-DSIjV2vFvCXd3vbZbUzhgMZPf-b3kE2fcms5B-4JKLSwjKB9yi6mYqow6J_")

    def send_cli_pkg(self, name, message,):
        pass

    def send_cli_reminders(self):
        pass

    def send_cli_confirmation(self, cli_name, cli_date, cli_time):
        data = {
            'title': f'Your appointment has been confirmed ',
            'body': f'We expect you on {cli_date} at {cli_time}. Please arrive on time, on late arrival appointment will be cancelled'
        }
        result = self.push_service.notify_multiple_devices(
            registration_ids=self.registration_ids, message_title=data['title'], message_body=data['body'])
        print(result)

    def send_admin_prompt(self, cli_name, cli_date, cli_services):
        data = {
            'title': f'New appointment : [{cli_name}] on [{cli_date}]',
            'body': f'Services : {cli_services}',
        }
        # result = self.push_service.multiple_devices_data_message(
        #     registration_ids=self.registeration_ids, data_message=data)
        # print(result)
        result = self.push_service.notify_multiple_devices(
            registration_ids=self.registration_ids, message_title=data['title'], message_body=data['body'])
        print(result)
