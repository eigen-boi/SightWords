# built for kindergarten vocabulary, June 2020, Aidan Patton
import PySimpleGUI as sg # import modules
import random as rd
import sys
import os
import PyDictionary
import pyttsx3
import pronouncing
#import enchant
import time
import datetime
import requests
import json
import playsound

#this_folder = os.path.dirname(__file__) # set up relative paths

def find_data_file():
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return datadir

this_folder = find_data_file()
dep = os.path.join(this_folder, "dep")
textures = os.path.join(dep, "textures")
saves = os.path.join(dep, "saves")
sparkle = os.path.join(dep, "sparkle")

word_file = os.path.join(saves, "word_list_current.txt") # link files
tempfile = os.path.join(saves, "tempfile.txt")
MyNameFile = os.path.join(saves, "myname.txt")
TimeKeeper = os.path.join(saves, "timekeeper.txt")
ABC = os.path.join(textures, "ronan_icon.png")
icon = os.path.join(textures, "ronan_icon.ico")
SAVE_BUTTON = os.path.join(textures, "save.png")
START_BUTTON = os.path.join(textures, "start.png")
BACK_BUTTON = os.path.join(textures, "back.png")
OPEN_BUTTON = os.path.join(textures, "open.png")
CANCEL_BUTTON = os.path.join(textures, "cancel.png")
NEXT_WORD_BUTTON = os.path.join(textures, "nextword.png")
NEXT_BUTTON = os.path.join(textures, "nextnumber.png")
AGAIN_BUTTON = os.path.join(textures, "again.png")
SPEECH_BUTTON = os.path.join(textures, "speech.png")
LOOKUP_BUTTON = os.path.join(textures, "lookup.png")
SEARCH_BUTTON = os.path.join(textures, "search.png")
BackgroundImage = os.path.join(textures, "sizedbuttons.png")
colour_file = os.path.join(sparkle, "DARKCOLOURS.txt")
encouragement = os.path.join(sparkle, "supportdisplay.txt")
encouragementverbal = os.path.join(sparkle, "supportverbal.txt")

# ============================================================ function defs from here

