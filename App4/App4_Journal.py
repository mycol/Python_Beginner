import Journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('--------------------------------')
    print('           JOURNAL APP')
    print('--------------------------------')
    print()


def run_event_loop():
    print('What do you want to do with your journal? ')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = Journal.load(journal_name) # list()

    while cmd != 'x' and cmd:
        cmd = input('[L]ist, [A]dd and Entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'".format(cmd))

    print('Done, goodbye!')
    Journal.save(journal_name, journal_data)


def list_entries(data):
    print("Your journal entries: ")
    entries = reversed(data)
    for indx, entry in enumerate(entries):
        print("* [{}] {}".format(indx + 1, entry))


def add_entry(data):
    text = input("Type in your entry, <enter> to exit: ")
    Journal.add_entry(text, data)


if __name__ == "__main__":
    main()
