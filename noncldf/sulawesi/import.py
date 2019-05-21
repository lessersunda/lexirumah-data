from pathlib import Path

import xlrd

import pybtex
import pyglottolog
from pyglottolog.fts import search_langs

from pylexirumah import get_dataset
from pylexirumah.geo_lookup import geonames, get_region
from pylexirumah.util import identifier

DIALECT = pyglottolog.languoids.models.Level.dialect
gl = pyglottolog.Glottolog(Path(pyglottolog.__file__).parent.parent.parent.parent / "glottolog")

__file__ = "this"

lr = get_dataset()
concepts = {
    'kepala': 'head',
    'rambut': 'hair',
    'mata': 'eye',
    'hidung': 'nose',
    'mulut': 'mouth',
    'bibir': 'lips',
    'lidah': 'tongue',
    'gigi': 'teeth',
    'telinga': 'ear',
    'leher': 'neck',
    'tangan': 'hand',
    'kuku': 'fingernail',
    'perut': 'stomach_belly',
    'kaki': 'foot',
    'lutut': 'knee',
    'kulit': 'skin',
    'daging': 'meat',
    'tulang': 'bone',
    'jantung': 'heart',
    'darah': 'blood',
    'hati': 'liver',
    'air kencing': 'urine',
    'orang': 'person',
    'perempuan': 'woman',
    'suami': 'husband',
    'anak': 'child',
    'kakak laki-laki': 'older_brother',
    'kakak perempuan': 'older_sister',
    'adik laki-laki': 'younger_brother',
    'tamu': 'guest',
    'kami': '1pl_excl',
    'kita': '1pl_incl',
    'mereka': '3pl',
    'tanduk': 'horn',
    'ekor': 'tail',
    'burung': 'bird',
    'telur': 'egg',
    'kelelawar': 'bat',
    'nyamuk': 'mosquito',
    'ular': 'snake',
    'ikan': 'fish',
    'tikus': 'rat',
    'anjing': 'dog',
    'pohon': 'tree',
    'daun': 'leaf',
    'akar': 'root',
    'kayu': 'wood',
    'buah': 'fruit',
    'duri': 'thorn',
    'pisang': 'banana',
    'tempurung': 'coconut_shell',
    'rotan': 'rattan',
    'sirih': 'betel_vine',
    'alang-alang': 'thatch_for_roofing',
    'padi': 'rice_plant',
    'beras': 'uncooked_rice',
    'nasi': 'cooked_rice',
    'matahari': 'sun',
    'bintang': 'star',
    'langit': 'sky',
    'awan': 'cloud',
    'hujan': 'rain',
    'angin': 'wind',
    'pasir': 'sand',
    'tanah': 'soil',
    'garam': 'salt',
    'gula': 'sugar',
    'air': 'water',
    'gunung': 'mountain',
    'hutan': 'forest',
    'danau': 'lake',
    'api': 'fire',
    'asap': 'smoke',
    'batu': 'stone',
    'perahu': 'canoe',
    'lesung': 'mortar',
    'pisau': 'knife',
    'parang': 'machete',
    'tali': 'rope',
    'besar': 'big',
    'kecil': 'small',
    'baik': 'good',
    'kering': 'dry',
    'jauh': 'far',
    'dekat': 'near',
    'panas': 'hot',
    'dingin': 'cold',
    'pendek': 'short',
    'buta': 'blind',
    'tuli': 'deaf',
    'haus': 'thirsty',
    'lapar': 'hungry',
    'semua': 'all',
    'banyak': 'many',
    'penuh': 'full',
    'putih': 'white',
    'hitam': 'black',
    'kuning': 'yellow',
    'merah': 'red',
    'ini': 'this',
    'itu': 'that',
    'satu': 'one',
 'dua': 'two',
 'tiga': 'three',
 'empat': 'four',
 'lima': 'five',
 'enam': 'six',
 'tujuh': 'seven',
 'delapan': 'eight',
 'sembilan': 'nine',
 'sepuluh': 'ten',
 'seratus': 'one_hundred',
 'di depan': 'in_front_of',
 'di luar': 'outside',
 'di dalam': 'inside',
 'pinggir': 'edge',
 'malam': 'night',
 'tahu': 'to_know',
 'menangis': 'to_cry',
 'dengar': 'to_hear',
 'lihat': 'to_see',
 'makan': 'to_eat',
 'minum': 'to_drink',
 'tumbuk': 'to_pound',
 'mati': 'to_die',
 'mandi': 'to_bathe',
 'berenang': 'to_swim',
 'terbang': 'to_fly',
 'bunuh': 'to_kill',
 'batuk': 'to_cough',
 'muntah': 'to_vomit',
 'gatal': 'itchy',
 'berjalan': 'to_walk',
 'duduk': 'to_sit',
 'baring': 'to_lie_down',
 'mengantuk': 'sleepy',
 'tidur': 'to_sleep',
 'mimpi': 'to_dream',
 'bangun': 'to_wake_up',
 'datang': 'to_come',
 'mengandung': 'pregnant',
 'nama': 'name',
 'otak': 'brain',
 'dahi': 'forehead',
 'air mata': 'tear',
 'lubang hidung': 'nostril',
 'ingus': 'mucus',
 'pipi': 'cheek',
 'ludah': 'to_spit',
 'dagu': 'chin',
 'bahu': 'shoulder',
 'tulang punggung': 'spine_lower_back',
 'dada': 'chest',
 'pusat': 'navel',
 'pinggang': 'waist',
 'tumit': 'heel',
 'paru-paru': 'lungs',
 'ginjal': 'kidney',
 'kemaluan laki-laki': 'penis',
 'buah pelir': 'testicles',
 'luka': 'wound',
 'keringat': 'sweat',
 'madu': 'honey',
 'musuh': 'enemy',
 'binatang': 'animal',
 'ayam': 'chicken',
 'sayap': 'wing',
 'kutu busuk': 'bedbug',
 'lalat': 'fly',
 'semut': 'ant',
 'kalajengking': 'scorpion',
 'penyu': 'turtle',
 'tokek': 'lizard',
 'rusa': 'deer',
 'babi': 'pig',
 'cakar': 'claw',
 'musang': 'civet_cat',
 'batang': 'stem',
 'tebu': 'sugarcane',
 'pepaya': 'papaya',
 'mangga': 'mango',
 'sukun': 'breadfruit',
 'ubi kayu': 'cassava',
 'ubi jalar': 'sweet_potato',
 'rumput': 'grass',
 'jagung': 'corn_maize',
 'jawawut': 'millet',
 'kabut': 'fog',
 'embun': 'dew',
 'guntur': 'thunder',
 'pelangi': 'rainbow',
 'ombak': 'wave',
 'pulau': 'island',
 'lumpur': 'mud',
 'gempa bumi': 'earthquake',
 'lubang': 'hole',
 'debu': 'dust',
 'kapur': 'lime',
 'rumah': 'house',
 'lantai': 'floor',
 'dinding': 'wall',
 'pintu': 'door',
 'jendela': 'window',
 'bubungan': 'ridge',
 'kasau': 'roof_rafter',
 'pagar': 'fence',
 'layar': 'sail',
 'tungku': 'oven',
 'kayu api': 'firewood',
 'tugal': 'dibble_stick',
 'tongkat': 'stick_pole',
 'sisir': 'comb',
 'kalung': 'necklace',
 'jarum': 'needle',
 'tikar': 'mat',
 'pasar': 'market',
 'basah': 'wet',
 'gelap': 'dark',
 'terang': 'light_not_dark',
 'lebar': 'wide',
 'tebal': 'thick',
 'tipis': 'thin',
 'kurus': 'skinny',
 'tajam': 'sharp',
 'pahit': 'bitter',
 'manis': 'sweet',
 'asin': 'salty',
 'sakit': 'sick_painful',
 'demam': 'fever',
 'lain': 'other',
 'sedikit': 'few',
 'beberapa': 'some',
 'berat': 'heavy',
 'ringan': 'light_weight',
 'kotor': 'dirty',
 'bersih': 'clean',
 'lurus': 'straight',
 'mahal': 'expensive',
 'murah': 'cheap',
 'benar': 'correct',
 'salah': 'wrong',
 'kalau': 'if',
 'karena': 'because',
 'dan': 'and',
 'sebelas': 'eleven',
 'dua belas': 'twelve',
 'tiga belas': 'thirteen',
 'empat belas': 'fourteen',
 'lima belas': 'fifteen',
 'enam belas': 'sixteen',
 'tujuh belas': 'seventeen',
 'delapan belas': 'eighteen',
 'sembilan belas': 'nineteen',
 'dua puluh satu': 'twenty_one',
 'dua puluh dua': 'twenty_two',
 'dua puluh tiga': 'twenty_three',
 'dua puluh empat': 'twenty_four',
 'dua puluh lima': 'twenty_five',
 'tiga puluh': 'thirty',
 'empat puluh': 'forty',
 'lima puluh': 'fifty',
 'enam puluh': 'sixty',
 'tujuh puluh': 'seventy',
 'delapan puluh': 'eighty',
 'sembilan puluh': 'ninety',
 'dua ratus': 'two_hundred',
 'kiri': 'left_side',
 'kanan': 'right_side',
 'dengan': 'with',
 'hari': 'day',
 'pagi': 'morning',
 'kemarin': 'yesterday',
 'kemarin dulu': 'day_before_yesterday',
 'besok': 'tomorrow',
 'lusa': 'day_after_tomorrow',
 'tahun': 'year',
 'malu': 'shy_ashamed',
 'marah': 'angry',
 'takut': 'scared',
 'hitung': 'to_count',
 'belajar': 'to_learn',
 'pikir': 'to_think',
 'pilih': 'to_choose',
 'menyuruh': 'to_command',
 'mengundang': 'to_invite',
 'menjawab': 'to_answer',
 'menuduh': 'to_accuse',
 'masak': 'to_cook',
 'buka': 'to_open',
 'kunyah': 'to_chew',
 'tiup': 'to_blow',
 'menyala': 'to_shine',
 'kerja': 'to_work',
 'tumbuh': 'to_grow',
 'gali': 'to_dig',
 'tarik': 'to_pull',
 'ikat': 'to_tie',
 'belok': 'to_turn',
 'cuci': 'to_wash',
 'naik': 'to_climb',
 'sembunyi': 'to_hide',
 'lempar': 'to_throw',
 'jahit': 'to_sew',
 'menenun': 'to_weave',
 'beli': 'to_buy',
 'meminjam': 'to_borrow',
 'napas': 'to_breathe',
 'garuk': 'to_scratch',
 'gosok': 'to_rub',
 'bengkak': 'to_swell',
 'pergi': 'to_go',
 'tinggal': 'to_dwell',
 'selesai': 'finished',
 'kata': 'word',
 'bahasa': 'language',
 'uang': 'money',
 'kakak': 'older_sibling',
 'adik': 'younger_sibling',
 'tombak': 'spear',
 'jala': 'fishnet',
 'baju': 'shirt',
 'menari': 'to_dance',
 'es': 'ice',
 'salju': 'snow',
 'tembakau': 'tobacco',
 'jelek': 'bad',
 'sekarang': 'now',
 'tembak': 'to_shoot',
 'kosong': 'empty',
            'kebun': 'garden',
    'lengan': 'arm',
'anak panah': 'arrow',
'di': 'at',
'bambu, buluh': 'bamboo',
'di bawah': 'below',
'biru': 'blue',
'badan, tubuh': 'body',
'bulu': 'body_hair',
'panah': 'bow',
'susu, buah dada': 'breast',
'mas kawin': 'bride_price',
'kupu kupu': 'butterfly',
'buaya': 'crocodile',
'sukar': 'difficult',
'lumba-lumba': 'dolphin',
'gampang, mudah': 'easy',
'tahi': 'excrement',
'wajah, muka': 'face',
'ayah': 'father',
'saudara perempuan dari ayah': 'fathers_sister',
'bulu': 'feather',
'jari tangan': 'finger',
'rata': 'flat',
'pinjal': 'flea',
'katak': 'frog',
'bagus': 'good',
'cucu': 'grandchild',
'nenek laki-laki, kakek': 'grandfather',
'nenek perempuan': 'grandmother',
'hijau': 'green',
'di sini': 'here',
'lintah, pacet': 'leech',
'kilat, petir': 'lightning',
'biawak': 'monitor_lizard',
'bulan': 'moon',
'ibu': 'mother',
'tapak tangan': 'palm_of_hand',
'tulang rusuk': 'rib',
'bundar': 'round',
'benih': 'seed',
'ikan hiu': 'shark',
'hamba, budak': 'slave',
'licin, halus': 'smooth',
'tapak kaki': 'sole_of_foot',
'masam, asam': 'sour',
'labalaba': 'spider',
'tangkai': 'stem',
'enau, aren': 'sugar_palm',
'talas, keladi': 'taro',
'di situ': 'there',
'seribu': 'thousand',
'panjat (me-)': 'to_climb',
'beku (mem-)': 'to_freeze',
'menjual': 'to_sell',
'mencuri': 'to_steal',
'celana': 'trousers',
'duapuluh': 'twenty',
'kemaluan perempuan': 'vagina',
'kampung': 'village',
'ikan paus': 'whale',
'mengapa?, kenapa?': 'why',
'isteri': 'wife',
    
    masak (buah)	ripe	
sungai	river_stream	
jalan* (-an)	road	
busuk	rotten	
rumbia	sago	sago palm
laut	sea	
tinggi	tall	
jerami, lalang	thatch_for_roofing	
atap	thatched_roof	
di sana	there	
cium	to smell	
bertanya	to_ask_question	
memandikan	to_bathe_a_child	
gigit	to_bite	
bakar	to_burn_clear_land	
berteriak	to_call_out	berteriak
mendaki	to_climb	mendaki
berjongkok	to_crouch	
potong (me-)	to_cut	
menebang	to_cut_down	
jatuh	to_fall_from_above	
kelahi (ber)	to_fight	
alir (me)	to_flow	
melipat	to_fold	
beri	to_give	
hantam	to_hit	
pegang (me-)	to_hold	
buru (ber)	to_hunt	
tertawa	to_laugh	
main (ber-)	to_play	
berlari	to_run	
kata (ber-)	to_say	
mencari	to_search_for_to_hunt_for	
memanah	to_shoot	to shoot an arrow
nyanyi	to_sing	
ludah (me-)	to_spit	
belah (me)	to_split	
peras (me-)	to_squeeze	
tikam (me)	to_stab	
diri (ber)	to_stand	
hisap	to_suck	
memberitahu	to_tell	memberitahu, to inform
berbohong, mendusta	to_tell_untruth	
menunggu	to_wait	
membangunkan	to_wake_someone_up	
mencuci tangan	to_wash	wash hands
hapus	to_wipe	
kura-kura darat	turtle	tortoise (the one which walks)
urat darah	vein	
apa	what	
bilamana	when	
di mana	where	
siapa	who	
muda	young_people	

}

