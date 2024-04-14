import pytest
from fetch_current_events import remove_pictured

test_data = [

(
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles&nbsp;III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a> <i>(both pictured)</i> of the United Kingdom <b><a href="/wiki/Coronation_of_Charles_III_and_Camilla" title="Coronation of Charles III and Camilla">are crowned</a></b> at <a href="/wiki/Westminster_Abbey" title="Westminster Abbey">Westminster Abbey</a> in London.</li>',  
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles&nbsp;III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a> of the United Kingdom <b><a href="/wiki/Coronation_of_Charles_III_and_Camilla" title="Coronation of Charles III and Camilla">are crowned</a></b> at <a href="/wiki/Westminster_Abbey" title="Westminster Abbey">Westminster Abbey</a> in London.</li>'  
),
(
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles&nbsp;III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a> <i>(both pictured)</i>.<li>',  
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles&nbsp;III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a>.<li>'
),
(
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles&nbsp;III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a> <i>(pictured)</i>.<li>',  
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles&nbsp;III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a>.<li>' 
),
(
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a> <i>(pictured)</i> of the United Kingdom <b><a href="/wiki/Coronation_of_Charles_III_and_Camilla" title="Coronation of Charles III and Camilla">are crowned</a></b> at <a href="/wiki/Westminster_Abbey" title="Westminster Abbey">Westminster Abbey</a> in London.</li>',  
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a> of the United Kingdom <b><a href="/wiki/Coronation_of_Charles_III_and_Camilla" title="Coronation of Charles III and Camilla">are crowned</a></b> at <a href="/wiki/Westminster_Abbey" title="Westminster Abbey">Westminster Abbey</a> in London.</li>'  
),
(
'<li>Nine people, including eight children, <b><a href="/wiki/Vladislav_Ribnikar_Elementary_School_shooting" title="Vladislav Ribnikar Elementary School shooting">are killed</a></b> in an elementary school <i>(pictured)</i> shooting in <a href="/wiki/Belgrade" title="Belgrade">Belgrade</a>, Serbia.</li>',  
'<li>Nine people, including eight children, <b><a href="/wiki/Vladislav_Ribnikar_Elementary_School_shooting" title="Vladislav Ribnikar Elementary School shooting">are killed</a></b> in an elementary school shooting in <a href="/wiki/Belgrade" title="Belgrade">Belgrade</a>, Serbia.</li>'  
),
(
'<li><a href="/wiki/Ding_Liren" title="Ding Liren">Ding Liren</a> <i>(pictured)</i> defeats <a href="/wiki/Ian_Nepomniachtchi" title="Ian Nepomniachtchi">Ian Nepomniachtchi</a> to win <b><a href="/wiki/World_Chess_Championship_2023" title="World Chess Championship 2023">the World Chess Championship</a></b>.</li>',  
'<li><a href="/wiki/Ding_Liren" title="Ding Liren">Ding Liren</a> defeats <a href="/wiki/Ian_Nepomniachtchi" title="Ian Nepomniachtchi">Ian Nepomniachtchi</a> to win <b><a href="/wiki/World_Chess_Championship_2023" title="World Chess Championship 2023">the World Chess Championship</a></b>.</li>'  
),
(
'<li>Finland <b><a href="/wiki/Finland%E2%80%93NATO_relations" title="Finland–NATO relations">joins</a></b> <a href="/wiki/NATO" title="NATO">NATO</a> as its <a href="/wiki/Enlargement_of_NATO" title="Enlargement of NATO">31st member</a> <i>(flags pictured)</i>.</li>',  
'<li>Finland <b><a href="/wiki/Finland%E2%80%93NATO_relations" title="Finland–NATO relations">joins</a></b> <a href="/wiki/NATO" title="NATO">NATO</a> as its <a href="/wiki/Enlargement_of_NATO" title="Enlargement of NATO">31st member</a>.</li>'  
),
(
'<li><b><a href="/wiki/Tornado_outbreak_of_March_24%E2%80%9327,_2023" title="Tornado outbreak of March 24–27, 2023">A tornado outbreak</a></b> <i>(damage pictured)</i> in <a href="/wiki/Mississippi" title="Mississippi">Mississippi</a> and <a href="/wiki/Alabama" title="Alabama">Alabama</a>, United States, leaves at least 24 people dead.</li>',  
'<li><b><a href="/wiki/Tornado_outbreak_of_March_24%E2%80%9327,_2023" title="Tornado outbreak of March 24–27, 2023">A tornado outbreak</a></b> in <a href="/wiki/Mississippi" title="Mississippi">Mississippi</a> and <a href="/wiki/Alabama" title="Alabama">Alabama</a>, United States, leaves at least 24 people dead.</li>'  
),
(
'<li>In <a href="/wiki/American_football" title="American football">American football</a>, the <a href="/wiki/Kansas_City_Chiefs" title="Kansas City Chiefs">Kansas City Chiefs</a> defeat the <a href="/wiki/Philadelphia_Eagles" title="Philadelphia Eagles">Philadelphia Eagles</a> in <b><a href="/wiki/Super_Bowl_LVII" title="Super Bowl LVII">the Super Bowl</a></b> <i>(<a href="/wiki/Super_Bowl_Most_Valuable_Player_Award" title="Super Bowl Most Valuable Player Award">MVP</a> <a href="/wiki/Patrick_Mahomes" title="Patrick Mahomes">Patrick Mahomes</a> pictured)</i>.</li>',  
'<li>In <a href="/wiki/American_football" title="American football">American football</a>, the <a href="/wiki/Kansas_City_Chiefs" title="Kansas City Chiefs">Kansas City Chiefs</a> defeat the <a href="/wiki/Philadelphia_Eagles" title="Philadelphia Eagles">Philadelphia Eagles</a> in <b><a href="/wiki/Super_Bowl_LVII" title="Super Bowl LVII">the Super Bowl</a></b>.</li>'  
),
(
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles&nbsp;III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a> (both pictured) of the United Kingdom <b><a href="/wiki/Coronation_of_Charles_III_and_Camilla" title="Coronation of Charles III and Camilla">are crowned</a></b> at <a href="/wiki/Westminster_Abbey" title="Westminster Abbey">Westminster Abbey</a> in London.</li>',  
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles&nbsp;III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a> of the United Kingdom <b><a href="/wiki/Coronation_of_Charles_III_and_Camilla" title="Coronation of Charles III and Camilla">are crowned</a></b> at <a href="/wiki/Westminster_Abbey" title="Westminster Abbey">Westminster Abbey</a> in London.</li>'  
),
(
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles&nbsp;III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a> (both pictured).<li>',  
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles&nbsp;III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a>.<li>'  
),
(
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles&nbsp;III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a> (pictured).<li>',  
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles&nbsp;III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a>.<li>'  
),
(
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a> (pictured) of the United Kingdom <b><a href="/wiki/Coronation_of_Charles_III_and_Camilla" title="Coronation of Charles III and Camilla">are crowned</a></b> at <a href="/wiki/Westminster_Abbey" title="Westminster Abbey">Westminster Abbey</a> in London.</li>',  
'<li><a href="/wiki/Charles_III" title="Charles III">King Charles III</a> and <a href="/wiki/Queen_Camilla" title="Queen Camilla">Queen Camilla</a> of the United Kingdom <b><a href="/wiki/Coronation_of_Charles_III_and_Camilla" title="Coronation of Charles III and Camilla">are crowned</a></b> at <a href="/wiki/Westminster_Abbey" title="Westminster Abbey">Westminster Abbey</a> in London.</li>'  
),
(
'<li>Nine people, including eight children, <b><a href="/wiki/Vladislav_Ribnikar_Elementary_School_shooting" title="Vladislav Ribnikar Elementary School shooting">are killed</a></b> in an elementary school (pictured) shooting in <a href="/wiki/Belgrade" title="Belgrade">Belgrade</a>, Serbia.</li>',  
'<li>Nine people, including eight children, <b><a href="/wiki/Vladislav_Ribnikar_Elementary_School_shooting" title="Vladislav Ribnikar Elementary School shooting">are killed</a></b> in an elementary school shooting in <a href="/wiki/Belgrade" title="Belgrade">Belgrade</a>, Serbia.</li>'  
),
(
'<li><a href="/wiki/Ding_Liren" title="Ding Liren">Ding Liren</a> (pictured) defeats <a href="/wiki/Ian_Nepomniachtchi" title="Ian Nepomniachtchi">Ian Nepomniachtchi</a> to win <b><a href="/wiki/World_Chess_Championship_2023" title="World Chess Championship 2023">the World Chess Championship</a></b>.</li>',  
'<li><a href="/wiki/Ding_Liren" title="Ding Liren">Ding Liren</a> defeats <a href="/wiki/Ian_Nepomniachtchi" title="Ian Nepomniachtchi">Ian Nepomniachtchi</a> to win <b><a href="/wiki/World_Chess_Championship_2023" title="World Chess Championship 2023">the World Chess Championship</a></b>.</li>'  
),
(
'<li>Finland <b><a href="/wiki/Finland%E2%80%93NATO_relations" title="Finland–NATO relations">joins</a></b> <a href="/wiki/NATO" title="NATO">NATO</a> as its <a href="/wiki/Enlargement_of_NATO" title="Enlargement of NATO">31st member</a> (flags pictured).</li>',  
'<li>Finland <b><a href="/wiki/Finland%E2%80%93NATO_relations" title="Finland–NATO relations">joins</a></b> <a href="/wiki/NATO" title="NATO">NATO</a> as its <a href="/wiki/Enlargement_of_NATO" title="Enlargement of NATO">31st member</a>.</li>'  
),
(
'<li><b><a href="/wiki/Tornado_outbreak_of_March_24%E2%80%9327,_2023" title="Tornado outbreak of March 24–27, 2023">A tornado outbreak</a></b> (damage pictured) in <a href="/wiki/Mississippi" title="Mississippi">Mississippi</a> and <a href="/wiki/Alabama" title="Alabama">Alabama</a>, United States, leaves at least 24 people dead.</li>',  
'<li><b><a href="/wiki/Tornado_outbreak_of_March_24%E2%80%9327,_2023" title="Tornado outbreak of March 24–27, 2023">A tornado outbreak</a></b> in <a href="/wiki/Mississippi" title="Mississippi">Mississippi</a> and <a href="/wiki/Alabama" title="Alabama">Alabama</a>, United States, leaves at least 24 people dead.</li>'  
),
(
'<li>In <a href="/wiki/American_football" title="American football">American football</a>, the <a href="/wiki/Kansas_City_Chiefs" title="Kansas City Chiefs">Kansas City Chiefs</a> defeat the <a href="/wiki/Philadelphia_Eagles" title="Philadelphia Eagles">Philadelphia Eagles</a> in <b><a href="/wiki/Super_Bowl_LVII" title="Super Bowl LVII">the Super Bowl</a></b> (<a href="/wiki/Super_Bowl_Most_Valuable_Player_Award" title="Super Bowl Most Valuable Player Award">MVP</a> <a href="/wiki/Patrick_Mahomes" title="Patrick Mahomes">Patrick Mahomes</a> pictured).</li>',  
'<li>In <a href="/wiki/American_football" title="American football">American football</a>, -tmp- the <a href="/wiki/Kansas_City_Chiefs" title="Kansas City Chiefs">Kansas City Chiefs</a> defeat the <a href="/wiki/Philadelphia_Eagles" title="Philadelphia Eagles">Philadelphia Eagles</a> in <b><a href="/wiki/Super_Bowl_LVII" title="Super Bowl LVII">the Super Bowl</a></b>.</li>'  
),
(
'<li>The final <b><a href="/wiki/Boeing_747" title="Boeing 747">Boeing 747</a></b> (prototype pictured) to be built rolls off the assembly line at <a href="/wiki/Everett,_Washington" title="Everett, Washington">Everett, Washington</a>, United States.</li>',  
'<li>The final <b><a href="/wiki/Boeing_747" title="Boeing 747">Boeing 747</a></b> to be built rolls off the assembly line at <a href="/wiki/Everett,_Washington" title="Everett, Washington">Everett, Washington</a>, United States.</li>'  
),
(
'<li>The final <b><a href="/wiki/Boeing_747" title="Boeing 747">Boeing 747</a></b> <i>(prototype pictured)</i> to be built rolls off the assembly line at <a href="/wiki/Everett,_Washington" title="Everett, Washington">Everett, Washington</a>, United States.</li>',  
'<li>The final <b><a href="/wiki/Boeing_747" title="Boeing 747">Boeing 747</a></b> to be built rolls off the assembly line at <a href="/wiki/Everett,_Washington" title="Everett, Washington">Everett, Washington</a>, United States.</li>'  
),
(
'<li>In the United States, six people are killed in <b><a href="/wiki/2022_Dallas_airshow_mid-air_collision" title="2022 Dallas airshow mid-air collision">a mid-air collision</a></b> <i>(aircraft </i><a href="/wiki/Texas_Raiders" title="Texas Raiders">Texas Raiders</a><i> pictured)</i> at an air show in <a href="/wiki/Dallas" title="Dallas">Dallas</a>.</li>',  
'<li>In the United States, six people are killed in <b><a href="/wiki/2022_Dallas_airshow_mid-air_collision" title="2022 Dallas airshow mid-air collision">a mid-air collision</a></b> at an air show in <a href="/wiki/Dallas" title="Dallas">Dallas</a>.</li>'  
),
(
'<li>In the United States, six people are killed in <b><a href="/wiki/2022_Dallas_airshow_mid-air_collision" title="2022 Dallas airshow mid-air collision">a mid-air collision</a></b> <i>(one aircraft pictured)</i> at an air show in <a href="/wiki/Dallas" title="Dallas">Dallas</a>.</li>',  
'<li>In the United States, six people are killed in <b><a href="/wiki/2022_Dallas_airshow_mid-air_collision" title="2022 Dallas airshow mid-air collision">a mid-air collision</a></b> at an air show in <a href="/wiki/Dallas" title="Dallas">Dallas</a>.</li>'  
),
(
'<li>In baseball, the <a href="/wiki/Orix_Buffaloes" title="Orix Buffaloes">Orix Buffaloes</a> defeat the <a href="/wiki/Tokyo_Yakult_Swallows" title="Tokyo Yakult Swallows">Tokyo Yakult Swallows</a> to win <b><a href="/wiki/2022_Japan_Series" title="2022 Japan Series">the Japan Series</a></b> <i>(<a href="/wiki/Japan_Series_Most_Valuable_Player_Award" title="Japan Series Most Valuable Player Award">MVP</a> <a href="/wiki/Yutaro_Sugimoto" title="Yutaro Sugimoto">Yutaro Sugimoto</a> pictured)</i>.</li>',  
'<li>In baseball, the <a href="/wiki/Orix_Buffaloes" title="Orix Buffaloes">Orix Buffaloes</a> defeat the <a href="/wiki/Tokyo_Yakult_Swallows" title="Tokyo Yakult Swallows">Tokyo Yakult Swallows</a> to win <b><a href="/wiki/2022_Japan_Series" title="2022 Japan Series">the Japan Series</a></b>.</li>'  
),
(
'<li>The <a href="/wiki/Centre-right_coalition" class="mw-redirect" title="Centre-right coalition">centre-right coalition</a> wins a majority of seats in the <b><a href="/wiki/2022_Italian_general_election" title="2022 Italian general election">Italian general election</a></b> <i>(<a href="/wiki/Brothers_of_Italy" title="Brothers of Italy">Brothers of Italy</a> leader <a href="/wiki/Giorgia_Meloni" title="Giorgia Meloni">Giorgia Meloni</a> pictured)</i>.</li>',  
'<li>The <a href="/wiki/Centre-right_coalition" class="mw-redirect" title="Centre-right coalition">centre-right coalition</a> wins a majority of seats in the <b><a href="/wiki/2022_Italian_general_election" title="2022 Italian general election">Italian general election</a></b>.</li>'  
),
(
'<li>In <a href="/wiki/Australian_rules_football" title="Australian rules football">Australian rules football</a>, <a href="/wiki/Geelong_Football_Club" title="Geelong Football Club">Geelong</a> defeat the <a href="/wiki/Sydney_Swans" title="Sydney Swans">Sydney Swans</a> to win <b><a href="/wiki/2022_AFL_Grand_Final" title="2022 AFL Grand Final">the AFL Grand Final</a></b> <i>(<a href="/wiki/Norm_Smith_Medal" title="Norm Smith Medal">Norm Smith Medal</a> winner <a href="/wiki/Isaac_Smith_(footballer)" title="Isaac Smith (footballer)">Isaac Smith</a> pictured)</i>.</li>',  
'<li>In <a href="/wiki/Australian_rules_football" title="Australian rules football">Australian rules football</a>, <a href="/wiki/Geelong_Football_Club" title="Geelong Football Club">Geelong</a> defeat the <a href="/wiki/Sydney_Swans" title="Sydney Swans">Sydney Swans</a> to win <b><a href="/wiki/2022_AFL_Grand_Final" title="2022 AFL Grand Final">the AFL Grand Final</a></b>.</li>'  
),
(
'<li>In <a href="/wiki/Association_football" title="Association football">association football</a>, <a href="/wiki/Manchester_City_F.C." title="Manchester City F.C.">Manchester City</a> defeat <a href="/wiki/Inter_Milan" title="Inter Milan">Inter Milan</a> to win the <b><a href="/wiki/2023_UEFA_Champions_League_final" title="2023 UEFA Champions League final">UEFA Champions League final</a></b> <i>(man of the match <a href="/wiki/Rodri_(footballer,_born_1996)" title="Rodri (footballer, born 1996)">Rodri</a> pictured)</i>.</li>',  
'<li>In <a href="/wiki/Association_football" title="Association football">association football</a>, <a href="/wiki/Manchester_City_F.C." title="Manchester City F.C.">Manchester City</a> defeat <a href="/wiki/Inter_Milan" title="Inter Milan">Inter Milan</a> to win the <b><a href="/wiki/2023_UEFA_Champions_League_final" title="2023 UEFA Champions League final">UEFA Champions League final</a></b>.</li>'  
),
(
'<li>In <a href="/wiki/Basketball" title="Basketball">basketball</a>, the <a href="/wiki/Denver_Nuggets" title="Denver Nuggets">Denver Nuggets</a> defeat the <a href="/wiki/Miami_Heat" title="Miami Heat">Miami Heat</a> to win <b><a href="/wiki/2023_NBA_Finals" title="2023 NBA Finals">the NBA Finals</a></b> <i>(<a href="/wiki/NBA_Finals_Most_Valuable_Player_Award" title="NBA Finals Most Valuable Player Award">MVP</a> <a href="/wiki/Nikola_Joki%C4%87" title="Nikola Jokić">Nikola Jokić</a> pictured)</i>.</li>',  
'<li>In <a href="/wiki/Basketball" title="Basketball">basketball</a>, the <a href="/wiki/Denver_Nuggets" title="Denver Nuggets">Denver Nuggets</a> defeat the <a href="/wiki/Miami_Heat" title="Miami Heat">Miami Heat</a> to win <b><a href="/wiki/2023_NBA_Finals" title="2023 NBA Finals">the NBA Finals</a></b>.</li>'  
),
(
'<li><a href="/wiki/Loreen_(singer)" title="Loreen (singer)">Loreen</a> <i>(pictured)</i> <a href="/wiki/Sweden_in_the_Eurovision_Song_Contest" title="Sweden in the Eurovision Song Contest">of Sweden</a> wins <b><a href="/wiki/Eurovision_Song_Contest_2023" title="Eurovision Song Contest 2023">the Eurovision Song Contest</a></b> with the song "<a href="/wiki/Tattoo_(Loreen_song)" title="Tattoo (Loreen song)">Tattoo</a>", becoming the first woman to win the contest twice.</li>',  
'<li><a href="/wiki/Loreen_(singer)" title="Loreen (singer)">Loreen</a> <a href="/wiki/Sweden_in_the_Eurovision_Song_Contest" title="Sweden in the Eurovision Song Contest">of Sweden</a> wins <b><a href="/wiki/Eurovision_Song_Contest_2023" title="Eurovision Song Contest 2023">the Eurovision Song Contest</a></b> with the song "<a href="/wiki/Tattoo_(Loreen_song)" title="Tattoo (Loreen song)">Tattoo</a>", becoming the first woman to win the contest twice.</li>'  
),
(
'<li>In <a href="/wiki/Golf" title="Golf">golf</a>, <a href="/wiki/Wyndham_Clark" title="Wyndham Clark">Wyndham Clark</a> <i>(pictured)</i> wins <b><a href="/wiki/2023_U.S._Open_(golf)" title="2023 U.S. Open (golf)">the U.S. Open</a></b>.</li>',  
'<li>In <a href="/wiki/Golf" title="Golf">golf</a>, <a href="/wiki/Wyndham_Clark" title="Wyndham Clark">Wyndham Clark</a> wins <b><a href="/wiki/2023_U.S._Open_(golf)" title="2023 U.S. Open (golf)">the U.S. Open</a></b>.</li>'  
),
(
'<li>In Russia, the <a href="/wiki/Wagner_Group" title="Wagner Group">Wagner mercenary group</a> <i>(leader <a href="/wiki/Yevgeny_Prigozhin" title="Yevgeny Prigozhin">Yevgeny Prigozhin</a> pictured)</i> <b><a href="/wiki/Wagner_Group_rebellion" title="Wagner Group rebellion">rebels</a></b> against the government.</li>',  
'<li>In Russia, the <a href="/wiki/Wagner_Group" title="Wagner Group">Wagner mercenary group</a> <b><a href="/wiki/Wagner_Group_rebellion" title="Wagner Group rebellion">rebels</a></b> against the government.</li>'  
),
(
'<li>In Portugal, the <a href="/wiki/Democratic_Alliance_(Portugal,_2024)" title="Democratic Alliance (Portugal, 2024)">Democratic Alliance</a> <i>(leader <a href="/wiki/Lu%C3%ADs_Montenegro" title="Luís Montenegro">Luís Montenegro</a> pictured)</i> wins the most seats in <b><a href="/wiki/2024_Portuguese_legislative_election" title="2024 Portuguese legislative election">a snap legislative election</a></b>.</li>',
'<li>In Portugal, the <a href="/wiki/Democratic_Alliance_(Portugal,_2024)" title="Democratic Alliance (Portugal, 2024)">Democratic Alliance</a> wins the most seats in <b><a href="/wiki/2024_Portuguese_legislative_election" title="2024 Portuguese legislative election">a snap legislative election</a></b>.</li>',
),
(
'<li>Sweden <i>(highlighted)</i> becomes <b><a href="/wiki/Sweden%E2%80%93NATO_relations" title="Sweden–NATO relations">the thirty-second member state</a></b>  of <a href="/wiki/NATO" title="NATO">NATO</a>.</li>',
'<li>Sweden becomes <b><a href="/wiki/Sweden%E2%80%93NATO_relations" title="Sweden–NATO relations">the thirty-second member state</a></b> of <a href="/wiki/NATO" title="NATO">NATO</a>.</li>',
),
(
'<li>In <b><a href="/wiki/2023_Serbian_parliamentary_election" title="2023 Serbian parliamentary election">the parliamentary election</a></b>, the <a href="/wiki/Serbian_Progressive_Party" title="Serbian Progressive Party">Serbian Progressive Party</a> <i>(leader <a href="/wiki/Milo%C5%A1_Vu%C4%8Devi%C4%87" title="Miloš Vučević">Miloš Vučević</a> pictured)</i> regains its <a href="/wiki/Majority_government" title="Majority government">parliamentary majority</a> in the <a href="/wiki/National_Assembly_(Serbia)" title="National Assembly (Serbia)">National Assembly</a>.</li>',
'<li>In <b><a href="/wiki/2023_Serbian_parliamentary_election" title="2023 Serbian parliamentary election">the parliamentary election</a></b>, the <a href="/wiki/Serbian_Progressive_Party" title="Serbian Progressive Party">Serbian Progressive Party</a> regains its <a href="/wiki/Majority_government" title="Majority government">parliamentary majority</a> in the <a href="/wiki/National_Assembly_(Serbia)" title="National Assembly (Serbia)">National Assembly</a>.</li>',
),
(
'<li><b><a href="/wiki/Hurricane_Otis" title="Hurricane Otis">Hurricane Otis</a></b> <i>(satellite image shown)</i> makes landfall near <a href="/wiki/Acapulco" title="Acapulco">Acapulco</a>, Mexico, leaving at least 39 people dead.</li>',
'<li><b><a href="/wiki/Hurricane_Otis" title="Hurricane Otis">Hurricane Otis</a></b> makes landfall near <a href="/wiki/Acapulco" title="Acapulco">Acapulco</a>, Mexico, leaving at least 39 people dead.</li>',
)
]

@pytest.mark.parametrize("input_html, expected_output", test_data)
def test_remove_pictured(input_html, expected_output):
    assert remove_pictured(input_html) == expected_output