def MyDictionaryF():

    class MyDictionary:
        def __init__(self, WordName, WordTypes, WordDefinitions):
            self.name = WordName
            self.meaning = dict()
            for meanings in range(len(WordTypes)):
                self.meaning[WordTypes[meanings]] = WordDefinitions[meanings]
        GetMeaningValid = True

    WordsOut = []
    WordsOut.append(MyDictionary('am', ['Verb'], [[' First person singular present of "be"']]))
    WordsOut.append(MyDictionary('ant', ['Noun', 'Phrases'], [[' A small insect that usually lives in a complex social colony with one or more breeding queens. It is wingless except for fertile adults.'], [" Have ants in one's pants — be fidgety or restless"]]))
    WordsOut.append(MyDictionary('dad', ['Noun'], [[' Father. ']]))
    WordsOut.append(MyDictionary('is', ['Verb'], [[' Third person singular present of "be", Occur; take place, Having the state/quality/identity/nature/role/etc. specified']]))
    WordsOut.append(MyDictionary('I', ['Pronoun'], [[' Used to refer to oneself']]))
    WordsOut.append(MyDictionary('to', ['Preposition'], [[' Expressing motion in the direction of a location, Approaching or reaching a condition, Identifying the person or thing affected, Identifying a relationship or attachment, Concerning, Used to introduce the second element in a comparison.']]))
    WordsOut.append(MyDictionary('no', ['Noun', 'Adverb', 'Exclamation', 'Determiner'], [[' A negative answer or decision'], [' Not at all; to no extent'], [' Used to give a negative response, Expressing disagreement or contradiction, Expressing agreement with or affirmation of a negative statement, Expressing shock or disappointment at something one has been made known of'], [' Not/hardly any, Used to forbid or reject, Used to indicate somthing is the opposite of what is being specified']]))
    WordsOut.append(MyDictionary('me', ['Pronoun'], [[' Used to refer to oneself as the object of a verb or preposition.']]))
    WordsOut.append(MyDictionary('it', ['Pronoun'], [[' Used to refer to something to be identified through context., The player who has to catch the others.']]))
    WordsOut.append(MyDictionary('and', ['Conjugation'], [[' Used to connect ideas to be taken jointly, Used to introduce an additional comment or interjection, Sometimes informally used to indicate intention instead of "to"']]))
    WordsOut.append(MyDictionary('at', ['Preposition'], [[' Expressing a particular location/time/state/condition/relationship, Expressing the object of a look/gesture/thought/action/plan, Expressing the means by which something is done']]))
    WordsOut.append(MyDictionary('be', ['Verb'], [[' Exist, Occur; take place, Having the state/quality/identity/nature/role/etc. specified']]))
    WordsOut.append(MyDictionary('you', ['Pronoun'], [[' Used to refer to the person or people that the speaker is addressing']]))
    WordsOut.append(MyDictionary('the', ['Determiner'], [[' Denoting one or more people or things already mentioned or assumed to be known, Used to refer to a person/place/thing that is unique, Used to make a generalized reference to something rather than identifying a particular instance,Used to point forward to a following qualifying or defining clause or phrase']]))
    WordsOut.append(MyDictionary('yes', ['Noun', 'Exclamation'], [[' An affirmative answer or decision especially in voting.'], [' Used to give an affirmative response., Used to question a remark or ask for more detail about it; encouraging someone to continue speaking., Expressing delight.']]))
    WordsOut.append(MyDictionary('love', ['Noun', 'Verb'], [[' An intense feeling of deep affection, A great interest and pleasure in something'], ['Feel a deep romantic or spicy attachment to (someone)']]))
    WordsOut.append(MyDictionary('like', ['Verb', 'Preposition', 'Conjugation', 'Noun', 'Adjective', 'Adverb'], [[' Find agreeable enjoyable or satisfactory, Wish for; want'], [' Having the same characteristics or qualities as; similar to.'], [' In the same way that; as though.'], [' The things one likes or prefers'], [' Having similar qualities or characteristics to another person or thing'], [' Used to convey reported attitude or feelings in the form of direct speech']]))
    WordsOut.append(MyDictionary('mom', ['Noun'], [[' Mother ']]))
    WordsOut.append(MyDictionary('my', ['Determiner'], [[' Belonging to or associated with the speaker, Used in various expressions of surprise']]))
    WordsOut.append(MyDictionary('a', ['Determiner'], [[' Used when referring to someone or something for the first time in a text or conversation, One single; any, Used to indicate membership of a class of people or things.']]))
    WordsOut.append(MyDictionary('we', ['Pronoun'], [[' Used by a speaker to refer to themself and one or more other people considered together, Used in formal contexts for or by a royal person or by a writer or editor to refer to themself, Used condescendingly to refer to the person being addressed']]))
    WordsOut.append(MyDictionary('are', ['Verb'], [[' Second person singular present and first/second/third person plural present of "be".']]))
    WordsOut.append(MyDictionary('our', ['Determiner'], [[' Belonging to or associated with the speaker and one or more other people previously mentioned or easily identified.']]))
    WordsOut.append(MyDictionary('but', ['Conjunction', 'Preposition', 'Adverb', 'Noun'], [[' Used to introduce a phrase or clause contrasting with what has already been mentioned'], [' Except; apart from; other than'], [' No more than; only.'], [' An argument against something; an objection.']]))
    WordsOut.append(MyDictionary('that', ['Pronoun/Determiner', 'Adverb', 'Conjunction'], [[' Used to identify a specific person or thing observed by the speaker., Referring to a specific thing previously mentioned/known/understood., Used in singling out someone or something and ascribing a distinctive feature to them., Used instead of “which” “who” “whom” or “when” to introduce a defining or restrictive clause'], [' To such a degree; so., Used with a gesture to indicate size or distance., Very'], [' Introducing a subordinate clause expressing a statement or hypothesis., Expressing a wish or regret.']]))
    WordsOut.append(MyDictionary('what', ['Pronoun', 'Determiner', 'Adverb'], [[' Asking for information specifying something., The thing or things that'], [' Asking for information specifying something., (referring to the whole of an amount) whatever., (in exclamations) how great or remarkable.'], [' Used to indicate an estimate or approximation., To what extent?']]))
    WordsOut.append(MyDictionary('this', ['Pronoun/Determiner', 'Adverb'], [[' Used to identify a specific person or thing close at hand or being indicated or experienced., Referring to a specific thing or situation just mentioned.'], [' To the degree or extent indicated.']]))
    WordsOut.append(MyDictionary('he', ['Pronoun', 'Noun'], [[' Used to refer to a male previously mentioned or easily identified.'], [' A male; a man.']]))
    WordsOut.append(MyDictionary('she', ['Pronoun', 'Noun'], [[' Used to refer to a female previously mentioned or easily identified.'], [' A female; a woman.']]))
    WordsOut.append(MyDictionary('they', ['Pronoun'], [[' Used to refer to someone previously mentioned or easily identified., Used to refer to two or more people or things previously mentioned or easily identified.']]))
    WordsOut.append(MyDictionary('abbot', ['Name'], [[' The cat., Inspired by Ronan saying he wants to "have it".']]))
    WordsOut.append(MyDictionary('binoo', ['Name'], [[' The dog., Inspired by the 2005 animated Canadian TV show "Toopy and Binoo" ']]))
    WordsOut.append(MyDictionary('ronan', ['Name'], [[' A great brother ^-^']]))
    WordsOut.append(MyDictionary('luna', ['Noun'], [[' Luna commonly refers to: the Moon in Latin, Luna (goddess) - the ancient Roman personification of the Moon ']]))
    WordsOut.append(MyDictionary('luna', ['Noun'], [[' Luna commonly refers to: the Moon in Latin, Luna (goddess) - the ancient Roman personification of the Moon ']]))
    WordsOut.append(MyDictionary('akira', ['Film'], [[' Akira is a 1988 Japanese animated post-apocalyptic cyberpunk film directed by Katsuhiro Otomo, produced by Ryōhei Suzuki and Shunzō Katō and written by Otomo and Izo Hashimoto, based on Otomos 1982 manga of the same name.']]))
    WordsOut.append(MyDictionary('minecraft', ['Game'], [[' Minecraft is a sandbox video game developed by Mojang Studios. Created by Markus "Notch" Persson with Java and released as a public alpha for personal computers in 2009 , and officially released in November 2011 with Jens Bergensten taking over development around then. Minecraft has since been ported to various platforms and become the best-selling video game of all time, with 200 million copies sold across all platforms and 126 million monthly active users as of 2020.']]))
    WordsOut.append(MyDictionary('bladerunner', ['Film'], [[' Blade Runner is a 1982 science fiction film directed by Ridley Scott, and written by Hampton Fancher and David Peoples. Starring Harrison Ford Rutger Hauer Sean Young and Edward James Olmos, it is loosely based on Philip K. Dicks novel Do Androids Dream of Electric Sheep? (1968). The film is set in a dystopian future Los Angeles of 2019, in which synthetic humans known as replicants are bio-engineered by the powerful Tyrell Corporation to work at space colonies., When a fugitive group of advanced replicants led by Roy Batty (Hauer) escapes back to Earth, burnt-out cop Rick Deckard (Ford) reluctantly agrees to hunt them down.']]))
    WordsOut.append(MyDictionary('bruh', ['Interjection '], [[' Bruh is an expression of disdain or incredulity said often during bruh moments., It is derived from "brother".']]))
    WordsOut.append(MyDictionary('ghibili', ['Studio'], [['Studio Ghibli Inc. is a Japanese animation film studio headquartered in Koganei Tokyo. The studio is best known for its animated feature films, and has also produced several short films, television commercials, and one television film.']]))
    return WordsOut

