def transformStr(string: str):
    transformedStr = string
    if len(string) > 5:
        transformedStr = transformedStr[0:5] +'...'
    if transformedStr[0] in 'Ll':
        transformedStr = transformedStr.lower()
    elif transformedStr[0] in 'Uu':
        transformedStr = transformedStr.upper()

    print(transformedStr)

transformStr('Testing string')
transformStr('Lux')
transformStr('up')
transformStr('Luxery')

    