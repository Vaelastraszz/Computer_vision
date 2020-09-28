import json
import csv
import pypickle as pickle

path = "/Users/RomainLejeune/Downloads/"


def get_ids_tomatoes(url=path):
    tomatoes = []
    allergic = ["tomato", "gaspacho"]

    with open(url + "label_mapping.csv", "r") as csv_file:
        food_inv = csv.reader(csv_file, delimiter=',')
        next(food_inv)
        food_dic = {row[0]: row[2] for row in food_inv}

    for key, value in food_dic.items():
        for x in allergic:
            if x in value.lower():
                tomatoes.append(key)

    return tomatoes


def create_labels(url=path):
    aliment_ids = {}

    with open(url + "img_annotations.json", "r") as json_file:
        photos = json.load(json_file)

    for k, v in photos.items():
        aliment_ids.setdefault(k, [])
        aliment_ids[k] = [x["id"] for x in v]

    return aliment_ids


def get_labels(tomatoes=get_ids_tomatoes(), aliment_ids=create_labels()):

    labels = {}
    for k, v in aliment_ids.items():
        labels.setdefault(k,)
        labels[k] = 0
        for tomato in tomatoes:
            if tomato in v:
                labels[k] = 1
                break
    return labels


if __name__ == '__main__':
    print(get_labels())
    pickle.save(var=get_labels(), filepath='/Users/RomainLejeune/Downloads/tomato_label.pkl')
