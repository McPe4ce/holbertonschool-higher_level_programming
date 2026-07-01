#!/usr/bin/env python3
import os


attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

def generate_invitations(template, attendees):
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    if not isinstance(template, str) or not all(isinstance(index, dict) for index in attendees):
        print("Error: Invalid data type")
        return
    
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for i, attendee in enumerate(attendees, start=1):
        invitation = template
        for key in placeholders:
            value = attendee.get(key)
            placeholder = "{" + key + "}"
            invitation = invitation.replace(placeholder, str(value) if value is not None else 'N/A')

        file = f"output_{i}.txt"
        try:
            if os.path.exists(file):
                print(f"{file} already exists")
                continue
            with open(file, "w") as f:
                f.write(invitation)
        except Exception as err:
            print("Couldnt write to the file")