def ReadFile(input_file): # purely reads, used on word_file to get current words, used in save_changes, cancel dictionary changes, read colours, read username.

    if input_file == word_file: # file is return separated, this just turns into list
        with open(input_file, 'r') as input_file:
            all_words = [word.rstrip() for word in input_file]

    elif input_file == encouragement:
        with open(input_file, 'r') as input_file:
            all_words = [word.rstrip() for word in input_file.readlines()]       

    else: # file is return separated, remove commas and single quotes
        with open(input_file, 'r') as input_file:
            all_words = [word.rstrip().replace("'", "").replace(",", "") for word in input_file.readlines()]

    input_file.close()

    return all_words # list of all words

def Process(input_words):
    
    if input_words is not None and input_words: # for processing pronouncing results, probably the worst way to do this but 
        output_words = str(input_words)
        output_words = output_words.replace("[", "").replace("]", "").replace("'", "").replace("{", "").replace("}", "").replace("(", "")
        output_words = output_words.replace(", ", "\n")
    else:
        output_words = "Currently Unavailable"

    return output_words

def GetRhymes(input_word):
    
    input_word = input_word.replace(" ", "").lower() # remove space in input so all one word, and also cause typing a space after a word is habit 
    
    try: # try n get result from pronouncing, otherwise empty sets
        set1 = set(pronouncing.search(pronouncing.phones_for_word(input_word)[0])) 
        set2 = set(pronouncing.rhymes(input_word))
    except:
        return 'Nothing Found.'
    if set1 and set2: # find union of kinda rhymes and kinda sounds like, more likely to be good maybe ? unless if one is empty
        return Process(set1.union(set2))
    else:
        return 'Nothing Found.'

def write_out(input_words) : # save every change made to tempfile in case wants to be saved, makes cancelling and saving easier ^-^

    with open(tempfile, 'w') as fo:

        for word in input_words:
            fo.write(word)

        fo.close()

def save_changes(): # transfers stuff in tempfile to current word file :)

    with open(tempfile, 'r') as tempfile_, open(word_file, 'w') as word_file_:

        for word in tempfile_:
            word_file_.writelines(word)

        tempfile_.close() # don't close word_file, trust ReadFile() will handle it 

    return ReadFile(word_file)

def save_time(in_time): # lol its late and im sleepy so this is probably not the best way to do this but it works!
    try: # see if new day, keep track of how much time spent in the quiz
        previoustimes = ReadFile(TimeKeeper)
        currentdate = str(datetime.datetime.now().date())
        if previoustimes[1] != currentdate : # if not same date, start fresh
            timetosave = str(in_time)+'\n'+str(currentdate)
        else: # otherwise sum times
            timetosave = str( float(previoustimes[0]) + float(in_time) ) + '\n' + currentdate

        with open(TimeKeeper, 'w') as fo: # save times
            for beantime in timetosave:
                fo.write(beantime)
            fo.close()
        for ii in range(len(timetosave)): # return up to decimal if there is one
            if timetosave[ii] == 'n' :
                return str(timetosave)[0:ii-1]
            elif timetosave[ii] == '.':
                return str(timetosave)[0:ii]
    except:
        return str(0)

