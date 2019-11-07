from pylexirumah import get_dataset

lr = get_dataset()

old_to_new_formid = {}
new_formids = set()
id_column = lr["FormTable", "id"].name
language_column = lr["FormTable", "languageReference"].name
concept_column = lr["FormTable", "parameterReference"].name
all_forms = []
for form in lr["FormTable"].iterdicts():
    synonym = 1
    new_id = "{:s}-{:s}-{:d}".format(form[language_column],
                                     form[concept_column],
                                     synonym)
    while new_id in new_formids:
        synonym += 1
        new_id = "{:s}-{:s}-{:d}".format(form[language_column],
                                         form[concept_column],
                                         synonym)
    old_to_new_formid[form[id_column]] = new_id
    form[id_column] = new_id
    all_forms.append(form)

form_column = lr["CognateTable", "formReference"].name
all_judgements = []
for judgement in lr["CognateTable"]:
    try:
        judgement[form_column] = old_to_new_formid[judgement[form_column]]
        all_judgements.append(judgement)
    except KeyError:
        print(judgement)

lr["FormTable"].write(all_forms)
lr["CognateTable"].write(all_judgements)
