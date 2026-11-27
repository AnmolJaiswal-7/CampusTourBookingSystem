
from data import visitors, tour_slots, bookings
from display import view_slots
from input_utils import get_integer


def register_visitor():
    print("\n--- Visitor Registration ---")

    name = input("Enter visitor name: ")
    email = input("Enter email: ")

    visitor = {
        "id": len(visitors) + 1,
        "name": name,
        "email": email
    }

    visitors.append(visitor)

    print("Visitor registered successfully!")
    print("Your Visitor ID is:", visitor["id"])


def book_tour():
    if len(visitors) == 0:
        print("Please register as a visitor first.")
        return

    visitor_id = get_integer("Enter your Visitor ID: ")

    visitor_found = False

    for visitor in visitors:
        if visitor["id"] == visitor_id:
            visitor_found = True
            break

    if not visitor_found:
        print("Visitor not found.")
        return

    view_slots()

    if len(tour_slots) == 0:
        return

    slot_id = get_integer("Enter Slot ID to book: ")

    selected_slot = None

    for slot in tour_slots:
        if slot["id"] == slot_id:
            selected_slot = slot
            break

    if selected_slot is None:
        print("Invalid Slot ID.")
        return

    available = selected_slot["capacity"] - selected_slot["booked"]

    if available <= 0:
        print("Sorry, this slot is full.")
        return

    group_size = get_integer("Enter number of people: ")

    if group_size <= 0:
        print("Group size must be greater than zero.")
        return

    if group_size > available:
        print("Not enough seats available.")
        return

    booking = {
        "id": len(bookings) + 1,
        "visitor_id": visitor_id,
        "slot_id": slot_id,
        "group_size": group_size
    }

    bookings.append(booking)

    selected_slot["booked"] += group_size

    print("Tour booked successfully!")
    print("Your Booking ID is:", booking["id"])
