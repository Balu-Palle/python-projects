class Hotel:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.booked_rooms = []

    def book_room(self, room_number):
        if room_number in self.booked_rooms:
            print(f"Room {room_number} is already booked.")
        elif room_number <= self.capacity:
            self.booked_rooms.append(room_number)
            print(f"Room {room_number} is booked successfully.")
        else:
            print(f"Room {room_number} is not available.")

    def get_available_rooms(self):
        available_rooms = []
        for room_number in range(1, self.capacity + 1):
            if room_number not in self.booked_rooms:
                available_rooms.append(room_number)
        return available_rooms


def display_menu():
    print("\nHotel Booking System")
    print("1. Book a room")
    print("2. Check available rooms")
    print("3. Exit")


def book_room_menu(hotel):
    room_number = int(input("Enter the room number you want to book: "))
    hotel.book_room(room_number)


def check_available_rooms_menu(hotel):
    available_rooms = hotel.get_available_rooms()
    if available_rooms:
        print("Available rooms:", available_rooms)
    else:
        print("No available rooms.")


def main():
    hotel_name = input("Enter the hotel name: ")
    hotel_capacity = int(input("Enter the total number of rooms: "))
    hotel = Hotel(hotel_name, hotel_capacity)

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            book_room_menu(hotel)
        elif choice == "2":
            check_available_rooms_menu(hotel)
        elif choice == "3":
            print("Thank you for using the Hotel Booking System. vist again!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
