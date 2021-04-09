from django import template
from django.utils.timezone import now

register = template.Library()


def convert(seconds):
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60
    days = int(seconds // seconds_in_day)
    hours = int((seconds - (days * seconds_in_day)) // seconds_in_hour)
    minutes = int((seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute)
    seconds = int(seconds - (days * seconds_in_day) - (hours * seconds_in_hour) - (minutes * seconds_in_minute))
    if days > 1:
        return '{} days {}:{}:{}'.format(days, hours, minutes, seconds)
    elif days == 1:
        return '1 day {}:{}:{}'.format(hours, minutes, seconds)
    else:
        return '{}:{}:{}'.format(hours, minutes, seconds)


@register.simple_tag(name='remain_time')
def remain_time(time):
    rem_time = time - now()
    rem_seconds = rem_time.total_seconds()
    if rem_seconds > 0:
        return convert(rem_seconds)
    if rem_seconds == 0:
        return 'Alarming'
    return 'Passed'
