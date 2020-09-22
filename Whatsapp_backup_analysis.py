from pprint import pprint
import matplotlib.pyplot as plt

threshold_value = 0.001


def load_data(filepath):
    """
    Takes a txt file as input and categories each line of data into 4 parameters: date, time, author and message; stores
    the data into list of dictionary  and  outputs this list.
    :param filepath: str: contains the chat backup from whatsapp in a text format
    :return: returns a list which consists of dictionary in each position which  contains 4 key value pairs
    """
    data = []
    with open(filepath, encoding="utf-8") as file_object:
        for line in file_object:
            date = line[0:7]
            time = line[9:17].strip()
            temp = line.split("-", 1)
            try:
                temp2 = temp[1].split(":", 1)
                author = temp2[0].strip()
                message = temp2[1].strip("\n").strip()
                value = {"date": date, "time": time, "Author": author, "Message": message}
                data.append(value)
            except IndexError:
                extract_previous_dict = data[-1]
                extract_previous_message = extract_previous_dict["Message"]
                new_message = extract_previous_message + "\n" + line.strip("\n")
                data[-1]["Message"] = new_message
    return data


def word_count(data):
    """
    counts frequency of words and returns a dictionary containing key as name of word and value as frequency
    :param data: list of dict: take organized data
    :return: list of tuple with word, frequency at position of list
    """
    histo = {}
    for value in data:
        full_line = value["Message"]
        list_of_words = full_line.split()
        for word in list_of_words:
            word = word.lower()
            histo[word] = histo.get(word, 0) + 1
    return list(histo.items())


def filter_data(histo):
    """
    Takes a list of tuples containing word and frequency at each position of list, ranks the  tuples in order of highest
    frequency, and then selects an x percentage of words from the top and returns the modified list of tuples
    :param histo: list of tuples: word, frequency  at each position of  list
    :return: modified list of tuples containing  top x% of words based on frequency
    """
    histo = sorted(histo, key=lambda x: x[1], reverse=True)
    no_of_x_fields = int(len(histo) * threshold_value)
    histo = histo[:no_of_x_fields]
    return histo


def plot_graph(histo):
    """
    Takes dictionary containing words as keys and frequency as value and plots a bar graph
    :param histo: list containing word, frequency at each position
    :return: none
    """
    x_axis = [x[0] for x in histo]
    y_axis = [x[1] for x in histo]
    plt.title("Whatsapp Backup Message Analysis")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.bar(x_axis, y_axis)
    plt.show()


def main():
    data = load_data("WhatsApp Chat with Alwaz.txt")
    histo = word_count(data)
    histo = filter_data(histo)
    plot_graph(histo)


if __name__ == '__main__':
    main()
