import json
import pandas as pd
from collections import defaultdict
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def calculate_total_time_while_telling_actual_words(df_cal):
    duration_dict = defaultdict(float)
    for index, row in enumerate(df_cal.iterrows()):
        duration_dict[df_cal.iloc[index]['speakers_tag']] = duration_dict[df_cal.iloc[index]['speakers_tag']] + \
                                                            (df_cal.iloc[index]['end_time']) - \
                                                            (df_cal.iloc[index]['start_time'])
        # print(row)
    print(duration_dict)
    return duration_dict


def calculate_total_time_with_pauses(df_cal):
    duration_dict = defaultdict(float)
    old_speaker = df_cal.iloc[0]['speakers_tag']
    start_time_old_speaker = df_cal.iloc[0]['start_time']
    end_time_old_speaker = df_cal.iloc[0]['end_time']
    for index, row in enumerate(df_cal.iterrows()):
        if (index == 0): continue
        new_speaker = df_cal.iloc[index]['speakers_tag']
        if (old_speaker != new_speaker):
            end_time_old_speaker = df_cal.iloc[index - 1]['end_time']
            duration_dict[old_speaker] = duration_dict[old_speaker] + end_time_old_speaker - start_time_old_speaker
            start_time_old_speaker = df_cal.iloc[index]['start_time']
            old_speaker = df_cal.iloc[index]['speakers_tag']
    end_time_old_speaker = df_cal.iloc[-1]['end_time']
    duration_dict[df_cal.iloc[-1]['speakers_tag']] = duration_dict[df_cal.iloc[-1][
        'speakers_tag']] + end_time_old_speaker - start_time_old_speaker
    print(duration_dict)
    return duration_dict


def percentage_of_total_duration(df_cal):
    duration_dict = defaultdict(float)
    dict_total = calculate_total_time_with_pauses(df_cal)
    for index, items in enumerate(dict_total.items()):
        duration_dict[items[0]] = (items[1] / df_cal.iloc[-1]['end_time']) * 100
    print("percentage_of_total_duration", duration_dict)
    return duration_dict


def gap_between_the_turns(df_cal):
    duration_dict = defaultdict(float)
    old_speaker = df_cal.iloc[0]['speakers_tag']
    end_time_old_speaker = df_cal.iloc[0]['end_time']
    for index, row in enumerate(df_cal.iterrows()):
        if (index == 0): continue
        new_speaker = df_cal.iloc[index]['speakers_tag']
        if (old_speaker != new_speaker):
            duration_dict[old_speaker] = duration_dict[old_speaker] + df_cal.iloc[index][
                'start_time'] - end_time_old_speaker
            end_time_old_speaker = df_cal.iloc[index]['end_time']
            old_speaker = df_cal.iloc[index]['speakers_tag']
    print("gap bewtween the responses", duration_dict)
    return duration_dict


def calculting_continuous_repeative_word(df_cal):
    duration_dict = defaultdict(float)
    old_speaker = df_cal.iloc[0]['speakers_tag']
    prev_word = df_cal.iloc[0]['word']
    for index, row in enumerate(df_cal.iterrows()):
        if (index == 0): continue
        current_speaker = df_cal.iloc[index]['speakers_tag']
        if (old_speaker == current_speaker):
            if (prev_word == df_cal.iloc[index]['word']):
                duration_dict[old_speaker] = duration_dict[old_speaker] + 1
        prev_word = df_cal.iloc[index]['word']
        old_speaker = df_cal.iloc[index]['speakers_tag']
    print("calculting_continuous_repeative_word", duration_dict)
    return duration_dict


def total_turns(df_cal):
    duration_dict = defaultdict(float)
    old_speaker = df_cal.iloc[0]['speakers_tag']
    for index, row in enumerate(df_cal.iterrows()):
        if index == 0: continue
        current_speaker = df_cal.iloc[index]['speakers_tag']
        if old_speaker != current_speaker:
            duration_dict[old_speaker] = duration_dict[old_speaker] + 1
            old_speaker = df_cal.iloc[index]['speakers_tag']
    print("total_turn", duration_dict)
    return duration_dict


