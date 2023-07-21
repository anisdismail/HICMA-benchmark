import re
import Levenshtein


def wer(gt, ocr_prediction):

    operations = Levenshtein.editops(gt, ocr_prediction)
    operations = [element for element in operations if element[1] < len(gt)]
    operations = [element for element in operations if gt[element[1]] != " "]
    res = [(ele.start(), ele.end() - 1) for ele in re.finditer(r'\S+', gt)]
    arr = [0]*len(res)
    for operation in operations:
        for i, word in enumerate(res):
            if word[0] <= operation[1] <= word[1]:
                if arr[i] == 0:
                    arr[i] += 1
                break
    return sum(arr)/len(arr)


def cer(gt, ocr_prediction):
    return Levenshtein.distance(gt, ocr_prediction)/len(gt)


def levenshtein_ratio(gt, ocr_prediction):
    return Levenshtein.ratio(gt, ocr_prediction)
