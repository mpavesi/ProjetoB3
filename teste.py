import io

from correpy.parsers.brokerage_notes.b3_parser.b3_parser import B3Parser

with open('nota_23824.pdf', 'rb') as f:
    content = io.BytesIO(f.read())
    content.seek(0)
    
    brokerage_notes = B3Parser(brokerage_note=content, password="password").parse_brokerage_note()
    print(brokerage_notes)