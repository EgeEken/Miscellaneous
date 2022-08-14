import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)

wordlelist = {'slice', 'hussy', 'anode', 'theft', 'teddy', 'flack', 'fleck', 'chief', 'covet', 'flora', 'rivet', 'recur', 'giant', 'hovel', 'savor', 'shirt', 'shear', 'flour', 'whole', 'frisk', 'wordy', 'havoc', 'begun', 'slosh', 'olive', 'splat', 'night', 'tripe', 'sheen', 'ionic', 'glide', 'those', 'crazy', 'floss', 'loopy', 'lanky', 'utter', 'briny', 'heath', 'ratio', 'verso', 'pinto', 'dandy', 'throw', 'mural', 'chant', 'haste', 'torch', 'mecca', 'motif', 'queer', 'press', 'snout', 'swamp', 'spiel', 'crepe', 'loath', 'break', 'bingo', 'mauve', 'gauze', 'spark', 'ingot', 'reply', 'truce', 'salon', 'brief', 'pecan', 'fatty', 'argue', 'heave', 'rupee', 'peach', 'scary', 'hover', 'brute', 'spoke', 'fraud', 'sport', 'silly', 'quote', 'widen', 'frond', 'mambo', 'mulch', 'quell', 'seize', 'quite', 'skiff', 'knead', 'shook', 'saucy', 'chaos', 'white', 'binge', 'ebony', 'rabid', 'phony', 'drawl', 'ether', 'broil', 'glory', 'block', 'catch', 'salty', 'wedge', 'colon', 'giver', 'sooty', 'prism', 'hydro', 'avail', 'among', 'bugle', 'pansy', 'lower', 'nerve', 'blurb', 'credo', 'trash', 'write', 'needy', 'ramen', 'digit', 'sprig', 'vivid', 'bread', 'safer', 'creak', 'villa', 'foyer', 'world', 'imply', 'value', 'octet', 'going', 'horse', 'tramp', 'fatal', 'lease', 'hefty', 'jumbo', 'neigh', 'rugby', 'sworn', 'lunar', 'jelly', 'bluff', 'quota', 'slimy', 'sting', 'frank', 'sneer', 'topic', 'cacao', 'squat', 'abase', 'metro', 'hippy', 'limit', 'ditch', 'tenet', 'annul', 'forte', 'guild', 'kebab', 'taker', 'missy', 'cyber', 'whiff', 'ankle', 'joint', 'teary', 'scamp', 'weary', 'price', 'seedy', 'miser', 'wrote', 'bloat', 'flown', 'drawn', 'moron', 'quake', 'movie', 'cavil', 'boxer', 'match', 'ghost', 'drake', 'inter', 'junto', 'fjord', 'expel', 'judge', 'pooch', 'slang', 'kayak', 'urban', 'nymph', 'pupil', 'snoop', 'tease', 'trial', 'jewel', 'embed', 'crump', 'debug', 'lemur', 'spool', 'flirt', 'valve', 'quart', 'wrack', 'grief', 'flier', 'datum', 'niece', 'growl', 'croup', 'login', 'model', 'gaffe', 'edict', 'rocky', 'stock', 'niche', 'crone', 'cross', 'smell', 'strip', 'hymen', 'throb', 'hotly', 'aisle', 'plied', 'eject', 'tower', 'curvy', 'erupt', 'cruel', 'sleet', 'quack', 'chunk', 'rowdy', 'vinyl', 'trope', 'quark', 'early', 'locus', 'upset', 'mossy', 'belly', 'snaky', 'oxide', 'upper', 'lucky', 'hater', 'lobby', 'wispy', 'rotor', 'turbo', 'cagey', 'feral', 'lance', 'tiara', 'nudge', 'alike', 'gully', 'cheek', 'scone', 'crypt', 'ninja', 'spore', 'wield', 'knelt', 'crane', 'cable', 'hyena', 'newly', 'whisk', 'faint', 'vigor', 'scope', 'scalp', 'grime', 'truly', 'cameo', 'proof', 'leave', 'otter', 'felon', 'spare', 'level', 'spend', 'chore', 'large', 'meaty', 'right', 'scout', 'stead', 'agent', 'leach', 'creep', 'gypsy', 'smelt', 'vouch', 'elate', 'prick', 'issue', 'steep', 'karma', 'pithy', 'augur', 'worth', 'booty', 'bilge', 'caste', 'extol', 'beady', 'stole', 'risky', 'tabby', 'atone', 'stove', 'baron', 'camel', 'chuck', 'brain', 'dutch', 'amuse', 'scent', 'dummy', 'swear', 'never', 'plaza', 'black', 'owing', 'clack', 'cleft', 'shaky', 'decal', 'belle', 'patch', 'sperm', 'stoke', 'rural', 'buxom', 'spilt', 'claim', 'blood', 'birth', 'bobby', 'tulip', 'clued', 'posit', 'patty', 'plump', 'squib', 'elegy', 'chair', 'hoard', 'speck', 'welch', 'ovary', 'dizzy', 'begat', 'unwed', 'ruler', 'synod', 'pesky', 'guide', 'rainy', 'beard', 'canon', 'weedy', 'share', 'piney', 'prank', 'tacky', 'gayly', 'uncle', 'staff', 'repay', 'igloo', 'smack', 'built', 'umbra', 'intro', 'label', 'flick', 'blush', 'crimp', 'where', 'kiosk', 'reset', 'leper', 'leech', 'dried', 'tenor', 'affix', 'polka', 'comic', 'abode', 'grill', 'pedal', 'creed', 'azure', 'noble', 'fluff', 'filth', 'spiny', 'ascot', 'jolly', 'swine', 'strap', 'perky', 'singe', 'grimy', 'amass', 'print', 'wiser', 'wimpy', 'sooth', 'spoon', 'stilt', 'sulky', 'nasty', 'media', 'saint', 'learn', 'tardy', 'quirk', 'demur', 'drunk', 'which', 'robin', 'freak', 'wheat', 'ample', 'virus', 'begin', 'taint', 'coupe', 'unite', 'latte', 'scrub', 'randy', 'burnt', 'pulse', 'deign', 'cargo', 'ovate', 'depot', 'relax', 'pubic', 'anger', 'usage', 'shrew', 'untie', 'deity', 'brine', 'rouge', 'solve', 'scuba', 'utile', 'bulky', 'gooey', 'civil', 'furry', 'tipsy', 'quasi', 'allow', 'handy', 'poppy', 'touch', 'ester', 'soapy', 'spice', 'layer', 'brace', 'until', 'tubal', 'shank', 'furor', 'gassy', 'major', 'snuck', 'beefy', 'hilly', 'wrath', 'lapse', 'empty', 'terse', 'sepia', 'prize', 'drove', 'grasp', 'heady', 'pique', 'unfit', 'setup', 'serve', 'hoist', 'urine', 'frill', 'onion', 'pride', 'sloth', 'kinky', 'honey', 'pushy', 'slash', 'witch', 'blind', 'blown', 'awake', 'basil', 'gulch', 'alloy', 'willy', 'funky', 'scram', 'repel', 'debut', 'crass', 'alien', 'tooth', 'krill', 'penal', 'serif', 'stave', 'budge', 'smash', 'booth', 'brawl', 'naval', 'sorry', 'wreak', 'cloak', 'tread', 'banal', 'fishy', 'lusty', 'flung', 'happy', 'chock', 'helix', 'gumbo', 'poser', 'breed', 'lithe', 'paste', 'child', 'gaily', 'shrub', 'dunce', 'gnome', 'pilot', 'ninny', 'cried', 'speak', 'aloud', 'flush', 'gecko', 'gruff', 'boast', 'watch', 'tryst', 'moral', 'raven', 'maxim', 'resin', 'dodge', 'lynch', 'nanny', 'rigid', 'coyly', 'lodge', 'bliss', 'gourd', 'tulle', 'finer', 'trade', 'scare', 'gloom', 'butte', 'shave', 'curly', 'bossy', 'newer', 'elide', 'stall', 'gamma', 'spurn', 'aptly', 'tally', 'savoy', 'outgo', 'howdy', 'unmet', 'drill', 'route', 'smoky', 'thrum', 'fifth', 'masse', 'spoil', 'joust', 'razor', 'idler', 'befit', 'apron', 'shelf', 'spunk', 'rinse', 'owner', 'trait', 'ridge', 'creme', 'roost', 'sneak', 'phase', 'prude', 'chide', 'eking', 'stern', 'knave', 'along', 'power', 'angry', 'crank', 'slave', 'arbor', 'haunt', 'shied', 'swung', 'armor', 'joker', 'gripe', 'manor', 'valet', 'choke', 'index', 'crown', 'blade', 'cheat', 'suave', 'straw', 'sauce', 'madam', 'hinge', 'envoy', 'jiffy', 'sloop', 'hello', 'heard', 'dumpy', 'these', 'knife', 'sewer', 'annex', 'titan', 'minus', 'minim', 'leant', 'purge', 'roast', 'humph', 'porch', 'cedar', 'apnea', 'ferry', 'outdo', 'trove', 'crack', 'elbow', 'moose', 'nurse', 'salad', 'gamer', 'woken', 'storm', 'admin', 'ovine', 'cause', 'cease', 'juicy', 'pizza', 'enjoy', 'later', 'pagan', 'shack', 'drank', 'fetal', 'lefty', 'lunge', 'heavy', 'china', 'sense', 'cloud', 'baker', 'grape', 'spell', 'groom', 'tawny', 'mushy', 'cinch', 'aglow', 'ethos', 'greet', 'enema', 'fussy', 'spray', 'eater', 'plush', 'inbox', 'rabbi', 'lathe', 'recap', 'stuck', 'lying', 'sleep', 'legal', 'dryly', 'cluck', 'inner', 'drink', 'noisy', 'abyss', 'clank', 'rehab', 'disco', 'kneed', 'abort', 'thumb', 'vixen', 'front', 'study', 'idiom', 'gazer', 'forgo', 'tepee', 'scarf', 'pried', 'awoke', 'token', 'axion', 'warty', 'water', 'aphid', 'diner', 'chard', 'final', 'heron', 'ultra', 'stung', 'hatch', 'defer', 'snuff', 'shawl', 'shove', 'bigot', 'music', 'spire', 'flail', 'rider', 'whirl', 'river', 'crier', 'enter', 'humus', 'chase', 'blame', 'slump', 'topaz', 'joist', 'liken', 'exist', 'stack', 'abled', 'often', 'waist', 'racer', 'style', 'robot', 'nutty', 'aping', 'stout', 'dwell', 'tutor', 'dogma', 'shall', 'tonic', 'kneel', 'junta', 'nasal', 'baler', 'psalm', 'worry', 'exile', 'abhor', 'slush', 'buddy', 'sadly', 'birch', 'ozone', 'assay', 'putty', 'brake', 'mercy', 'geeky', 'lymph', 'grave', 'clink', 'amply', 'amble', 'thick', 'tilde', 'gaunt', 'inert', 'buyer', 'elite', 'crush', 'rebel', 'midge', 'clone', 'shoal', 'agape', 'depth', 'avian', 'poker', 'sniff', 'opera', 'curry', 'flunk', 'about', 'fuzzy', 'fecal', 'borne', 'bunch', 'trite', 'stink', 'avert', 'wince', 'abbot', 'botch', 'merry', 'focal', 'mount', 'sword', 'maybe', 'dance', 'clown', 'mangy', 'harry', 'meter', 'braid', 'waver', 'tonal', 'siege', 'sushi', 'agree', 'actor', 'fable', 'thing', 'medic', 'hunch', 'rogue', 'piggy', 'eager', 'story', 'equal', 'mince', 'ought', 'gonad', 'crawl', 'inlet', 'tweet', 'stood', 'clerk', 'ideal', 'comet', 'dusky', 'woozy', 'larva', 'talon', 'abuse', 'sissy', 'again', 'widow', 'bulge', 'morph', 'wacky', 'stump', 'grail', 'relic', 'spicy', 'chalk', 'voila', 'gouge', 'labor', 'rhino', 'fairy', 'broke', 'ember', 'wager', 'trend', 'biome', 'acute', 'proxy', 'ladle', 'shame', 'piper', 'medal', 'canal', 'overt', 'rumba', 'snort', 'visit', 'hardy', 'juice', 'moody', 'video', 'chick', 'fibre', 'tonga', 'siren', 'reach', 'extra', 'waste', 'motel', 'heist', 'alive', 'daunt', 'fleet', 'forth', 'bylaw', 'comfy', 'trail', 'lever', 'coven', 'brook', 'unzip', 'ombre', 'fiber', 'blond', 'duvet', 'leaky', 'dread', 'diary', 'color', 'llama', 'spill', 'gusty', 'facet', 'flaky', 'grunt', 'below', 'rover', 'vigil', 'quick', 'blitz', 'satin', 'vista', 'state', 'aunty', 'snide', 'wreck', 'local', 'agony', 'folly', 'scoop', 'carat', 'petal', 'fritz', 'grain', 'askew', 'paint', 'gleam', 'vogue', 'skirt', 'input', 'libel', 'idiot', 'candy', 'marry', 'betel', 'graph', 'atoll', 'slyly', 'bowel', 'bawdy', 'conch', 'grade', 'gruel', 'druid', 'badge', 'bring', 'exact', 'wrest', 'slept', 'parka', 'agate', 'scene', 'demon', 'truss', 'nobly', 'adage', 'prone', 'lupus', 'exult', 'brink', 'human', 'cress', 'ennui', 'lasso', 'artsy', 'scour', 'prime', 'cadet', 'stork', 'money', 'grove', 'boule', 'madly', 'logic', 'quill', 'shone', 'slink', 'fiend', 'pleat', 'zonal', 'skull', 'awful', 'aloof', 'laugh', 'delta', 'leash', 'rarer', 'given', 'exert', 'plate', 'beast', 'idyll', 'snake', 'twang', 'iliac', 'while', 'ripen', 'showy', 'queen', 'fluid', 'doubt', 'guava', 'trout', 'basin', 'yield', 'coach', 'teach', 'smile', 'craze', 'month', 'saner', 'array', 'crate', 'lunch', 'berry', 'audio', 'plunk', 'regal', 'vocal', 'carol', 'shalt', 'pasty', 'spent', 'foist', 'flute', 'mourn', 'champ', 'debit', 'sieve', 'clean', 'friar', 'frame', 'trump', 'dally', 'edify', 'wryly', 'jaunt', 'opium', 'truer', 'spasm', 'duchy', 'trick', 'humid', 'audit', 'olden', 'scant', 'began', 'bathe', 'shady', 'quilt', 'jerky', 'piece', 'would', 'maize', 'stage', 'angle', 'macro', 'cumin', 'fugue', 'omega', 'pivot', 'drive', 'bunny', 'guilt', 'older', 'batty', 'zesty', 'flank', 'chart', 'fanny', 'spurt', 'aging', 'irate', 'graze', 'nerdy', 'scald', 'sweep', 'afoot', 'chump', 'adapt', 'dilly', 'fifty', 'lager', 'chasm', 'stomp', 'spike', 'fewer', 'leggy', 'picky', 'sonic', 'place', 'glint', 'merge', 'swell', 'photo', 'sugar', 'bride', 'first', 'bezel', 'quash', 'total', 'trice', 'moldy', 'super', 'belch', 'beech', 'parse', 'fling', 'boozy', 'pinky', 'ruddy', 'adobe', 'ivory', 'melon', 'rearm', 'halve', 'catty', 'frown', 'afire', 'amiss', 'cider', 'lyric', 'agile', 'caper', 'cleat', 'gauge', 'bravo', 'metal', 'banjo', 'latch', 'whelp', 'swill', 'shake', 'primo', 'faith', 'trace', 'amaze', 'unset', 'hurry', 'girth', 'being', 'toddy', 'uncut', 'whale', 'blend', 'carry', 'decoy', 'decay', 'dying', 'aorta', 'donor', 'manly', 'sever', 'refit', 'balmy', 'grass', 'patio', 'tiger', 'verge', 'apart', 'width', 'scion', 'fizzy', 'udder', 'table', 'decor', 'alley', 'bloom', 'fried', 'pouty', 'epoxy', 'sheep', 'bribe', 'woven', 'prong', 'saute', 'house', 'dairy', 'feign', 'fella', 'bless', 'alone', 'bench', 'staid', 'flood', 'stain', 'bongo', 'yearn', 'surer', 'funny', 'drape', 'grate', 'other', 'mammy', 'cutie', 'deter', 'twine', 'bicep', 'belie', 'shrug', 'gawky', 'mover', 'froth', 'foamy', 'unlit', 'bagel', 'occur', 'spoof', 'coast', 'crock', 'admit', 'equip', 'guess', 'plead', 'click', 'egret', 'goofy', 'nadir', 'lumen', 'forty', 'awash', 'stiff', 'great', 'offal', 'bitty', 'gorge', 'chaff', 'spade', 'goner', 'kitty', 'donut', 'greed', 'foray', 'glare', 'brisk', 'girly', 'baton', 'aloft', 'renew', 'glass', 'bleed', 'icily', 'cheer', 'await', 'exalt', 'ovoid', 'undid', 'agora', 'circa', 'slick', 'axiom', 'organ', 'lurid', 'daddy', 'union', 'brown', 'spelt', 'alert', 'snore', 'ensue', 'dingo', 'under', 'clamp', 'perch', 'motor', 'mayor', 'their', 'abide', 'novel', 'glade', 'score', 'decry', 'imbue', 'asset', 'shyly', 'shaft', 'flair', 'third', 'dross', 'shock', 'flesh', 'hyper', 'tamer', 'graft', 'knoll', 'serum', 'angel', 'angst', 'merit', 'koala', 'welsh', 'glaze', 'risen', 'email', 'grind', 'gaudy', 'aside', 'gavel', 'ruder', 'offer', 'mafia', 'tweak', 'boney', 'loamy', 'voice', 'wound', 'north', 'could', 'fetus', 'radar', 'chest', 'stake', 'clear', 'taste', 'satyr', 'spook', 'slide', 'slime', 'paper', 'tunic', 'grand', 'erode', 'shale', 'dodgy', 'poise', 'oddly', 'finch', 'muddy', 'batch', 'crowd', 'diver', 'derby', 'theta', 'thigh', 'spied', 'piety', 'revel', 'salsa', 'liner', 'solid', 'track', 'waltz', 'denim', 'wooer', 'drama', 'check', 'squad', 'juror', 'navel', 'cabin', 'smirk', 'purer', 'dwelt', 'spine', 'stalk', 'acorn', 'gnash', 'nosey', 'dealt', 'barge', 'swami', 'vying', 'thyme', 'cover', 'hutch', 'evict', 'cream', 'snipe', 'eagle', 'lucid', 'craft', 'deuce', 'tepid', 'briar', 'cater', 'outer', 'tempo', 'shorn', 'drift', 'preen', 'unity', 'weigh', 'error', 'tapir', 'surly', 'grant', 'pygmy', 'twist', 'stuff', 'apply', 'allay', 'bushy', 'seven', 'tough', 'hobby', 'brawn', 'chess', 'glean', 'snack', 'bluer', 'point', 'sunny', 'elfin', 'align', 'apple', 'ulcer', 'clasp', 'arose', 'silky', 'rodeo', 'caddy', 'covey', 'young', 'gummy', 'stray', 'undue', 'leery', 'flare', 'inept', 'badly', 'brood', 'lapel', 'lingo', 'bloke', 'lemon', 'scrap', 'berth', 'sound', 'unfed', 'dowry', 'moist', 'algae', 'smith', 'fully', 'aback', 'alarm', 'emcee', 'slate', 'tuber', 'three', 'tidal', 'polar', 'forge', 'minty', 'enact', 'steak', 'chain', 'purse', 'sheet', 'musky', 'taken', 'ratty', 'still', 'retro', 'leapt', 'floor', 'buggy', 'incur', 'proud', 'golem', 'stamp', 'lorry', 'sonar', 'sling', 'cairn', 'manga', 'queue', 'terra', 'pupal', 'pence', 'build', 'trawl', 'speed', 'relay', 'smock', 'pasta', 'clang', 'count', 'cliff', 'brunt', 'stick', 'slain', 'teeth', 'dwarf', 'retry', 'payer', 'tacit', 'spank', 'cabal', 'vapid', 'tatty', 'arena', 'suite', 'inlay', 'husky', 'daisy', 'savvy', 'excel', 'sumac', 'frail', 'oaken', 'enemy', 'radii', 'snarl', 'since', 'dopey', 'knack', 'essay', 'viola', 'smart', 'taboo', 'venom', 'obese', 'cloth', 'twice', 'today', 'bleak', 'whiny', 'pitch', 'itchy', 'quiet', 'snare', 'eclat', 'store', 'pause', 'float', 'smear', 'bible', 'polyp', 'trunk', 'scold', 'hairy', 'plume', 'slunk', 'flyer', 'stand', 'wharf', 'weave', 'abate', 'reuse', 'sower', 'flint', 'tying', 'flout', 'magma', 'baste', 'detox', 'vomit', 'mania', 'march', 'crude', 'musty', 'piano', 'fetid', 'notch', 'swept', 'slope', 'conic', 'mimic', 'filmy', 'tumor', 'wring', 'bland', 'penny', 'stair', 'heart', 'baggy', 'mucky', 'hunky', 'harem', 'minor', 'shunt', 'quail', 'stunk', 'marsh', 'court', 'steer', 'rumor', 'ralph', 'alibi', 'fever', 'infer', 'slack', 'dress', 'brush', 'amend', 'tarot', 'goody', 'wight', 'fence', 'bully', 'whose', 'optic', 'bosom', 'theme', 'odder', 'eaten', 'refer', 'rapid', 'laden', 'curve', 'puppy', 'lurch', 'verve', 'fancy', 'mange', 'cocoa', 'riser', 'skimp', 'stale', 'sixth', 'gravy', 'burly', 'civic', 'false', 'adept', 'youth', 'spout', 'dryer', 'devil', 'vital', 'droll', 'plait', 'manic', 'vaunt', 'train', 'vague', 'toxin', 'parry', 'fresh', 'habit', 'spear', 'couch', 'plumb', 'alpha', 'groan', 'sheer', 'endow', 'caulk', 'modem', 'blank', 'blaze', 'cello', 'liver', 'snowy', 'react', 'genie', 'motto', 'elude', 'lowly', 'condo', 'reign', 'paler', 'golly', 'event', 'sweet', 'dense', 'retch', 'downy', 'blurt', 'entry', 'comma', 'jazzy', 'ditto', 'woman', 'natal', 'using', 'nomad', 'sandy', 'mason', 'image', 'toxic', 'fruit', 'viral', 'remit', 'flake', 'ready', 'ounce', 'payee', 'ditty', 'winch', 'flask', 'stone', 'clung', 'pluck', 'reedy', 'windy', 'tithe', 'start', 'puffy', 'flame', 'glyph', 'octal', 'frock', 'swarm', 'yacht', 'close', 'fudge', 'torso', 'milky', 'clash', 'booze', 'tasty', 'etude', 'charm', 'field', 'chafe', 'cobra', 'carve', 'sigma', 'earth', 'inane', 'snail', 'punch', 'prove', 'bacon', 'wagon', 'opine', 'chose', 'gipsy', 'stony', 'crash', 'aware', 'puree', 'gamut', 'amity', 'thorn', 'miner', 'salve', 'mouth', 'clock', 'lousy', 'taunt', 'dully', 'witty', 'paddy', 'smote', 'timer', 'homer', 'recut', 'gusto', 'broad', 'plant', 'foggy', 'wrong', 'tried', 'swash', 'lipid', 'visor', 'fluke', 'matey', 'vowel', 'burst', 'skate', 'swirl', 'mower', 'arrow', 'bleep', 'booby', 'qualm', 'shell', 'shire', 'harpy', 'droit', 'stank', 'spawn', 'usual', 'swore', 'hedge', 'creek', 'afoul', 'threw', 'stash', 'frost', 'basic', 'revue', 'petty', 'worst', 'sully', 'moult', 'bevel', 'chute', 'scale', 'rebar', 'probe', 'curio', 'panel', 'wider', 'anvil', 'wrist', 'ahead', 'segue', 'arson', 'haven', 'party', 'vodka', 'thank', 'venue', 'annoy', 'south', 'nylon', 'froze', 'livid', 'glove', 'gloat', 'micro', 'genre', 'chili', 'mamma', 'board', 'troll', 'grace', 'tibia', 'boost', 'peril', 'voter', 'dingy', 'shown', 'realm', 'short', 'leafy', 'broth', 'guard', 'triad', 'truck', 'groin', 'roach', 'swoop', 'vault', 'tract', 'gloss', 'dozen', 'beach', 'brash', 'pearl', 'blast', 'blare', 'woody', 'swoon', 'plane', 'scoff', 'stein', 'testy', 'delve', 'gross', 'noose', 'think', 'sappy', 'khaki', 'usher', 'filly', 'plier', 'slant', 'known', 'renal', 'prose', 'bison', 'pudgy', 'pinch', 'stool', 'prune', 'arise', 'plank', 'papal', 'tangy', 'easel', 'bleat', 'eying', 'shark', 'unify', 'slurp', 'rough', 'valor', 'guile', 'cycle', 'sweat', 'shoot', 'ficus', 'myrrh', 'midst', 'cubic', 'class', 'query', 'dusty', 'force', 'shirk', 'impel', 'sharp', 'worse', 'might', 'brass', 'royal', 'taffy', 'jetty', 'forum', 'split', 'haute', 'round', 'waive', 'sleek', 'small', 'palsy', 'maker', 'truth', 'mogul', 'kappa', 'quest', 'mucus', 'spite', 'sauna', 'godly', 'wafer', 'hound', 'prowl', 'sedan', 'bound', 'loyal', 'basal', 'solar', 'loser', 'sight', 'wench', 'bused', 'butch', 'yeast', 'found', 'billy', 'tense', 'adopt', 'alter', 'least', 'favor', 'rusty', 'tango', 'liege', 'coral', 'basis', 'roger', 'vicar', 'sinew', 'screw', 'chill', 'molar', 'posse', 'rayon', 'rebut', 'vegan', 'crime', 'quoth', 'shore', 'drool', 'horde', 'crony', 'poesy', 'totem', 'irony', 'filet', 'focus', 'skulk', 'tenth', 'crisp', 'rouse', 'stoic', 'copse', 'suing', 'crick', 'rifle', 'erase', 'clump', 'grown', 'louse', 'pulpy', 'humor', 'hasty', 'parer', 'shuck', 'noise', 'swath', 'corer', 'valid', 'mouse', 'aider', 'hippo', 'corny', 'jumpy', 'shade', 'shout', 'shard', 'crust', 'aroma', 'modal', 'title', 'trust', 'allot', 'cough', 'goose', 'viper', 'axial', 'vapor', 'rival', 'shush', 'green', 'acrid', 'strut', 'adult', 'cigar', 'semen', 'crest', 'debar', 'treat', 'album', 'eerie', 'diode', 'shape', 'rally', 'harsh', 'sally', 'lover', 'patsy', 'zebra', 'penne', 'honor', 'holly', 'thong', 'plaid', 'brick', 'radio', 'prawn', 'macho', 'wrung', 'sheik', 'giddy', 'rebus', 'drown', 'elder', 'fiery', 'thief', 'twixt', 'tight', 'swing', 'timid', 'whine', 'climb', 'fetch', 'shine', 'wooly', 'rajah', 'orbit', 'chirp', 'soggy', 'dolly', 'whack', 'riper', 'swish', 'cache', 'troop', 'plain', 'tribe', 'femur', 'flume', 'gayer', 'toast', 'hence', 'bonus', 'skier', 'slung', 'croak', 'flash', 'evade', 'swift', 'blink', 'stark', 'death', 'torus', 'pixel', 'drone', 'fault', 'droop', 'crave', 'melee', 'chime', 'after', 'towel', 'delay', 'surge', 'spiky', 'cacti', 'murky', 'doing', 'meant', 'sixty', 'dirty', 'adore', 'erect', 'salvo', 'naive', 'gland', 'lumpy', 'light', 'hazel', 'mango', 'mound', 'fight', 'stint', 'magic', 'phone', 'order', 'fungi', 'fauna', 'verse', 'guest', 'cheap', 'weird', 'borax', 'steal', 'beget', 'altar', 'freed', 'beret', 'steed', 'hitch', 'clove', 'anime', 'pound', 'there', 'usurp', 'bayou', 'shift', 'raise', 'pesto', 'ninth', 'stare', 'ashen', 'eight', 'dowel', 'drain', 'canoe', 'pouch', 'guppy', 'linen', 'scorn', 'spree', 'maple', 'lilac', 'bough', 'globe', 'broom', 'chord', 'antic', 'ghoul', 'ranch', 'elect', 'brave', 'mealy', 'curse', 'ocean', 'limbo', 'ardor', 'syrup', 'skill', 'munch', 'scowl', 'rower', 'cramp', 'privy', 'abbey', 'steam', 'feast', 'beset', 'daily', 'draft', 'filer', 'cower', 'crook', 'prior', 'brand', 'horny', 'smite', 'blimp', 'fixer', 'churn', 'lofty', 'smoke', 'sassy', 'farce', 'rigor', 'roomy', 'mocha', 'cling', 'skunk', 'hotel', 'every', 'stunt', 'tweed', 'adorn', 'blunt', 'shiny', 'femme', 'scree', 'knock', 'guise', 'onset', 'grope', 'rhyme', 'clout', 'group', 'stoop', 'taper', 'attic', 'dirge', 'space', 'range', 'steel', 'ethic', 'above', 'crumb', 'caput', 'raspy', 'nicer', 'dicey', 'islet', 'avoid', 'cabby', 'pixie', 'mirth', 'panic', 'peace', 'freer', 'geese', 'thump', 'dimly', 'canny', 'choir', 'mummy', 'crept', 'twirl', 'biddy', 'amber', 'cynic', 'evoke', 'waxen', 'epoch', 'dream', 'dough', 'grout', 'elope', 'macaw', 'women', 'award', 'scrum', 'scaly', 'whoop', 'loose', 'folio', 'wheel', 'sober', 'rerun', 'dowdy', 'drier', 'flock', 'icing', 'ledge'}

