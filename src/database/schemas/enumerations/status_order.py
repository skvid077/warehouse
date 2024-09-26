from enum import Enum


class StatusOrder(Enum):
    processed = 'processed'
    in_progress = 'in progress'
    sent = 'sent'
    delivered = 'delivered'
    accept = 'accept'
