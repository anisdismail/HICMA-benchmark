import re
import Levenshtein


"""def wer(gt, ocr_prediction):

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
"""


def cer(gt, ocr_prediction):
    """
    Computes the Character Error Rate, defined as the edit distance.

    Arguments:
        gt (string): space-separated ground truth sentence
        ocr_prediction (string): space-separated predicted sentence
    """
    gt, ocr_prediction, = gt.replace(' ', ''), ocr_prediction.replace(' ', '')
    return Levenshtein.distance(gt, ocr_prediction)/len(gt)


def levenshtein_ratio(gt, ocr_prediction):
    """
    Computes the Levenshtein Ratio

    Arguments:
        gt (string): space-separated ground truth sentence
        ocr_prediction (string): space-separated predicted sentence
    """
    return Levenshtein.ratio(gt, ocr_prediction)



def wer(gt, ocr_prediction):
    """
    Computes the Word Error Rate, defined as the edit distance between the
    two provided sentences after tokenizing to words.
    adapted from https://github.com/jitsi/jiwer/issues/7

    Arguments:
        gt (string): space-separated ground truth sentence
        ocr_prediction (string): space-separated predicted sentence
    """

    # build mapping of words to integers
    b = set(gt.split() + ocr_prediction.split())
    word2char = dict(zip(b, range(len(b))))

    # map the words to a char array (Levenshtein packages only accepts
    # strings)
    w1 = [chr(word2char[w]) for w in gt.split()]
    w2 = [chr(word2char[w]) for w in ocr_prediction.split()]

    return Levenshtein.distance(''.join(w1), ''.join(w2))/float(len(w1))

