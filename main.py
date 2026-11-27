
from data import guides, tour_slots
from display import view_guides, view_slots
from booking import register_visitor, book_tour
from cancellation import cancel_booking
from input_utils import get_integer


def add_guide():
    print("\n--- Add Guide ---")

    name = input("Enter guide name: ")

    guide = {
        "id": len(guides) + 1,
        "name": name
    }

    guides.append(guide)

    print("Guide added successfully!")


def add_tour_slot():
    if len(guides) == 0:
        print("Please add a guide first.")
        return

    print("\n--- Add Tour Slot ---")

    date = input("Enter tour date: ")
    time = input("Enter tour time: ")

    view_guides()

    guide_id = get_integer("Enter Guide ID: ")

    guide_found = False

    for guide in guides:
        if guide["id"] == guide_id:
            guide_found = True
            break

    if not guide_found:
        print("Invalid Guide ID.")
        return

    capacity = get_integer("Enter tour capacity: ")

    if capacity <= 0:
        print("Capacity must be greater than zero.")
        return

    slot = {
        "id": len(tour_slots) + 1,
        "date": date,
        "time": time,
        "guide_id": guide_id,
        "capacity": capacity,
        "booked": 0
    }

    tour_slots.append(slot)

    print("Tour slot added successfully!")


def admin_menu():
    while True:
        print("\n===== ADMIN MENU =====")
        print("1. Add Guide")
        print("2. Add Tour Slot")
        print("3. View Guides")
        print("4. View Tour Slots")
        print("5. Back to Main Menu")

        choice = get_integer("Enter your choice: ")

        if choice == 1:
            add_guide()

        elif choice == 2:
            add_tour_slot()

        elif choice == 3:
            view_guides()

        elif choice == 4:
            view_slots()

        elif choice == 5:
            break

        else:
            print("Invalid choice. Try again.")


def visitor_menu():
    while True:
        print("\n===== VISITOR MENU =====")
        print("1. Register")
        print("2. View Tour Slots")
        print("3. Book Tour")
        print("4. Cancel Booking")
        print("5. Back to Main Menu")

        choice = get_integer("Enter your choice: ")

        if choice == 1:
            register_visitor()

        elif choice == 2:
            view_slots()

        elif choice == 3:
            book_tour()

        elif choice == 4:
            cancel_booking()

        elif choice == 5:
            break

        else:
            print("Invalid choice. Try again.")


def main():
    while True:
        print("\n===== CAMPUS TOUR BOOKING SYSTEM =====")
        print("1. Admin")
        print("2. Visitor")
        print("3. Exit")

        choice = get_integer("Enter your choice: ")

        if choice == 1:
            admin_menu()

        elif choice == 2:
            visitor_menu()

        elif choice == 3:
            print("Thank you for using Campus Tour Booking System!")
            break

        else:
            print("Invalid choice. Try again.")


main()
