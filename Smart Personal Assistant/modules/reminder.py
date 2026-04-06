from plyer import notification

def show_notification(message):
    notification.notify(
        title="🔔 Reminder",
        message=message,
        timeout=5
    )