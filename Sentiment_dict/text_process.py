# -*- coding: utf-8 -*-

#define some functions that will be used
import jieba
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Use jieba cut sentence into words and return a list
def segmentation(sentence):
    seg_list = jieba.cut(sentence)
    seg_result = []
    for word in seg_list:
        seg_result.append(word)
    return seg_result


# sentence segmentation
def cut_sentence(sentence):
    sentence= sentence.decode('utf8')
    start = 0
    i = 0
    token=''
    sents = []
    punt_list = ',.!?;~，。！？；～… '.decode('utf8')
    #print "punc_list", punt_list
    for word in sentence:
        # print "word", word
        if word not in punt_list:   # if word is not in stoplists
            # print "word not punt_list", word
            i += 1
            token = list(sentence[start:i+2]).pop()
            # print "token:", token
        elif word in punt_list and token in punt_list:  # handle a series of punt
            # print "word2", word
            i += 1
            token = list(sentence[start:i+2]).pop()
            # print "token:", token
        else:
            # print "word3", word
            # print i
            sents.append(sentence[start:i+1])   # cut sentence
            start = i + 1
            i += 1
    if start < len(sentence):   # handle the last part remained
        sents.append(sentence[start:])
    return sents

def read_lines(filename):
    fp = open(filename, 'r')
    lines = []
    for line in fp.readlines():
        line = line.strip()
        line = line.decode("utf-8")
        lines.append(line)
    fp.close()
    return lines

#  delete stop words
def del_stopwords(seg_sent):
    stopwords = read_lines("D:/PythonProject/Sentiment_dict/emotion_dict/stop_words.txt")  # read stopwords from stoplists
    new_sent = []   # return this when delete all stop words
    for word in seg_sent:
        if word in stopwords:
            continue
        else:
            new_sent.append(word)
    return new_sent



test_sentence1 = "这款手机大小合适。"
test_sentence2 = "这款手机大小合适，配置也还可以，很好用，只是屏幕有点小。。。总之，戴妃+是一款值得购买的智能手机。"
test_sentence3 = "这手机的画面挺好，操作也比较流畅。不过拍照真的太烂了！系统也不好。"

# seg_result = segmentation(test_sentence3)  # 分词，输入一个句子，返回一个list
# for w in seg_result:
#     print w,
# print '\n'
#
# new_seg_result = del_stopwords(seg_result)  # 去除停用词
# for w in new_seg_result:
#     print w,

# sen2=cut_sentence(test_sentence2)
# for w in sen2:
#     print w