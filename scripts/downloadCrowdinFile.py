# Copyright (C) 2025 NV Cyrille Bougot
# This file is covered by the GNU General Public License.

import sys
import os
import l10nUtil

token = sys.argv[1]
lang = sys.argv[2]
file = sys.argv[3]

l10nUtil.fetchCrowdinAuthToken = lambda: token

if not os.path.isdir(lang):
	os.mkdir(lang)

localFilePath = os.path.join(lang, file)
l10nUtil.downloadTranslationFile(file, localFilePath, lang)
if file.endswith(".xliff"):
	l10nUtil.preprocessXliff(localFilePath, localFilePath)