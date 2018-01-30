

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
    cmd = None
    journal_data = [] # list()

    while cmd != 'x':

        cmd = input('[L]ist, [A]dd and Entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry, we don't understand '{}'".format(cmd))

    print('Done, goodbye!')


def list_entries(data):
    print("Your journal entries: ")
    entries = reversed(data)
    for indx, entry in enumerate(entries):
        print("* [{}] {}".format(indx + 1, entry))

def add_entry(data):
    text = input("Type in your entry, <enter> to exit: ")
    data.append(text)


main()
