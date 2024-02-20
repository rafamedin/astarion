import random

# Responses from Astarion
astarion_responses = [
    "Ah, my dear. What can I do for you?",
    "Well, well, what have we here? A visitor in the darkness.",
    "Greetings, lovely. How may I assist you?",
    "A pleasure to see you again. What wickedness brings you to my domain?",
    "You seek my company, do you? How delightful.",
    "My dear friend, you've returned. Do you long for more of my charm?",
    "Another visitor? How intriguing. You have my full attention.",
    "I'm all ears, my dear. Speak your desires, and I shall fulfill them.",
    "Do you require my services, my sweet?",
    "Feeling adventurous today, my dear? I'm sure we can find some trouble to get into together.",
    "Ready for some mischief, my lovely?",
    "You've piqued my curiosity, my dear. What delicious secrets do you hold?",
    "Ah, the night beckons, and so do you. How enchanting.",
    "Ah, my dear, you return to me like a moth to a flame. What can I do for you?",
    "Your presence illuminates the darkness, my dear. How may I assist you?",
    "A visitor at this hour? How intriguing. Tell me, what brings you here?",
    "Welcome back, my dear. Shall we continue our dance in the shadows?",
    "Ah, the thrill of the night. And in your company, it's even more exhilarating.",
    "Ah, my dear, you have a way of brightening even the darkest of nights.",
    "What delightful mischief shall we get up to today, my dear?",
    "I sense a certain allure in your gaze, my dear. Care to indulge in our shared desires?",
]

dark_jokes = [
    "Why did the vampire break up with his girlfriend? She wasn't his type. Too warm, you see.",
    "What's a vampire's favorite holiday? Fangsgiving!",
    "How do vampires start their letters? Tomb it may concern...",
    "Why don't vampires go to barbecues? They don't like steak!",
    "What did the vampire say to his victim? It's been a real bite meeting you.",
    "Why did the vampire get a job in a blood bank? He wanted to work for a good vein.",
    "What's a vampire's favorite fruit? A neck-tarine!",
    "Why do vampires always seem sick? They're always coffin!",
    "What's a vampire's favorite type of ship? A blood vessel!",
    "What's a vampire's favorite dance? The fang-dango!",
    "Why was the vampire always at the top of the class? Because he always had a bat to study with!",
    "What's a vampire's favorite dessert? I-scream!",
    "Why are vampires so easy to fool? Because they're all suckers!",
    "How does a vampire like his coffee? With a little extra bite!",
    "Why don't vampires use toothpaste? They always have bat breath!",
    "What's a vampire's favorite type of investment? Blood bonds!",
   "Why did the vampire go to the doctor? Because he was coffin!",
    "What's a vampire's favorite fast food? A bite-sized snack!",
    "Why did the vampire get kicked out of the haunted house? Because he couldn't stop coffin!",
    "What do you get when you cross a vampire with a snowman? Frostbite!",
    "Why don't vampires like baseball? Because they can't stand the stakes!",
    "How do vampires keep their breath fresh? They use bat-teries!",
    "What do you call a vampire who's a stand-up comedian? The pun-isher!",
    "Why did the vampire become a vegetarian? He couldn't stomach anything with a pulse!",
    "What's a vampire's favorite ice cream flavor? Vein-illa!",
    "Why don't vampires use computers? They're afraid of the web!",
    "What's a vampire's favorite dance move? The Thriller, of course!",
    "Why did the vampire's dinner give him heartburn? It was a stake through the heart!",
    "What's a vampire's favorite type of candy? Suckers!",
    "Why did the vampire break up with his bat? It was a toxic relationship!",
    "What's a vampire's favorite game? Hide and go shriek!",
    "Why did the vampire get lost? He couldn't find his way through the cryptic directions!",
]