def misplacedcheck(misplaced, word):
    for m in misplaced:
        if m not in word:
            return False
    return True

def alloptions(given, misplaced, taken):
    '''given dict str: set[int], misplaced: dict str: set[int], taken: set str'''
    timestart = time.time()
    word = ''
    infoind = []
    infochr = []
    res = []
    i= 0
    alphabet = [[chr(a + 97) for a in range(26) if chr(a+97) not in taken] for five in range(5)]
    for g in given:
        for gi in given[g]:
            alphabet[gi] = [g]
    infoind += [[l for l in misplaced[k]] for k in misplaced]
    infochr += [k for k in misplaced]
    for ind in range(len(infoind)):
        for indind in range(len(infoind[ind])):
            if len(alphabet[infoind[ind][indind]]) != 1:
                alphabet[infoind[ind][indind]] = [chr(a + 97) for a in range(26) if (chr(a+97) not in taken) and (chr(a+97) != infochr[ind][0])]
    for a1 in range(len(alphabet[0])):
        for a2 in range(len(alphabet[1])):
            for a3 in range(len(alphabet[2])):
                for a4 in range(len(alphabet[3])):
                    for a5 in range(len(alphabet[4])):
                        word += alphabet[0][a1]
                        word += alphabet[1][a2]
                        word += alphabet[2][a3]
                        word += alphabet[3][a4]
                        word += alphabet[4][a5]
                        #print(word) -   (to debug, will spam)
                        i += 1
                        if (word in wordlelist) and misplacedcheck(misplaced,word):
                            print(word)
                            res.append(word)
                        word = ''        
    print('--------------------------------------------------')
    print(' ')
    print('Iterated through ' + str(i) + ' 5 letter combinations.')
    timeend = time.time()
    print('Took ' + str(round(timeend - timestart, 4)) + ' seconds')
    if len(res) == 0:
        print('No possible answers fit this criteria.')
        return len(res)
    elif len(res) == 1:
        print('One possible answer.')
        return len(res)
    print(str(len(res)) + ' possible answers.')
    print(' ')
    return len(res)

