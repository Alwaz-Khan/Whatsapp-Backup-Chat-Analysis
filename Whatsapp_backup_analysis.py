from pprint import pprint
import matplotlib.pyplot as plt

threshold_value =  0.001
data = []
with open(r"F:\Downloads 2020\WhatsApp Chat with Alwaz.txt", encoding="utf-8") as file_object:
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

histo = {}
for value in data:
    full_line = value["Message"]
    list_of_words = full_line.split()
    for word in list_of_words:
        word = word.lower()
        histo[word] =  histo.get(word, 0) + 1

histo = sorted(histo.items(), key=lambda x: x[1], reverse=True)
no_of_x_fields = int(len(histo) * threshold_value)
histo = histo[:no_of_x_fields]

x_axis = [x[0] for x in histo]
y_axis = [x[1] for x in histo]
plt.title("Whatsapp Backup Message Analysis")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.bar(x_axis, y_axis)
plt.show()