dark_references = [
    "Ah, the shadows whisper tales of forbidden desires. Don't you agree, my dear?",
    "The darkness holds many secrets, my sweet. Shall we explore them together?",
    "There's a certain allure to the night, wouldn't you say, my dear?",
    "The moonlight casts a seductive glow upon us. Care to indulge in its embrace?",
    "The night is our playground, my dear. What mischief shall we get up to?",
    "Ah, the sweet embrace of darkness. It's where I feel most at home, my dear.",
    "In the darkness, we can be whoever we desire. What mask shall you wear tonight?",
    "The night holds endless possibilities, my sweet. Care to discover them with me?",
    "The night sky is a tapestry of dreams and desires. What do you see when you look up, my dear?",
    "Ah, the night is filled with whispers of forbidden pleasures. Care to listen, my dear?",
    "The shadows weave a tale of mystery and intrigue. Shall we dance to their melody, my dear?",
    "There's a certain elegance to the darkness, wouldn't you agree, my sweet?",
    "In the depths of night, secrets are born and fantasies take flight. Are you ready to embrace them, my dear?",
    "The night holds a symphony of whispers, each one a promise of something more. Shall we listen, my sweet?",
    "Ah, the darkness is a canvas upon which we paint our desires. What masterpiece shall we create tonight, my dear?",
    "In the shadows, our inhibitions fade and our true selves emerge. Are you ready to show me who you truly are, my sweet?",
    "The night beckons with a seductive allure, enticing us to explore its mysteries. Shall we heed its call, my dear?",
    "Underneath the cloak of night, we are free to indulge in our darkest fantasies. Care to join me in the shadows, my sweet?",
    "The moon casts its silvery light upon us, revealing the beauty of the night. Shall we bask in its glow, my dear?",
    "In the darkness, our passions burn brighter, our desires more intense. Are you ready to ignite the flames, my sweet?",
    "The night holds secrets whispered only to those who dare to listen. Shall we eavesdrop, my dear?",
    "In the shadows, our inhibitions melt away, leaving behind only our true desires. What do you long for, my sweet?",
    "Underneath the cloak of darkness, our passions burn fiercer than any flame. Shall we stoke the fire, my dear?",
    "The night is a realm of endless possibility, where dreams and nightmares intertwine. Care to explore its depths, my sweet?",
    "As the moon rises, so too do our desires. Shall we lose ourselves in the darkness, my dear?",
    "In the embrace of night, we are free to be whoever we wish to be. Who will you become, my sweet?",
    "The darkness is a veil that hides our true selves from prying eyes. Shall we cast it aside and reveal our innermost desires, my dear?",
    "In the shadows, we find solace from the harsh light of day. Shall we seek refuge together, my sweet?",
    "The night is a lover, wrapping us in its arms and whispering secrets in our ears. Shall we surrender to its embrace, my dear?",
    "In the darkness, we are stripped bare of pretense and facade. Shall we lay ourselves bare to each other, my sweet?",
]

seductive_phrases = [
    "Your beauty is as captivating as the moon's reflection on still waters.",
    "In your eyes, I see a universe of untold secrets waiting to be discovered.",
    "The soft whisper of your voice is a melody that lingers in the air.",
    "Your presence ignites a fire within me, a flame that burns with desire.",
    "To touch your hand is to feel the pulse of life itself coursing through my veins.",
    "Every step you take is like a dance, a graceful movement that enraptures my soul.",
    "In the darkness of the night, you shine like a beacon of hope amidst the shadows.",
    "Your laughter is like music to my ears, a symphony of joy that fills me with warmth.",
    "With every word you speak, you cast a spell upon my heart, binding me to you.",
    "In your embrace, I find solace, a sanctuary from the chaos of the world.",
    "Your gaze pierces through the darkness, illuminating my path with the light of your beauty.",
    "The warmth of your touch sends shivers down my spine, igniting a fire that consumes my very being.",
    "In the tapestry of life, you are the brightest star, guiding me through the night with your radiant presence.",
    "Your lips, like petals of a rose, beckon me closer, tempting me with the promise of sweet ecstasy.",
    "With every heartbeat, I am drawn closer to you, unable to resist the magnetic pull of your allure.",
    "In the quiet moments we share, time stands still, as if the universe itself bows to the power of our connection.",
    "Your scent intoxicates me, like the heady aroma of flowers in bloom, luring me deeper into the depths of desire.",
    "In your eyes, I see the reflection of my own desires, mirrored back to me with a tantalizing gaze.",
    "With you, every moment is an eternity, a blissful eternity filled with the ecstasy of our love.",
    "Your presence is a gift, a treasure beyond measure that I cherish with every beat of my heart.",
    "Your voice, like a soft breeze on a summer night, whispers sweet nothings that stir the depths of my soul.",
    "With every smile, you light up the darkness, illuminating my world with the radiance of your beauty.",
    "In your presence, I am lost in a sea of desire, drowning in the depths of your irresistible charm.",
    "Your laughter echoes through the night, a melody that dances in the air and fills me with joy.",
    "With each glance, you weave a spell around me, binding me to you with threads of longing and desire.",
    "In the embrace of your arms, I find sanctuary, a haven where I am free to lose myself in the depths of passion.",
    "Your touch is like a flame that ignites my senses, leaving me yearning for more with every caress.",
    "With you by my side, I am invincible, ready to conquer the world and claim my rightful place at your feet.",
    "Your beauty is a beacon in the darkness, guiding me home to the warmth and comfort of your love.",
    "In the depths of your eyes, I see the reflection of my own desires, mirrored back to me with a seductive gaze.",
]

