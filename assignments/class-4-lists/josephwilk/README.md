# Big List

Scrapping http://accent.gmu.edu a research project exploring pronunciation.
I created a list of 2,842 audio files of unique voices along with metadata on age, birth place, native language, age, sex, age of english onset, learning method, residence, length of english residence.

Every audio file is saying exactly the same thing. Using beat detection I sliced the audio and created a collage of every single voice saying the word “Train station” and “Please”.

https://w.soundcloud.com/player/?url=https%3A%2F%2Fsoundcloud.com%2Fjosephwilk%2Ftrain-station-1&autoplay=false

https://soundcloud.com/josephwilk/train-station-1

https://w.soundcloud.com/player/?url=https%3A%2F%2Fsoundcloud.com%2Fjosephwilk%2Fplease&autoplay=false

https://soundcloud.com/josephwilk/please


All the languages of native speakers:

aceh, afrikaans, agni, agny, akan, albanian, amazigh, american sign language, amharic, ancient greek, antigua and barbuda creole english, anyin, appolo, arabic, aramaic, armenian, aromanian, ashanti, asl, azerbaijani, azerbaijani, south, azeri turk, babur, bafang, baga, bahasa indonesia, bai, balant, balanta ganja, bamanankan, bambara, bamun, banganthe, bangla, baoule, bari, basque, bassa, bavarian, belarusan, bengali, bikol, bisayan, bislama, bosnian, bulgarian, burmese, cameroon creole english, cantonese, carolinian, castellano, catalan, cebuano, chaam, chagga, chaldean, chaldean neo aramaic, chamorro, charapa-spanish, chichewa, chin, mizo, chinese, chittagonian, chuukese, classical greek, cotocoli, creole, creole french, crioulo, croatian, czech, danish, dari, darija, dholuo, dinka, djola, dutch, eastern farsi, ebira, edo, efik, english, esperanto, estonian, ewe, fang, fanti, faroese, farsi, fataluku, fefe, fijian, filipino, finnish, flemish, french, frisian, fulani, fulfulde adamawa, ga, gaelic, gamugna, gan, ganda, garhwali, garifuna, gedeo, georgian, german, giriama, grebo, greek, greek, ancient, gujarati, gurung, gusii, hadiyya, hainanese, haitian creole french, hakka, harari, haruku, hausa, hawai'i creole english, hawai'ian pidgin, hawu, hebrew, hijazi, hiligaynon, hindi, hindi-urdu, hindko, hmong, hmong daw, hokkien, home sign, hungarian, ibibio, icelandic, ife, igbo, ikalanga, ilocano, ilonggo, indonesian, interlingua, irish, irish gaelic, italian, jamaican creole english, japanese, japanese sign language, javanese, jola, kabye, kabyle, kalanga, kamba, kambaata, kamtok, kannada, kanuri, kapampangan, kazakh, kembata, khalkha mongol, khasonke, khmer, kiambu, kiha, kikongo, kikuyu, kilba, kinyarwanda, kirghiz, kirundi, kisii, kiswahili, klao, koine greek, kongo, konkani, korean, kresh, krio, kru, kuanua, kupang, kurdi, kurdish, kurmanji, kutchi, kyrgyz, lamaholot, lamotrekese, lao, latin, latvian, liberian english, liberian pidgin english, lingala, lithuanian, losso, low saxon, luba-kasai, luganda, luo, luxembourgeois, maasai, macedonian, malagasy, malay, malayalam, maltese, mancagne, mandarin, mandingo, mandingue, mandinka, manem, maninkakan, mankanya, manual communication, maori, marathi, marwari, masbatenyo, mauritian, mbala, mende, min, min dong, min nan, mina, miskito, mizo, moba, mongolian, montenegrin, moore, morisyen, mortlockese, nagi, najdi, nama, nandi, naxi, ndebele, nepali, newar, newari, ngemba, nicaragua creole english, nobiin, northern sotho, norwegian, nuer, nyanja, nyankore, oku, old english, omani arabic, oriya, oromo, ossetic, pahari, pali, panjabi, papiamentu, pashto, patois, persian, pidgin, pidgin english, piemontese, pijin, pohnpeian, polish, poonchi, portuguese, potwari, pulaar, punjabi, quechua, rajasthani, romanian, rotuman, rundi, russian, rwanda, sa'a, sanskrit, saraiki, sardinian, sarua, satawalese, schwyzerdütsch, sepedi, serbian, serer, serer sine, sesotho, setswana, shan, sherpa, shilluk, shona, sicilian, sign language, sikka, sindhi, sinhala, sinhalese, slovak, slovenian, soga, solomon islands pidgin, somali, songhay, sotho, spanish, sunda, sundanese, susu, swahili, swedish, swiss german, sylheti, synthesized, tachelhit, tagalog, taishan, taiwanese, tajiki, tamajeq, tamazight, tamil, tangale, tatar, telugu, temne, teochew, tetum, tetun-dili, thai, tibetan, tigre, tigrigna, tok pisin, tongan, tshiluba, tswana, tulu, tumbuka, turkish, turkmen, twi, ukrainian, ulithian, ulster scots, urdu, uyghur, uzbek, vietnamese, visayan, vlaams, voro, wali, welsh, woleaian, wolof, wu, xasonga, xiang, yakut, yao, yapese, yiddish, yoruba, yue, yupik, zarma, zulu


## Example Metadata:

    {"age": "33", "age of english onset": "10", "birth place": "drammen, norway (map)", "english learning method": "academic", "english residence": "usa", "file": "data/norwegian1.mp3", "language": "norwegian1,", "length of english residence": "0.3 years", "native language": "norwegian", "other language(s)": "french", "sample": "http://chnm.gmu.edu/accent/soundtracks/norwegian1.mp3", "sex": "female"}
    {"age": "55", "age of english onset": "12", "birth place": "oslo, norway (map)", "english learning method": "academic", "english residence": "usa", "file": "data/norwegian2.mp3", "language": "norwegian2,", "length of english residence": "32 years", "native language": "norwegian", "other language(s)": "french german", "sample": "http://chnm.gmu.edu/accent/soundtracks/norwegian2.mp3", "sex": "female"}
    {"age": "19", "age of english onset": "5", "birth place": "volda, norway (map)", "english learning method": "naturalistic", "english residence": "usa", "file": "data/norwegian3.mp3", "language": "norwegian3,", "length of english residence": "0.8 years", "native language": "norwegian", "other language(s)": "swedish danish german", "sample": "http://chnm.gmu.edu/accent/soundtracks/norwegian3.mp3", "sex": "male"}

## Example Sample files:


![](https://paper-attachments.dropbox.com/s_64F1D0DC49ED8FBE10B687D33334D88DAA503100D5FC138A549A250CADE4CA2F_1554890881566_image.png)


## Python Code:

https://gist.github.com/josephwilk/7c2f0750ee05342a63e480298ee57bb7


https://gist.github.com/josephwilk/7c2f0750ee05342a63e480298ee57bb7

Audio processing was done in sox and aubio on the command line.
