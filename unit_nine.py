# Bonus tasks - afik

# exercise 9.1.1
def are_files_equal(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read() == f2.read()


# exercise 9.1.2
def sort_words(file_path):
    with open(file_path) as f:
        words = set()
        for line in f:
            words.update(line.strip().split())
        return sorted(words)


def reverse_lines(path):
    with open(path) as f:
        for line in f:
            print(line.strip()[::-1])


def last_lines(path, n):
    with open(path) as f:
        lines = f.readlines()
        for line in lines[-n:]:
            print(line.strip())


def main_program():
    file_path = input("enter path for file: ")
    task = input("Enter a task (sort, rev, last): ")

    if task == "sort":
        sorted_words = sort_words(file_path)
        print(sorted_words)

    elif task == "rev":
        reverse_lines(file_path)

    elif task == "last":
        n = int(input("Enter number of last lines: "))
        last_lines(file_path, n)

    else:
        print("Invalid task entered.")


# exercise 9.2.2
def copy_file_content(source, destination):
    with open(source, 'r') as file1:
        with open(destination, 'w') as file2:
            file2.write(file1.read())


# exercise 9.2.3
def who_is_missing(file_name):
    with open(file_name, 'r') as file:
        numbers = file.read().split(',')
        numbers = [int(num) for num in numbers]
        missing = None
        for i in range(1, len(numbers) + 1):
            if i not in numbers:
                missing = i
                break
        with open('found.txt', 'w') as found_file:
            found_file.write(str(missing))
        return missing


# exercise 9.3.1
def my_mp3_playlist(file_path):
    len_longest_song = -1
    longest_song_name = ""
    songs_count = 0
    operations = {}

    with open(file_path, "r") as file:
        for line in file:
            song_info = line.strip().split("; ")
            if len(song_info) != 3:
                continue

            song_name, performer_name, len_song = song_info
            songs_count += 1

            if len_longest_song < 0 or len_song > len_longest_song:
                len_longest_song = len_song
                longest_song_name = song_name

            operation_name = performer_name if performer_name != "Unknown" else song_name
            if operation_name in operations:
                operations[operation_name] += 1
            else:
                operations[operation_name] = 1

    most_common_operation = max(operations, key=operations.get)

    return longest_song_name, songs_count, most_common_operation


# ex 9.3.2
def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    while len(lines) < 3:
        lines.append('\n')
    lines[2] = f"{new_song};Unknown;\n"
    with open(file_path, 'w') as f:
        f.writelines(lines)
    with open(file_path, 'r') as f:
        print(f.read())


def main():
    pass


if __name__ == '__main__':
    main()
