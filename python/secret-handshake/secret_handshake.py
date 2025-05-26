def commands(binary_str):
    actions = ['wink','double blink','close your eyes','jump','reverse actions']
    actions_to_do = []
    for index,binary in enumerate(binary_str[::-1]):
        if binary == '1': 
            print(index,binary)
            if index == 4:
                actions_to_do.reverse()
            else:
                actions_to_do.append(actions[index])
    return actions_to_do
