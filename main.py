class Parking:
    def __init__(self, ticket='01', terminal='A1', entry='E1'):
        self.ticket = ticket
        self.terminal = terminal
        self.entry = entry

    def get_ticket(self):
        return self.ticket

    def set_ticket(self, ticket):
        self.ticket = ticket

    def get_terminal(self):
        return self.terminal

    def set_terminal(self, terminal):
        self.terminal = terminal

    def get_entry(self):
        return self.entry

    def set_entry(self, entry):
        self.entry = entry

    def print_details(self):
        print('Ticket: ', self.ticket)
        print('Terminal: ', self.terminal)
        print('Entry: ', self.entry)


def main():
    # parking = Parking('t2', 'term2', 'entry3')
    parking = Parking()
    parking.print_details()

    parking.set_entry('entry 4')
    print('New entry: ', parking.get_entry())
    parking.print_details()


if __name__ == "__main__":
    main()