def OxfordDef(word_id, justsyn):

    OxfordDefString = ''
    synonymlist = []
    app_id  = '1b9fe78e'
    app_key  = '9f201d9de36e1e3a33aa19a7f1cd0fec'
    soundURL = False

    try:
        oxfordurl = 'https://od-api.oxforddictionaries.com/api/v2/lemmas/en/' + word_id # find out if derivative of another word
        r = requests.get(oxfordurl, headers = {"app_id": app_id, "app_key": app_key})
        root_term = r.json()['results'][0]['lexicalEntries'][0]['inflectionOf'][0]['text']
    except:
        return False, False

    try:
        oxfordurl = 'https://od-api.oxforddictionaries.com/api/v2/entries/en/' + root_term # use root word 
        r = requests.get(oxfordurl, headers = {"app_id": app_id, "app_key": app_key})
        all_info = r.json()['results']

        if not justsyn:
            for ia in all_info:
                for ib in ia['lexicalEntries']:
                    OxfordDefString += '\n'+ib['lexicalCategory']['text'] 
                    for ic in ib['entries']:
                        for i_d in ic['pronunciations']:
                            if i_d.get('audioFile') is not None:
                                soundURL = i_d.get('audioFile')
                        for i_d in ic['senses']:
                            for i_e in i_d['definitions']:
                                OxfordDefString += '\n\t'+i_e 
                            OxfordDefString += "\n\t eg.) "+i_d['examples'][0]['text'] # one example of one sense of the word
                            if i_d.get('synonyms') is not None:
                                synonymlist.append(i_d.get('synonyms')[0]['text'])
        if justsyn:
            for ia in all_info:
                for ib in ia['lexicalEntries']:
                    for ic in ib['entries']:
                        for i_d in ic['pronunciations']:
                            if i_d.get('audioFile') is not None:
                                soundURL = i_d.get('audioFile')
                        for i_d in ic['senses']:
                            if i_d.get('synonyms') is not None:
                                synonymlist.append(i_d.get('synonyms')[0]['text'])
    except:
        return False, False
    try:
        if not justsyn:
            OxfordDefString += "\n\nCommon Phrases:\n"
            OxfordDefString += +all_info[0]['lexicalEntries'][0]['phrases'][0]['text']+'\n'
            OxfordDefString += +all_info[0]['lexicalEntries'][0]['phrases'][0]['text']+'\n\n'
    except:
        pass
    try:
        if justsyn:
            OxfordDefString += "Synonyms:\n"
        else:
            OxfordDefString += "\nSynonyms:\n"
        for x in range(len(synonymlist)-1):
            OxfordDefString += synonymlist[x]+'\n'
        OxfordDefString += synonymlist[len(synonymlist)-1]
    except:
        pass
    
    return OxfordDefString, soundURL
    
def GetDef(input_word, justsyn): # find definition of a word
    
    my_word = False
    ox_word = False
    soundURL = False
    valid_word = True

    if not input_word : # if somehow passed NoneType *shrug*
        valid_word = False
        definition = 'No definition available'

    if not valid_word: # break here 
        return definition

    input_word = input_word.replace(" ", "").lower() # remove space in input cause typing a space after a word is habit, lowercase

    try: # my own dictionary has preference, also some are words known not to be in PyDictionary that were needed 
        for word in my_dict:
            if input_word == word.name:
                my_word = True
                definition = str(word.meaning).replace("{", "").replace("}", "").replace("[", "\n\t").replace("], ", "\n").replace("'", "").replace(",", "\n\t").replace("]", "")
                break
    except :
        definition = 'No definition available.'  

    try:
        if not my_word :
            definition, soundURL = OxfordDef(input_word, justsyn)    
            if definition != False:
                ox_word = True
    except:
        definition = 'No definition available.'

    try: # then check PyDictionary ,  requires internet so much slower
        if not my_word and not ox_word :#and enchant.Dict("en_US").check(input_word):
            definition = str(PyDictionary.PyDictionary().meaning(input_word)).replace("{", "").replace("}", "").replace("[", "\n\t").replace("], ", "\n").replace("'", "").replace(",", "\n\t").replace("]", "").replace("(", "")
        #elif not my_word and not ox_word and not enchant.Dict("en_US").check(input_word):
        #    definition = 'No definition available - check spelling?'
        if definition in (None, 'None'):
            definition = 'No definition available.'
    except:
        definition = 'No definition available.' 

    return definition, soundURL

def LoadWords(words): # load all word defs being quized on before starting so smoothe like butter once in

    ii = 0
    definitions = [] # list hold definitions for each word in quiz
    quizsounds = []
    textdisplay = 'Loading Words' # init textdisplay so easier to change in loop
    continuwu_quiz = True 

    layout_progress = [[sg.Text(textdisplay, size=(22, 2), font=('Comic Sans Ms', 10), key='progress_key')],[sg.ProgressBar(len(words)-1, orientation='h', size=(20, 20), key='progbar')],[sg.Button('', image_filename=CANCEL_BUTTON, button_color=('CadetBlue3',sg.theme_background_color()), border_width=0, key='load_cancel_key')]]
    window_progress = sg.Window('Quiz', layout_progress, icon=icon)

    for ii in range(len(words)-1): # sick progress metre
        
        event_progress, values_progress = window_progress.read(timeout=0)

        if event_progress in (None, 'load_cancel_key') :
            continuwu_quiz = False # need to be able to kill quiz if hit cancel or exit
            break
        textdisplay = 'Loading Definitions (%i/%i)'%(ii+1,len(words)-1)
        window_progress['progbar'].update_bar(ii)
        window_progress['progress_key'].update(textdisplay)
        current_def, current_sound = GetDef(words[ii], True)
        definitions.append(current_def)
        quizsounds.append(current_sound)

    definitions.append("Great Job!") # need renforcement *thumbs up*
    quizsounds.append(False)
    window_progress.close(); del window_progress
    return definitions, quizsounds, continuwu_quiz

