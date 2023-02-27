import pyautogui
from time import sleep

# Esse Script é bem similar ao outro, a diferença é que é necessário colocar as palavras anteriormente no programa manualmente.
# Ele tem o obajetivo de funcionar em mais sites e consegue replicar melhor a digitação Humana.

# Um alerta para saber se o Usuário está pronto
pyautogui.alert('posso rodar?')
sleep(5)

# Palavras que vão ser digitadas pelo o Script
wordlist = "The|complex|French|position|by|great|three|March|debt|PC|important|banks|display|world|P|press|almost|purchase|some|made|officials|Windows|clear|source|compared|computer|become|study|later|Now|unit|ended|image|previous|easy|companies|my|people|turn|weeks|With|managers|member|children|when|World|financial|Since|case|sold|quarter|amount|Reagan|Exchange|how|Service|Congress|along|staff|involved|level|general|a|period|processing|doing|machines|expects|until|July|early|continue|document|outside|shows|rather|record|feature|full|response|economy|bonds|telephone|cut|make|into|Bank|report|third|those|When|card|investigation|growth|approach|company's|could|did|National|security|firm|That|number|her|shares|operations|water|killed|military|His|Washington|cars|bank|past|remain|DOS|officer|team|death|were|as|further|still|One|trying|week|we|keep|whose|He|current|agreed|reason|six|Commission|gas|very|yesterday|seems|local|test|Thursday|software|Computer|particularly|him|future|November|rule|value|trial|President|kind|works|women|among|who|There|buying|specific|want|research|million|fact|will|functions|received|light|prices|men|read|By|has|expected|sent|known|between|workers|saying|nation's|services|Party|process|To|London|create|While|times|taking|own|needs|held|South|International|screen|created|thing|complete|East|Calif|Co|economic|power|effect|since|months|memory|RAM|storage|Mr|exchange|spokesman|city|enough|charges|Democratic|City|role|October|though|ever|charge|loss|play|It|United|space|plan|Apple|television|down|present|interest|many|close|the|end|way|terms|points|series|personal|fall|last|structure|field|died|scheduled|IBM|provide|analyst|area|its|January|deal|design|income|seven|York|options|another|requirements|might|able|drives|took|April|return|distribution|is|bid|For|inflation|system|control|Board|equipment|come|forces|recent|increase|would|issues|employees|cannot|open|Macintosh|analysts|long|didn't|reached|war|lot|As|second|going|processor|side|new|central|troops|man|"
# O caractere especial que divide cada palavra
words = wordlist.split("|")

# Para cada palavra na lista de palavras
for word in words:
    # Para cada letra em palavras
    for letter in word:
        # Escrevendo a letra
        pyautogui.write(letter)
    #Escrevendo um espaço em branco depois de cada palavra
    pyautogui.write(" ")
