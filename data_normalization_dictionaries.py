clean_up_regexes = {
    'extras': [r'\[s\]', ''],
    'parenthesis': [r'[\(\)]', ' '],
    'currencyUnits': [r'((\d+)\s?/-|\brs\.?\s?(\d+)?|(\d+)?\s?mrp|$\s?(\d+))?', ''],
    'apostrophes': [r'[`\'\"]', ''],
    'packaging': [r'\b\d+\*\d+tab\b', ''],
    'specialChars': [r'(\d\.\d)|[^a-z0-9+%]', ' \\1'],
    'extraPlus': [r'\++', ' plus '],
    'percentage': [r'%', ' % '],
    'bgCode': [r'bg\s?(\d+)', 'bg\\1'],
    'tynorTyro': [
        r'(\btynor\b)(.*?)(\btyro\b)(.*)(\bband\b)(.*)(\bsilver|blue|green|red|yellow\b)(.*)(\b\d\.?\d+)(kgf)?',
        '\\1 \\3 \\5 \\7 \\9'],
    'tynorCervical': [
        r'(\btynor\b)(.*?)(\bcervical\b)(.*)(\b(?:support)\b)(.*)(\b(?:l|m|s|xxl|xl|xs)\b)(.*)',
        '\\1 \\3 \\5 \\7'],
    'tynorMedical': [
        r'(\btynor\b)\s(\bmedical\b)(.*)(\b(?:knee|thigh)\b)(.*)(\b(?:l|m|s|xxl|xl|xs)\b)(.*)',
        '\\1 \\2 \\4 \\6'],
    'tynorPouch': [
        r'(\btynor\b)(.*?)(\bpouch\b)(.*)(\burbane|baggy|tropical\b)(.*)(\b(?:ch|l|m|s|xxl|xl|xs)\b)(.*)',
        '\\1 \\3 \\5 \\7'],
    'tynorHeating': [r'(\btynor\b)(.*?)(\bortho\b)(.*)(\buniversal\b)(.*)', '\\1 \\3 \\5'],
    'tynorElastic': [r'(\btynor\b)(.*?)(\belastic\b)(.*)(\blf|rt\b)(.*)(\b(?:l|m|s|xxl|xl|xs)\b)(.*)',
                     '\\1 \\3 \\5 \\7'],
    'tynorLumbo': [r'(\btynor\b)(.*?)(\blumbo\b)(.*)(\bsacral\b)(.*)(\b(?:l|m|s|xxl|xl|xs)\b)(.*)',
                   '\\1 \\3 \\5 \\7'],
    'tynorAnkle': [r'(\btynor\b)(.*?)(\bankle\b)(.*)(\bbinder\b)(.*)(\b(?:l|m|s|xxl|xl|xs)\b)(.*)',
                   '\\1 \\3 \\5 \\7'],
    'tynorKneeWrapHinged': [
        r'(\btynor\b)(.*?)(\bknee\b)(.*)(\bwrap\b)(.*)(\bhinged\b)(.*)(\bneoprene\b)(.*)(\b(?:l|m|s|xxl|xl|xs)\b)(.*)',
        '\\1 \\3 \\5 \\7 \\9 \\11'],
    'flamingoSoft': [r'(\bflamingo\b)(.*?)(\bsoft\b)(.*)(\b(?:l|m|s|xxl|xl|xs)\b)(.*)', '\\1 \\3 \\5'],
    'flamingoOpenPatella': [
        r'(\bflamingo\b)(.*?)(\bopen\b)(.*)(\bpatella\b)(.*)(\b(?:l|m|s|xxl|xl|xxxl|xs)\b)(.*)',
        '\\1 \\3 \\5 \\7'],
    'flamingoElasticWrist': [
        r'(\bflamingo\b)(.*?)(\belastic\b)(.*)(\bwrist\b)(.*)(\b(?:l|m|s|xxl|xl|xs)\b)(.*)',
        '\\1 \\3 \\5 \\7'],
    'dynaparQpsPlus': [r'(\bdynapar\b)(.*?)(\bqps\b)(.*)(\bplus\b)(.*)', '\\1 \\3 \\5' + ' sol'],
    'dynaparQps': [r'(\bdynapar\b)(.*?)(\bqps\b)(?!.*\bplus\b)(.*)', '\\1 \\3' + ' sol'],
    'durexExtraRibbed': [r'(\bdurex\b)(.*?)(\bextra\b)(.*)(\bribbed\b)(.*)',
                         'durex extra ribbed condoms'],
    'durexExtraThin': [r'(\bdurex\b)(.*?)(\bextra\b)(.*)(\bthin\b)(.*)', 'durex extra thin condoms'],
    'durexExtraDots': [r'(\bdurex\b)(.*?)(\bextra\b)(.*)(\bdots\b)(.*)', 'durex extra dots condoms'],
    'units': [r'\b([0-9.]+)\s?(mg(?:\sml)?|mcg|iu ml|iu|ml|g|s|tab|cap)', '\\1 \\2'],
    'milligramsConversion': [r'(\d+)(\d)00 mg', '\\1.\\2 g'],
    'microgramsConversion': [r'(\d+)(\d)0 mcg', '\\1.\\2 mg'],
    'decreaseZeros': [r'\b(\d+)(\.0+)', '\\1'],
    'humanErrors': [r'\bzz+', ''],
    'extraSpaces': [r'\s+', ' ']
}

