from datetime import datetime


def convert_timestamp(timestamp: int, time_format: str = '%Y-%m-%dT%H:%M:%SZ') -> str:
    if timestamp > 9999999999:
        # Divide the timestamp by 1000 to get the number of seconds if it's in milliseconds
        timestamp_in_seconds = timestamp / 1000
    else:
        timestamp_in_seconds = timestamp
    
    # Use the datetime module to convert the Unix timestamp to a datetime object
    time = datetime.fromtimestamp(timestamp_in_seconds)
    # Format the datetime object in the desired time format
    return time.strftime(time_format)