def quiz(current_quiz_words, nwords, definitions, quizsounds, time_in_quiz_thus_far): # 1/4 MAIN FOUR FUNCTIONS

    continuwu_quiz = True
    number_list = [str(s)+"." for s in list(range(1, nwords+1))]
    do_again = False
    iquiz = 0

    if definitions: # shuffle order of words if function called from itself

        starttime = time.perf_counter()
        ConsistantShuffle = list(zip(current_quiz_words, definitions, quizsounds))
        rd.shuffle(ConsistantShuffle)
        current_quiz_words, definitions, quizsounds = zip(*ConsistantShuffle)
        current_quiz_words, definitions, quizsounds = list(current_quiz_words), list(definitions), list(quizsounds)
        definitions.append("Great Job!")
        quizsounds.append(False)

    current_quiz_words.append("All Done!")

    layout_quiz   = [[sg.Text(f'Quizing you on {nwords} Sight Words!', font=("Comic Sans MS", 12), size=(60,1))]]
    layout_quiz  += [[sg.Button('', image_filename=BACK_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='quiz_done_key')]]

    if not definitions: # if called from main window, load definitions, start time from here
        definitions, quizsounds, continuwu_quiz = LoadWords(current_quiz_words)
        starttime = time.perf_counter()

    if continuwu_quiz == False:
        return 0 # quit if cancelled during loading definitions, 0 minutes in quiz

    internal_quiz  = [[sg.Text(f'{number_list[iquiz]}', size=(2, 1), font=('Times', 80), justification='c', key='numb_key', visible=True), sg.Text(f'{current_quiz_words[iquiz]}', size=(10, 1), enable_events=True, font=('Comic Sans MS', 80), justification='c', key='word_key', tooltip=definitions[iquiz])]]  
    middle_quiz    = [[sg.Frame("", internal_quiz)]]
    layout_quiz_load = [[sg.ProgressBar(len(current_quiz_words)-2, orientation='h', size=(63,5),  key='quiz_prog_key', visible=True)]]
    layout_quiz_bottom = [[sg.Frame("", middle_quiz, background_color=rd.choice(DARKCOLOURS), element_justification='c')]]
    layout_quiz_button = [[sg.Button('', image_filename=NEXT_WORD_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='next_word_button_key'), sg.Button('', enable_events=True, image_filename=SPEECH_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='speech_key')]]
    layout_quiz_again = [[sg.Button('', image_filename=AGAIN_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='again_button_key', visible=False)]]
    layout_quiz += [[sg.Column(layout_quiz_load, justification='c'), sg.Column(layout_quiz_bottom, justification='c'), sg.Column(layout_quiz_button, justification='c'), sg.Column(layout_quiz_again, justification='c')]]
    window_quiz = sg.Window('Sight Words', layout_quiz, resizable=True, finalize = True, icon = icon)
    window_quiz.Maximize()

    while continuwu_quiz == True: 

        event_quiz, values_quiz = window_quiz.read()

        if event_quiz in (None, 'quiz_done_key') :
            continuwu_quiz = False

        elif event_quiz == 'speech_key' and iquiz < nwords : # NOT HAPPY W THIS PART, could't get it to only play once at a time / not accept more clicks or not add to queue when playing :/
            try:
                if quizsounds[iquiz] != False:
                    playsound.playsound(quizsounds[iquiz])
                else:
                    speech.say(current_quiz_words[iquiz])
                    speech.runAndWait()
                    speech.stop()
            except:
                sg.popup("Could Not Sound Out Word.", title='', icon = icon, font=("Comic Sans MS", 10))

        elif event_quiz == 'speech_key' and iquiz == nwords : # speech thing still messed here
            try:
                speech.stop()
                speech.say(rd.choice(encouragementsounds))
                speech.runAndWait()
            except:
                sg.popup("Could Not Sound Out Word.", title='', icon = icon, font=("Comic Sans MS", 10))

        elif event_quiz == 'next_word_button_key' and iquiz < nwords-1: # next word, update number, word, and def
            iquiz += 1
            window_quiz['quiz_prog_key'].update_bar(iquiz)
            window_quiz['numb_key'].update(number_list[iquiz])
            window_quiz['word_key'].update(current_quiz_words[iquiz])
            window_quiz['word_key'].set_tooltip(definitions[iquiz])

        elif event_quiz == 'next_word_button_key' and iquiz == nwords-1 : # got to last word, good job!
            iquiz += 1
            definitions.append("Great Job!")
            window_quiz['word_key'].set_tooltip(definitions[iquiz])
            window_quiz['numb_key'].update(visible=False)
            window_quiz['word_key'].update(current_quiz_words[iquiz])
            window_quiz['next_word_button_key'].update(visible=False)
            window_quiz['again_button_key'].update(visible=True)
            window_quiz['quiz_prog_key'].update(visible=False)
        
        elif event_quiz == 'again_button_key' : # repeat same words, shuffle diff order
            do_again = True
            continuwu_quiz = False
        
    window_quiz.close(); del window_quiz

    if do_again == True:
        try:
            current_quiz_words.pop() # remove congratulations, will be added back in after shuffle
            definitions.pop()
            quizsounds.pop()
            return quiz(current_quiz_words, nwords, definitions, quizsounds, (time.perf_counter() - starttime)/60) # again !
        except:
            sg.popup("There Was An Error Repeating These Words.", title='', icon = icon, font=("Comic Sans MS", 10))
    else:
        return (time.perf_counter() - starttime)/60  # minutes in quiz
        #return int(time.perf_counter() - starttime) + time_in_quiz_thus_far # seconds in quiz
        
