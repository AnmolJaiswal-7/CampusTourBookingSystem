
from data import guides, tour_slots


def view_guides():
    if len(guides) == 0:
        print("No guides available.")
        return

    print("\n--- Available Guides ---")

    for guide in guides:
        print("Guide ID:", guide["id"])
        print("Guide Name:", guide["name"])
        print("----------------------")


def view_slots():
    if len(tour_slots) == 0:
        print("No tour slots available.")
        return

    print("\n--- Available Tour Slots ---")

    for slot in tour_slots:
        available = slot["capacity"] - slot["booked"]

        guide_name = "Unknown"

        for guide in guides:
            if guide["id"] == slot["guide_id"]:
                guide_name = guide["name"]

        print("\nSlot ID:", slot["id"])
        print("Date:", slot["date"])
        print("Time:", slot["time"])
        print("Guide:", guide_name)
        print("Total Capacity:", slot["capacity"])
        print("Available Seats:", available)
        print("----------------------")