substitution = {
    'alkacare': {
        'preConditions': None,
        'postConditions': None,
        'words': ['alkacarb'],
        'replacer': 'alkacare',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'tynor': {
        'preConditions': None,
        'postConditions': None,
        'words': ['tyn'],
        'replacer': 'tynor',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'warp': {
        'preConditions': None,
        'postConditions': None,
        'words': ['warp', 'warps'],
        'replacer': 'wrap',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'tashel': {
        'preConditions': None,
        'postConditions': None,
        'words': ['tashel'],
        'replacer': 'rashel',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'drRashel': {
        'preConditions': None,
        'postConditions': None,
        'words': ['drrashel', 'dr.rashel'],
        'replacer': 'dr rashel',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'condom': {
        'preConditions': None,
        'postConditions': None,
        'words': ['condom'],
        'replacer': 'condoms',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'removeWords': {
        'preConditions': ['not first'],
        'postConditions': None,
        'words': ['mrp', 'hsn', 'sku', 'skg', 'items', 'pricing', 'bag', 'box', 'bib'],
        'replacer': '',
        'removeForPerfectMatch': True,
        'removeForMatchAssistance': True,
    },
    'bgCode': {
        'preConditions': None,
        'postConditions': ['digits'],
        'words': ['bg', 'bg '],
        'replacer': 'bg',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'suppository1': {
        'preConditions': None,
        'postConditions': None,
        'words': ['.supp', 'supp', '.suppo', 'suppo'],
        'replacer': 'suppository',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'suppository2': {
        'preConditions': None,
        'postConditions': ['words'],
        'words': ['.suppo', 'suppo'],
        'replacer': 'suppository',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'grams': {
        'preConditions': None,
        'postConditions': ['digits'],
        'words': ['g', 'gm', 'gms'],
        'replacer': 'g',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'milligrams': {
        'preConditions': None,
        'postConditions': None,
        'words': ['mg', 'mgs'],
        'replacer': 'mg',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'tablet1': {
        'preConditions': None,
        'postConditions': None,
        'words': ['tab', 'tabs', 'tablet', 'tablets'],
        'replacer': 'tablet',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'tablet2': {
        'preConditions': None,
        'postConditions': ['words'],
        'words': ['tabl'],
        'replacer': 'tablet',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'capsule': {
        'preConditions': None,
        'postConditions': None,
        'words': ['cap', 'caps', 'capsule', 'capsules'],
        'replacer': 'capsule',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'sofgel': {
        'preConditions': None,
        'postConditions': None,
        'words': ['soft gelatin', 'softgel capsule', 'softgels', 'softgel', 'soft gel', 'sofgels', 'sofgel', 'softules',
                  ],
        'replacer': 'capsule',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'child':{
        'preConditions': None,
        'postConditions': None,
        'words': ['ch'],
        'replacer': 'child',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'respules1': {
        'preConditions': None,
        'postConditions': None,
        'words': ['resp'],
        'replacer': 'respule',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'respules2': {
        'preConditions': None,
        'postConditions': ['words'],
        'words': ['resp'],
        'replacer': 'respule',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'rotacaps': {
        'preConditions': None,
        'postConditions': None,
        'words': ['rotacaps', 'rotacap', 'rota caps', 'rota cap', 'r c'],
        'replacer': 'rotacap',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'transcaps': {
        'preConditions': None,
        'postConditions': None,
        'words': ['transcaps', 'transcap'],
        'replacer': 'transcap',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'sugarFree': {
        'preConditions': None,
        'postConditions': None,
        'words': ['sugar free', 'sf'],
        'replacer': 'sugarfree',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'syrup': {
        'preConditions': None,
        'postConditions': None,
        'words': ['syrup', 'syru', 'syr', 'syp', 'dry syrup', 'dry syr', 'dry syp', 'cough syrup', 'cough syr',
                  'cough syp', 'cough formula', 'exp', 'expt', 'expectorant', 'exepectorant', 'elixer', 'elixir'],
        'replacer': 'syrup',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'suspension': {
        'preConditions': None,
        'postConditions': None,
        'words': ['susp', 'sus pension', 'suspension'],
        'replacer': 'syrup',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'liquid': {
        'preConditions': None,
        'postConditions': None,
        'words': ['liq', 'liqiud', 'liqu', 'liquid'],
        'replacer': 'liquid',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'drops': {
        'preConditions': None,
        'postConditions': None,
        'words': ['drops', 'drop', 'dro'],
        'replacer': 'drop',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'eyeEarDrop': {
        'preConditions': None,
        'postConditions': None,
        'words': ['e e drop', 'e edrop', 'eye eardrop', 'opthalmic sol', 'opthalmic solu', 'opthalmic solution'],
        'replacer': 'eye drop',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'eyeDrop': {
        'preConditions': None,
        'postConditions': None,
        'words': ['e drop', 'edrop', 'eyedrop', 'eyesdrop'],
        'replacer': 'eye ear drop',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'nasalDrops': {
        'preConditions': None,
        'postConditions': None,
        'words': ['n drop', 'ndrop'],
        'replacer': 'nasal drop',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'ointment': {
        'preConditions': None,
        'postConditions': None,
        'words': ['oint', 'ointment', 'onit'],
        'replacer': 'ointment',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'eyeOintment': {
        'preConditions': None,
        'postConditions': None,
        'words': ['eyeoint', 'eyesoint', 'eyeointment', 'eyesointment', 'eye oint', 'eye soint',
                  'eye ointment', 'eyes ointment'],
        'replacer': 'ointment',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'infusion': {
        'preConditions': None,
        'postConditions': None,
        'words': ['inf', 'infusion'],
        'replacer': 'infusion',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'injection': {
        'preConditions': None,
        'postConditions': None,
        'words': ['injection', 'inj'],
        'replacer': 'injection',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'inhaler': {
        'preConditions': None,
        'postConditions': None,
        'words': ['inhaler', 'inh'],
        'replacer': 'inhaler',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'cream': {
        'preConditions': None,
        'postConditions': None,
        'words': ['crm', 'cream', 'cre'],
        'replacer': 'cream',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'lotion': {
        'preConditions': None,
        'postConditions': None,
        'words': ['lot', 'lotion'],
        'replacer': 'lotion',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'solution': {
        'preConditions': None,
        'postConditions': None,
        'words': ['soln', 'solution', 'solu', 'solut', 'soultion', 'sol'],
        'replacer': 'solution',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'sachets': {
        'preConditions': None,
        'postConditions': None,
        'words': ['sach', 'sachets', 'sachet', 'sachs'],
        'replacer': 'sachet',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'vial': {
        'preConditions': None,
        'postConditions': None,
        'words': ['vial', 'vail'],
        'replacer': '',
        'removeForPerfectMatch': True,
        'removeForMatchAssistance': True,
    },
    'lozenges': {
        'preConditions': None,
        'postConditions': None,
        'words': ['loz', 'lozenge', 'lozenges', 'lozs'],
        'replacer': 'lozenges',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
    },
    'facewash': {
        'preConditions': None,
        'postConditions': None,
        'words': ['fa wash', 'face wash', 'faces wash', 'f wash', 'fwash', 'fawash', 'facewash', 'faceswash',
                  'fash wash'],
        'replacer': 'face wash',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'babyFoodStage': {
        'preConditions': None,
        'postConditions': None,
        'words': ['no', 'stage', 'n', 'sta'],
        'replacer': 'stage',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'bib': {
        'preConditions': None,
        'postConditions': ['anything'],
        'words': ['bib'],
        'replacer': '',
        'removeForPerfectMatch': True,
        'removeForMatchAssistance': True,
    },
    'pk': {
        'preConditions': None,
        'postConditions': None,
        'words': ['pk', 'p k', 'pankajkasthuri', 'pankaja kasthuri'],
        'replacer': 'pankajakasthuri',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'adult': {
        'preConditions': None,
        'postConditions': None,
        'words': ['adults'],
        'replacer': 'adult',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'cadbury': {
        'preConditions': ['beginning'],
        'postConditions': None,
        'words': ['cdm'],
        'replacer': 'cadbury dairy milk',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'colgate': {
        'preConditions': ['beginning'],
        'postConditions': None,
        'words': ['cl'],
        'replacer': 'colgate',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'colgateDental': {
        'preConditions': ['beginning'],
        'postConditions': None,
        'words': ['cdc'],
        'replacer': 'colgate dental cream',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'colgateMax': {
        'preConditions': ['beginning'],
        'postConditions': None,
        'words': ['cmf'],
        'replacer': 'colgate max fresh',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'whisper': {
        'preConditions': None,
        'postConditions': None,
        'words': ['whspr', 'whispe'],
        'replacer': 'whisper',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'cerelac': {
        'preConditions': ['beginning'],
        'postConditions': None,
        'words': ['cerl'],
        'replacer': 'cerelac',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'kamaSutra': {
        'preConditions': ['beginning'],
        'postConditions': None,
        'words': ['ks'],
        'replacer': 'kamasutra',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'patanjali': {
        'preConditions': ['beginning'],
        'postConditions': None,
        'words': ['ptn'],
        'replacer': 'patanjali',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'dettol': {
        'preConditions': None,
        'postConditions': None,
        'words': ['detol'],
        'replacer': 'dettol',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'garnier': {
        'preConditions': None,
        'postConditions': None,
        'words': ['gar'],
        'replacer': 'garnier',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    "jb": {
        'preConditions': None,
        'postConditions': None,
        'words': ['jb'],
        'replacer': 'johnsons baby',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'horlicks': {
        'preConditions': ['beginning'],
        'postConditions': None,
        'words': ['hlx'],
        'replacer': 'horlicks',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'test strip': {
        'preConditions': None,
        'postConditions': None,
        'words': ['test strips', 'test strip', 'teststrip', 'teststrips'],
        'replacer': 'test strip',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True
    },
    'extraLarge': {
        'preConditions': None,
        'postConditions': None,
        'words': ['xtra large'],
        'replacer': 'extra large',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False
    },
    'packaging1': {
        'preConditions': ['digits'],
        'postConditions': ['ending'],
        'words': ['ml', 'g', 's'],
        'replacer': '',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'packaging2': {
        'preConditions': None,
        'postConditions': ['digits'],
        'words': ['pack of'],
        'replacer': '',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'packType': {
        'preConditions': ['not first'],
        'postConditions': None,
        'words': ['big', 'each', 'pack', 'box', 'combipack', 'tin', 'jar', 'tube', 'tub'],
        'replacer': '',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': True,
        'replaceForPerfectMatch': False
    },
    'allnight': {
        'preConditions': None,
        'postConditions': None,
        'words': ['allnight'],
        'replacer': 'all night',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'ankle': {
        'preConditions': None,
        'postConditions': None,
        'words': ['anke'],
        'replacer': 'ankle',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'mamyPokoPants': {
        'preConditions': None,
        'postConditions': None,
        'words': ['many pocopants'],
        'replacer': 'manypoko pants',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'breathe': {
        'preConditions': None,
        'postConditions': None,
        'words': ['breth', 'breathe'],
        'replacer': 'breathe',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'universal': {
        'preConditions': None,
        'postConditions': None,
        'words': ['uni'],
        'replacer': 'universal',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'vanilla': {
        'preConditions': None,
        'postConditions': None,
        'words': ['vani', 'vf'],
        'replacer': 'vanilla',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'extras': {
        'preConditions': None,
        'postConditions': None,
        'words': ['flavour', 'falvour', 'rich', 'new', 'with cooling crystals ', 'therapy', 'powder', 'small', 'baggy',
                  'device', 'chips', 'followup', 'follow up', 'disinfectant'],
        'replacer': '',
        'removeForPerfectMatch': True,
        'removeForMatchAssistance': True,
    },
    'johnsons': {
        'preConditions': None,
        'postConditions': None,
        'words': ['jj'],
        'replacer': 'johnsons',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'foam': {
        'preConditions': None,
        'postConditions': None,
        'words': ['foaming'],
        'replacer': 'foam',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'sebamed': {
        'preConditions': None,
        'postConditions': None,
        'words': ['seb'],
        'replacer': 'sebamed',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'clida': {
        'preConditions': None,
        'postConditions': None,
        'words': ['clid'],
        'replacer': 'clida',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    },
    'deodorant': {
        'preConditions': None,
        'postConditions': None,
        'words': ['deo'],
        'replacer': 'deodorant',
        'removeForPerfectMatch': False,
        'removeForMatchAssistance': False,
    }
}
