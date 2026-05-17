import os
import logging

# Configure logging to display messages clearly
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    # 1. Check Input Types
    if not isinstance(template, str):
        logging.error(f"Invalid input type: template must be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        logging.error(f"Invalid input type: attendees must be a list of dictionaries.")
        return

    # 2. Handle Empty Inputs
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    # List of placeholders expected in the template
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # 3. Process Each Attendee
    for index, attendee in enumerate(attendees, start=1):
        personalized_invite = template

        for placeholder in placeholders:
            # Safely get the value; if it's missing or None, default to "N/A"
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"

            # Replace placeholder token {key} with the string value
            target_token = f"{{{placeholder}}}"
            personalized_invite = personalized_invite.replace(target_token, str(value))

        # 4. Generate Output Files
        filename = f"output_{index}.txt"

        try:
            # Check if the file already exists (as suggested by hints)
            if os.path.exists(filename):
                logging.warning(f"File {filename} already exists and will be overwritten.")

            with open(filename, 'w', encoding='utf-8') as output_file:
                output_file.write(personalized_invite)
            logging.info(f"Successfully generated {filename}")

        except IOError as e:
            logging.error(f"Failed to write to file {filename}: {e}")