def dictionary(all_words): # 2/4 MAIN FOUR FUNCTIONS

    continuwu_dict = True
    layout_dict = [[sg.Text('Edit this list to choose words to be quized on!', font=("Comic Sans MS", 12))]]
    layout_dict += [[sg.Multiline(Process(all_words), enter_submits=True, change_submits=True, enable_events=True, size=(60, 30), key='dict_key')], [sg.Button('', image_filename=BACK_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='dict_done_key'), sg.Button('', image_filename=SAVE_BUTTON, button_color=('CadetBlue3','azure2'), border_width=0, key='save_key'), sg.Button('', image_filename=CANCEL_BUTTON, button_color=('CadetBlue3',sg.theme_background_color()), border_width=0, key='cancel_key')]] 
    window_dict = sg.Window('Edit Current Words', layout_dict, grab_anywhere = False, resizable=True, finalize = True, icon = icon, text_justification='l', element_justification='c')
    
    while continuwu_dict == True:

        event_dict, values_dict = window_dict.read()

        if event_dict in (None, 'dict_done_key') : # quit
            continuwu_dict = False

        elif event_dict == 'dict_key': # save to tempfile if any changes
            try:
                write_out(values_dict.values())
            except:
                sg.popup("There Was An Error Making Your Changes.", title='', icon = icon, font=("Comic Sans MS", 10))

        elif event_dict == 'save_key' : # save tempfile to main file
            try:
                all_words = save_changes()
            except:
                sg.popup("There Was An Error Saving Your Changes.", title='', icon = icon, font=("Comic Sans MS", 10))
        
        elif event_dict == 'cancel_key': # removes all changes since last save, refreshes page ^-^
            try:
                all_words = ReadFile(word_file)
                window_dict['dict_key'].update(Process(all_words))
            except:
                sg.popup("There Was An Error Canceling Your Changes.", title='', icon = icon, font=("Comic Sans MS", 10))
    
    window_dict.close(); del window_dict

def lookup(): # 3/4 MAIN FUNCTIONS

    continuwu_lookup = True
    current_word = ' '
    current_def = ' '
    current_rhymes = ' '

    layout_lookup = [[sg.Button('', image_filename=BACK_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='lookup_done_key')]]
    layout_lookup += [[sg.InputText(default_text='(Search Here)', font=("Comic Sans MS", 10), do_not_clear=False, key='lookup_key'), sg.Button(button_text='', image_filename=SEARCH_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, bind_return_key=True, key='lookup_search_key')]]
    layout_lookup += [[sg.Text(current_word, size=(30, 2), font=("Comic Sans MS", 14), text_color=rd.choice(DARKCOLOURS), key='current_word_key'), sg.Button('', image_filename=SPEECH_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='lookup_speech_key', visible=False)]]
    
    layout_lookup_scroll_1 = [[sg.Text('Definition:', font=("Comic Sans MS Bold", 12))]]
    layout_lookup_scroll_1 += [[sg.Text(current_def, size=(200, 500), font=("Comic Sans MS", 12), key='definition_key')]]

    layout_lookup_scroll_2 = [[sg.Text('Sounds Like:', font=("Comic Sans MS Bold", 12))]]
    layout_lookup_scroll_2 += [[sg.Text(current_rhymes, size=(200, 20), font=("Comic Sans MS", 12), key='rhymes_key')]]

    layout_lookup_scroll = layout_lookup_scroll_1 + layout_lookup_scroll_2

    layout_lookup += [[sg.Column(layout_lookup_scroll, size=(1500, 570), scrollable=True, vertical_scroll_only=True, key='scroll_column_key', visible=False)]]
    
    window_lookup = sg.Window('Find A Word', layout_lookup, grab_anywhere = False, resizable=True, finalize = True, icon = icon, text_justification='l', element_justification='l')
    window_lookup.Maximize()

    while continuwu_lookup:

        event_lookup, values_lookup = window_lookup.read() 

        if event_lookup in (None, 'lookup_done_key') : # quit 
            continuwu_lookup = False
        
        elif event_lookup == 'lookup_search_key' and values_lookup is not None and values_lookup['lookup_key'] not in (None, ''): # if valid search

            current_word = values_lookup['lookup_key'] # get required info
            current_def, current_sound = GetDef(current_word, False)

            current_rhymes = GetRhymes(current_word)

            window_lookup['current_word_key'].set_size((len(current_word), 2)) # display searched word
            window_lookup['current_word_key'].update(current_word)
            window_lookup['current_word_key'].Update()
            
            window_lookup['definition_key'].set_size((200,current_def.count('\n')+2)) # display definition in scrollable
            window_lookup['definition_key'].update(current_def)
            window_lookup['definition_key'].Update()
            
            window_lookup['rhymes_key'].set_size((200,current_rhymes.count('\n')+2)) # update sounds like
            window_lookup['rhymes_key'].update(current_rhymes)
            window_lookup['rhymes_key'].Update()
            
            window_lookup['scroll_column_key'].update(visible=True) # make visible the scroll area
            window_lookup['lookup_speech_key'].update(visible=True) # make available the TTS
            
        elif event_lookup == 'lookup_speech_key': # speech still messed up :/
            try:
                if current_sound != False:
                    playsound.playsound(current_sound)
                else:
                    speech.say(current_word)
                    speech.runAndWait()
                    speech.stop()
            except:
                sg.popup("Could Not Sound Out Word.", title='', icon = icon, font=("Comic Sans MS", 10))
        
    window_lookup.close(); del window_lookup