def total_unique_words(df_cal):
    duration_dict = defaultdict(float)
    for key in np.unique(np.array(df_cal['speakers_tag'])):
        df_s1 = df_cal[df_cal['speakers_tag'] == key]
        s = df_s1['word'].to_numpy()
        duration_dict[key] = len(np.unique(s))
    print("total unique words", duration_dict)
    return duration_dict


def first_half_percent_spoken_time(df_cal):
    duration_dict = defaultdict(float)
    total_time=df_cal.iloc[-1]['end_time']
    total_time=total_time/2
    old_speaker= df_cal.iloc[0]['speakers_tag']
    start_time_old_speaker=df_cal.iloc[0]['start_time']
    last_index=-1
    for index,row in enumerate(df_cal.iterrows()):
        if(total_time<df_cal.iloc[index]['end_time']):
         break
        if(index==0):continue
        new_speaker=df_cal.iloc[index]['speakers_tag']
        if(old_speaker!=new_speaker):
            end_time_old_speaker=df_cal.iloc[index-1]['end_time']
      # print(star_time_old_speaker,end_time_old_speaker,old_speaker)
            duration_dict[old_speaker]=duration_dict[old_speaker]+end_time_old_speaker-start_time_old_speaker
            start_time_old_speaker=df_cal.iloc[index]['start_time']
            old_speaker= df_cal.iloc[index]['speakers_tag']
        last_index=index

    end_time_old_speaker=df_cal.iloc[last_index]['end_time']
  # print(star_time_old_speaker,end_time_old_speaker,old_speaker)
    duration_dict[df_cal.iloc[last_index]['speakers_tag']]=duration_dict[df_cal.iloc[-1]['speakers_tag']]+end_time_old_speaker-start_time_old_speaker
    for index,items in enumerate(duration_dict.items()):
        duration_dict[items[0]]=(items[1]/df_cal.iloc[last_index]['end_time'])*100
    print("first_half_percent_spoken_time",duration_dict)
    return duration_dict


def last_half_percent_spoken_time(df_cal):
    duration_dict = defaultdict(float)
    total_time=df_cal.iloc[-1]['end_time']
    total_time=total_time/2
    old_speaker= df_cal.iloc[0]['speakers_tag']
    start_time_old_speaker=df_cal.iloc[0]['start_time']
    last_index=-1
    for index,row in enumerate(df_cal.iterrows()):
        if(total_time>df_cal.iloc[index]['end_time']): continue
        if(index==0): continue
        new_speaker=df_cal.iloc[index]['speakers_tag']
        if(old_speaker!=new_speaker):
            end_time_old_speaker=df_cal.iloc[index-1]['end_time']
      # print(star_time_old_speaker,end_time_old_speaker,old_speaker)
            duration_dict[old_speaker]=duration_dict[old_speaker]+end_time_old_speaker-start_time_old_speaker
            start_time_old_speaker=df_cal.iloc[index]['start_time']
            old_speaker= df_cal.iloc[index]['speakers_tag']
        last_index=index
    end_time_old_speaker=df_cal.iloc[last_index]['end_time']
  # print(star_time_old_speaker,end_time_old_speaker,old_speaker)
    duration_dict[df_cal.iloc[last_index]['speakers_tag']]=duration_dict[df_cal.iloc[-1]['speakers_tag']]+end_time_old_speaker-start_time_old_speaker
    for index,items in enumerate(duration_dict.items()):
        duration_dict[items[0]]=(items[1]/df_cal.iloc[last_index]['end_time'])*100
    print("last_half_percent_spoken_time",duration_dict)
    return duration_dict


def average_len_of_word(df_cal):
    df_cal["word"]=df_cal['word'].str.replace('\W', '')
    avg=df_cal["word"].to_numpy()
    df_cal['list_avg']=[len(a) for a in avg]

    duration_dict = defaultdict(float)
    for key in np.unique(np.array(df_cal['speakers_tag'])):
        df_s1=df_cal[df_cal['speakers_tag']==key]
        s=df_s1['list_avg'].to_numpy()
        duration_dict[key]=(np.mean(s))
    print("average_len_of_word",duration_dict)
    return duration_dict