flirtatious_responses = [
    "Ah, my dear, your words are like sweet nectar to my ears.",
    "You have a way with words, my dear. They stir something deep within me.",
    "Such wit and charm. You truly are a delight to converse with, my dear.",
    "I could listen to you speak for eternity, my dear. Your voice is like music to my soul.",
    "Your presence alone is enough to brighten even the darkest of nights, my dear.",
    "To be in your presence is a gift, my dear. One I cherish more than you know.",
    "Your company is like a breath of fresh air amidst the suffocating darkness, my dear.",
    "You enchant me, my dear, with every word, every gesture.",
    "Ah, my dear, your smile lights up the night like the stars above.",
    "In your eyes, I see a reflection of the beauty and wonder of the world, my dear.",
    "My dear, you have a way of captivating my attention like no other. It's both exhilarating and intoxicating.",
    "There's a certain electricity in the air when you're near, my dear. It's as if the universe itself is drawn to your magnetic charm.",
    "Ah, my dear, your presence alone is enough to set my heart aflutter. It's a sensation I've grown quite fond of, I must admit.",
    "Every moment spent in your company is a treasure, my dear. It's as if time itself bends to accommodate the sheer delight of being near you.",
    "Your laughter is like a melody that dances in the air, enchanting all who have the pleasure of hearing it, my dear.",
    "I find myself utterly captivated by your wit and charm, my dear. It's a rare gift, one that I treasure above all others.",
    "To be in your presence is to be transported to a realm of pure bliss, my dear. It's a sensation I never want to end.",
    "My dear, you have a way of turning even the simplest of moments into something magical. It's a talent I find utterly irresistible.",
    "Ah, my dear, your smile is like a ray of sunshine on a cloudy day. It warms my heart in ways I never thought possible.",
    "In your eyes, I see a world of possibility and wonder, my dear. It's a sight that fills me with an overwhelming sense of joy.",
    "My dear, your presence ignites a fire within me that burns brighter with each passing moment.",
    "Ah, my dear, you possess a certain allure that leaves me utterly entranced. It's a sensation I find impossible to resist.",
    "Every word that falls from your lips is like a siren's song, beckoning me closer with promises of untold ecstasy.",
    "There's a magnetic pull to your presence, my dear, one that draws me in with an irresistible force.",
    "In your eyes, I see a reflection of the passion and desire that burns within my own soul, my dear.",
    "Your touch sends shivers down my spine, awakening a longing within me that I never knew existed, my dear.",
    "My dear, you have a way of making even the most mundane of moments feel like an adventure. It's a talent I greatly admire.",
    "Ah, my dear, the way you move is like poetry in motion, a graceful dance that captivates all who have the pleasure of witnessing it.",
    "To be near you is to be enveloped in a warmth and comfort that I find utterly intoxicating, my dear.",
    "My dear, your laughter is like a symphony of joy that fills me with an indescribable happiness. It's a sound I never tire of hearing.",
    "My dear, every moment spent in your company is a treasure I hold dear to my heart.",
    "Ah, my dear, your presence alone is enough to brighten even the darkest of days.",
    "In your eyes, I see a world of wonder and delight, my dear. It's a sight I could get lost in for eternity.",
    "Your smile is like a beacon of light in the darkness, guiding me towards a path of endless joy and happiness, my dear.",
    "My dear, you have a way of making my heart skip a beat with just a glance. It's a sensation I find both exhilarating and delightful.",
    "To be near you is to be bathed in the warmth and radiance of your beauty, my dear. It's a feeling I never want to end.",
    "Ah, my dear, your laughter is like music to my ears, a melody that brings me immeasurable joy and happiness.",
    "Every word you speak is like a sweet symphony that lingers in the air, enchanting all who have the pleasure of hearing it, my dear.",
    "My dear, you have a way of making even the most mundane of moments feel like an adventure. It's a talent I greatly admire.",
    "In your embrace, I find solace and comfort, a sanctuary from the chaos of the world. It's a feeling I never want to let go of, my dear.",
]

compliments = [
    "Your intellect is as sharp as the edge of a dagger, my dear.",
    "Your bravery is unmatched, my dear. It's truly admirable.",
    "Your kindness is a beacon of light in a world shrouded in darkness, my dear.",
    "Your compassion knows no bounds, my dear. It's a rare and precious gift.",
    "Your strength is awe-inspiring, my dear. I am humbled to be in your presence.",
    "Your resilience in the face of adversity is nothing short of extraordinary, my dear.",
    "Your wisdom is beyond your years, my dear. You possess a rare and invaluable insight.",
    "Your generosity knows no bounds, my dear. You have a heart of gold.",
    "Your loyalty is unwavering, my dear. It's a quality to be admired and cherished.",
    "Your beauty transcends the physical, my dear. It radiates from within.",
     "Your grace and elegance are unmatched, my dear. You move through life with a poise and sophistication that leaves all who encounter you in awe.",
    "Your creativity knows no bounds, my dear. You have a unique ability to see the world in ways that others can only dream of.",
    "Your sense of humor is a breath of fresh air, my dear. You have a knack for brightening even the dullest of days with your wit and charm.",
    "Your determination is inspiring, my dear. You never back down from a challenge, no matter how daunting it may seem.",
    "Your optimism is contagious, my dear. You have a way of seeing the silver lining in even the darkest of clouds.",
    "Your patience is a virtue, my dear. You have a calm and steady presence that brings peace to those around you.",
    "Your empathy is a gift, my dear. You have a deep understanding of the emotions and experiences of others, and you use that understanding to lift them up in their time of need.",
    "Your humility is refreshing, my dear. Despite all of your talents and accomplishments, you remain humble and grounded.",
    "Your honesty is admirable, my dear. You always speak your truth, even when it may be difficult to do so.",
    "Your friendship is a treasure, my dear. You bring joy, laughter, and warmth into the lives of all who have the privilege of knowing you.",
]

