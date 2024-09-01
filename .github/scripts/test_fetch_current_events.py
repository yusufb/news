import pytest
from fetch_current_events import remove_pictured

test_data = [

(
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a> <i>(both pictured)</i> of Wonderland <b><a href="/wiki/Crowning_of_the_Queen_of_Hearts" title="Crowning of the Queen of Hearts">are crowned</a></b> at <a href="/wiki/Tulgey_Wood" title="Tulgey Wood">Tulgey Wood</a> in Wonderland.</li>',  
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a> of Wonderland <b><a href="/wiki/Crowning_of_the_Queen_of_Hearts" title="Crowning of the Queen of Hearts">are crowned</a></b> at <a href="/wiki/Tulgey_Wood" title="Tulgey Wood">Tulgey Wood</a> in Wonderland.</li>'  
),
(
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a> <i>(both pictured)</i>.<li>',  
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a>.<li>'
),
(
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a> <i>(pictured)</i>.<li>',  
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a>.<li>' 
),
(
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a> <i>(pictured)</i> of Wonderland <b><a href="/wiki/Crowning_of_the_Queen_of_Hearts" title="Crowning of the Queen of Hearts">are crowned</a></b> at <a href="/wiki/Tulgey_Wood" title="Tulgey Wood">Tulgey Wood</a> in Wonderland.</li>',  
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a> of Wonderland <b><a href="/wiki/Crowning_of_the_Queen_of_Hearts" title="Crowning of the Queen of Hearts">are crowned</a></b> at <a href="/wiki/Tulgey_Wood" title="Tulgey Wood">Tulgey Wood</a> in Wonderland.</li>'  
),
(
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a> (both pictured) of Wonderland <b><a href="/wiki/Crowning_of_the_Queen_of_Hearts" title="Crowning of the Queen of Hearts">are crowned</a></b> at <a href="/wiki/Tulgey_Wood" title="Tulgey Wood">Tulgey Wood</a> in Wonderland.</li>',  
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a> of Wonderland <b><a href="/wiki/Crowning_of_the_Queen_of_Hearts" title="Crowning of the Queen of Hearts">are crowned</a></b> at <a href="/wiki/Tulgey_Wood" title="Tulgey Wood">Tulgey Wood</a> in Wonderland.</li>'  
),
(
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a> (both pictured).<li>',  
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a>.<li>'  
),
(
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a> (pictured).<li>',  
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a>.<li>'  
),
(
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a> (pictured) of Wonderland <b><a href="/wiki/Crowning_of_the_Queen_of_Hearts" title="Crowning of the Queen of Hearts">are crowned</a></b> at <a href="/wiki/Tulgey_Wood" title="Tulgey Wood">Tulgey Wood</a> in Wonderland.</li>',  
'<li><a href="/wiki/King_of_Hearts" title="King of Hearts">King of Hearts</a> and <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a> of Wonderland <b><a href="/wiki/Crowning_of_the_Queen_of_Hearts" title="Crowning of the Queen of Hearts">are crowned</a></b> at <a href="/wiki/Tulgey_Wood" title="Tulgey Wood">Tulgey Wood</a> in Wonderland.</li>'  
),
(
'<li>Nine people, including eight children, <b><a href="/wiki/Mad_Hatters_Tea_Party" title="Mad Hatters Tea Party">attend a delightful tea party</a></b> in an enchanted school <i>(pictured)</i> in <a href="/wiki/Wonderland" title="Wonderland">Wonderland</a>.</li>',  
'<li>Nine people, including eight children, <b><a href="/wiki/Mad_Hatters_Tea_Party" title="Mad Hatters Tea Party">attend a delightful tea party</a></b> in an enchanted school in <a href="/wiki/Wonderland" title="Wonderland">Wonderland</a>.</li>'  
),
(
'<li><a href="/wiki/Dormouse" title="Dormouse">Dormouse</a> <i>(pictured)</i> defeats <a href="/wiki/March_Hare" title="March Hare">March Hare</a> to win <b><a href="/wiki/Wonderland_Chess_Championship" title="Wonderland Chess Championship">the Wonderland Chess Championship</a></b>.</li>',  
'<li><a href="/wiki/Dormouse" title="Dormouse">Dormouse</a> defeats <a href="/wiki/March_Hare" title="March Hare">March Hare</a> to win <b><a href="/wiki/Wonderland_Chess_Championship" title="Wonderland Chess Championship">the Wonderland Chess Championship</a></b>.</li>'  
),
(
'<li>The White Rabbit <b><a href="/wiki/Wonderland_Explorers_Club" title="Wonderland Explorers Club">joins</a></b> the <a href="/wiki/Queen_of_Hearts_Court" title="Queen of Hearts Court">Queen of Hearts Court</a> as its <a href="/wiki/Wonderland_Honor_Guard" title="Wonderland Honor Guard">31st member</a> <i>(flags pictured)</i>.</li>',  
'<li>The White Rabbit <b><a href="/wiki/Wonderland_Explorers_Club" title="Wonderland Explorers Club">joins</a></b> the <a href="/wiki/Queen_of_Hearts_Court" title="Queen of Hearts Court">Queen of Hearts Court</a> as its <a href="/wiki/Wonderland_Honor_Guard" title="Wonderland Honor Guard">31st member</a>.</li>'  
),
(
'<li><b><a href="/wiki/Tulgey_Wood_Windstorm" title="Tulgey Wood Windstorm">A whimsical windstorm</a></b> <i>(damage pictured)</i> in <a href="/wiki/Tulgey_Wood" title="Tulgey Wood">Tulgey Wood</a> and <a href="/wiki/Looking_Glass_House" title="Looking Glass House">Looking Glass House</a>, Wonderland, brings magical surprises.</li>',  
'<li><b><a href="/wiki/Tulgey_Wood_Windstorm" title="Tulgey Wood Windstorm">A whimsical windstorm</a></b> in <a href="/wiki/Tulgey_Wood" title="Tulgey Wood">Tulgey Wood</a> and <a href="/wiki/Looking_Glass_House" title="Looking Glass House">Looking Glass House</a>, Wonderland, brings magical surprises.</li>'  
),
(
'<li>In the Wonderland Games, the <a href="/wiki/Chessboard" title="Chessboard">Red Knights</a> defeat the <a href="/wiki/Chessboard" title="Chessboard">White Knights</a> in <b><a href="/wiki/Wonderland_Championship" title="Wonderland Championship">the Wonderland Championship</a></b> <i>(<a href="/wiki/Champion_of_Hearts" title="Champion of Hearts">Champion of Hearts</a> <a href="/wiki/Red_King" title="Red King">Red King</a> pictured)</i>.</li>',  
'<li>In the Wonderland Games, the <a href="/wiki/Chessboard" title="Chessboard">Red Knights</a> defeat the <a href="/wiki/Chessboard" title="Chessboard">White Knights</a> in <b><a href="/wiki/Wonderland_Championship" title="Wonderland Championship">the Wonderland Championship</a></b>.</li>'  
),
(
'<li>Nine people, including eight children, <b><a href="/wiki/Mad_Hatters_Tea_Party" title="Mad Hatters Tea Party">attend a delightful tea party</a></b> in an enchanted school (pictured) in <a href="/wiki/Wonderland" title="Wonderland">Wonderland</a>.</li>',  
'<li>Nine people, including eight children, <b><a href="/wiki/Mad_Hatters_Tea_Party" title="Mad Hatters Tea Party">attend a delightful tea party</a></b> in an enchanted school in <a href="/wiki/Wonderland" title="Wonderland">Wonderland</a>.</li>'  
),
(
'<li><a href="/wiki/Dormouse" title="Dormouse">Dormouse</a> (pictured) defeats <a href="/wiki/March_Hare" title="March Hare">March Hare</a> to win <b><a href="/wiki/Wonderland_Chess_Championship" title="Wonderland Chess Championship">the Wonderland Chess Championship</a></b>.</li>',  
'<li><a href="/wiki/Dormouse" title="Dormouse">Dormouse</a> defeats <a href="/wiki/March_Hare" title="March Hare">March Hare</a> to win <b><a href="/wiki/Wonderland_Chess_Championship" title="Wonderland Chess Championship">the Wonderland Chess Championship</a></b>.</li>'  
),
(
'<li>The White Rabbit <b><a href="/wiki/White_Rabbit%E2%80%93Queen_of_Hearts_relations" title="White Rabbit–Queen of Hearts relations">joins</a></b> the <a href="/wiki/Queen_of_Hearts_Court" title="Queen of Hearts Court">Queen of Hearts Court</a> as its <a href="/wiki/Wonderland_Court_Expansion" title="Wonderland Court Expansion">31st member</a> <i>(flags pictured)</i>.</li>',  
'<li>The White Rabbit <b><a href="/wiki/White_Rabbit%E2%80%93Queen_of_Hearts_relations" title="White Rabbit–Queen of Hearts relations">joins</a></b> the <a href="/wiki/Queen_of_Hearts_Court" title="Queen of Hearts Court">Queen of Hearts Court</a> as its <a href="/wiki/Wonderland_Court_Expansion" title="Wonderland Court Expansion">31st member</a>.</li>'  
),
(
'<li><b><a href="/wiki/Whirlwind_of_March_24%E2%80%9327,_2023" title="Whirlwind of March 24–27, 2023">A whimsical whirlwind</a></b> <i>(damage pictured)</i> in <a href="/wiki/Tulgey_Wood" title="Tulgey Wood">Tulgey Wood</a> and <a href="/wiki/Looking_Glass_House" title="Looking Glass House">Looking Glass House</a>, Wonderland, leaves at least 24 curious creatures in a daze.</li>',  
'<li><b><a href="/wiki/Whirlwind_of_March_24%E2%80%9327,_2023" title="Whirlwind of March 24–27, 2023">A whimsical whirlwind</a></b> in <a href="/wiki/Tulgey_Wood" title="Tulgey Wood">Tulgey Wood</a> and <a href="/wiki/Looking_Glass_House" title="Looking Glass House">Looking Glass House</a>, Wonderland, leaves at least 24 curious creatures in a daze.</li>'  
),
(
'<li>In the Wonderland Games, the <a href="/wiki/Red_Knights" title="Red Knights">Red Knights</a> defeat the <a href="/wiki/White_Knights" title="White Knights">White Knights</a> in <b><a href="/wiki/Wonderland_Championship" title="Wonderland Championship">the Wonderland Championship</a></b> <i>(<a href="/wiki/Champion_of_Hearts" title="Champion of Hearts">Champion of Hearts</a> <a href="/wiki/Red_King" title="Red King">Red King</a> pictured)</i>.</li>',  
'<li>In the Wonderland Games, the <a href="/wiki/Red_Knights" title="Red Knights">Red Knights</a> defeat the <a href="/wiki/White_Knights" title="White Knights">White Knights</a> in <b><a href="/wiki/Wonderland_Championship" title="Wonderland Championship">the Wonderland Championship</a></b>.</li>'  
),
(
'<li>The final <b><a href="/wiki/Red_Queens_Carriage" title="Red Queen\'s Carriage">Red Queen\'s Carriage</a></b> (prototype pictured) to be built rolls off the assembly line at <a href="/wiki/Tweedledees_Workshop" title="Tweedledee\'s Workshop">Tweedledee\'s Workshop</a>, Wonderland.</li>',  
'<li>The final <b><a href="/wiki/Red_Queens_Carriage" title="Red Queen\'s Carriage">Red Queen\'s Carriage</a></b> to be built rolls off the assembly line at <a href="/wiki/Tweedledees_Workshop" title="Tweedledee\'s Workshop">Tweedledee\'s Workshop</a>, Wonderland.</li>'  
),
(
'<li>The final <b><a href="/wiki/Red_Queens_Carriage" title="Red Queen\'s Carriage">Red Queen\'s Carriage</a></b> <i>(prototype pictured)</i> to be built rolls off the assembly line at <a href="/wiki/Tweedledees_Workshop" title="Tweedledee\'s Workshop">Tweedledee\'s Workshop</a>, Wonderland.</li>',  
'<li>The final <b><a href="/wiki/Red_Queens_Carriage" title="Red Queen\'s Carriage">Red Queen\'s Carriage</a></b> to be built rolls off the assembly line at <a href="/wiki/Tweedledees_Workshop" title="Tweedledee\'s Workshop">Tweedledee\'s Workshop</a>, Wonderland.</li>'  
),
(
'<li>In Wonderland, six creatures are caught in <b><a href="/wiki/Mid_Air_Mishap_in_Wonderland" title="Mid Air Mishap in Wonderland">a mid-air collision</a></b> <i>(aircraft </i><a href="/wiki/Mock_Turtle_Flight" title="Mock Turtle\'s Flight">Mock Turtle\'s Flight</a><i> pictured)</i> at a fantastical air show in <a href="/wiki/Caterpillars_Meadow" title="Caterpillar\'s Meadow">Caterpillar\'s Meadow</a>.</li>',  
'<li>In Wonderland, six creatures are caught in <b><a href="/wiki/Mid_Air_Mishap_in_Wonderland" title="Mid Air Mishap in Wonderland">a mid-air collision</a></b> at a fantastical air show in <a href="/wiki/Caterpillars_Meadow" title="Caterpillar\'s Meadow">Caterpillar\'s Meadow</a>.</li>'  
),
(
'<li>In Wonderland, six creatures are caught in <b><a href="/wiki/Mid_Air_Mishap_in_Wonderland" title="Mid Air Mishap in Wonderland">a mid-air collision</a></b> <i>(one flying creature pictured)</i> at a fantastical air show in <a href="/wiki/Caterpillars_Meadow" title="Caterpillar\'s Meadow">Caterpillar\'s Meadow</a>.</li>',  
'<li>In Wonderland, six creatures are caught in <b><a href="/wiki/Mid_Air_Mishap_in_Wonderland" title="Mid Air Mishap in Wonderland">a mid-air collision</a></b> at a fantastical air show in <a href="/wiki/Caterpillars_Meadow" title="Caterpillar\'s Meadow">Caterpillar\'s Meadow</a>.</li>'  
),
(
'<li>In croquet, the <a href="/wiki/Red_Flamingos" title="Red Flamingos">Red Flamingos</a> defeat the <a href="/wiki/White_Hedgehogs" title="White Hedgehogs">White Hedgehogs</a> to win <b><a href="/wiki/Wonderland_Series" title="Wonderland Series">the Wonderland Series</a></b> <i>(<a href="/wiki/Croquet_Champion" title="Croquet Champion">MVP</a> <a href="/wiki/Alice" title="Alice">Alice</a> pictured)</i>.</li>',  
'<li>In croquet, the <a href="/wiki/Red_Flamingos" title="Red Flamingos">Red Flamingos</a> defeat the <a href="/wiki/White_Hedgehogs" title="White Hedgehogs">White Hedgehogs</a> to win <b><a href="/wiki/Wonderland_Series" title="Wonderland Series">the Wonderland Series</a></b>.</li>'  
),
(
'<li>The <a href="/wiki/Red_Queen\'s_Court" class="mw-redirect" title="Red Queen\'s Court">Red Queen\'s Court</a> wins a majority of seats in the <b><a href="/wiki/2022_Wonderland_election" title="2022 Wonderland election">Wonderland election</a></b> <i>(<a href="/wiki/Brothers_of_Tulgey_Wood" title="Brothers of Tulgey Wood">Brothers of Tulgey Wood</a> leader <a href="/wiki/Queen_of_Hearts" title="Queen of Hearts">Queen of Hearts</a> pictured)</i>.</li>',  
'<li>The <a href="/wiki/Red_Queen\'s_Court" class="mw-redirect" title="Red Queen\'s Court">Red Queen\'s Court</a> wins a majority of seats in the <b><a href="/wiki/2022_Wonderland_election" title="2022 Wonderland election">Wonderland election</a></b>.</li>'  
),
(
'<li>In <a href="/wiki/Croquet" title="Croquet">croquet</a>, the <a href="/wiki/Geelong_Flamingos" title="Geelong Flamingos">Flamingo Team</a> defeats the <a href="/wiki/Sydney_Hedgehogs" title="Sydney Hedgehogs">Hedgehog Club</a> to win <b><a href="/wiki/2022_Wonderland_Croquet_Final" title="2022 Wonderland Croquet Final">the Wonderland Croquet Final</a></b> <i>(<a href="/wiki/Norm_Snark_Medal" title="Norm Snark Medal">Norm Snark Medal</a> winner <a href="/wiki/Isidore_Carrol" title="Isidore Carrol">Isidore Carrol</a> pictured)</i>.</li>',  
'<li>In <a href="/wiki/Croquet" title="Croquet">croquet</a>, the <a href="/wiki/Geelong_Flamingos" title="Geelong Flamingos">Flamingo Team</a> defeats the <a href="/wiki/Sydney_Hedgehogs" title="Sydney Hedgehogs">Hedgehog Club</a> to win <b><a href="/wiki/2022_Wonderland_Croquet_Final" title="2022 Wonderland Croquet Final">the Wonderland Croquet Final</a></b>.</li>'  
),
(
'<li>In <a href="/wiki/Association_football" title="Association football">Wonderland football</a>, <a href="/wiki/Cheshire_City" title="Cheshire City">Cheshire Cats</a> defeat <a href="/wiki/Inter_Tulgey" title="Inter Tulgey">Tulgey Woods</a> to win the <b><a href="/wiki/2023_Wonderland_Champions_League_final" title="2023 Wonderland Champions League final">Wonderland Champions League final</a></b> <i>(man of the match <a href="/wiki/Ruddy_Tulgey" title="Ruddy Tulgey">Ruddy Tulgey</a> pictured)</i>.</li>',  
'<li>In <a href="/wiki/Association_football" title="Association football">Wonderland football</a>, <a href="/wiki/Cheshire_City" title="Cheshire City">Cheshire Cats</a> defeat <a href="/wiki/Inter_Tulgey" title="Inter Tulgey">Tulgey Woods</a> to win the <b><a href="/wiki/2023_Wonderland_Champions_League_final" title="2023 Wonderland Champions League final">Wonderland Champions League final</a></b>.</li>'  
),
(
'<li>In <a href="/wiki/Hoop_Rolling" title="Hoop Rolling">hoop rolling</a>, the <a href="/wiki/Tweedledee_Team" title="Tweedledee Team">Tweedledee Team</a> defeat the <a href="/wiki/Tweedledum_Club" title="Tweedledum Club">Tweedledum Club</a> to win <b><a href="/wiki/2023_Wonderland_Hoop_Final" title="2023 Wonderland Hoop Final">the Wonderland Hoop Final</a></b> <i>(<a href="/wiki/Hoop_Rolling_Champion" title="Hoop Rolling Champion">Champion</a> <a href="/wiki/Nikola_Tweedle" title="Nikola Tweedle">Nikolas Tweedle</a> pictured)</i>.</li>',  
'<li>In <a href="/wiki/Hoop_Rolling" title="Hoop Rolling">hoop rolling</a>, the <a href="/wiki/Tweedledee_Team" title="Tweedledee Team">Tweedledee Team</a> defeat the <a href="/wiki/Tweedledum_Club" title="Tweedledum Club">Tweedledum Club</a> to win <b><a href="/wiki/2023_Wonderland_Hoop_Final" title="2023 Wonderland Hoop Final">the Wonderland Hoop Final</a></b>.</li>'  
),
(
'<li><a href="/wiki/Queen_of_Hearts_(singer)" title="Queen of Hearts (singer)">The Queen of Hearts</a> <i>(pictured)</i> <a href="/wiki/Hearts_in_the_Wonderland_Song_Contest" title="Hearts in the Wonderland Song Contest">of Wonderland</a> wins <b><a href="/wiki/Wonderland_Song_Contest_2023" title="Wonderland Song Contest 2023">the Wonderland Song Contest</a></b> with the song "<a href="/wiki/Off_with_their_Heads" title="Off with their Heads">Off with their Heads</a>", becoming the first ruler to win the contest twice.</li>',  
'<li><a href="/wiki/Queen_of_Hearts_(singer)" title="Queen of Hearts (singer)">The Queen of Hearts</a> <a href="/wiki/Hearts_in_the_Wonderland_Song_Contest" title="Hearts in the Wonderland Song Contest">of Wonderland</a> wins <b><a href="/wiki/Wonderland_Song_Contest_2023" title="Wonderland Song Contest 2023">the Wonderland Song Contest</a></b> with the song "<a href="/wiki/Off_with_their_Heads" title="Off with their Heads">Off with their Heads</a>", becoming the first ruler to win the contest twice.</li>'  
),
(
'<li>In <a href="/wiki/Tea_Party" title="Tea Party">tea party games</a>, <a href="/wiki/Mad_Hatter" title="Mad Hatter">Mad Hatter</a> <i>(pictured)</i> wins <b><a href="/wiki/2023_Wonderland_Tea_Party" title="2023 Wonderland Tea Party">the Wonderland Tea Party</a></b>.</li>',  
'<li>In <a href="/wiki/Tea_Party" title="Tea Party">tea party games</a>, <a href="/wiki/Mad_Hatter" title="Mad Hatter">Mad Hatter</a> wins <b><a href="/wiki/2023_Wonderland_Tea_Party" title="2023 Wonderland Tea Party">the Wonderland Tea Party</a></b>.</li>'  
),
(
'<li>In Tulgey Wood, the <a href="/wiki/Grinning_Brigade" title="Grinning Brigade">Grinning Brigade</a> mercenary group <i>(leader <a href="/wiki/Smirk_Gruff" title="Smirk Gruff">Smirk Gruff</a> pictured)</i> <b><a href="/wiki/Grinning_Brigade_rebellion" title="Grinning Brigade rebellion">rebels</a></b> against the Queen\'s court.</li>',  
'<li>In Tulgey Wood, the <a href="/wiki/Grinning_Brigade" title="Grinning Brigade">Grinning Brigade</a> mercenary group <b><a href="/wiki/Grinning_Brigade_rebellion" title="Grinning Brigade rebellion">rebels</a></b> against the Queen\'s court.</li>'  
),
(
'<li>In Wonderland, the <a href="/wiki/Crimson_Alliance" title="Crimson Alliance">Crimson Alliance</a> <i>(leader <a href="/wiki/Alice" title="Alice">Alice</a> pictured)</i> wins the most seats in <b><a href="/wiki/2024_Wonderland_legislative_election" title="2024 Wonderland legislative election">a snap legislative election</a></b>.</li>',
'<li>In Wonderland, the <a href="/wiki/Crimson_Alliance" title="Crimson Alliance">Crimson Alliance</a> wins the most seats in <b><a href="/wiki/2024_Wonderland_legislative_election" title="2024 Wonderland legislative election">a snap legislative election</a></b>.</li>',
),
(
'<li>Underland <i>(highlighted)</i> becomes <b><a href="/wiki/Underland%E2%80%93Card_Association" title="Underland–Card Association">the thirty-second member state</a></b>  of <a href="/wiki/Card_Union" title="Card Union">the Card Union</a>.</li>',
'<li>Underland becomes <b><a href="/wiki/Underland%E2%80%93Card_Association" title="Underland–Card Association">the thirty-second member state</a></b> of <a href="/wiki/Card_Union" title="Card Union">the Card Union</a>.</li>',
),
(
'<li>In <b><a href="/wiki/2023_Wonderland_parliamentary_election" title="2023 Wonderland parliamentary election">the parliamentary election</a></b>, the <a href="/wiki/Heart_Progress_Party" title="Heart Progress Party">Heart Progress Party</a> <i>(leader <a href="/wiki/Red_Knight" title="Red Knight">Red Knight</a> pictured)</i> regains its <a href="/wiki/Majority_in_the_Assembly" title="Majority in the Assembly">parliamentary majority</a> in the <a href="/wiki/Wonderland_Assembly" title="Wonderland Assembly">Wonderland Assembly</a>.</li>',
'<li>In <b><a href="/wiki/2023_Wonderland_parliamentary_election" title="2023 Wonderland parliamentary election">the parliamentary election</a></b>, the <a href="/wiki/Heart_Progress_Party" title="Heart Progress Party">Heart Progress Party</a> regains its <a href="/wiki/Majority_in_the_Assembly" title="Majority in the Assembly">parliamentary majority</a> in the <a href="/wiki/Wonderland_Assembly" title="Wonderland Assembly">Wonderland Assembly</a>.</li>',
),
(
'<li><b><a href="/wiki/Stormy_Tempest" title="Stormy Tempest">Stormy Tempest</a></b> <i>(magic orb image shown)</i> makes landfall near <a href="/wiki/Acorn_Town" title="Acorn Town">Acorn Town</a>, Underland, leaving at least 39 creatures bewildered.</li>',
'<li><b><a href="/wiki/Stormy_Tempest" title="Stormy Tempest">Stormy Tempest</a></b> makes landfall near <a href="/wiki/Acorn_Town" title="Acorn Town">Acorn Town</a>, Underland, leaving at least 39 creatures bewildered.</li>',
),
(
'<li>In <a href="/wiki/Snow_Hockey" title="Snow Hockey">snow hockey</a>, the <a href="/wiki/Flamingo_Flurries" title="Flamingo Flurries">Flamingo Flurries</a> <i>(captain <a href="/wiki/Alexander_Peck" title="Alexander Peck">Alexander Peck</a> pictured)</i> defeat the <a href="/wiki/Badger_Blizzards" title="Badger Blizzards">Badger Blizzards</a> to win <b><a href="/wiki/2024_Snowflake_Cup_Finals" title="2024 Snowflake Cup Finals">the Snowflake Cup Finals</a></b>.</li>',
'<li>In <a href="/wiki/Snow_Hockey" title="Snow Hockey">snow hockey</a>, the <a href="/wiki/Flamingo_Flurries" title="Flamingo Flurries">Flamingo Flurries</a> defeat the <a href="/wiki/Badger_Blizzards" title="Badger Blizzards">Badger Blizzards</a> to win <b><a href="/wiki/2024_Snowflake_Cup_Finals" title="2024 Snowflake Cup Finals">the Snowflake Cup Finals</a></b>.</li>',
),
(
'<li><b><a href="/wiki/2024_Queen\'s_Croquet_Tournament" title="2024 Queen\'s Croquet Tournament">The Queen\'s Croquet Tournament</a></b> <a href="/wiki/2024_Queen\'s_Croquet_Tournament_opening_ceremony" title="2024 Queen\'s Croquet Tournament opening ceremony">open</a> <i>(<a href="/wiki/2024_Croquet_Cauldron" title="2024 Croquet Cauldron">cauldron</a> lighting pictured)</i> in <a href="/wiki/Wonderland" title="Wonderland">Wonderland</a>.</li>',
'<li><b><a href="/wiki/2024_Queen\'s_Croquet_Tournament" title="2024 Queen\'s Croquet Tournament">The Queen\'s Croquet Tournament</a></b> <a href="/wiki/2024_Queen\'s_Croquet_Tournament_opening_ceremony" title="2024 Queen\'s Croquet Tournament opening ceremony">open</a> in <a href="/wiki/Wonderland" title="Wonderland">Wonderland</a>.</li>'
)
    
]

@pytest.mark.parametrize("input_html, expected_output", test_data)
def test_remove_pictured(input_html, expected_output):
    assert remove_pictured(input_html) == expected_output