def numquiz(number_list, nnums, time_in_quiz_thus_far): # 4/4 MAIN FOUR FUNCTIONS

    if not number_list: # if called from main window, load definitions, start time from here
        number_list = [str(s) for s in list(range(1, 101))]
        number_list = rd.sample(number_list, nnums)
    
    starttime = time.perf_counter()
    rd.shuffle(number_list)
    number_list.append("All Done!")
    inum = 0
    do_again = False
    continuwu_num = True

    layout_num   = [[sg.Text(f'Quizing you on {nnums} Numbers!', font=("Comic Sans MS", 12), size=(60,1))]]
    layout_num  += [[sg.Button('', image_filename=BACK_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='num_done_key')]]
    
    internal_num  = [[sg.Text(number_list[inum], size=(9, 1), font=('Comic Sans MS', 80), justification='c', key='numb_key', visible=True)]]  
    middle_num    = [[sg.Frame("", internal_num)]]
    
    layout_num_load = [[sg.ProgressBar(len(number_list)-2, orientation='h', size=(60,5),  key='num_prog_key', visible=True)]]
    layout_num_bottom = [[sg.Frame('', middle_num, background_color=rd.choice(DARKCOLOURS), element_justification='c')]]
    layout_num_button = [[sg.Button('', image_filename=NEXT_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='next_num_button_key'), sg.Button('', enable_events=True, image_filename=SPEECH_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='num_speech_key')]]
    layout_num_again = [[sg.Button('', image_filename=AGAIN_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='again_num_button_key', visible=False)]]
    layout_num += [[sg.Column(layout_num_load, justification='c'), sg.Column(layout_num_bottom, justification='c'), sg.Column(layout_num_button, justification='c'), sg.Column(layout_num_again, justification='c')]]
    
    window_num = sg.Window('Numbers', layout_num, resizable=True, finalize = True, icon = icon)
    window_num.Maximize()

    while continuwu_num == True: 

        event_num, values_num = window_num.read()

        if event_num in (None, 'num_done_key') :
            continuwu_num = False

        elif event_num == 'num_speech_key' and inum < nnums : # NOT HAPPY W THIS PART, could't get it to only play once at a time / not accept more clicks or not add to queue when playing :/
            try:
                speech.say(number_list[inum])
                speech.runAndWait()
                speech.stop()
            except:
                sg.popup("Could Not Sound Out Number.", title='', icon = icon, font=("Comic Sans MS", 10))

        elif event_num == 'num_speech_key' and inum == nnums : # speech thing still messed here
            try:
                speech.stop()
                speech.say(rd.choice(encouragementsounds))
                speech.runAndWait()
            except:
                sg.popup("Could Not Sound Out Word.", title='', icon = icon, font=("Comic Sans MS", 10))

        elif event_num == 'next_num_button_key' and inum < nnums-1: # next number, update number
            inum += 1
            window_num['num_prog_key'].update_bar(inum)
            window_num['numb_key'].update(number_list[inum])

        elif event_num == 'next_num_button_key' and inum == nnums-1 : # got to last number, great job!
            inum += 1
            window_num['numb_key'].update(number_list[inum])
            window_num['next_num_button_key'].update(visible=False)
            window_num['again_num_button_key'].update(visible=True)
            window_num['num_prog_key'].update(visible=False)
        
        elif event_num == 'again_num_button_key' : # repeat same nums, shuffle diff order
            do_again = True
            continuwu_num = False
        
    window_num.close(); del window_num

    if do_again == True:
        try:
            number_list.pop() # remove congratulations, will be added back in after shuffle
            return numquiz(number_list, nnums, (time.perf_counter() - starttime)/60) # again !
        except:
            sg.popup("There Was An Error Repeating These Numbers.", title='', icon = icon, font=("Comic Sans MS", 10))
    else:
        return (time.perf_counter() - starttime)/60  # minutes in quiz

# ==================================== # done function defs! these are inits for main window

my_dict = MyDictionaryF()
DARKCOLOURS = ReadFile(colour_file) # colours to be chosen from for text and quiz frame! have to be dark enough to read on white background
all_words = ReadFile(word_file) # read in words to be quized on
encouragementtext = ReadFile(encouragement)
encouragementsounds = ReadFile(encouragementverbal)

try:    
    MyName = ReadFile(MyNameFile)[0] # read in username
except:
    MyName = 'My' # ive been in here too long, I thought this 'My' was a horse picture

speech = pyttsx3.init() # init the TTS speech here, tried doing other ways but didn't have better results :/
speech.setProperty('rate', 100)
speech.setProperty('volume',1.0)
speech.setProperty('voice', speech.getProperty('voices') [1].id)

# ====================================
    
sg.change_look_and_feel('LightGrey1')

q_layout = [[sg.Button("", image_filename=START_BUTTON, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, bind_return_key=True, key='quiz')], [sg.Combo(['10', '20', '30', '40', '50', '60', '70', len(all_words)], default_value='10', enable_events=True, key='how_many_words_key'), sg.Text("words ")], [sg.Text('Quiz Me On Current Words!')]]
d_layout = [[sg.Button('', image_filename=OPEN_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='dict_open_key')], [sg.Text("Words To Quiz Me On!")]]
l_layout = [[sg.Button('', image_filename=LOOKUP_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='lookup_open_key')], [sg.Text("Find a Word!")]]
n_layout = [[sg.Button('', image_filename=START_BUTTON, button_color=('CadetBlue3', sg.theme_background_color()), border_width=0, key='number_open_key')], [sg.Combo(['10', '20', '30', '40', '50'], default_value='10', enable_events=True, key='how_many_numbers_key'), sg.Text("numbers ")], [sg.Text("Quiz Me On Numbers!")]]

