import datetime

unix_datetime = datetime.datetime.utcfromtimestamp(0)
unix_datetime_format_string = unix_datetime.strftime('%B, %d, %Y')

now_utc_datetime = datetime.datetime.now(datetime.timezone.utc)
now_utc_timestamp = now_utc_datetime.timestamp()
unix_datetime_format_string = now_utc_datetime.strftime('%B %d %Y')

print(f"Seconds {unix_datetime_format_string}: {now_utc_timestamp} or \
{now_utc_timestamp:.2e} in scientific notation")

print(unix_datetime_format_string)
