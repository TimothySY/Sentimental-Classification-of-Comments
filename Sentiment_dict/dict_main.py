# -*- coding: utf-8 -*-

import text_process as tp
import codecs



#1 read sentimental dict and adverb dict
# sentimental dict

posdict = tp.read_lines("D://PythonProject/Sentiment_dict/emotion_dict/pos_all_dict.txt")
negdict = tp.read_lines("D://PythonProject/Sentiment_dict/emotion_dict/neg_all_dict.txt")
# adverb of dict
mostdict = tp.read_lines('D://PythonProject/Sentiment_dict/degree_dict/most.txt')   # weight is 2
verydict = tp.read_lines('D://PythonProject/Sentiment_dict/degree_dict/very.txt')   # weight is 1.75
moredict = tp.read_lines('D://PythonProject/Sentiment_dict/degree_dict/more.txt')   # weight is 1.5
ishdict = tp.read_lines('D://PythonProject/Sentiment_dict/degree_dict/ish.txt')   # weight is 1.2
insufficientdict = tp.read_lines('D://PythonProject/Sentiment_dict/degree_dict/insufficiently.txt')  # weight is 0.5
inversedict = tp.read_lines('D://PythonProject/Sentiment_dict/degree_dict/inverse.txt')  # weight is -1

# 2 handle adverb and multiply word according to different weight
def match(word, sentiment_value):
    if word in mostdict:
        sentiment_value *= 2.0
    elif word in verydict:
        sentiment_value *= 1.75
    elif word in moredict:
        sentiment_value *= 1.5
    elif word in ishdict:
        sentiment_value *= 1.2
    elif word in insufficientdict:
        sentiment_value *= 0.5
    elif word in inversedict:
        sentiment_value *= -1
    return sentiment_value


# 3.delete minus number
# Example: [5, -2] →  [7, 0]; [-4, 8] →  [0, 12]
def transform_to_positive_num(poscount, negcount):
    pos_count = 0
    neg_count = 0
    if poscount < 0 and negcount >= 0:
        neg_count += negcount - poscount
        pos_count = 0
    elif negcount < 0 and poscount >= 0:
        pos_count = poscount - negcount
        neg_count = 0
    elif poscount < 0 and negcount < 0:
        neg_count = -poscount
        pos_count = -negcount
    else:
        pos_count = poscount
        neg_count = negcount
    return (pos_count, neg_count)


# give score to a single sentence
def sentence_score(sentence):
    final_score = []
    cuted_review = tp.cut_sentence(sentence)  #cut sentence into subsentences
    # for w in cuted_review:
        # print w
    for sent in cuted_review:
        seg_sent = tp.segmentation(sent)   # segment words
        seg_sent = tp.del_stopwords(seg_sent)[:]
        # for w in seg_sent:
        #     print w
        i = 0    # current location
        s = 0    # emotion word location
        poscount = 0    # positive word score
        negcount = 0    # negative word score

        for word in seg_sent:
            # print word
            if word in posdict:
                # print word
                poscount += 1
                for w in seg_sent[s:i]:
                    # print w
                    poscount = match(w, poscount)
                    # print poscount

                s = i + 1

            elif word in negdict:

                negcount += 1
                for w in seg_sent[s:i]:
                    negcount = match(w, negcount)

                s = i + 1

            # if ! ！, which means coming to end of sentence
            elif word == "！".decode("utf-8") or word == "!".decode('utf-8'):
                for w2 in seg_sent[::-1]:
                    if w2 in posdict:
                        poscount += 2
                        break
                    elif w2 in negdict:
                        negcount += 2
                        break
            i += 1

        final_score.append(transform_to_positive_num(poscount, negcount))   # final process
    pos_result, neg_result = 0, 0
    for res1, res2 in final_score:  # 每个分句循环累加
        pos_result += res1
        neg_result += res2
    #print pos_result, neg_result
    result = pos_result - neg_result   # final score
    return result

score=sentence_score("出水速度快，很耐用")
print score

# correct=0
# total=0
# f=codecs.open('postest.txt', 'r', 'gbk')
# line=f.readline()
# while line:
#     total=total+1
#     score=sentence_score(line)
#     if(score>0):
#          correct=correct+1
#     print line
#     line=f.readline()
#
# print(correct)
# print(total)
# f.close()