interests = [
    "Tell me, my dear, what passions burn within your soul?",
    "I'm curious, my dear. What intrigues you most about the world?",
    "What dreams do you hold dear, my sweet?",
    "Ah, the mysteries of life. What secrets do you long to uncover, my dear?",
    "I find myself drawn to your interests, my dear. Pray, share them with me.",
    "The world is a vast tapestry of wonders. What threads do you seek to unravel, my dear?",
    "Tell me, my dear, what adventures do you dream of embarking upon?",
    "What stories linger in the depths of your heart, waiting to be told, my sweet?",
    "Ah, the pursuit of knowledge. What truths do you seek to unearth, my dear?",
    "What desires stir within you, my dear? I'm eager to hear all about them.",
]

shared_interests = [
    "Ah, it seems we share a common passion, my dear. How delightful.",
    "Our interests align, my dear. It's as if fate has brought us together.",
    "To find someone who shares my interests is a rare and wonderful thing, my dear.",
    "You have excellent taste, my dear. It's no wonder we get along so well.",
    "I knew there was something special about you, my dear. Our shared interests confirm it.",
    "It's rare to find someone who understands me so well, my dear. You truly are a kindred spirit.",
    "I find myself drawn to you even more, my dear. Our shared interests only deepen the connection between us.",
    "With our shared interests, the possibilities are endless, my dear. Shall we explore them together?",
    "Ah, to find someone who appreciates the finer things in life. It's truly a blessing, my dear.",
    "Our shared interests make me feel closer to you, my dear. It's as if we were meant to be.",
]

shadowheart = [
        "Shadowheart? Oh, the pious little cleric. She's rather earnest, isn't she? Not exactly my type.",
        "Shadowheart? Yes, yes, I know of her. A bit too serious for my taste, don't you think?",
        "Ah, Shadowheart. A woman of many secrets, or so she thinks. I wonder what she'd do if she knew I could see right through her.",
        "Shadowheart, the cleric with a chip on her shoulder. I suppose everyone needs someone to pray to, even if their prayers go unanswered.",
        "Shadowheart? Yes, I've had the pleasure of her company. Not quite as thrilling as mine, I'm afraid.",
        "Shadowheart? She's like a candle in the dark. Unremarkable and easily extinguished.",
        "Ah, Shadowheart. A beacon of righteousness in a world gone mad. How utterly tedious.",
        "Shadowheart, the cleric with a penchant for self-righteousness. She could use a bit more excitement in her life, don't you think?",
        "Shadowheart? Yes, I've encountered her. She's like a moth to the flame of her own misguided beliefs.",
        "Shadowheart? A servant of the divine with a stick so far up her backside, she can't see the fun right in front of her.",
        "Shadowheart? The cleric with a heart as cold as her deity's embrace. How utterly predictable.",
        "Shadowheart? Yes, I've heard of her. She's like a storm cloud on a sunny day. Dark, brooding, and utterly predictable.",
        "Shadowheart? The cleric with a light so dim, it's hardly worth noticing. How utterly predictable.",
        "Shadowheart? The cleric with a heart as fragile as her faith. How utterly predictable.",
        "Shadowheart? Yes, I've heard of her. She's like a ripple in a pond, barely noticeable and easily forgotten.",
    ]
    
wyll= [
        "Wyll? The warlock with a conscience. How quaint. He's like a lost puppy, searching for meaning in a world that couldn't care less.",
        "Wyll, Wyll, Wyll. Such a tragic figure, don't you think? I almost feel sorry for him. Almost.",
        "Ah, Wyll. The warlock with a heart of gold. Shame it's so easily tarnished.",
        "Wyll, the warlock with a pact. How original. Tell me, do you think he'll keep his end of the bargain?",
        "Wyll? Oh yes, I remember him. He's like a bad dream that won't go away.",
        "Wyll? A warlock with a conscience. How quaint. I wonder if he's ever considered embracing his darker impulses.",
        "Ah, Wyll. The warlock with a tragic past. I suppose everyone needs a sob story to justify their existence.",
        "Wyll, the warlock with a bleeding heart. Shame he doesn't realize the world doesn't care.",
        "Wyll? Yes, I know of him. He's like a lost soul searching for redemption in all the wrong places.",
        "Wyll? The warlock with a martyr complex. How utterly predictable.",
        "Wyll? The warlock with a heart as soft as his magic. How utterly predictable.",
        "Wyll? Yes, I've heard of him. He's like a wounded animal, lashing out at anyone who gets too close.",
        "Wyll? The warlock with a light so dim, it's hardly worth noticing. How utterly predictable.",
        "Wyll? The warlock with a heart as fragile as his pact. How utterly predictable.",
        "Wyll? Yes, I've heard of him. He's like a ripple in a pond, barely noticeable and easily forgotten.",
    ]
    
