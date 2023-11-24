"""
Basic script to convert a document for a single-byte encoding into a decoding
table for use by the module.
"""


import sys


conversionDict = {0:"'\\x00'",1:"'\\x01'",2:"'\\x02'",3:"'\\x03'",4:"'\\x04'",5:"'\\x05'",6:"'\\x06'",7:"'\\x07'",8:"'\\x08'",9:"'\\t'",10:"'\\n'",11:"'\\x0b'",12:"'\\x0c'",13:"'\\r'",14:"'\\x0e'",15:"'\\x0f'",16:"'\\x10'",17:"'\\x11'",18:"'\\x12'",19:"'\\x13'",20:"'\\x14'",21:"'\\x15'",22:"'\\x16'",23:"'\\x17'",24:"'\\x18'",25:"'\\x19'",26:"'\\x1a'",27:"'\\x1b'",28:"'\\x1c'",29:"'\\x1d'",30:"'\\x1e'",31:"'\\x1f'",32:"' '",33:"'!'",34:'\'"\'',35:"'#'",36:"'$'",37:"'%'",38:"'&'",39:'"\'"',40:"'('",41:"')'",42:"'*'",43:"'+'",44:"','",45:"'-'",46:"'.'",47:"'/'",48:"'0'",49:"'1'",50:"'2'",51:"'3'",52:"'4'",53:"'5'",54:"'6'",55:"'7'",56:"'8'",57:"'9'",58:"':'",59:"';'",60:"'<'",61:"'='",62:"'>'",63:"'?'",64:"'@'",65:"'A'",66:"'B'",67:"'C'",68:"'D'",69:"'E'",70:"'F'",71:"'G'",72:"'H'",73:"'I'",74:"'J'",75:"'K'",76:"'L'",77:"'M'",78:"'N'",79:"'O'",80:"'P'",81:"'Q'",82:"'R'",83:"'S'",84:"'T'",85:"'U'",86:"'V'",87:"'W'",88:"'X'",89:"'Y'",90:"'Z'",91:"'['",92:"'\\\\'",93:"']'",94:"'^'",95:"'_'",96:"'`'",97:"'a'",98:"'b'",99:"'c'",100:"'d'",101:"'e'",102:"'f'",103:"'g'",104:"'h'",105:"'i'",106:"'j'",107:"'k'",108:"'l'",109:"'m'",110:"'n'",111:"'o'",112:"'p'",113:"'q'",114:"'r'",115:"'s'",116:"'t'",117:"'u'",118:"'v'",119:"'w'",120:"'x'",121:"'y'",122:"'z'",123:"'{'",124:"'|'",125:"'}'",126:"'~'",127:"'\\x7f'",128:"'\\x80'",129:"'\\x81'",130:"'\\x82'",131:"'\\x83'",132:"'\\x84'",133:"'\\x85'",134:"'\\x86'",135:"'\\x87'",136:"'\\x88'",137:"'\\x89'",138:"'\\x8A'",139:"'\\x8B'",140:"'\\x8C'",141:"'\\x8D'",142:"'\\x8E'",143:"'\\x8F'",144:"'\\x90'",145:"'\\x91'",146:"'\\x92'",147:"'\\x93'",148:"'\\x94'",149:"'\\x95'",150:"'\\x96'",151:"'\\x97'",152:"'\\x98'",153:"'\\x99'",154:"'\\x9A'",155:"'\\x9B'",156:"'\\x9C'",157:"'\\x9D'",158:"'\\x9E'",159:"'\\x9F'",160:"'\\xA0'",161:"'\\xA1'",162:"'\\xA2'",163:"'\\xA3'",164:"'\\xA4'",165:"'\\xA5'",166:"'\\xA6'",167:"'\\xA7'",168:"'\\xA8'",169:"'\\xA9'",170:"'\\xAA'",171:"'\\xAB'",172:"'\\xAC'",173:"'\\xAD'",174:"'\\xAE'",175:"'\\xAF'",176:"'\\xB0'",177:"'\\xB1'",178:"'\\xB2'",179:"'\\xB3'",180:"'\\xB4'",181:"'\\xB5'",182:"'\\xB6'",183:"'\\xB7'",184:"'\\xB8'",185:"'\\xB9'",186:"'\\xBA'",187:"'\\xBB'",188:"'\\xBC'",189:"'\\xBD'",190:"'\\xBE'",191:"'\\xBF'",192:"'\\xC0'",193:"'\\xC1'",194:"'\\xC2'",195:"'\\xC3'",196:"'\\xC4'",197:"'\\xC5'",198:"'\\xC6'",199:"'\\xC7'",200:"'\\xC8'",201:"'\\xC9'",202:"'\\xCA'",203:"'\\xCB'",204:"'\\xCC'",205:"'\\xCD'",206:"'\\xCE'",207:"'\\xCF'",208:"'\\xD0'",209:"'\\xD1'",210:"'\\xD2'",211:"'\\xD3'",212:"'\\xD4'",213:"'\\xD5'",214:"'\\xD6'",215:"'\\xD7'",216:"'\\xD8'",217:"'\\xD9'",218:"'\\xDA'",219:"'\\xDB'",220:"'\\xDC'",221:"'\\xDD'",222:"'\\xDE'",223:"'\\xDF'",224:"'\\xE0'",225:"'\\xE1'",226:"'\\xE2'",227:"'\\xE3'",228:"'\\xE4'",229:"'\\xE5'",230:"'\\xE6'",231:"'\\xE7'",232:"'\\xE8'",233:"'\\xE9'",234:"'\\xEA'",235:"'\\xEB'",236:"'\\xEC'",237:"'\\xED'",238:"'\\xEE'",239:"'\\xEF'",240:"'\\xF0'",241:"'\\xF1'",242:"'\\xF2'",243:"'\\xF3'",244:"'\\xF4'",245:"'\\xF5'",246:"'\\xF6'",247:"'\\xF7'",248:"'\\xF8'",249:"'\\xF9'",250:"'\\xFA'",251:"'\\xFB'",252:"'\\xFC'",253:"'\\xFD'",254:"'\\xFE'",255:"'\\xFF'"}

def symbolToEntry(input : int, output : int) -> str:
    if output < 256:
        return f'{input}:{conversionDict[output]}'
    elif output < 0x10000:
        return f'{input}:\'\\u{output:04X}\''
    else:
        return f'{input}:\'\\U{output:08X}\''


if __name__ == "__main__":
    table = {}
    if len(sys.argv) != 2:
        print('Invalid number of arguments (requires exactly one file name)!')
        exit(-1)

    with open(sys.argv[1], 'r') as f:
        for line in f:
            # Skip comment lines.
            if not line.strip().startswith('#'):
                items = line.split('\t')
                if len(items) != 1 and items[1]:
                    table[int(items[0], 16)] = int(items[1], 16)

    with open('.'.join(sys.argv[1].split('.')[:-1] + ['py']), 'w') as f:
        # Write the top of the file.
        f.write('__all__ = [\n    \'decodingTable\',\n]\n\n\ndecodingTable={')
        f.write(','.join(symbolToEntry(x, table[x]) for x in table))
        f.write('}')