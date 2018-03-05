from analysis_and_vkAPI import funcs
from analysis_and_vkAPI import vk_api

def topicAnalysis(text):
    words = funcs.splitText(text)
    words = funcs.normalForm(words)
    words = funcs.removeStopWords(words)
    return funcs.analyseFrequency(words)[2:-2]

if __name__ == '__main__':
    ids = ','.join([str(i) for i in range(1, 10)])
    groups = vk_api.getGroupDescription(ids)
    # print(groups)
    for k, v in groups.items():
        analysis = topicAnalysis(v)
        print(k, ':::', analysis)