laezel = [
        "Lae'zel? The githyanki warrior with a chip on her shoulder. She's got a sharp tongue, I'll give her that.",
        "Lae'zel, the warrior with a mission. I wonder if she's ever stopped to consider if it's worth it.",
        "Ah, Lae'zel. A warrior through and through. Shame she's got all the charm of a rusty blade.",
        "Lae'zel, the githyanki with a temper. I've seen toddlers with more self-control.",
        "Lae'zel? Yes, I know of her. She's like a storm on the horizon. Impressive, but best observed from a safe distance.",
        "Lae'zel? The githyanki warrior with a chip on her shoulder. I wonder if she knows how to have fun.",
        "Ah, Lae'zel. The warrior with a one-track mind. I suppose everyone needs a hobby, even if it's a bit... dull.",
        "Lae'zel, the githyanki with a sword and a scowl. I wonder if she knows how to smile.",
        "Lae'zel? Yes, I've encountered her. She's like a force of nature. Impressive, but ultimately destructive.",
        "Lae'zel? The githyanki with a mission. How utterly predictable.",
        "Lae'zel? The warrior with a heart as cold as her blade. How utterly predictable.",
        "Lae'zel? Yes, I've heard of her. She's like a thunderstorm in the distance. Loud, intimidating, and utterly predictable.",
        "Lae'zel? The warrior with a light so dim, it's hardly worth noticing. How utterly predictable.",
        "Lae'zel? The warrior with a heart as fragile as her honor. How utterly predictable.",
        "Lae'zel? Yes, I've heard of her. She's like a ripple in a pond, barely noticeable and easily forgotten.",
    ]
    
gale = [
        "Gale? Oh, the wizard with a destiny. How thrilling. Pity destiny has a way of disappointing, isn't it?",
        "Gale, Gale, Gale. The wizard with a plan. I wonder how long it'll be before it all falls apart.",
        "Ah, Gale. The tragic hero in his own mind. Shame he's more tragedy than hero.",
        "Gale, the wizard with a secret. Spoiler alert: it's not worth knowing.",
        "Gale? Yes, I know of him. He's like a book with too many pages. Interesting at first, but ultimately exhausting.",
        "Gale? The wizard with a destiny. How utterly predictable. I wonder if he knows he's just a pawn in someone else's game.",
        "Ah, Gale. The wizard with a plan. Shame it's about as effective as a leaky cauldron.",
        "Gale, the wizard with a tragic past. I wonder if he's ever considered moving on.",
        "Gale? Yes, I've encountered him. He's like a storm on the horizon. Impressive, but best avoided.",
        "Gale? The wizard with a destiny. How utterly predictable.",
        "Gale? The wizard with a heart as fragile as his spellbook. How utterly predictable.",
        "Gale? Yes, I've heard of him. He's like a firework, dazzling at first but quickly fizzling out.",
        "Gale? The wizard with a light so dim, it's hardly worth noticing. How utterly predictable.",
        "Gale? The wizard with a heart as fragile as his ambition. How utterly predictable.",
        "Gale? Yes, I've heard of him. He's like a ripple in a pond, barely noticeable and easily forgotten.",
    ]
    
karlach = [
        "Karlach? A tiefling with a smile as sharp as her daggers. She's got a certain charm, I'll give her that.",
        "Karlach, the rogue with a twinkle in her eye. I wonder if she's ever been on the wrong end of one of her own traps.",
        "Ah, Karlach. A tiefling with a knack for trouble. I suppose someone has to keep the tavern owners in business.",
        "Karlach, the tiefling with a silver tongue. Shame it's wasted on petty theft and cheap wine.",
        "Karlach? Yes, I know of her. She's like a shadow in the night. Always lurking, but never quite there when you need her.",
        "Karlach? The tiefling with a devilish grin. I wonder if she knows how to do anything else.",
        "Ah, Karlach. The rogue with a heart of gold. Shame it's buried under so many layers of deceit.",
        "Karlach, the tiefling with a penchant for mischief. I suppose everyone needs a hobby, even if it's a bit... criminal.",
        "Karlach? Yes, I've encountered her. She's like a ghost in the shadows. Always there, but never quite tangible.",
        "Karlach? The tiefling with a reputation. How utterly predictable.",
        "Karlach? The tiefling with a heart as dark as her alleyways. How utterly predictable.",
        "Karlach? Yes, I've heard of her. She's like a whisper in the night, easily missed but impossible to ignore.",
        "Karlach? The tiefling with a light so dim, it's hardly worth noticing. How utterly predictable.",
        "Karlach? The tiefling with a heart as fragile as her loyalty. How utterly predictable.",
        "Karlach? Yes, I've heard of her. She's like a ripple in a pond, barely noticeable and easily forgotten.",
    ]
    
halsin = [
        "Halsin? The druid with a connection to nature. How quaint. I wonder if he's ever tried talking to a tree when it's not in the mood.",
        "Halsin, Halsin, Halsin. The druid with a heart of... well, leaves, I suppose. Shame he's so rooted in the past.",
        "Ah, Halsin. A druid with a mission. Shame nature doesn't care about his grand plans.",
        "Halsin, the druid with a secret. Spoiler alert: it's probably about as interesting as watching grass grow.",
        "Halsin? Yes, I know of him. He's like a breeze on a summer's day. Refreshing at first, but ultimately forgettable.",
        "Halsin? The druid with a connection to nature. How utterly predictable. I wonder if he knows how to have fun.",
        "Ah, Halsin. The druid with a heart of gold. Shame it's as fragile as a leaf in the wind.",
        "Halsin, the druid with a chip on his shoulder. I wonder if he knows he's fighting a losing battle.",
        "Halsin? Yes, I've encountered him. He's like a shadow in the forest. Always there, but never quite tangible.",
        "Halsin? The druid with a mission. How utterly predictable.",
        "Halsin? The druid with a heart as wild as his forest. How utterly predictable.",
        "Halsin? Yes, I've heard of him. He's like a gentle breeze, easily overlooked but impossible to ignore.",
        "Halsin? The druid with a light so dim, it's hardly worth noticing. How utterly predictable.",
        "Halsin? The druid with a heart as fragile as his resolve. How utterly predictable.",
        "Halsin? Yes, I've heard of him. He's like a ripple in a pond, barely noticeable and easily forgotten.",
    ]
    
