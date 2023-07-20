from metrics import wer, cer, levenshtein_ratio


def evaluate(gt, prediction, metric_name):
    metrics = {
        "WER": wer,
        "CER": cer,
        "Levenshtein_ratio": levenshtein_ratio
    }

    if metric_name not in metrics:
        raise ValueError(f"""OCR model '{metric_name}' not available. 
                         \n Available models are {list(metrics.keys())}""")

    metric = metrics[metric_name]
    value = metric(gt, prediction)
    return {"prediction": prediction, "gt": gt, f"{metric_name}": value}


def batch_evaluate(preds_df, metric_name):
    metrics = {
        "WER": wer,
        "CER": cer,
        "Levenshtein_ratio": levenshtein_ratio
    }

    if metric_name not in metrics:
        raise ValueError(f"""OCR model '{metric_name}' not available. 
                         \n Available models are {list(metrics.keys())}""")

    metric = metrics[metric_name]
    results_df = preds_df.copy()
    results_df[f"{metric}"] = results_df.apply(
        lambda x: metric(x["label"], x["cleaned_prediction"]), axis=0)
    return results_df
