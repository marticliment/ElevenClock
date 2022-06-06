
import lang_de, lang_fr, lang_ca, lang_es, lang_ru, lang_en, lang_tr, lang_pl, lang_it, lang_nl, lang_nb, lang_nn, lang_ko, lang_vi, lang_el
import lang_zh_CN, lang_pt_PT, lang_pt_BR, lang_ja, lang_fi, lang_id, lang_sr, lang_lt, lang_sv, lang_ua, lang_da, lang_lv, lang_hu, lang_sk
import lang_he, lang_cs, lang_ar, lang_th, lang_zh_TW

lang = None

languages = {
    "ar":    lang_ar,
    "ca":    lang_ca,
    "cs":    lang_cs,    
    "da":    lang_da,
    "de":    lang_de,
    "el":    lang_el,
    "en":    lang_en,
    "es":    lang_es,
    "fi":    lang_fi,
    "he":    lang_he,
    "fr":    lang_fr,
    "hu":    lang_hu,
    "id":    lang_id,
    "it":    lang_it,
    "ja":    lang_ja,
    "ko":    lang_ko,
    "lt":    lang_lt,
    "lv":    lang_lv,
    "nb":    lang_nb,
    "nl":    lang_nl,
    "nn":    lang_nn,
    "pl":    lang_pl,
    "pt_PT": lang_pt_PT,
    "pt_BR": lang_pt_BR,
    "ru":    lang_ru,
    "sk":    lang_sk,
    "sr":    lang_sr,
    "sv":    lang_sv,
    "th":    lang_th,
    "tr":    lang_tr,
    "ua":    lang_ua,
    "vi":    lang_vi,
    "zh_TW": lang_zh_TW,
    "zh_CN": lang_zh_CN,
}

import json

for lng in languages.keys():
    contents = languages[lng].lang    
    with open(f"lang_{lng}.json", "w") as outfile:
        json.dump(contents, outfile)