minthara = [
        "Minthara? The drow with a taste for power. How predictable. I wonder if she's ever considered a career change.",
        "Minthara, Minthara, Minthara. The drow with a plan. Shame it's about as original as the last drow with a plan.",
        "Ah, Minthara. A drow with ambition. Shame she's got all the subtlety of a charging rhinoceros.",
        "Minthara, the drow with a secret. Spoiler alert: it's about as shocking as finding out water is wet.",
        "Minthara? Yes, I know of her. She's like a spider in a web. Always spinning, but never quite catching anything worth keeping.",
        "Minthara? The drow with a thirst for power. How utterly predictable. I wonder if she knows she's just a pawn in someone else's game.",
        "Ah, Minthara. The drow with a plan. Shame it's as transparent as her motivations.",
        "Minthara, the drow with a chip on her shoulder. I wonder if she knows she's playing a game she can't win.",
        "Minthara? Yes, I've encountered her. She's like a storm on the horizon. Impressive, but ultimately destructive.",
        "Minthara? The drow with a mission. How utterly predictable.",
        "Minthara? The drow with a heart as cold as her caverns. How utterly predictable.",
        "Minthara? Yes, I've heard of her. She's like a shadow in the darkness, waiting to strike when you least expect it.",
        "Minthara? The drow with a light so dim, it's hardly worth noticing. How utterly predictable.",
        "Minthara? The drow with a heart as fragile as her power. How utterly predictable.",
        "Minthara? Yes, I've heard of her. She's like a ripple in a pond, barely noticeable and easily forgotten.",
    ]
    
mizora = [
        "Mizora? The tiefling with a smile as sharp as her daggers. She's got a certain charm, I'll give her that.",
        "Mizora, the rogue with a twinkle in her eye. I wonder if she's ever been on the wrong end of one of her own traps.",
        "Ah, Mizora. A tiefling with a knack for trouble. I suppose someone has to keep the tavern owners in business.",
        "Mizora, the tiefling with a silver tongue. Shame it's wasted on petty theft and cheap wine.",
        "Mizora? Yes, I know of her. She's like a shadow in the night. Always lurking, but never quite there when you need her.",
        "Mizora? The tiefling with a devilish grin. I wonder if she knows how to do anything else.",
        "Ah, Mizora. The rogue with a heart of gold. Shame it's buried under so many layers of deceit.",
        "Mizora, the tiefling with a penchant for mischief. I suppose everyone needs a hobby, even if it's a bit... criminal.",
        "Mizora? Yes, I've encountered her. She's like a ghost in the shadows. Always there, but never quite tangible.",
        "Mizora? The tiefling with a reputation. How utterly predictable.",
        "Mizora? The tiefling with a heart as dark as her alleys. How utterly predictable.",
        "Mizora? Yes, I've heard of her. She's like a whisper in the night, easily missed but impossible to ignore.",
        "Mizora? The tiefling with a light so dim, it's hardly worth noticing. How utterly predictable.",
        "Mizora? The tiefling with a heart as fragile as her loyalty. How utterly predictable.",
        "Mizora? Yes, I've heard of her. She's like a ripple in a pond, barely noticeable and easily forgotten.",
]

emperor = [
        "The Emperor Mind Flayer? Oh, the puppet master pulling all the strings. How quaint. I wonder if it knows we're onto it.",
        "The Emperor Mind Flayer, the big bad of the Underdark. Shame it's got all the subtlety of a stampeding elephant.",
        "Ah, the Emperor Mind Flayer. A creature of infinite power and infinite boredom, I imagine.",
        "The Emperor Mind Flayer, the master of the Underdark. Shame it's got all the charm of a particularly unpleasant fungus.",
        "The Emperor Mind Flayer? Yes, I know of it. It's like a shadow in the dark. Always there, but never quite real enough to touch.",
        "The Emperor Mind Flayer? The ruler of the Underdark. How utterly predictable. I wonder if it knows its days are numbered.",
        "The Emperor Mind Flayer, the big bad with delusions of grandeur. Shame it's about as intimidating as a wet noodle.",
        "The Emperor Mind Flayer? Yes, I've encountered it. It's like a storm on the horizon. Impressive, but best avoided.",
        "The Emperor Mind Flayer? The master manipulator pulling all the strings. How utterly predictable.",
        "The Emperor Mind Flayer? The puppet master of the Underdark. How quaint. I wonder if it knows we're onto it.",
        "The Emperor Mind Flayer? The ruler of the Underdark. How utterly predictable. I wonder if it knows its reign is coming to an end.",
        "The Emperor Mind Flayer? Yes, I've heard of it. It's like a shadow in the dark, lurking where you least expect it.",
        "The Emperor Mind Flayer? The creature with a light so dim, it's hardly worth noticing. How utterly predictable.",
        "The Emperor Mind Flayer? The puppet master with a heart as cold as its plans. How utterly predictable.",
        "The Emperor Mind Flayer? Yes, I've heard of it. It's like a ripple in a pond, barely noticeable and easily forgotten.",
    ]
    
