from pyfcm import FCMNotification

registration_ids = [
    'dcW_xfMQeHUpDIhpUVHG19:APA91bHgtqnO_StUOadWzhMY17pqPR_SAv6VlyJQn16SOHxmCMJpsekIgJH96A0RSZ208tS8AawEKxvbZIZpnZtX5r1ObS50z1ZTHf7Vw2GlaHqtGwVp0EbTSiQjrD41E49PKk0nHrn6']
push_service = FCMNotification(
    "AAAAH6Bum4k:APA91bHvgeQKjdTk58PEJZu80LfyvwtWOOBNxRvUVxLZX84sCVpIBG-Tl2IU5GTlI96LcKj4AVAJ8Jrd-DSIjV2vFvCXd3vbZbUzhgMZPf-b3kE2fcms5B-4JKLSwjKB9yi6mYqow6J_")
data = {
    'title': f'Your appointment has been confirmed ',
    'body': f'Please arrive on time, on late arrival appointment will be cancelled'
}
result = push_service.notify_multiple_devices(
    registration_ids=registration_ids, message_title=data['title'], message_body=data['body'])
print(result)