alternative_names = {
    "Wakatobi (informant from Kecamatan Wangi-Wangi)": ("Tukang Besi North", "tuka1248-wakat"),
    "Popalia (Binongko)": ("Binongko", None),
    "Kalao Toa": ("Bonerate", "bone1254-kalao"),
    "Lasalimu (east Buton)": ("Lasalimu", None),
    "Kaisabu Baru": ("Kaesabu", "kaes1237-baru"),
    "Karya Baru": ("Karya Baru", "ciac1237-karya"),
    "Gonda Baru": ("Cia-Cia", "ciac1237-gonda"),
    "Bola (southwest Buton)": ("Cia-Cia", "ciac1237-bola"),
    "Masiri - Bola": ("Masiri", None),
    "Sampolawa - Bangun - Buka": ("Sampolawa", None),
    "Mambulu (south Buton)": ("Cia-Cia", "ciac1237-mambu"),
    "Mambulu": ("Cia-Cia", "ciac1237-mambu"),
    "Gunung Sejuk (Cia Liwungau dialect)": ("Cia-Cia", "ciac1237-gunun"),
    "Lapandewa": ("Cia-Cia", "ciac1237-lapan"),
    "Desa Lapandewa, Tambunaloko": ("Cia-Cia", "ciac1237-lapan"),
    "Lapandewa (Kaindea dialect)": ("Cia-Cia", "ciac1237-lapan"),
    "Wabhula": ("Nuclear Wabula", None),
    "Wabula (Pasar Wajo)": ("Wabula", "wabu1242-wajo"),
    "Pasarwajo": ("Wabula", "wabu1242-wajo"),
    "Cia-Cia (informant from Pasarwajo)": ("Wabula", "wabu1242-wajo"),
    "Matanauwe": ("Cia-Cia", "ciac1237-matan"),
    "Batu Atas": ("Cia-Cia", "ciac1237-batua"),
    "Pulau Batuatas": ("Cia-Cia", "ciac1237-batua"),
    "Wali": ("Wali", "wali1265"),
    "Desa Wali": ("Wali", "wali1265"),
    "Wali (Binongko)": ("Wali", "wali1265"),
    'Lan [d?] [?] e': ("Lande", "ciac1237-lande"),
    "Desa Kambowa": ("Kambowa", None),
    "Kamboa": ("Kambowa", None),
    "Lipu": ("Lipu", "kiok1239-lipu"),
    "Lagundi (Konde)": ("Lagundi", "kiok1239-laun"),
    'Kel Bonegunu (a.k.a. Kioko)': ("Kioko", None),
    'Palowata (west Buton)': ("Palowata", "panc1247-palow"),
    "Lawele (east Buton)": ("Lawele", "kale1247-lawel"),
    "Kalende (east Buton)": ("Kalende", None),
    "Lambusango (west central Buton)": ("Kakenauwe", "panc1247-lambu"),
    "Desa Lawele": ("Lawele", "kale1247-lawel"),
    "Dusun Kalende, Desa Lawele": ("Lawele", "kale1247-lawel"),
    "Wasuemba/Labuandiri": ("Labuandiri", None),
    "Kakenauwe": ("Kakenauwe", "panc1247-kaken"),
    "Kapontori (Soropia)": ("Kapontori", None),
    "Waoleona": ("Waoleona", "panc1247-waole"),
    "Lawele": ("Lawele", "kale1247-lawel"),
    "Todanga": ("Todanga", "panc1247-todan"),
    "Wasuamba": ("Wasuamba", "panc1247-wasua"),
    "Lambusango": ("Lambusango", "panc1247-lambu"),
    "Kampeonaho": ("Kampeonaho", "panc1247-kampe"),
    "Watumotobhe": ("Watumotobhe", "panc1247-watum"),
    "Labundoua [within desa Lambelu]": ("Labundoua", "panc1247-labun"),
    "Desa Lawele": ("Kalende", None),
    "Lawele": ("Lawele", "kale1247-lawel"),
    "Kakenauwe": ("Kakenauwe", "panc1247-kaken"),
    "Todanga": ("Todanga", "panc1247-todan"),
    "Kolowa (east Muna) [Kecamatan Gu]": ("Gu", "guuu1237"),
    "Wasilonata (Mawasangka, west Muna)": ("Wasilonata", "muna1247-wasil"),
    "Katobengke (near Baubau)": ("Katobengke", None),
    "Lakudo (Kecamatan Gu)": ("Gu", "guuu1237"),
    "Mawasangka (Kecamatan Mawasangka)": ("Mawasangka", None),
    "Lombe (near Bombonawulu) (Kecamatan Gu)": ("Lombe", "muna1247-lombe"),
    "Bombonawulu (Kecamatan Gu)": ("Bombonawulu", "muna1247-bombo"),
    "Siompu (island next to south Buton)": ("Siompu", None),
    "Siompu desa Molona": ("Siompu", None),
    "Kadatuang (island next to south Buton)": ("Kadatua", None),
    "Bombonawulu": ("Bombonawulu", "muna1247-bombo"),
    "Gu": ("Gu", "guuu1237"),
    "Siompu": ("Siompu", None),
    "Wuna": ("Wuna", "muna1247-wuna"),
    "Bente": ("Bente", "muna1247-bente"),
    "Siompi [sic]": ("Siompu", None),
    "Katobengko": ("Katobengke", None),
    "Sida Mangura - Muna": ("Sida", "muna1247-sida"),
    "Talaga I - Siompu": ("Talaga", None),
    "Wakambangura - Wasilomata": ("Wakambangura", "muna1247-wakam"),
    "Lakaramba": ("Lakaramba", "muna1247-lakar"),
    "": ("Muna", "muna1247"),
    "Desa Kaimbulawa": ("Kaimbulawa", None),
    "Kamaru (east Buton)": ("Kamaru", None),
    "Baubau": ("Baubau", "woli1241-bauba"),
    "Kelurahan Baadia": ("Baubau", "woli1241-baadi"),
    "Kelurahan Bone Bone": ("Baubau", "woli1241-boneb"),
    "Kelurahan Talaga 1": ("Baubau", "woli1241-talag"),
    "ka, kb Kalao": ("Lambego", "kala1394-lambe"),
    "Lambego": ("Lambego", "kala1394-lambe"),
    "ly Laiyolo": ("Laiyolo", "nucl1577"),
    "lo Barang Barang (Loa')": ("Barang-Barang", None),
    "Laiyolo - Barang-Barang": ("Barang-Barang", None),
    "Bawa Lipu": ("Bawa Lipu", "wotu1240-bawal"),
    "wo Wotu": ("Wotu", None),
    "Bajo": ("Bajau", "indo1317"),
    "Bajau Kayoa": ("Kajoa", None),
    "Kulisusu (north Buton)": ("Kulisusu", None),
    "Moronene (Kabaena)": ("Kabaena", None),
    "Tolaki Konawe": ("Konawe", None),
    "Tolaki Mekongga": ("Mekongga", None),
}

