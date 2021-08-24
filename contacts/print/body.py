from reportlab.platypus import Table
from reportlab.lib import colors
def genBodyTable(width, height):

    widthList = [
        width * 10/100,
        width * 80/100,
        width * 10/100,
    ]

    heightList = [
        height * 10/100,
        height * 15/100,
        height * 35/100,
        height * 30/100,
        height * 10/100,
    ]

    res = Table([
        ['', 'FACTURE',''],
        ['', _genContactsTable(widthList[1], heightList[1]),''],
        ['', _genPriceListTable(widthList[1], heightList[2]),''],
        ['', _genDescriptionParas(heightList, widthList),''],
        ['', _genAboutTable(widthList[1], heightList[4]),''],
    ],

    widthList,
    heightList
    )

    color = colors.HexColor('#003363')
    leftPadding = 20

    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        # ('LEFTPADDING', (0, 0), (-1, -1), 0,),
        # ('BOTTOMPADDING', (0, 0), (-1, -1), 0,),
        ('LINEBELOW', (1, 0), (1, 1), 1, color),
        ('LINEBELOW', (1, 3), (1, 3), 1, color),
        ('LEFTPADDING', (1, 0), (1, 3), leftPadding),
        ('FRONTSIZE', (1, 0), (1, 0), 30),
        ('BOTTAMPADDING', (1, 0), (1, 0), 60),
        ('BOTTAMPADDING', (1, 1), (1, 2), 0),
        ('BOTTAMPADDING', (1, 3), (1, 3), 40),
        ('BOTTAMPADDING', (1, 4), (1, 4), 0),
        ('LEFTPADDING', (1, 4), (1, 4), 0),
    ])

    return res

def _genContactsTable(width, height):

    return 'CONTACTS'


def _genPriceListTable(width, height):

    return 'PRICE'

def _genDescriptionParas(width, height):

    return 'DESCRIPTION'


def _genAboutTable(width, height):

    widthList = [
        width * 20 / 100,
        width * 80 / 100,
    ]
    res = Table([
         ['col1', 'col2'],
    ],
    widthList,
    height)

    res.setStyle([
        ('GRID', (0, 0), (-1, -1), 1, 'red'),
    ])
    return res