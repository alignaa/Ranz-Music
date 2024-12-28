#
# Copyright (C) 2024 by AnonymousX888@Github, < https://github.com/AnonymousX888 >.
#
# This file is part of < https://github.com/hakutakaid/Music-Indo.git > project,
# and is released under the MIT License.
# Please see < https://github.com/hakutakaid/Music-Indo.git/blob/master/LICENSE >
#
# All rights reserved

import os
import sys
from typing import List

import yaml

languages = {}
commands = {}

languages_present = {}


def get_command(value: str) -> List:
    return commands["command"][value]


def get_string(lang: str):
    return languages.get(lang, languages["id"])


for filename in os.listdir(r"./strings"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        commands[language_name] = yaml.safe_load(
            open(r"./strings/" + filename, encoding="utf8")
        )


for filename in os.listdir(r"./strings"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        commands[language_name] = yaml.safe_load(
            open(r"./strings/" + filename, encoding="utf8")
        )

for filename in os.listdir(r"./strings/langs/"):
    if "id" not in languages:
        languages["id"] = yaml.safe_load(
            open(r"./strings/langs/id.yml", encoding="utf8")
        )
        languages_present["id"] = languages["id"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "id":
            continue  # Lewati karena sudah dimuat sebagai default
        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        # Tambahkan kunci yang hilang dari bahasa default (id)
        for item in languages["id"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["id"][item]
    try:
        languages_present[language_name] = languages[language_name]["name"]
    except:
        print(
            "There is some issue with the language file inside bot. Please report it to the TeamYukki at @YukkiSupport on Telegram"
        )
        sys.exit()
