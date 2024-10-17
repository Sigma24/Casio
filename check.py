import re


def validate_and_format_input(input_sequence):
    # Regex pattern to match valid DMS formats
    pattern = r'^(\d+)(°(\d+)°(\d+)?°?)?$'
    match = re.match(pattern, input_sequence)

    if not match:
        return "Syntax Error"

    # Extracting the matched degree, minute, and second values
    degrees = match.group(1)  # Mandatory degrees
    minutes = match.group(3)  # Optional minutes (if provided)
    seconds = match.group(4)  # Optional seconds (if provided)

    degrees = int(degrees)
    minutes = int(minutes) if minutes else 0
    seconds = int(seconds) if seconds else 0

    # Return the DMS input string with zero placeholders where needed
    return f"{degrees}°{minutes}'{seconds}\""


def dms_to_decimal(degrees, minutes=0, seconds=0):

    return degrees + (minutes / 60) + (seconds / 3600)


def process_input(input_sequence):
    formatted_input = validate_and_format_input(input_sequence)
    if formatted_input == "Syntax Error":
        return "Syntax Error"

    dms_match = re.match(r'(\d+)°(\d+)' + "'" + r'(\d+)"', formatted_input)
    degrees = int(dms_match.group(1))
    minutes = int(dms_match.group(2))
    seconds = int(dms_match.group(3))

    decimal_value =round( dms_to_decimal(degrees, minutes, seconds),8)


    return    formatted_input  , decimal_value


# Example usage
if __name__ == "__main__":
  input_sequence = "23°32°21°"
  formatted_input, decimal_value = process_input(input_sequence)
  print("Formatted Input:", formatted_input)
  print("Decimal Value:", decimal_value)