new_sources = pybtex.database.BibliographyData()
new_lects = list(lr["LanguageTable"].iterdicts())
new_forms = list(lr["FormTable"].iterdicts())
new_form_id = max(int(f["ID"]) for f in new_forms) + 1

header = None
for row in xlrd.open_workbook(
        Path(__file__).parent /
        "Muna-Buton word lists/Buton Muna Wordlists (2017-07-11).xlsx").sheet_by_index(0).get_rows():
    row = [cell.value for cell in row]
    if row[1] == "Informant":
        row[0] = "Lect"
        header = row
        data_start = header.index("kepala")
        metadata = header[:data_start - 1]
        conceptlist = [concepts.get(g) for g in header[data_start:]]
    elif header and not row[4]:
        continue
    elif header:
        metadata = dict(zip(metadata, row))

        words = {c: value.split("/") for c, value in zip(conceptlist, row[data_start:])
                 if c
                 if value}

        metadata["Lect"], lect_id = alternative_names.get(metadata["Lect"], (metadata["Lect"], None))
        if lect_id:
            lect = gl.languoid(lect_id[:8])
        else:
            n, lects = search_langs(
                gl, lect_id[:8] if lect_id else metadata['Lect'])
            lect = gl.languoid(lects[0].id)
        print(metadata['Lect'], lect)
        p = lect
        try:
            while True:
                if p.latitude:
                    lat = p.latitude
                    lon = p.longitude
                    print(lat, lon)
                    break
                else:
                    p = p.parent
        except AttributeError:
            pass
        query = "Kecamatan " + metadata["Kecamatan"].strip("?") + ", Indonesia"
        location = geonames.geocode(query)
        try:
            assert -7 < location.latitude < -1
            assert 120 < location.longitude < 130
            lat = location.latitude
            lon = location.longitude
            print(lat, lon)
        except (AttributeError, AssertionError):
            print(query)
        lect_id = lect_id or lect.glottocode
        if lect_id not in [l["ID"] for l in new_lects]:
            new_lects.append({
                "ID": lect_id,
                "Name": metadata["Lect"],
                "Family": "Austronesian",
                "Latitude": lat,
                "Longitude": lon,
                "Region": get_region(lat, lon),
                "Glottocode": lect.glottocode,
                "Iso": metadata["EthCode"],
                "Culture": None,
                "Description": None,
                "Orthography": ["p/general"],
                "Comment": (metadata["Notes-classification"] or "")
                + "Locations estimated from Kecamatan and/or Glottolog"})

        source = metadata["Linguist / Source"]
        source_key = identifier(source)
        try:
            new_sources.add_entry(
                source_key,
                pybtex.database.Entry(
                    "incollection",
                    fields={"title": source,
                            "editor": "Mead, David",
                            "quality": metadata["Quality"]}))
        except pybtex.database.BibliographyDataError:
            pass

        for concept, forms in words.items():
            for form in forms:
                if form == "—":
                    # Missing form
                    continue
                new_forms.append({
                    "ID": str(new_form_id),
                    "Lect_ID": lect_id,
                    "Concept_ID": concept,
                    "Form_according_to_Source": form,
                    "Source": [source_key]
                })
                new_form_id += 1

lr["LanguageTable"].write(new_lects)
lr["FormTable"].write(new_forms)
lr.sources.add(new_sources)
lr.write_sources()