TimeDisplay = ' '
col_1 = sg.Frame("Quiz", q_layout, title_color=rd.choice(DARKCOLOURS), font=("Comic Sans MS", 12), element_justification='c')
col_2 = sg.Frame("Current Words", d_layout, title_color=rd.choice(DARKCOLOURS), font=("Comic Sans MS", 12), element_justification='c')
col_3 = sg.Frame("Search", l_layout, title_color=rd.choice(DARKCOLOURS), font=("Comic Sans MS", 12), element_justification='c')
col_4 = sg.Frame("Numbers", n_layout, title_color=rd.choice(DARKCOLOURS), font=("Comic Sans MS", 12), element_justification='c')
col_5 = sg.Text('', size=(90,3), justification='c')
col_6 = sg.Text(TimeDisplay, font=('Comic Sans MS', 9), size=(90,3), key='time_key', justification='c')

if MyName != 'My': # to properly display username (or lack thereof)
    Username = MyName+"'s Sight Words!"
else:
    Username = MyName+" Sight Words!"

layout_main = [[sg.Image(filename = ABC, background_color=sg.theme_background_color(), size=(40, 40)), sg.Text(Username, font=('Comic Sans MS Bold', 14), justification='center', size=(40, 2)), sg.Image(filename = ABC, background_color=sg.theme_background_color(), size=(40, 40))]]
layout_main += [[col_1, col_2, col_3, col_4]]
layout_main += [[col_5], [col_6]]

window_main = sg.Window('Sight Words', layout_main,  resizable=True, icon = icon, element_justification='c')

continuwu_main = True # start main loop now! wow, how exiting!

while continuwu_main == True:
    
    event_main, values_main = window_main.read()

    if values_main is not None and values_main['how_many_words_key'] is not None:
        nwords = values_main['how_many_words_key'] # how many words to quiz me on, can't start without selecting number of words
    
    if values_main is not None and values_main['how_many_numbers_key'] is not None:
        nnums = values_main['how_many_numbers_key']
    
    if event_main is None : # exit program with X
        continuwu_main = False
        
    elif event_main == 'quiz' : # start quiz, sorry this is so nested
        try:
            nwords = int(nwords) # make sure valid input (positive int), nwords is number of words to quiz on
            if nwords > 0: 
                valid_n_words = True
            else:
                valid_n_words = False
        except:
            sg.popup("Invalid Number of Words Chosen.", title='', icon = icon, font=("Comic Sans MS", 10))
            valid_n_words = False

        if valid_n_words :
            try:
                if nwords > len(all_words): # if try and quiz on more words than possible, just round down to max
                    nwords = len(all_words)
                current_quiz_words = rd.sample(all_words, nwords) # random sample of nwords from all_words
                CurrentRunTime = quiz(current_quiz_words, nwords, [], [], 0) # start quiz
                DisplayTime = save_time(CurrentRunTime)
                if int(DisplayTime) == 1 :
                    TimeDisplay = 'You spent '+DisplayTime+' minute quizing today! '+rd.choice(encouragementtext)
                    window_main['time_key'].update(TimeDisplay)
                elif int(DisplayTime) > 1 :
                    TimeDisplay = 'You spent '+DisplayTime+' minutes quizing today! '+rd.choice(encouragementtext) # random from list of compliments?
                    window_main['time_key'].update(TimeDisplay)
            except:
                sg.popup("There Was An Error In The Quiz.", title='', icon = icon) # or exiting old quiz !
        
    elif event_main == 'dict_open_key': # start dictionary of current words
        try:
            dictionary(all_words)
        except:
            sg.popup("There Was An Error In The Dictionary.", title='', icon = icon, font=("Comic Sans MS", 10))
    
    elif event_main == 'lookup_open_key': # start word searcher
        try:
            lookup()
        except:
            sg.popup("There Was An Error In The Word Searcher.", title='', icon = icon, font=("Comic Sans MS", 10))

    elif event_main == 'number_open_key':
        try:
            nnums = int(nnums) # make sure valid input (positive int), nnums is number of numbers to quiz on
            if nnums > 0: 
                valid_n_nums = True
            else:
                valid_n_nums = False
        except:
            sg.popup("Invalid Number of Numbers Chosen.", title='', icon = icon, font=("Comic Sans MS", 10))
            valid_n_nums = False

        if valid_n_nums:
            try:
                CurrentRunTime = numquiz([], nnums, 0)
                DisplayTime = save_time(CurrentRunTime)
                if int(DisplayTime) == 1 :
                    TimeDisplay = 'You spent '+DisplayTime+' minute quizing today! Great Work!'
                    window_main['time_key'].update(TimeDisplay)
                elif int(DisplayTime) > 1 :
                    TimeDisplay = 'You spent '+DisplayTime+' minutes quizing today! Great Work!' # random from list of compliments?
                    window_main['time_key'].update(TimeDisplay)
            except:
                sg.popup("There Was An Error In The Number Quiz.", title='', icon = icon, font=("Comic Sans MS", 10))

window_main.close(); del window_main # done !

