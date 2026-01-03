import sys
import csv
import webbrowser

if __name__ == '__main__':
    content = ''
    print("Running application...")

    filename = sys.argv[1]
    print("Filename is ", filename)

    with open(filename, "r") as file:
        content = csv.reader(file, delimiter=',')

        print("CSV file is ", content)

        for row in content:
            print("Link is ", row[3])
            webbrowser.open(row[3], new=0, autoraise=True)