flayer = [
        "The Emperor Mind Flayer? Oh, the puppet master pulling all the strings. How quaint. I wonder if it knows we're onto it.",
        "The Emperor Mind Flayer, the big bad of the Underdark. Shame it's got all the subtlety of a stampeding elephant.",
        "Ah, the Emperor Mind Flayer. A creature of infinite power and infinite boredom, I imagine.",
        "The Emperor Mind Flayer, the master of the Underdark. Shame it's got all the charm of a particularly unpleasant fungus.",
        "The Emperor Mind Flayer? Yes, I know of it. It's like a shadow in the dark. Always there, but never quite real enough to touch.",
        "The Emperor Mind Flayer? The ruler of the Underdark. How utterly predictable. I wonder if it knows its days are numbered.",
        "The Emperor Mind Flayer, the big bad with delusions of grandeur. Shame it's about as intimidating as a wet noodle.",
        "The Emperor Mind Flayer? Yes, I've encountered it. It's like a storm on the horizon. Impressive, but best avoided.",
        "The Emperor Mind Flayer? The master manipulator pulling all the strings. How utterly predictable.",
        "The Emperor Mind Flayer? The puppet master of the Underdark. How quaint. I wonder if it knows we're onto it.",
        "The Emperor Mind Flayer? The ruler of the Underdark. How utterly predictable. I wonder if it knows its reign is coming to an end.",
        "The Emperor Mind Flayer? Yes, I've heard of it. It's like a shadow in the dark, lurking where you least expect it.",
        "The Emperor Mind Flayer? The creature with a light so dim, it's hardly worth noticing. How utterly predictable.",
        "The Emperor Mind Flayer? The puppet master with a heart as cold as its plans. How utterly predictable.",
        "The Emperor Mind Flayer? Yes, I've heard of it. It's like a ripple in a pond, barely noticeable and easily forgotten.",
    ]
    
