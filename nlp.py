import paralleldots as pdots


def sentiment_analysis(text, key):
    pdots.set_api_key(key)

    output = []
    result = pdots.sentiment(text)

    for key, val in result['sentiment'].items():
        ans = f'{key} ---> {val}'
        output.append(ans)

    return output


def named_entity_recognition(text, key):
    pdots.set_api_key(key)

    output = []
    result = pdots.ner(text)
    result = result['entities']

    for res in result:
        name = res['name']
        cat = res['category']
        ans_list = [f'{name} ---> {cat}']
        output.append(ans_list)

    return output


def abuse_detection(text, key):
    pdots.set_api_key(key)

    output = []
    result = pdots.abuse(text)

    for key, val in result.items():
        ans = f'{key} ---> {val}'
        output.append(ans)

    return output


def similarity_score(text1, text2, key):
    pdots.set_api_key(key)

    output = []
    result = pdots.similarity(text1,text2)

    for key, val in result.items():
        ans = f'{key} ---> {val}'
        output.append(ans)

    return output