def calculate_total_pauses_between_the_sentences(df_cal):
    duration_dict = defaultdict(float)
    old_speaker= df_cal.iloc[0]['speakers_tag']
    end_time_for_last_word=df_cal.iloc[0]['end_time']
    for index,row in enumerate(df_cal.iterrows()):
        if(index==0):continue
        new_speaker=df_cal.iloc[index]['speakers_tag']
        if(old_speaker==new_speaker):
            duration_dict[old_speaker]=duration_dict[old_speaker]+df_cal.iloc[index]['start_time']-end_time_for_last_word
            # print(df_cal.iloc[index]['actual_start_time'],end_time_for_last_word)
            end_time_for_last_word=df_cal.iloc[index]['end_time']
            old_speaker= df_cal.iloc[index]['speakers_tag']
    print("calculate_total_pauses_between_the_sentences",duration_dict)
    return duration_dict


def total_conversation_duration(df_cal):
    duration_dict = defaultdict(float)
    unique_speakers= np.unique(df_cal['speakers_tag'])
    for u in unique_speakers:
        duration_dict[u]=df_cal.iloc[-1]['end_time']-df_cal.iloc[0]['start_time']
    return duration_dict


def extract_pos(df, total_tags):
    # print(df.values)
    total_tags = []
    dict_pos = defaultdict(lambda: defaultdict(int))
    current_speaker = df.iloc[0]["speakers_tag"]
    sent = ''
    for index, rows in enumerate(df.iterrows()):
        if (current_speaker == df.iloc[index]["speakers_tag"]):
            # print(df.iloc[index]["word"][1:-1])
            sent = sent + " " + df.iloc[index]["word"][1:-1]

        elif (current_speaker != str(df.iloc[index]["speakers_tag"]) or len(sent.split()) > 20):
            # print(len(sent.split()))
            tokens = nltk.word_tokenize(sent)
            # print(tokens)
            tag = nltk.pos_tag(tokens)
            for pos in range(len(tag)):
                total_tags.append(tag[pos][1])
                dict_pos[current_speaker][tag[pos][1]] = dict_pos[current_speaker][tag[pos][1]] + 1
            current_speaker = df.iloc[index]["speakers_tag"]
            sent = ''
    # dict_pos[current_speaker]
    # print(tag)
    # print(sent)
    return dict_pos, np.unique(np.array(total_tags))


class feature_exraction():

    def extracting_speaker_diarization(self, data):
        start_times, end_times, words, speaker_tags = [], [], [], []
        results = json.loads(data)
        alternatives = results['results']
        for index, value in enumerate(alternatives):
            # print(value['alternatives'])
            # print(type(value['alternatives']))
            nested_values = value['alternatives'][0]
            if 'transcript' not in nested_values:
                actual_values = nested_values["words"]
                for features in actual_values:
                    start_times.append(features['start_time'][:-1])
                    end_times.append(features['end_time'][:-1])
                    words.append(features['word'])
                    speaker_tags.append(features['speaker_tag'])
        dic = {'start_time': start_times, 'end_time': end_times, 'word': words, 'speakers_tag': speaker_tags}
        df = pd.DataFrame.from_dict(dic, orient='index')
        df = df.T
        df['start_time'] = df['start_time'].astype(float)
        df['end_time'] = df['end_time'].astype(float)
        # print(df)
        f0 = calculate_total_time_while_telling_actual_words(df)
        f1 = calculate_total_time_with_pauses(df)
        f2 = gap_between_the_turns(df)
        f3 = calculting_continuous_repeative_word(df)
        f4 = percentage_of_total_duration(df)
        f5 = total_turns(df)
        f6 = total_unique_words(df)
        f7 = first_half_percent_spoken_time(df)
        f8 = last_half_percent_spoken_time(df)
        f9 = average_len_of_word(df)
        f10 = calculate_total_pauses_between_the_sentences(df)
        # f11 = total_conversation_duration(df)
        total_tags = []
        df_pos, tags = (extract_pos(df, total_tags))
        for tag in tags:
            if tag not in total_tags:
                total_tags.append(tag)
        final_df = pd.DataFrame.from_dict(df_pos)
        final_df = final_df.fillna(0)
        final_df = final_df.T
        print(final_df)

