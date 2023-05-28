import pyautogui
from time import sleep

# Esse Script é bem similar ao outro, a diferença é que é necessário colocar as palavras anteriormente no programa manualmente.
# Ele tem o obajetivo de funcionar em mais sites e consegue replicar melhor a digitação Humana.

# Um alerta para saber se o Usuário está pronto
pyautogui.alert('posso rodar?')
sleep(5)

# Palavras que vão ser digitadas pelo o Script
wordlist = "think|right|set|its|which|should|is|kind|great|life|or|found|sea|because|feet|along|after|last|open|you|very|above|enough|saw|almost|we|it's|set|good|while|food|want|feet|being|are|learn|boy|light|city|life|much|any|over|form|thought|above|before|carry|were|water|want|said|make|these|why|still|quickly|what|right|few|were|year|each|own|very|own|close|book|here|first|still|my|different|is|often|she|large|family|get|paper|song|in|you|other|by|was|add|river|show|ask|some|help|mother|what|still|above|right|stop|night|those|where|leave|leave|be|Indian|now|all|eye|then|other|miss|work|name|quite|but|land|water|girl|who|because|little|three|write|take|before|took|after|by|people|like|girl|this|find|second|for|long|animal|open|like|miss|we|earth|from|number|white|put|at|them|seem|off|white|she|later|between|good|were|open|he|went|read|those|play|such|went|answer|if|more|way|because|close|an|the|grow|also|or|look|thought|almost|he|mile|out|small|could|kind|now|tree|sentence|run|almost|face|has|she|must|country|two|for|idea|up|from|than|enough|father|study|came|and|even|some|under|let|of|follow|been|many|many|too|something|in|leave|grow|mean|both|his|land|then|over|could|eye|ask|look|year|hand|read|school|change|think|let|four|so|away|head|day|the|them|school|why|again|when|need|hand|state|last|place|city|quick|might|down|side|how|question|thing|to|far|all|are|his|as|one|walk|came|that|are|what|when|one|will|watch|want|him|most|there|will|play|just|page|tell|me|through|run|children|such|have|move|change|move|use|has|it|this|let|high|car|old|answer|time|go|later|great|miss|letter|go|down|know|study|on|boy|sea|put|talk|white|make|here|does|start|went|place|about|even|no|know|it|point|off|seem|old|they|air|and|left|don't|your|into|below|its|they|house|have|talk|earth|many|it's|would|he|if|first|page|into|young|not|hear|our|with|give|got|even|family|young|mountain|eat|carry|if|little|us|begin|our|look|keep|world|father|America|state|work|watch|until|on|head|any|animal|car|very|sou"
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
