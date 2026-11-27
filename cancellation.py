
from data import bookings, tour_slots
from input_utils import get_integer


def cancel_booking():
    if len(bookings) == 0:
        print("No bookings available to cancel.")
        return

    booking_id = get_integer("Enter Booking ID to cancel: ")

    selected_booking = None

    for booking in bookings:
        if booking["id"] == booking_id:
            selected_booking = booking
            break

    if selected_booking is None:
        print("Booking not found.")
        return

    for slot in tour_slots:
        if slot["id"] == selected_booking["slot_id"]:
            slot["booked"] -= selected_booking["group_size"]
            break

    bookings.remove(selected_booking)

    print("Booking cancelled successfully!")