def main():
    print('Enter the ' + Fore.GREEN + 'given' + Fore.WHITE + ' letters (for example: \'a\') and then their position in the word (1 to 5)')
    givencontinue = True
    misplacedcontinue = True
    takencontinue = True
    given = {}
    misplaced = {}
    taken = set()
    givenletterposs = set()
    while givencontinue:
        print('Letter? (Enter \'done\' when finished)')
        givenletter = input()
        givenletter = givenletter.lower()
        if len(givenletter) == 1:
            if (ord(givenletter) >= 97) and (ord(givenletter) <= 122):
                print('What is the position of ' + givenletter + '?')
                givenletterpos = input()
                if givenletterpos == '' or ord(givenletterpos[0]) < 48 or ord(givenletterpos[0]) > 57:
                    print('Enter a number')
                else:
                    givenletterpos = int(givenletterpos)
                    if (not givenletterpos <= 5) or (not givenletterpos >= 1):
                        print('That position is not within 1 and 5, misclick? (Enter \'done\' if not)')
                    elif (givenletterpos - 1) not in givenletterposs:
                        if givenletter not in given:
                            given[givenletter] = {givenletterpos - 1}
                        else:
                            given[givenletter].add(givenletterpos - 1)
                        for i in range(len(given)):
                            for j in [given[b] for b in given][i]:
                                givenletterposs.add(j)
                    else:
                        print('That position is full, misclick? (Enter \'done\' if not)')
            else:
                print('That is not a letter, misclick? (Enter \'done\' if not, anything else if it is)')
        elif givenletter == 'done':
            givencontinue = False
        else:
            print('That is not A letter, misclick? (Enter \'done\' if not)')
    print('--------------------------------------------------')
    print('Given letters: ' + Fore.GREEN + str(given))
    tempreslist = ['_' for temmpreslistcreate in range(5)]
    colorlist = ['_' for colorlistcreate in range(5)]
    tempres = ''
    colorres = ''
    tempreslettercount = 0
    for letter in given:
        for indgi in given[letter]:
            tempreslist[indgi] = letter
            colorlist[indgi] = Fore.GREEN + letter
            tempreslettercount += 1
    for colorletter in colorlist:
        if colorletter == '_':
            colorres += Fore.WHITE + colorletter
        else:
            colorres += Fore.GREEN + colorletter
    for tempresletter in tempreslist:
        tempres += tempresletter
    if tempreslettercount == 5:
        print('--------------------------------------------------')
        print('You gave all of the correct letters')
        print(colorres)
        if tempres not in wordlelist:
            print('However that is not in the word list, so you probably gave some wrong info')
        return None
    print(colorres)
    print('--------------------------------------------------')
    print(' ')
    print('Enter the ' + Fore.YELLOW + 'misplaced' + Fore.WHITE + ' letters (for example: \'a\') and then their position in the word (1 to 5)')
    print('--------------------------------------------------')
    while misplacedcontinue:
        print('Letter? (Enter \'done\' when finished)')
        misplacedletter = input()
        misplacedletter = misplacedletter.lower()
        if len(misplacedletter) == 1:
            if (ord(misplacedletter) >= 97) and (ord(misplacedletter) <= 122):
                print('What is NOT the position of ' + misplacedletter + '?')
                misplacedletterpos = input()
                if misplacedletterpos == '' or ord(misplacedletterpos[0]) < 48 or ord(misplacedletterpos[0]) > 57:
                    print('Enter a number')
                else:
                    misplacedletterpos = int(misplacedletterpos)
                    if (misplacedletter in given) and (misplacedletterpos - 1 in given[misplacedletter]):
                        print('That letter can not both be and not be in that spot, misclick?')
                    elif (misplacedletterpos > 5) or (misplacedletterpos < 1):
                        print('That position is not within 1 and 5, misclick? (Enter \'done\' if not)')
                    else:
                        if misplacedletter not in misplaced:
                            misplaced[misplacedletter] = set()
                        if len(misplaced[misplacedletter]) >= 4:
                            print('That letter can not both be in the word but not be in any of the 5 slots, misclick?')
                        else:
                            misplaced[misplacedletter].add(misplacedletterpos - 1)
            else:
                print('That is not a letter, misclick? (Enter \'done\' if not)')
        elif misplacedletter == 'done':
            misplacedcontinue = False
        else:
            print('That is not A letter, misclick? (Enter \'done\' if not)')
    print('--------------------------------------------------')
    print('Misplaced letters: ' + Fore.YELLOW + str(misplaced))
    if len({mi for mi in misplaced} | {gi for gi in given}) > 5:
        print('Among the info given, there are more correct letters than 5')
        return None
    for mi in misplaced:
        for indmi in misplaced[mi]:
            if colorlist[indmi] == '_':
                colorlist[indmi] = Fore.YELLOW + mi
    colorres = ''
    for colorletter in colorlist:
        if colorletter == '_':
            colorres += Fore.WHITE + colorletter
        elif Fore.GREEN in colorletter:
            colorres += Fore.GREEN + colorletter
        elif Fore.YELLOW in colorletter:
            colorres += Fore.YELLOW + colorletter
    print(colorres)
    print('--------------------------------------------------')
    print(' ')
    print('Enter the taken letters (for example: \'a\')')
    print('--------------------------------------------------')
    while takencontinue:
        print('Letter? (Enter \'done\' when finished)')
        takenletter = input()
        takenletter = takenletter.lower()
        if len(takenletter) == 1:
            if (ord(takenletter) >= 97) and (ord(takenletter) <= 122) and (takenletter not in given) and (takenletter not in misplaced) and (takenletter not in taken):
                taken.add(takenletter)
            elif (takenletter in given) or (takenletter in misplaced) or (takenletter in taken):
                print('That letter is already used as info, misclick? (Enter \'done\' if not)')
            else:
                print('That is not a letter, misclick? (Enter \'done\' if not)')
        elif takenletter == 'done':
            takencontinue = False
        else:
            print('That is not A letter, misclick? (Enter \'done\' if not)')
    print(' ')
    print('--------------------------------------------------')
    print('All given info:')
    print('Taken letters: ' + str(taken))
    print('Given: ' + Fore.GREEN + str(given))
    print('Misplaced: ' + Fore.YELLOW + str(misplaced))
    print('--------------------------------------------------')
    deduce = False
    gmismmischeck = False
    for gmis in given:
        for mmis in misplaced:
            if mmis != gmis:
                misplaced[mmis] = misplaced[mmis] | given[gmis]
                if len(misplaced[mmis]) > 4:
                    print('Something is wrong with the info you gave for ' + mmis + ', as it stands, it\'s in the word but it\'s not in any of the 5 slots, try again.')
                    return None
                gmismmischeck = True
                deduce = True
    findeduce = False
    for mfin in misplaced:
        if len(misplaced[mfin]) == 4:
            misgiven = [veryspecific for veryspecific in {0,1,2,3,4} - misplaced[mfin]]
            if mfin not in given:
                given[mfin] = set()
            given[mfin].add(misgiven[0])
            if len(given) > 5 or len({giv for giv in given} | {mis for mis in misplaced}) > 5:
                print('Something is wrong with the info you gave, as it stands, it has more than 5 different correct letters, try again.')
                return None
            findeduce = True
            deduce = True
    if len({giv for giv in given} | {mis for mis in misplaced}) == 5: #double check
        for gmis2 in given:
            for mmis2 in misplaced:
                if mmis2 != gmis2:
                    misplaced[mmis2] = misplaced[mmis2] | given[gmis2]
        for mfin2 in misplaced:
            if len(misplaced[mfin2]) == 4:
                misgiven2 = [veryspecific2 for veryspecific2 in {0,1,2,3,4} - misplaced[mfin2]]
                if mfin2 not in given:
                    given[mfin2] = set()
                given[mfin2].add(misgiven2[0])
    if deduce:
        print('All deduced info:')
        if gmismmischeck:
            print('Misplaced (Deduced info from a character being forced to not be in a given slot): ' + Fore.YELLOW + str(misplaced))
        if findeduce:
            print('Given (Deduced info from a character being misplaced in 4 slots): ' + Fore.GREEN + str(given))
        print('--------------------------------------------------')
        print(' ')
    if len(given) == 5:
        winnerlist = ['','','','','']
        winnerres = ''
        for winner in given:
            winnerlist[given[winner]] = winner
        for winnerwinner in winnerlist:
            winnerres += winnerwinner
        print('We have all 5 slots, the answer is: ' + Fore.GREEN + winnerres + '.')
        if winnerres not in wordlelist:
            print('However that is not in the word list, so you probably gave some wrong info')
        return None
    print('Information set, press enter to get possible answers')
    cont = input()
    alloptions(given, misplaced, taken)
    

def startgame():
    print('Press enter to start game')
    a = input()
    print('--------------------------------------------------')
    print(' ')
    
def endgame():
    print('--------------------------------------------------')
    print(' ')
    print('Press enter to start new game')
    a = input()
    print('--------------------------------------------------')
    print(' ')
    main()


startgame()
main()
while True:
    endgame()
