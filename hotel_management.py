# Python program to implement Hotel Management System

# Create class for Hotel data
class Hotel:
    sort_param = 'name'

    def __init__(self, name, room_avl, location, rating, price_per_room):
        self.name = name
        self.room_avl = room_avl
        self.location = location
        self.rating = rating
        self.price_per_room = price_per_room

    def __lt__(self, other):
        return getattr(self, Hotel.sort_param) < getattr(other, Hotel.sort_param)

    def __repr__(self):
        return f"Hotel Name: {self.name}, Rooms Available: {self.room_avl}, Location: {self.location}, Rating: {self.rating}, Price: {self.price_per_room}"

    @classmethod
    def sort_by_name(cls):
        cls.sort_param = 'name'

    @classmethod
    def sort_by_rating(cls):
        cls.sort_param = 'rating'

    @classmethod
    def sort_by_room_available(cls):
        cls.sort_param = 'room_avl'


# Create class for User data
class User:
    def __init__(self, uname, uid, cost):
        self.uname = uname
        self.uid = uid
        self.cost = cost

    def __repr__(self):
        return f"User Name: {self.uname}, User ID: {self.uid}, Booking Cost: {self.cost}"


# Function to print hotel data
def print_hotel_data(hotels):
    for hotel in hotels:
        print(hotel)


# Function to sort hotels by name
def sort_hotels_by_name(hotels):
    print("\nSORT BY NAME:")
    Hotel.sort_by_name()
    hotels.sort()
    print_hotel_data(hotels)


# Function to sort hotels by rating
def sort_hotels_by_rating(hotels):
    print("\nSORT BY RATING:")
    Hotel.sort_by_rating()
    hotels.sort(reverse=True)
    print_hotel_data(hotels)


# Function to filter hotels by location
def filter_hotels_by_location(location, hotels):
    print(f"\nHOTELS IN {location.upper()}:")
    filtered_hotels = [hotel for hotel in hotels if hotel.location.lower() == location.lower()]
    print_hotel_data(filtered_hotels)


# Function to sort hotels by room availability
def sort_hotels_by_room_availability(hotels):
    print("\nSORT BY ROOM AVAILABILITY:")
    Hotel.sort_by_room_available()
    hotels.sort(reverse=True)
    print_hotel_data(hotels)


# Function to print user booking data
def print_user_data(users, hotels):
    print("\nUSER BOOKINGS:")
    for i, user in enumerate(users):
        print(f"{user} | Booked Hotel: {hotels[i].name}")


# Main function
def hotel_management():
    # Initialize hotel data
    hotels = [
        Hotel("H1", 4, "Bangalore", 5, 100),
        Hotel("H2", 5, "Bangalore", 5, 200),
        Hotel("H3", 6, "Mumbai", 3, 100)
    ]

    # Initialize user data
    users = [
        User("U1", 2, 1000),
        User("U2", 3, 1200),
        User("U3", 4, 1100)
    ]

    # Perform operations
    print("\nPRINT HOTEL DATA:")
    print_hotel_data(hotels)

    sort_hotels_by_name(hotels)
    sort_hotels_by_rating(hotels)
    filter_hotels_by_location("Bangalore", hotels)
    sort_hotels_by_room_availability(hotels)
    print_user_data(users, hotels)


# Run the program
if __name__ == "__main__":
    hotel_management()