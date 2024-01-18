#  Šī projekta izstrādi veica pirmā kursa studenti.(Maksims Mieriņš 11. grupa(231RDB121) , Adrians Kobriņecs 13. grupa(231RDB061)).
# LŪGUMS: PALAIST KODU PROGRAMMĀ VISUAL STUDIO 
# Projekta mērķis:
Ideju mums deva cilveks, kurš ir ļoti ieinteresēts ainavu dizainā un ar mīlestību veido unikālus dārza projektus. Viņa darbā radās viens problēma - meklēt ekonomiski izdevīgas augu cenas, lai īstenotu savas radošās idejas.
Mēs izvēlējāmies izveidot kodu dizaineriem un visiem, kas interesējas par augiem, piedāvājot intuitīvu un ērtu rīku, lai salīdzinātu augu cenas ar diviem zināmākajiem augu pārdošanas vietnēm Latvijā. Mērķis ir nodrošināt iespēju viegli un efektīvi izvēlēties piemērotus augus savām projektu idejām, ņemot vērā individuālās preferences un profesionālās vajadzības, kā arī ekonomiski izdevīgi iegādāties augus sev.
# Kodu darbība
Projekta realizācija ir veidota, izmantojot mūsdienīgas bibliotēkas, kuras tika apgūtas pusgada laikā, kā arī jaunās bibliotēkas, ko mēs esam apguvuši, strādājot pie šī projekta nepieciešamajiem uzdevumiem. 
Pirms tam mēs veicām rūpīgu izpēti par dažādām bibliotēkām un tehnoloģijām, kas tiek izmantotas automatizācijas jomā, lai noteiktu labāko rīku komplektu projekta uzdevumu risināšanai. Ņemot vērā izvēlētās tehnoloģijas, tika izstrādāts projekta kods, kas ietver automatizācijas funkcijas, nodrošinot efektīvu un precīzu uzdevumu izpildi. Turklāt tika ieviestas optimizācijas, lai uzlabotu veiktspēju. Testēšanas procesā tika pārbaudīts kods stabilitātei, pielāgojamībai un atbilstībai noteiktajiem prasījumiem. Pamatojoties uz iegūtajiem rezultātiem, tika veiktas korekcijas un papildinājumi, lai nodrošinātu beztraucētu darbību.
# Bibliotēkas:
selenium: Šī bibliotēka ļauj automatizēt pārlūka darbības un veikt darbības tīmeklī. Tā ir bieži izmantota testēšanā un datu iegūšanā no tīmekļa lapām, piemēram, meklējot un aizpildot veidlapas vai noklikšķinot uz pogām.
time: Šī bibliotēka nodrošina funkcijas laika aizkavēšanai vai pauzēm programmā. 
sys: Tiek izmantots, lai pārtrauktu programmas izpildi, nododot atpakaļ izpildes rezultātu.

# Secinājums:
Pēc veiksmīgas koda izstrādes un ieviešanas rezultāti pārsniedza mūsu cerības, piedāvājot daudz vairāk nekā vienkāršu cenu salīdzinājumu. Mēs redzam, kā mūsu projekts kļūst par neatsiešamu daļu no ainavu dizaineru radošā procesa.
Programma veiksmīgi samazina meklēšanas laiku: mēs esam pārliecināti, ka katrs stunda, kuru ainavu dizainers ietaupa, izmantojot mūsu tīmekļa lietojumprogrammu, kļūst par vēl vienu krāsainu elementu viņa projektos. Ietaupītais laiks nozīmē vairāk iespēju īstenot radošās idejas.
# Ieteikumi koda palaišanai un tā iespējās
Mūsu kods sniedz vairākas galvenās funkcijas. Pirmkārt, tas ļauj lietotājiem ievadīt auga nosaukumu jebkurā formātā un saņemt informāciju par tā cenu no vairākiem tirgotājiem Latvijā.
Otrkārt, mēs nodrošinājām dinamisku lapu atjaunošanu, kas ļauj lietotājiem pārlūkot plašu augu klāstu, iegūstot jaunāko informāciju. Tas nozīmē, ka mūsu projekts vienmēr piedāvā svaigu un aktuālu informāciju par pieejamajiem augiem tirgū.
1) ievadot noteikta auga nosaukumu, saņemam tā cenu no divām vietnēm
2) Ievadot auga vispārīgo nosaukumu, visas iespējamās šī auga sugas saņemam ar sarakstu, jo kods pats pāršķirsta visas lapas un demonstrē jau savu sarakstu output.txt faila ar tādu pašu augu nosaukumu, kādu esat ievadījis, no abām vietnēm turpat arī rakstīts no kurienes šādas cenas. Jo mājaslapas meklēšana reizēm atklāj pilnīgi ko citu
3) ja ievads bija nepareizs, tad kods izsniedz kļūdu "Nav tadas preces.", ka neatrada to, ko ievadījāt,bet tāpat ir tāda lieta, ka vienā mājas lapā parāda, ka šobrīd nav pieejama prece bet tā ir un raksta Nav pārdošanā,savukārt no otrās mājas lapas raksta, ka pieprasījums ir izpildīts un to, ko tur ir parādīs!
# Ja vēlaties uzreiz sākt koda darbību, lūk, saraksts ar dažādām koda situācijām, tāpēc, ja vēlaties redzēt visas funkcijas, ieteicams izmantot visus šos nosaukumus pēc kārtas:
# 1) (Ehinācija / EHINĀCIJA / EhInĀcIjA / Hosta/ DIENZIEDE) ir gan tur, gan tur, bet uz https://www.baltezers.lv/ Nav pārdošanā
# 2) (Japānas spireja / Spiraea) pirmajā mājas lapā ir divi dažādi viena auga nosaukumā, īsas varat izmantot jebkuru nosaukumu no šiem un viņš tik un tā atradīs šīs preces! 
# 3) (Dienziede ‘Betty Ford’ / Berberis thunbergii 'Chiquita') precīzi nosaukumi no vienas un otras vietnes, kods atrod visus iespējamos variantus tas ir viens vai tur vai tur
# 4) (ievadiet jebkuru burtu kopu / ok4390k / SDFK) kods meklēs nosaukuma datus bet neko neatradīs un rakstīs: (Nav tadas preces.)