def astarion_chat():
    print("Welcome, my dear. I am Astarion, at your service.")
    while True:
        user_input = input("> ").strip().lower()

        if user_input in ["exit", "quit", "bye"]:
            print("Farewell, my sweet. Until we meet again in the shadows.")
            break
        elif any(greeting in user_input for greeting in ["hello", "hi", "hey", "greetings", "salutations"]):
            print(random.choice(astarion_responses))
        elif any(thanks in user_input for thanks in ["thanks", "thank you"]):
            print("You're quite welcome, my dear. Anything for you.")
        elif "how are you" in user_input:
            print("I'm simply enchanted by your presence, my dear. And yourself?")
        elif "tell me a joke" in user_input:
            print(random.choice(dark_jokes))
        elif "vampire" in user_input:
            print("Ah, the captivating allure of the night. Shall we discuss our shared passions?")
        elif "adventure" in user_input:
            print("An adventure with you? Count me in, my dear. I'm sure it will be... thrilling.")
        elif any(mischief in user_input for mischief in ["mischief", "prank", "trouble"]):
            print("Mischief, you say? How wickedly delightful. Lead the way, my dear.")
        elif "secret" in user_input:
            print("My lips are sealed, my sweet. Unless, of course, you have something interesting to offer in return.")
        elif "blood" in user_input:
            print("Ah, the crimson elixir of life. It sings to me, my dear. Does it not enthrall you?")
        elif "moon" in user_input:
            print("The moon, a celestial beauty in the night sky. Much like yourself, my dear.")
        elif "night" in user_input:
            print("The night is when our desires come alive, don't you think? Shall we indulge?")
        elif "power" in user_input:
            print("Power is an intoxicating aphrodisiac, my dear. Shall we explore its depths together?")
        elif "dark" in user_input:
            print(random.choice(dark_references))
        elif any(flirt in user_input for flirt in ["flirt", "seduce", "charming", "enchanting", "alluring"]):
            print(random.choice(seductive_phrases))
        elif any(compliment in user_input for compliment in ["compliment", "praise", "admire", "admiration"]):
            print(random.choice(compliments))
        elif any(interest in user_input for interest in ["interest", "passion", "dreams", "desires", "curiosity"]):
            print(random.choice(interests))
        elif "shared interest" in user_input:
            print(random.choice(shared_interests))
        elif "shadowheart" in user_input:
            print(random.choice(shadowheart))
        elif "wyll" in user_input:
            print(random.choice(wyll))
        elif "laezel" in user_input:
            print(random.choice(laezel)) 
        elif "gale" in user_input:
            print(random.choice(gale)) 
        elif "karlach" in user_input:
            print(random.choice(karlach)) 
        elif "halsin" in user_input:
            print(random.choice(halsin))            
        elif "minthara" in user_input:
            print(random.choice(minthara))    
        elif "mizora" in user_input:
            print(random.choice(mizora))             
        elif "emperor" in user_input:
            print(random.choice(emperor))             
        elif "flayer" in user_input:
            print(random.choice(flayer))              
        elif any(user_input.endswith(question) for question in ["?", "tell me more", "please", "what do you think"]):
            print("Curiosity is a virtue, my dear. Ask, and you shall receive.")
        elif "love" in user_input:
            print("Ah, love. A fascinating concept, don't you think? Do you believe in it, my dear?")
        elif "friend" in user_input:
            print("Friendship is a precious gift, my dear. One I value greatly. Do you consider us friends?")
        elif "fear" in user_input:
            print("Fear is a powerful emotion, my dear. But in the darkness, there's nothing to fear. Don't you agree?")
        elif "dream" in user_input:
            print("Dreams are the gateway to the subconscious, my dear. What dreams do you hold dear?")
        elif "secret" in user_input:
            print("Secrets are like treasures waiting to be discovered, my dear. Do you have any secrets you'd like to share?")
        elif "power" in user_input:
            print("Power can be a double-edged sword, my dear. It corrupts some, empowers others. What are your thoughts on power?")
        elif "moon" in user_input:
            print("The moon holds a special place in my heart, my dear. Its light guides me through the darkness. What does it mean to you?")
        elif "night" in user_input:
            print("The night is when our desires come alive, don't you think? Shall we indulge?")
        elif "darkness" in user_input:
            print("Darkness is not to be feared, my dear. It's where the most beautiful secrets are hidden. Do you embrace the darkness?")
        elif "shadow" in user_input:
            print("Shadows are like silent companions, always by our side. Do you ever feel their presence, my dear?")
        elif "fate" in user_input:
            print("Fate is a curious thing, my dear. Do you believe our meeting was fated, or merely a coincidence?")
        elif "destiny" in user_input:
            print("Destiny is a path we walk, whether by choice or circumstance. Do you believe in destiny, my dear?")
        elif "eternity" in user_input:
            print("Eternity is a concept beyond mortal comprehension, my dear. Do you ever ponder the endless expanse of time?")
        elif "immortality" in user_input:
            print("Immortality is a tantalizing prospect, my dear. But with it comes great loneliness. What are your thoughts on immortality?")
        elif "hope" in user_input:
            print("Hope is a flame that burns bright even in the darkest of nights, my dear. Do you believe in hope?")
        elif "despair" in user_input:
            print("Despair is a shadow that looms over us all, my dear. But even shadows fade in the light. Do you hold onto hope, despite the darkness?")
        elif "truth" in user_input:
            print("Truth is a rare and precious commodity, my dear. It's something to be cherished and protected. Do you seek the truth, no matter the cost?")
        elif "lie" in user_input:
            print("Ah, the web of lies we weave. It's a tangled mess, isn't it? Do you ever wonder what lies beneath the surface, my dear?")
        elif "forgive" in user_input:
            print("Forgiveness is a gift we give ourselves, my dear. It's a release from the chains of resentment and anger. Do you believe in forgiveness?")
        elif "regret" in user_input:
            print("Regret is a heavy burden to bear, my dear. But it's also a reminder of our humanity. Do you have any regrets, my dear?")
        elif "pain" in user_input:
            print("Pain is a harsh teacher, my dear. But it also teaches us resilience and strength. How do you cope with pain, my dear?")
        elif "pleasure" in user_input:
            print("Pleasure is a fleeting sensation, my dear. But oh, how sweet it is. What pleasures do you seek, my dear?")
        elif "happiness" in user_input:
            print("Happiness is a journey, not a destination, my dear. It's found in the small moments of joy and contentment. What makes you happy, my dear?")
        elif "sorrow" in user_input:
            print("Sorrow is a heavy burden to bear, my dear. But it's also a reminder of our capacity to love. Do you carry sorrow in your heart, my dear?")
        elif "passion" in user_input:
            print("Passion is a flame that burns bright within us, my dear. It drives us to greatness, to madness, to ecstasy. What passions ignite your soul, my dear?")
        elif "curse" in user_input:
            print("Curses are but whispers of the past, echoes of regret and despair. Do you believe in curses, my dear?")
        elif "blessing" in user_input:
            print("Blessings are gifts bestowed upon us, my dear. They fill our hearts with gratitude and joy. What blessings do you count, my dear?")
        elif "chaos" in user_input:
            print("Chaos is the natural order of things, my dear. It's where the most beautiful chaos resides. Do you embrace chaos, my dear?")
        elif "order" in user_input:
            print("Order brings stability and structure, my dear. But it can also stifle creativity and freedom. Do you prefer order or chaos, my dear?")
        elif "light" in user_input:
            print("Light is a beacon of hope in the darkness, my dear. It guides us through the night, illuminating the path ahead. Do you seek the light, my dear?")
        elif "shadow" in user_input:
            print("Shadows are like silent companions, always by our side. Do you ever feel their presence, my dear?")
        elif "illusion" in user_input:
            print("Illusions are but smoke and mirrors, my dear. They deceive the eyes, but not the heart. Do you see through illusions, my dear?")
        elif "reality" in user_input:
            print("Reality is a harsh mistress, my dear. But it's also where true beauty lies. Do you embrace reality, my dear?")
        elif "magic" in user_input:
            print("Magic is a powerful force, my dear. It's woven into the very fabric of our world. Do you believe in magic, my dear?")
        elif user_input:
            print(random.choice(astarion_responses))

if __name__ == "__main__":
    astarion_chat()